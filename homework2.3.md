# Homework 2.3

## Problem 1

The easiest way to show that this DFA is minimal is to show that each state represents a unique binary string. Considering that the names of the states are based on the string they represent we can clearly see that it is minimal.

## Problem 2

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (9.6,-25.4) circle (3);
\draw (9.6,-25.4) node {$q0$};
\draw [black] (28.9,-25.4) circle (3);
\draw (28.9,-25.4) node {$q1$};
\draw [black] (28.9,-42.8) circle (3);
\draw (28.9,-42.8) node {$q8$};
\draw [black] (28.9,-42.8) circle (2.4);
\draw [black] (9.6,-42.8) circle (3);
\draw (9.6,-42.8) node {$q9$};
\draw [black] (9.6,-42.8) circle (2.4);
\draw [black] (-0.7,-25.4) -- (6.6,-25.4);
\fill [black] (6.6,-25.4) -- (5.8,-24.9) -- (5.8,-25.9);
\draw [black] (12.6,-25.4) -- (25.9,-25.4);
\fill [black] (25.9,-25.4) -- (25.1,-24.9) -- (25.1,-25.9);
\draw (19.25,-25.9) node [below] {$a$};
\draw [black] (27.17,-40.357) arc (-151.28592:-208.71408:13.024);
\fill [black] (27.17,-40.36) -- (27.22,-39.42) -- (26.35,-39.9);
\draw (25.07,-34.1) node [left] {$a$};
\draw [black] (30.655,-27.825) arc (29.21629:-29.21629:12.857);
\fill [black] (30.66,-27.82) -- (30.61,-28.77) -- (31.48,-28.28);
\draw (32.79,-34.1) node [right] {$a$};
\draw [black] (9.6,-28.4) -- (9.6,-39.8);
\fill [black] (9.6,-39.8) -- (10.1,-39) -- (9.1,-39);
\draw (9.1,-34.1) node [left] {$b$};
\draw [black] (10.923,-45.48) arc (54:-234:2.25);
\draw (9.6,-50.05) node [below] {$b$};
\fill [black] (8.28,-45.48) -- (7.4,-45.83) -- (8.21,-46.42);
\draw [black] (30.223,-45.48) arc (54:-234:2.25);
\draw (28.9,-50.05) node [below] {$b$};
\fill [black] (27.58,-45.48) -- (26.7,-45.83) -- (27.51,-46.42);
\draw [black] (11.83,-40.79) -- (26.67,-27.41);
\fill [black] (26.67,-27.41) -- (25.74,-27.57) -- (26.41,-28.32);
\draw (20.33,-34.59) node [below] {$a$};
\draw [black] (27.577,-22.72) arc (234:-54:2.25);
\draw (28.9,-18.15) node [above] {$b$};
\fill [black] (30.22,-22.72) -- (31.1,-22.37) -- (30.29,-21.78);
\end{tikzpicture}
```

## Problem 3

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (11.6,-25.4) circle (3);
\draw (11.6,-25.4) node {$q0$};
\draw [black] (11.6,-25.4) circle (2.4);
\draw [black] (28.9,-25.4) circle (3);
\draw (28.9,-25.4) node {$q1$};
\draw [black] (28.9,-25.4) circle (2.4);
\draw [black] (48.3,-25.4) circle (3);
\draw (48.3,-25.4) node {$q2$};
\draw [black] (1.3,-25.4) -- (8.6,-25.4);
\fill [black] (8.6,-25.4) -- (7.8,-24.9) -- (7.8,-25.9);
\draw [black] (14.6,-25.4) -- (25.9,-25.4);
\fill [black] (25.9,-25.4) -- (25.1,-24.9) -- (25.1,-25.9);
\draw (20.25,-25.9) node [below] {$1$};
\draw [black] (31.9,-25.4) -- (45.3,-25.4);
\fill [black] (45.3,-25.4) -- (44.5,-24.9) -- (44.5,-25.9);
\draw (38.6,-25.9) node [below] {$0,1$};
\draw [black] (10.277,-22.72) arc (234:-54:2.25);
\draw (11.6,-18.15) node [above] {$0$};
\fill [black] (12.92,-22.72) -- (13.8,-22.37) -- (12.99,-21.78);
\draw [black] (46.977,-22.72) arc (234:-54:2.25);
\draw (48.3,-18.15) node [above] {$0,1$};
\fill [black] (49.62,-22.72) -- (50.5,-22.37) -- (49.69,-21.78);
\end{tikzpicture}
```
