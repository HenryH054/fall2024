# Homework 7.3

## Problem 1

There's no way to generate the string bbab

|Len|b|b|a|b|
|--|--|--|--|--|
|4|0||||
|3|0|0|||
|2|0|S,YA,ba|S,XB,ab||
|1|0|0|0|0|

## Problem 2

It does through multiple paths ones is S $\rightarrow$ ZW $\rightarrow$ XYW $\rightarrow$ XYAB $\rightarrow$ abbb

|Len|a|b|b|b|
|--|--|--|--|--|
|4|S,ZW,XYW,XYAB,abbb or S,ZA,XYA,XYYA(B),abbb||||
|3|S,ZA,XYA,abb or S,ZB,XYB,abb|0|||
|2|S,XY|0|0||
|1|0|0|0|0|

## Problem 3

No, X will always add an additional X and there is no way to avoid generating an X

## Problem 4

finite

## Problem 5

finite, as it will never generate any strings

## Problem 6

Infinite, can generate any number of strings of any length beyond some length n, where n represents the shortest path to conclusion.

