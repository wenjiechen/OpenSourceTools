#!/bin/bash
##2.
cut -f3,4 -d'|' part1.dat | grep '193[0-9]' | cut -f1 -d'|'
##3.
grep -i '[^|]*\(\<[^[:space:]]\{1,\}\>\) .* \<\1\>' part1.dat | wc -l
##4.
cut -f1,3 -d'|' part1.dat | grep '|.*[^[:alpha:][:space:]]\{1,\}' | cut -f1 -d'|'
##5.
cut -f5 -d'|' part1.dat | grep '^\([1-3][0-9]\{1,4\}\)$\|^\([0-9]\{1,4\}\)$' | wc -l
