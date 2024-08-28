# Homework 1

## Problem 1

|Order|Element|
|-|-|
|1|0|
|2|1|
|3|000|
|4|001|
|5|010|
|6|011|
|7|100|
|8|101|
|9|110|
|10|111|
|11|00000|

## Problem 2

|Order|Element|
|-|-|
|1|""|
|2|"aba"|
|3|"ba"|
|4|"abaaba"|
|5|"ababa"|
|6|"baba"|
|7|"abaabaaba"|
|8|"abaababa"|
|9|"abababa"|
|10|"bababa"|
|11|"abaabaabaaba"|

## Problem 3

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (21.9,-27.5) circle (3);
\draw (21.9,-27.5) node {$q0$};
\draw [black] (38,-27.5) circle (3);
\draw (38,-27.5) node {$q1*$};
\draw [black] (24.2,-25.589) arc (121.83408:58.16592:10.901);
\fill [black] (35.7,-25.59) -- (35.28,-24.74) -- (34.76,-25.59);
\draw (29.95,-23.45) node [above] {$a,b$};
\draw [black] (35.41,-29.001) arc (-66.25153:-113.74847:13.557);
\fill [black] (24.49,-29) -- (25.02,-29.78) -- (25.42,-28.87);
\draw (29.95,-30.65) node [below] {$a,b$};
\end{tikzpicture}
```

## Problem 4

Non-terminals: {S,A}{S,A}

Terminals: {a,b}{a,b}

Production Rules:
  S$\rightarrow$aA
  
  S$\rightarrow$bA
  
  A$\rightarrow$aS
  
  A$\rightarrow$bS

Start Symbol: SS
