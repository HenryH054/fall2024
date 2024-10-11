# Homework 4.3

## Problem 1

$a^{n^3}b^{n^3}$ is not regular

aaabbb

pick a letter to pump such that the string can be divided into xyz

x = aa
y = a
z = bbb

pumping y 1 or more times now causes a contradiction

## Problem 2

This is yet again not regular, in order for a word to enter into the vocabularly the amount of a's and b's must be different

IE: aabbb works but aaabbb does not work

utilizing the pumping lemma theorem we can see the contradiction in the string aabbb

we choose x = a, y = a, z = bbb

we now pump a once and the language no longer fits and this language is no longer regular.

## Problem 3

m/n must form an integer as such we can prove this wrong with the accepted string

aaabbb which gives the integer 1, we can now choose to pump either an a or a b and the m and n will turn into 4/3 or 3/4 both of which do not work, as such this is a contradiction

## Problem 4

a^{2^n} is not regular as the string

aaaaaaaaaaaaaaaa works if n = 2, but if we pump one of the central a-s such that x = a^j y = a z = a^k we now have 17 a-s which no longer fits into the language
