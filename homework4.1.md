# Homework 4.1

## Problem 1

|R|S=""|S=AAA|S=AAB|S=ABA|S=ABB|S=BAA|S=BAB|S=BBA|S=BBB|
|--|--|--|--|--|--|--|--|--|--|
|R=AA|AA|AAAAA|AAAAB|AAABA|AAABB|AABAA|AABAB|AABBA|AABBB|
|R=AAB||||||||||

So on so forth

## Problem 2

The union of the two will accept every state that appears from either.

IE: AA, AAA, BAB

## Problem 3

This will only accept states in which meet both criteria as such it will only meet criteria when len(R)%3==0

IE: AAB, "", AABBBB

## Problem 4

This will occur everytime the conditions for R is met and len(R)%3!=0

IE: AA, AABB, AABBB

## Problem 5

This occurs anytime a string of length mod 3 == 0 and either the first two characters have a B or an A appears at any point after the second character

IE: BAB, BAA, AAA

## Problem 6

This occurs every time either of the prior answers are correct

IE: Refer to prior two questions

## Problem 7

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (10,-31.1) circle (3);
\draw (10,-31.1) node {$0$};
\draw [black] (10,-31.1) circle (2.4);
\draw [black] (23,-31.1) circle (3);
\draw (23,-31.1) node {$1$};
\draw [black] (36.7,-31.1) circle (3);
\draw (36.7,-31.1) node {$10$};
\draw [black] (50.2,-31.1) circle (3);
\draw (50.2,-31.1) node {$100$};
\draw [black] (23,-42.4) circle (3);
\draw (23,-42.4) node {$11$};
\draw [black] (36.7,-42.4) circle (3);
\draw (36.7,-42.4) node {$101$};
\draw [black] (36.7,-54.3) circle (3);
\draw (36.7,-54.3) node {$110$};
\draw [black] (23,-54.3) circle (3);
\draw (23,-54.3) node {$111$};
\draw [black] (11.927,-28.803) arc (136.56339:43.43661:25.027);
\fill [black] (48.27,-28.8) -- (48.09,-27.88) -- (47.36,-28.57);
\draw (30.1,-20.48) node [above] {$0$};
\draw [black] (25.356,-29.247) arc (123.91821:56.08179:20.15);
\fill [black] (47.84,-29.25) -- (47.46,-28.39) -- (46.9,-29.22);
\draw (36.6,-25.32) node [above] {$1$};
\draw [black] (47.2,-31.1) -- (39.7,-31.1);
\fill [black] (39.7,-31.1) -- (40.5,-31.6) -- (40.5,-30.6);
\draw (43.45,-30.6) node [above] {$0$};
\draw [black] (33.7,-31.1) -- (26,-31.1);
\fill [black] (26,-31.1) -- (26.8,-31.6) -- (26.8,-30.6);
\draw (29.85,-30.6) node [above] {$0$};
\draw [black] (20,-31.1) -- (13,-31.1);
\fill [black] (13,-31.1) -- (13.8,-31.6) -- (13.8,-30.6);
\draw (16.5,-30.6) node [above] {$1$};
\draw [black] (39.06,-32.903) arc (38.66392:-38.66392:6.157);
\fill [black] (39.06,-40.6) -- (39.95,-40.28) -- (39.17,-39.66);
\draw (40.91,-36.75) node [right] {$0$};
\draw [black] (34.514,-40.385) arc (-145.92019:-214.07981:6.487);
\fill [black] (34.51,-33.12) -- (33.65,-33.5) -- (34.48,-34.06);
\draw (32.9,-36.75) node [left] {$1$};
\draw [black] (26,-42.4) -- (33.7,-42.4);
\fill [black] (33.7,-42.4) -- (32.9,-41.9) -- (32.9,-42.9);
\draw (29.85,-42.9) node [below] {$1$};
\draw [black] (36.7,-45.4) -- (36.7,-51.3);
\fill [black] (36.7,-51.3) -- (37.2,-50.5) -- (36.2,-50.5);
\draw (36.2,-48.35) node [left] {$1$};
\draw [black] (50.337,-34.095) arc (-1.19985:-59.19011:22.49);
\fill [black] (39.37,-52.94) -- (40.31,-52.96) -- (39.8,-52.1);
\draw (47.94,-46.17) node [right] {$0$};
\draw [black] (33.7,-54.3) -- (26,-54.3);
\fill [black] (26,-54.3) -- (26.8,-54.8) -- (26.8,-53.8);
\draw (29.85,-53.8) node [above] {$0$};
\draw [black] (20.32,-55.623) arc (324:36:2.25);
\draw (15.75,-54.3) node [left] {$1$};
\fill [black] (20.32,-52.98) -- (19.97,-52.1) -- (19.38,-52.91);
\draw [black] (23,-51.3) -- (23,-45.4);
\fill [black] (23,-45.4) -- (22.5,-46.2) -- (23.5,-46.2);
\draw (23.5,-48.35) node [right] {$1$};
\draw [black] (23,-39.4) -- (23,-34.1);
\fill [black] (23,-34.1) -- (22.5,-34.9) -- (23.5,-34.9);
\draw (23.5,-36.75) node [right] {$1$};
\draw [black] (34.44,-52.33) -- (25.26,-44.37);
\fill [black] (25.26,-44.37) -- (25.54,-45.27) -- (26.2,-44.51);
\draw (28.78,-48.84) node [below] {$0$};
\draw [black] (44.6,-42.4) -- (39.7,-42.4);
\fill [black] (39.7,-42.4) -- (40.5,-42.9) -- (40.5,-41.9);
\end{tikzpicture}
```
