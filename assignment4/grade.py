#!/usr/bin/python
import cgi
import cgitb

class Grader:

	def __init__(self,form_in):
		self.form = form_in

	def grade(self):
		wordi = dict([('word'+ str(i), 'q' + str(i)) for i in range(1,11)])
		self.rights = []
		self.wrongs = []
		for wi,qi in wordi.items():
			if qi in self.form:
				if self.form[qi].value == 'right':
					self.rights.append(self.form[wi].value)
				else:
					self.wrongs.append(self.form[wi].value)
			else:
				self.wrongs.append(self.form[wi].value)

	def show_result(self):
		print '<tr>'
		print '<td valign=top style="color:green;">'
		for w in self.rights:
			print w,'<br>'
		print '</td>'
		print '<td valign=top style="color:red;">'
		for r in self.wrongs:
			print r,'<br>'
		print '</td>'
		print '</tr>'
	
	def gen_html(self):
		self.grade()
		print 'Content-type: text/html\n'
		print '<html>'
		print '<body>'
		print '<p>'
		print 'You got <b>%d of 10</b> answers correct</p>' %(len(self.rights))
		print '<table border="1">'
		print '<tr>'
		print '<th>Correct</th>'
		print '<th>Incorrect</th>'
		self.show_result()	
		print '</table>'
		print '<p></p>'
		print '<form action="vocab-quiz.cgi">'
#		print '<input type="submit" value="test again">'
		print '</form></body></html>'

if __name__ == '__main__':
	g = Grader()
	g.gen_html()		
