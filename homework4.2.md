# Homework 4.2

## Problem 1

I must prove that no string is accepted by one over the other

|State|A|B|
|--|--|--|
|{r0,s0}|{r1+,s1+}|{r2+,s2+}|
|{r1+,s1+}|{r0,s2+}||

At this point we can say that these are not the same as once the string is AA S will accept and R will not

## Problem 2

|State|R|S|
|--|--|--|
|""|t|t|
|a|t|t|
|a+|t|t|
|b|t|t|
|b+|t|t|
|ab+|t|t|
|ba+|f|f|

There exists no such case in which these DFA's represent different values

## Problem 3

R must not accept that which s does

|State|R|S|
|--|--|--|
|a|t|t|
|b|f|f|
|a+|t|t|
|b+|f|f|
|b+a|t|t|

R is a subset of S in the sense that they are the same.

## Problem 4

Starting with r0 we will conduct a bredth first search and see if it comes to an accepting state and if so notate the first route.

r0 -> r4 && -> r5
r4 -> no unmarked nodes
r5 -> no unmarked nodes

No accepting state can be found
