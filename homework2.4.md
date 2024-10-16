# Homework 2.4

## Problem 1

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (10.3,-39.1) circle (3);
\draw (10.3,-39.1) node {$q0$};
\draw [black] (23.3,-39.1) circle (3);
\draw (23.3,-39.1) node {$1$};
\draw [black] (37.6,-39.1) circle (3);
\draw (37.6,-39.1) node {$10$};
\draw [black] (51.4,-39.1) circle (3);
\draw (51.4,-39.1) node {$100$};
\draw [black] (65.1,-39.1) circle (3);
\draw (65.1,-39.1) node {$1001$};
\draw [black] (0,-39.1) -- (7.3,-39.1);
\fill [black] (7.3,-39.1) -- (6.5,-38.6) -- (6.5,-39.6);
\draw [black] (13.3,-39.1) -- (20.3,-39.1);
\fill [black] (20.3,-39.1) -- (19.5,-38.6) -- (19.5,-39.6);
\draw (16.8,-39.6) node [below] {$1/0$};
\draw [black] (26.3,-39.1) -- (34.6,-39.1);
\fill [black] (34.6,-39.1) -- (33.8,-38.6) -- (33.8,-39.6);
\draw (30.45,-39.6) node [below] {$0/0$};
\draw [black] (40.6,-39.1) -- (48.4,-39.1);
\fill [black] (48.4,-39.1) -- (47.6,-38.6) -- (47.6,-39.6);
\draw (44.5,-39.6) node [below] {$0/0$};
\draw [black] (54.4,-39.1) -- (62.1,-39.1);
\fill [black] (62.1,-39.1) -- (61.3,-38.6) -- (61.3,-39.6);
\draw (58.25,-39.6) node [below] {$1/1$};
\draw [black] (10.726,-36.132) arc (168.70835:11.29165:27.506);
\fill [black] (10.73,-36.13) -- (11.37,-35.45) -- (10.39,-35.25);
\draw (37.7,-13.51) node [above] {$0/0;1/0$};
\draw [black] (11.623,-41.78) arc (54:-234:2.25);
\draw (10.3,-46.35) node [below] {$0/0$};
\fill [black] (8.98,-41.78) -- (8.1,-42.13) -- (8.91,-42.72);
\draw [black] (21.977,-36.42) arc (234:-54:2.25);
\draw (23.3,-31.85) node [above] {$1/0$};
\fill [black] (24.62,-36.42) -- (25.5,-36.07) -- (24.69,-35.48);
\draw [black] (38.036,-42.048) arc (-2.90265:-177.09735:7.596);
\fill [black] (22.86,-42.05) -- (22.41,-42.87) -- (23.4,-42.82);
\draw (30.45,-49.76) node [below] {$1/0$};
\draw [black] (10.623,-36.12) arc (169.64028:10.35972:20.563);
\fill [black] (10.62,-36.12) -- (11.26,-35.42) -- (10.27,-35.24);
\draw (30.85,-18.76) node [above] {$0/0$};
\end{tikzpicture}
```

## Problem 2

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (10,-31.1) circle (3);
\draw (10,-31.1) node {$q0$};
\draw [black] (18.9,-20) circle (3);
\draw (18.9,-20) node {$b$};
\draw [black] (18.9,-43.1) circle (3);
\draw (18.9,-43.1) node {$a$};
\draw [black] (35.5,-20) circle (3);
\draw (35.5,-20) node {$ba$};
\draw [black] (35.5,-43.1) circle (3);
\draw (35.5,-43.1) node {$ab$};
\draw [black] (26.9,-31.1) circle (3);
\draw (26.9,-31.1) node {$a*b*\$$};
\draw [black] (-0.3,-31.1) -- (7,-31.1);
\fill [black] (7,-31.1) -- (6.2,-30.6) -- (6.2,-31.6);
\draw [black] (11.88,-28.76) -- (17.02,-22.34);
\fill [black] (17.02,-22.34) -- (16.13,-22.65) -- (16.91,-23.28);
\draw (15.01,-26.97) node [right] {$a/b$};
\draw [black] (11.79,-33.51) -- (17.11,-40.69);
\fill [black] (17.11,-40.69) -- (17.04,-39.75) -- (16.23,-40.35);
\draw (13.87,-38.49) node [left] {$b/a$};
\draw [black] (17.577,-17.32) arc (234:-54:2.25);
\draw (18.9,-12.75) node [above] {$b/b$};
\fill [black] (20.22,-17.32) -- (21.1,-16.97) -- (20.29,-16.38);
\draw [black] (32.839,-21.375) arc (-68.30636:-111.69364:15.255);
\fill [black] (32.84,-21.37) -- (31.91,-21.21) -- (32.28,-22.14);
\draw (27.2,-22.96) node [below] {$a/b$};
\draw [black] (21.494,-18.505) arc (113.86788:66.13212:14.101);
\fill [black] (21.49,-18.5) -- (22.43,-18.64) -- (22.02,-17.72);
\draw (27.2,-16.8) node [above] {$b/a$};
\draw [black] (34.177,-17.32) arc (234:-54:2.25);
\draw (35.5,-12.75) node [above] {$a/a$};
\fill [black] (36.82,-17.32) -- (37.7,-16.97) -- (36.89,-16.38);
\draw [black] (32.835,-44.467) arc (-68.44787:-111.55213:15.339);
\fill [black] (32.83,-44.47) -- (31.91,-44.3) -- (32.27,-45.23);
\draw (27.2,-46.04) node [below] {$b/a$};
\draw [black] (21.522,-41.653) arc (112.98368:67.01632:14.542);
\fill [black] (21.52,-41.65) -- (22.45,-41.8) -- (22.06,-40.88);
\draw (27.2,-40) node [above] {$a/b$};
\draw [black] (20.56,-40.6) -- (25.24,-33.6);
\fill [black] (25.24,-33.6) -- (24.38,-33.98) -- (25.21,-34.54);
\draw (22.29,-35.77) node [left] {$\$/b$};
\draw [black] (33.75,-40.66) -- (28.65,-33.54);
\fill [black] (28.65,-33.54) -- (28.71,-34.48) -- (29.52,-33.9);
\draw (31.79,-35.72) node [right] {$\$/b$};
\draw [black] (20.65,-22.43) -- (25.15,-28.67);
\fill [black] (25.15,-28.67) -- (25.08,-27.72) -- (24.27,-28.31);
\draw (22.31,-26.93) node [left] {$\$/a$};
\draw [black] (33.66,-22.37) -- (28.74,-28.73);
\fill [black] (28.74,-28.73) -- (29.62,-28.4) -- (28.83,-27.79);
\draw (31.77,-26.96) node [right] {$\$/a$};
\draw [black] (20.223,-45.78) arc (54:-234:2.25);
\draw (18.9,-50.35) node [below] {$a/a$};
\fill [black] (17.58,-45.78) -- (16.7,-46.13) -- (17.51,-46.72);
\draw [black] (36.823,-45.78) arc (54:-234:2.25);
\draw (35.5,-50.35) node [below] {$b/b$};
\fill [black] (34.18,-45.78) -- (33.3,-46.13) -- (34.11,-46.72);
\end{tikzpicture}
```

