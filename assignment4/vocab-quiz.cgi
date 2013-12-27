#!/usr/bin/python
import random
import cgi
import cgitb
import grade

class Question:
	'''Store data for a word quiz question.
	'''

	def __init__(self,words):
		'''Use four words to initialize question class.
		
		The first word is considered as quiz answer.
		'''
		tmp = words[0].split('|')
		self.word = tmp[0]
		self.answer = tmp[2]
		self.options = []
		for i in range(1,4):
			tmp = words[i].split('|')
			self.options.append(tmp[2])

class VocabQuiz:
	'''Generate 10 quizes using given words file.
	'''

	def __init__(self,vocab_file):
		self.__vocab_file = vocab_file
		self.num = 1
	 
	def get_words(self):
		with open(self.__vocab_file,'r') as f:
			words = f.readlines()
		f.close()
		random.shuffle(words)
		self.nonus = []
		self.verbs = []
		self.adjs = []
		for i, w in enumerate(words):
			if(len(self.nonus) == 16 and len(self.verbs) == 12 and len(self.adjs) == 12):
				break
			tmp = w.split('|')
			if(tmp[1] == 'n.' and len(self.nonus) < 16):
				self.nonus.append(w.strip())
			elif(tmp[1] == 'v.' and len(self.verbs) < 12):
				self.verbs.append(w.strip())
			elif(tmp[1] == 'adj.' and len(self.adjs) < 12):
				self.adjs.append(w.strip())
		self.words = self.nonus + self.verbs + self.adjs
		

	def gen_quizes(self):
		'''Generate 10 quizes class.
		'''	

		self.get_words()
		self.quizes = []
		index = [x*4 for x in range(len(self.words)/4)]
		for i in index:
			self.quizes.append(Question(self.words[i:i+4]))
		random.shuffle(self.quizes)
				
	def test(self):
		self.gen_quizes()
		for q in self.quizes:
			print q.word
			print q.answer
			print q.options
			print '==================='
		random.shuffle(self.quizes)
		
	def add_one_quiz(self):
		if self.quizes :
			q = self.quizes.pop()
			q.options.append(q.answer)
			random.shuffle(q.options)
			print '<p><li><b>%s</b>:</br>' %(q.word)
			print '<input type="hidden" name="word%d" value="%s">' %(self.num,q.word)
			input_item = '<input type="radio" name="q%d" value="%s"> %s</br>'
			for opt in q.options:
				if opt == q.answer :
					value = 'right'
				else:
					value = 'wrong'
				print input_item %(self.num,value,opt)
			print '</li></p>'
			self.num += 1

	def generate_html(self):
		self.gen_quizes()
		print 'Content-type: text/html\n'
		print '<html>'
		print '<form action="vocab-quiz.cgi" method="post">'
		print '<body>'
		print '<h2 style="background-color:powderblue;text-align:center;"> Vocabulary Quiz </h2>'
		print '<p style="font-size:25px;"> Please choose the right meaning for each word </p>'
		print '<ol>'
		while self.quizes :
			self.add_one_quiz()
		print '</ol>'
		print '</body>'
		print '<input type="submit" value="Grade">'
		print '</form>'
		print '</html>'


if __name__ == '__main__':
	cgitb.enable()
	form = cgi.FieldStorage()
	if 'word2' in form :
		g = grade.Grader(form)
		g.gen_html()	
	else:
		vq = VocabQuiz('/home/unixtool/data/vocab.dat')
		vq.generate_html()
