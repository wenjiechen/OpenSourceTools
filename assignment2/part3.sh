#!/bin/bash

##6
awk 'BEGIN {FS = "|"}
{sum += $5;}
END{print sum}' part1.dat

##7
awk 'BEGIN {FS = "|"}
{years[$4] += $5}
END{
  for(i in years){
    if(years[i] > most){
      most = years[i];
      year = i;
    }
  }
  print year;
}' part1.dat

##8
awk 'BEGIN {FS = "|"}
{decades[substr($4,1,3)]++}
END{
  for(i in decades){
    if(decades[i] > most){
      most = decades[i];
      year = i;
    }
  }
  res = year "0"
  print res;
}' part1.dat

##9
awk 'BEGIN {FS = "|"}
$2 > 8.5 {vote1 += $5; num1++}
$2 < 8.5 {vote2 += $5; num2++}
END{print "above 8.5:",vote1/num1,"; below 8.5:",vote2/num2}' part1.dat

##10
awk 'BEGIN {FS = "|"}
{words += split($3,title, "[ \t]")}
END{ print words/NR}' part1.dat

##11
awk 'BEGIN {FS = "|"}
{
  split($3,title, "[ \t]");
  for(i in title){
    words[title[i]]++
  }
}
END{
  for(i in words){
    if( i != "The" && i != "the" && i != "of" && words[i] > most){
      most = words[i];
      res = i;
    }
  }
  print res;  
}' part1.dat

##12
awk 'BEGIN {FS = "|"; longest=0;shortest=100000;}
length($3) > longest { longest = length($3); name1 = $3;}
length($3) < shortest { shortest = length($3); name2 = $3;}
END{ printf("longes title: %s\nshortest title: %s\n",name1,name2)}' part1.dat