## Problem 3

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (10,-31.1) circle (3);
\draw (10,-31.1) node {$q0$};
\draw [black] (24.3,-31.1) circle (3);
\draw (24.3,-31.1) node {$q1$};
\draw [black] (39.7,-31.1) circle (3);
\draw (39.7,-31.1) node {$q2$};
\draw [black] (56,-31.1) circle (3);
\draw (56,-31.1) node {$q3$};
\draw [black] (-0.3,-31.1) -- (7,-31.1);
\fill [black] (7,-31.1) -- (6.2,-30.6) -- (6.2,-31.6);
\draw [black] (13,-31.1) -- (21.3,-31.1);
\fill [black] (21.3,-31.1) -- (20.5,-30.6) -- (20.5,-31.6);
\draw (17.15,-31.6) node [below] {$a/1;b/1$};
\draw [black] (27.3,-31.1) -- (36.7,-31.1);
\fill [black] (36.7,-31.1) -- (35.9,-30.6) -- (35.9,-31.6);
\draw (32,-31.6) node [below] {$a/1;b/0$};
\draw [black] (39.475,-28.124) arc (-185.87496:-354.12504:8.42);
\fill [black] (56.23,-28.12) -- (56.64,-27.28) -- (55.65,-27.38);
\draw (47.85,-20.07) node [above] {$a/0;b/0$};
\draw [black] (56.539,-34.036) arc (0.50286:-180.50286:8.689);
\fill [black] (39.16,-34.04) -- (38.65,-34.83) -- (39.65,-34.84);
\draw (47.85,-43.3) node [below] {$a/1;b/1$};
\end{tikzpicture}
```
