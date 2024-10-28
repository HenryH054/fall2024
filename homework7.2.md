# Homework 7.2

## Problem 1

A)

S $\rightarrow$ A | D

A $\rightarrow$ aAa | bAb | B

B $\rightarrow$ aCb | bCa

C $\rightarrow$ aC | bC | \lambda

D $\rightarrow$ EF

E $\rightarrow$ aEb | \lambda

F $\rightarrow$ aF | \lambda

B)

S $\rightarrow$ AD

A $\rightarrow$ aAa | bAb | B

B $\rightarrow$ aCb | bCa

C $\rightarrow$ aC | bC | \lambda

D $\rightarrow$ EF

E $\rightarrow$ aEb | \lambda

F $\rightarrow$ aF | \lambda

C) 

S $\rightarrow$ ASD | \lambda

A $\rightarrow$ aAa | bAb | B

B $\rightarrow$ aCb | bCa

C $\rightarrow$ aC | bC | \lambda

D $\rightarrow$ EF

E $\rightarrow$ aEb | \lambda

F $\rightarrow$ aF | \lambda

## Problem 2

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (27.2,-15.2) circle (3);
\draw (27.2,-15.2) node {$q_0$};
\draw [black] (50.1,-15.2) circle (3);
\draw (50.1,-15.2) node {$q_1$};
\draw [black] (50.1,-15.2) circle (2.4);
\draw [black] (19.2,-27.4) circle (3);
\draw (19.2,-27.4) node {$q_2$};
\draw [black] (34.9,-27.4) circle (3);
\draw (34.9,-27.4) node {$q_3$};
\draw [black] (30.2,-15.2) -- (47.1,-15.2);
\fill [black] (47.1,-15.2) -- (46.3,-14.7) -- (46.3,-15.7);
\draw (38.65,-15.7) node [below] {$b,\mbox{ }X\mbox{ }\rightarrow\mbox{ }\lambda$};
\draw [black] (48.777,-12.52) arc (234:-54:2.25);
\draw (50.1,-7.95) node [above] {$b,\mbox{ }X\mbox{ }\rightarrow\mbox{ }\lambda$};
\fill [black] (51.42,-12.52) -- (52.3,-12.17) -- (51.49,-11.58);
\draw [black] (25.55,-17.71) -- (20.85,-24.89);
\fill [black] (20.85,-24.89) -- (21.7,-24.5) -- (20.87,-23.95);
\draw (22.58,-19.98) node [left] {$a,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }X$};
\draw [black] (22.2,-27.4) -- (31.9,-27.4);
\fill [black] (31.9,-27.4) -- (31.1,-26.9) -- (31.1,-27.9);
\draw (27.05,-27.9) node [below] {$a,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }X$};
\draw [black] (33.3,-24.86) -- (28.8,-17.74);
\fill [black] (28.8,-17.74) -- (28.81,-18.68) -- (29.65,-18.15);
\draw (31.68,-20) node [right] {$a,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }X$};
\end{tikzpicture}
```

## Problem 3

No, removing strings can cause a language to no longer be deterministic
