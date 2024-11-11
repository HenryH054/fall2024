# Homework 8.2

## Problem 1

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (17,-30.8) circle (3);
\draw (17,-30.8) node {$q_0$};
\draw [black] (32.4,-30.8) circle (3);
\draw (32.4,-30.8) node {$q_1$};
\draw [black] (49.1,-30.8) circle (3);
\draw (49.1,-30.8) node {$q_2$};
\draw [black] (67.5,-30.8) circle (3);
\draw (67.5,-30.8) node {$q_3$};
\draw [black] (67.5,-30.8) circle (2.4);
\draw [black] (9.2,-30.8) -- (14,-30.8);
\fill [black] (14,-30.8) -- (13.2,-30.3) -- (13.2,-31.3);
\draw [black] (20,-30.8) -- (29.4,-30.8);
\fill [black] (29.4,-30.8) -- (28.6,-30.3) -- (28.6,-31.3);
\draw (24.7,-31.3) node [below] {$1/"\mbox{ }",\mbox{ }\rightarrow$};
\draw [black] (35.4,-30.8) -- (46.1,-30.8);
\fill [black] (46.1,-30.8) -- (45.3,-30.3) -- (45.3,-31.3);
\draw (40.75,-31.3) node [below] {$0/1,\mbox{ }\rightarrow$};
\draw [black] (52.1,-30.8) -- (64.5,-30.8);
\fill [black] (64.5,-30.8) -- (63.7,-30.3) -- (63.7,-31.3);
\draw (58.3,-31.3) node [below] {$1/1\mbox{ }\rightarrow$};
\draw [black] (31.077,-28.12) arc (234:-54:2.25);
\draw (32.4,-23.55) node [above] {$1/1,\mbox{ }\rightarrow$};
\fill [black] (33.72,-28.12) -- (34.6,-27.77) -- (33.79,-27.18);
\end{tikzpicture}
```

## Problem 2

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (29.4,-30.8) circle (3);
\draw (29.4,-30.8) node {$q_0$};
\draw [black] (29.4,-15) circle (3);
\draw (29.4,-15) node {$q_1$};
\draw [black] (59.3,-14.1) circle (3);
\draw (59.3,-14.1) node {$q_2$};
\draw [black] (59.3,-30.8) circle (3);
\draw (59.3,-30.8) node {$q_3$};
\draw [black] (29.4,-48.2) circle (3);
\draw (29.4,-48.2) node {$Yes$};
\draw [black] (59.3,-48.2) circle (3);
\draw (59.3,-48.2) node {$no$};
\draw [black] (44.4,-42.4) circle (3);
\draw (44.4,-42.4) node {$q_4$};
\draw [black] (29.4,-27.8) -- (29.4,-18);
\fill [black] (29.4,-18) -- (28.9,-18.8) -- (29.9,-18.8);
\draw (29.9,-22.9) node [right] {$1/X,\mbox{ }\rightarrow$};
\draw [black] (28.077,-12.32) arc (234:-54:2.25);
\draw (29.4,-7.75) node [above] {$1/1,\mbox{ }/rightarrow$};
\fill [black] (30.72,-12.32) -- (31.6,-11.97) -- (30.79,-11.38);
\draw [black] (32.4,-14.91) -- (56.3,-14.19);
\fill [black] (56.3,-14.19) -- (55.49,-13.71) -- (55.52,-14.71);
\draw (44.48,-15.25) node [below] {$0/0,\mbox{ }\rightarrow$};
\draw [black] (59.3,-17.1) -- (59.3,-27.8);
\fill [black] (59.3,-27.8) -- (59.8,-27) -- (58.8,-27);
\draw (58.8,-22.45) node [left] {$1/Y,\mbox{ }\rightarrow$};
\draw [black] (57.977,-11.42) arc (234:-54:2.25);
\draw (59.3,-6.85) node [above] {$Y/Y\mbox{ }\rightarrow$};
\fill [black] (60.62,-11.42) -- (61.5,-11.07) -- (60.69,-10.48);
\draw [black] (21.1,-36.8) -- (26.97,-32.56);
\fill [black] (26.97,-32.56) -- (26.03,-32.62) -- (26.61,-33.43);
\draw [black] (61.98,-29.477) arc (144:-144:2.25);
\draw (66.55,-30.8) node [right] {$1/1,\mbox{ }\leftarrow\mbox{ }|\mbox{ }0\0,\mbox{ }\leftarrow\mbox{ }|\mbox{ }Y/Y\mbox{ }\leftarrow$};
\fill [black] (61.98,-32.12) -- (62.33,-33) -- (62.92,-32.19);
\draw [black] (56.3,-30.8) -- (32.4,-30.8);
\fill [black] (32.4,-30.8) -- (33.2,-31.3) -- (33.2,-30.3);
\draw (44.35,-30.3) node [above] {$X/X,\mbox{ }\rightarrow$};
\draw [black] (26.72,-32.123) arc (-36:-324:2.25);
\draw (22.15,-30.8) node [left] {$X/X,\mbox{ }\rightarrow$};
\fill [black] (26.72,-29.48) -- (26.37,-28.6) -- (25.78,-29.41);
\draw [black] (31.77,-32.64) -- (42.03,-40.56);
\fill [black] (42.03,-40.56) -- (41.7,-39.68) -- (41.09,-40.47);
\draw (29.9,-37.1) node [below] {$0/X,\mbox{ }\rightarrow$};
\draw [black] (43.077,-39.72) arc (234:-54:2.25);
\draw (44.4,-35.15) node [above] {$Y/Y,\mbox{ }\rightarrow$};
\fill [black] (45.72,-39.72) -- (46.6,-39.37) -- (45.79,-38.78);
\draw [black] (41.6,-43.48) -- (32.2,-47.12);
\fill [black] (32.2,-47.12) -- (33.12,-47.3) -- (32.76,-46.36);
\draw (29.41,-44.64) node [above] {$"\mbox{ }"/"\mbox{ }",\mbox{ }\rightarrow$};
\draw [black] (47.2,-43.49) -- (56.5,-47.11);
\fill [black] (56.5,-47.11) -- (55.94,-46.36) -- (55.58,-47.29);
\draw (45.42,-45.94) node [below] {$1/1,\mbox{ }\rightarrow$};
\draw [black] (61.842,-12.512) arc (117.91461:-117.91461:21.092);
\fill [black] (61.84,-49.79) -- (62.32,-50.6) -- (62.78,-49.72);
\draw (93.31,-31.15) node [right] {$"\mbox{ }"/"\mbox{ }",\mbox{ }\leftarrow$};
\end{tikzpicture}
```

## Problem 3

1011
q1 X011
q2 X011
q3 X0Y1
q0 X0Y1
q4 XXY1
q4 XXY1
no XXY1

10
q1 x0
q2 x0
no x0

## Problem 4
