# Homework 2.2

## Problem 1

### Part A

This consist of all words containing the letters a and b that end in ab or ba

### Part B

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (17.8,-26.2) circle (3);
\draw (17.8,-26.2) node {$q0$};
\draw [black] (28.9,-18.6) circle (3);
\draw (28.9,-18.6) node {$q1$};
\draw [black] (42.6,-18.6) circle (3);
\draw (42.6,-18.6) node {$q2$};
\draw [black] (42.6,-18.6) circle (2.4);
\draw [black] (28.9,-33) circle (3);
\draw (28.9,-33) node {$q3$};
\draw [black] (42.6,-33) circle (3);
\draw (42.6,-33) node {$q4$};
\draw [black] (42.6,-33) circle (2.4);
\draw [black] (7.5,-26.2) -- (14.8,-26.2);
\fill [black] (14.8,-26.2) -- (14,-25.7) -- (14,-26.7);
\draw [black] (18.161,-23.24) arc (-197.9865:-273.2158:7.793);
\fill [black] (26.01,-17.87) -- (25.24,-17.32) -- (25.18,-18.32);
\draw (20.11,-18.72) node [above] {$a$};
\draw [black] (31.9,-18.6) -- (39.6,-18.6);
\fill [black] (39.6,-18.6) -- (38.8,-18.1) -- (38.8,-19.1);
\draw (35.75,-19.1) node [below] {$b$};
\draw [black] (25.938,-33.371) arc (-92.76092:-150.2234:8.688);
\fill [black] (25.94,-33.37) -- (25.16,-32.83) -- (25.11,-33.83);
\draw (20.7,-32.6) node [below] {$b$};
\draw [black] (31.9,-33) -- (39.6,-33);
\fill [black] (39.6,-33) -- (38.8,-32.5) -- (38.8,-33.5);
\draw (35.75,-33.5) node [below] {$a$};
\draw [black] (26.34,-31.43) -- (20.36,-27.77);
\fill [black] (20.36,-27.77) -- (20.78,-28.61) -- (21.3,-27.76);
\draw (24.46,-29.1) node [above] {$b$};
\draw [black] (26.42,-20.29) -- (20.28,-24.51);
\fill [black] (20.28,-24.51) -- (21.22,-24.47) -- (20.65,-23.64);
\draw (22.28,-21.9) node [above] {$a$};
\draw [black] (40.671,-30.719) arc (-148.81746:-211.18254:9.501);
\fill [black] (40.67,-30.72) -- (40.68,-29.78) -- (39.83,-30.29);
\draw (38.8,-25.8) node [left] {$a$};
\draw [black] (44.531,-20.88) arc (31.20777:-31.20777:9.496);
\fill [black] (44.53,-20.88) -- (44.52,-21.82) -- (45.37,-21.31);
\draw (46.4,-25.8) node [right] {$b$};
\draw [black] (30.123,-15.87) arc (148.35774:-61.21175:11.452);
\fill [black] (30.12,-15.87) -- (30.97,-15.45) -- (30.12,-14.93);
\draw (48.7,-12.52) node [right] {$a$};
\draw [black] (45.424,-19.587) arc (63.38485:-150.53084:11.678);
\fill [black] (30.03,-35.77) -- (29.98,-36.71) -- (30.85,-36.22);
\draw (49.18,-39.54) node [right] {$b$};
\end{tikzpicture}
```

### Part C

|State|A|B|
|--|--|--|
|q0|q1|q3|
|q1|q0|q2|
|q2*|q3|q4|
|q3|q4|q0|
|q4*|q1|q2|

## Problem 2

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (17.8,-26.2) circle (3);
\draw (17.8,-26.2) node {$q0$};
\draw [black] (30.1,-26.2) circle (3);
\draw (30.1,-26.2) node {$q1$};
\draw [black] (43,-26.2) circle (3);
\draw (43,-26.2) node {$q2$};
\draw [black] (43,-26.2) circle (2.4);
\draw [black] (30.1,-16.2) circle (3);
\draw (30.1,-16.2) node {$q3$};
\draw [black] (43,-16.2) circle (3);
\draw (43,-16.2) node {$q4$};
\draw [black] (43,-16.2) circle (2.4);
\draw [black] (7.5,-26.2) -- (14.8,-26.2);
\fill [black] (14.8,-26.2) -- (14,-25.7) -- (14,-26.7);
\draw [black] (20.8,-26.2) -- (27.1,-26.2);
\fill [black] (27.1,-26.2) -- (26.3,-25.7) -- (26.3,-26.7);
\draw (23.95,-26.7) node [below] {$b$};
\draw [black] (33.1,-26.2) -- (40,-26.2);
\fill [black] (40,-26.2) -- (39.2,-25.7) -- (39.2,-26.7);
\draw (36.55,-26.7) node [below] {$b$};
\draw [black] (45.68,-24.877) arc (144:-144:2.25);
\draw (50.25,-26.2) node [right] {$a,b$};
\fill [black] (45.68,-27.52) -- (46.03,-28.4) -- (46.62,-27.59);
\draw [black] (33.1,-16.2) -- (40,-16.2);
\fill [black] (40,-16.2) -- (39.2,-15.7) -- (39.2,-16.7);
\draw (36.55,-16.7) node [below] {$b$};
\draw [black] (20.13,-24.31) -- (27.77,-18.09);
\fill [black] (27.77,-18.09) -- (26.84,-18.21) -- (27.47,-18.99);
\draw (25.02,-21.69) node [below] {$a$};
\draw [black] (16.477,-23.52) arc (234:-54:2.25);
\draw (17.8,-18.95) node [above] {$a,b$};
\fill [black] (19.12,-23.52) -- (20,-23.17) -- (19.19,-22.58);
\end{tikzpicture}
```

## Problem 3

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (17.8,-26.2) circle (3);
\draw (17.8,-26.2) node {$q0$};
\draw [black] (39.5,-18.4) circle (3);
\draw (39.5,-18.4) node {$*ab$};
\draw [black] (39.5,-18.4) circle (2.4);
\draw [black] (39.5,-32.8) circle (3);
\draw (39.5,-32.8) node {$*bb*$};
\draw [black] (39.5,-32.8) circle (2.4);
\draw [black] (28,-18.4) circle (3);
\draw (28,-18.4) node {$*a$};
\draw [black] (28,-32.8) circle (3);
\draw (28,-32.8) node {$*b$};
\draw [black] (7.5,-26.2) -- (14.8,-26.2);
\fill [black] (14.8,-26.2) -- (14,-25.7) -- (14,-26.7);
\draw [black] (39.5,-21.4) -- (39.5,-29.8);
\fill [black] (39.5,-29.8) -- (40,-29) -- (39,-29);
\draw (39,-25.6) node [left] {$b$};
\draw [black] (17.61,-23.23) arc (-188.82178:-276.36751:6.89);
\fill [black] (25.18,-17.44) -- (24.44,-16.85) -- (24.33,-17.85);
\draw (19.17,-18.32) node [above] {$a$};
\draw [black] (25.141,-33.63) arc (-86.25259:-159.5579:6.91);
\fill [black] (25.14,-33.63) -- (24.31,-33.18) -- (24.38,-34.18);
\draw (19.82,-33.04) node [below] {$b$};
\draw [black] (31,-32.8) -- (36.5,-32.8);
\fill [black] (36.5,-32.8) -- (35.7,-32.3) -- (35.7,-33.3);
\draw (33.75,-33.3) node [below] {$b$};
\draw [black] (42.18,-31.477) arc (144:-144:2.25);
\draw (46.75,-32.8) node [right] {$a,b$};
\fill [black] (42.18,-34.12) -- (42.53,-35) -- (43.12,-34.19);
\draw [black] (28,-29.8) -- (28,-21.4);
\fill [black] (28,-21.4) -- (27.5,-22.2) -- (28.5,-22.2);
\draw (27.5,-25.6) node [left] {$a$};
\draw [black] (36.89,-19.853) arc (-70.1803:-109.8197:9.261);
\fill [black] (36.89,-19.85) -- (35.97,-19.65) -- (36.31,-20.59);
\draw (33.75,-20.9) node [below] {$b$};
\draw [black] (26.677,-15.72) arc (234:-54:2.25);
\draw (28,-11.15) node [above] {$a$};
\fill [black] (29.32,-15.72) -- (30.2,-15.37) -- (29.39,-14.78);
\draw [black] (30.609,-16.946) arc (109.84242:70.15758:9.253);
\fill [black] (30.61,-16.95) -- (31.53,-17.14) -- (31.19,-16.2);
\draw (33.75,-15.9) node [above] {$a$};
\end{tikzpicture}
```

## Problem 4

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (17.8,-26.2) circle (3);
\draw (17.8,-26.2) node {$q0$};
\draw [black] (36.5,-18.7) circle (3);
\draw (36.5,-18.7) node {$aa$};
\draw [black] (36.5,-34.5) circle (3);
\draw (36.5,-34.5) node {$bb$};
\draw [black] (59.2,-34.5) circle (3);
\draw (59.2,-34.5) node {$bbaa$};
\draw [black] (59.2,-34.5) circle (2.4);
\draw [black] (47.2,-18.7) circle (3);
\draw (47.2,-18.7) node {$aab$};
\draw [black] (27,-18.7) circle (3);
\draw (27,-18.7) node {$a$};
\draw [black] (59.2,-18.7) circle (3);
\draw (59.2,-18.7) node {$aabb$};
\draw [black] (59.2,-18.7) circle (2.4);
\draw [black] (27,-34.5) circle (3);
\draw (27,-34.5) node {$b$};
\draw [black] (47.2,-34.5) circle (3);
\draw (47.2,-34.5) node {$bba$};
\draw [black] (7.5,-26.2) -- (14.8,-26.2);
\fill [black] (14.8,-26.2) -- (14,-25.7) -- (14,-26.7);
\draw [black] (35.177,-16.02) arc (234:-54:2.25);
\draw (36.5,-11.45) node [above] {$a,b$};
\fill [black] (37.82,-16.02) -- (38.7,-15.67) -- (37.89,-15.08);
\draw [black] (37.823,-37.18) arc (54:-234:2.25);
\draw (36.5,-41.75) node [below] {$a,b$};
\fill [black] (35.18,-37.18) -- (34.3,-37.53) -- (35.11,-38.12);
\draw [black] (60.523,-37.18) arc (54:-234:2.25);
\draw (59.2,-41.75) node [below] {$a,b$};
\fill [black] (57.88,-37.18) -- (57,-37.53) -- (57.81,-38.12);
\draw [black] (57.877,-16.02) arc (234:-54:2.25);
\draw (59.2,-11.45) node [above] {$a,b$};
\fill [black] (60.52,-16.02) -- (61.4,-15.67) -- (60.59,-15.08);
\draw [black] (39.5,-18.7) -- (44.2,-18.7);
\fill [black] (44.2,-18.7) -- (43.4,-18.2) -- (43.4,-19.2);
\draw (41.85,-19.2) node [below] {$b$};
\draw [black] (50.2,-18.7) -- (56.2,-18.7);
\fill [black] (56.2,-18.7) -- (55.4,-18.2) -- (55.4,-19.2);
\draw (53.2,-19.2) node [below] {$b$};
\draw [black] (39.5,-34.5) -- (44.2,-34.5);
\fill [black] (44.2,-34.5) -- (43.4,-34) -- (43.4,-35);
\draw (41.85,-35) node [below] {$a$};
\draw [black] (50.2,-34.5) -- (56.2,-34.5);
\fill [black] (56.2,-34.5) -- (55.4,-34) -- (55.4,-35);
\draw (53.2,-35) node [below] {$a$};
\draw [black] (20.03,-28.21) -- (24.77,-32.49);
\fill [black] (24.77,-32.49) -- (24.51,-31.58) -- (23.84,-32.33);
\draw (21.27,-30.84) node [below] {$b$};
\draw [black] (30,-34.5) -- (33.5,-34.5);
\fill [black] (33.5,-34.5) -- (32.7,-34) -- (32.7,-35);
\draw (31.75,-35) node [below] {$b$};
\draw [black] (20.13,-24.3) -- (24.67,-20.6);
\fill [black] (24.67,-20.6) -- (23.74,-20.71) -- (24.37,-21.49);
\draw (23.47,-22.94) node [below] {$a$};
\draw [black] (30,-18.7) -- (33.5,-18.7);
\fill [black] (33.5,-18.7) -- (32.7,-18.2) -- (32.7,-19.2);
\draw (31.75,-19.2) node [below] {$a$};
\draw [black] (16.477,-23.52) arc (234:-54:2.25);
\draw (17.8,-18.95) node [above] {$a,b$};
\fill [black] (19.12,-23.52) -- (20,-23.17) -- (19.19,-22.58);
\end{tikzpicture}
```

## Problem 5

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (17.4,-26.2) circle (3);
\draw (17.4,-26.2) node {$q0$};
\draw [black] (31.5,-26.2) circle (3);
\draw (31.5,-26.2) node {$a$};
\draw [black] (44.4,-26.2) circle (3);
\draw (44.4,-26.2) node {$ab$};
\draw [black] (44.4,-26.2) circle (2.4);
\draw [black] (57.4,-26.2) circle (3);
\draw (57.4,-26.2) node {$aba*$};
\draw [black] (57.4,-26.2) circle (2.4);
\draw [black] (7.1,-26.2) -- (14.4,-26.2);
\fill [black] (14.4,-26.2) -- (13.6,-25.7) -- (13.6,-26.7);
\draw [black] (16.077,-23.52) arc (234:-54:2.25);
\draw (17.4,-18.95) node [above] {$b$};
\fill [black] (18.72,-23.52) -- (19.6,-23.17) -- (18.79,-22.58);
\draw [black] (20.4,-26.2) -- (28.5,-26.2);
\fill [black] (28.5,-26.2) -- (27.7,-25.7) -- (27.7,-26.7);
\draw (24.45,-25.7) node [above] {$a$};
\draw [black] (34.5,-26.2) -- (41.4,-26.2);
\fill [black] (41.4,-26.2) -- (40.6,-25.7) -- (40.6,-26.7);
\draw (37.95,-26.7) node [below] {$b$};
\draw [black] (47.182,-25.093) arc (105.50969:74.49031:13.904);
\fill [black] (54.62,-25.09) -- (53.98,-24.4) -- (53.71,-25.36);
\draw (50.9,-24.09) node [above] {$a$};
\draw [black] (54.791,-27.662) arc (-68.74614:-111.25386:10.735);
\fill [black] (47.01,-27.66) -- (47.57,-28.42) -- (47.94,-27.49);
\draw (50.9,-28.89) node [below] {$b$};
\draw [black] (56.077,-23.52) arc (234:-54:2.25);
\draw (57.4,-18.95) node [above] {$a$};
\fill [black] (58.72,-23.52) -- (59.6,-23.17) -- (58.79,-22.58);
\draw [black] (43.537,-29.067) arc (-23.02013:-156.97987:13.73);
\fill [black] (18.26,-29.07) -- (18.12,-30) -- (19.04,-29.61);
\draw (30.9,-37.93) node [below] {$b$};
\draw [black] (30.177,-23.52) arc (234:-54:2.25);
\draw (31.5,-18.95) node [above] {$a$};
\fill [black] (32.82,-23.52) -- (33.7,-23.17) -- (32.89,-22.58);
\end{tikzpicture}
```

## Problem 6

### Graph

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (18.4,-26.2) circle (3);
\draw (18.4,-26.2) node {$q0$};
\draw [black] (31.5,-26.2) circle (3);
\draw (31.5,-26.2) node {$a$};
\draw [black] (31.5,-26.2) circle (2.4);
\draw [black] (43.8,-26.2) circle (3);
\draw (43.8,-26.2) node {$b$};
\draw [black] (43.8,-26.2) circle (2.4);
\draw [black] (8.1,-26.2) -- (15.4,-26.2);
\fill [black] (15.4,-26.2) -- (14.6,-25.7) -- (14.6,-26.7);
\draw [black] (21.4,-26.2) -- (28.5,-26.2);
\fill [black] (28.5,-26.2) -- (27.7,-25.7) -- (27.7,-26.7);
\draw (24.95,-26.7) node [below] {$a$};
\draw [black] (34.5,-26.2) -- (40.8,-26.2);
\fill [black] (40.8,-26.2) -- (40,-25.7) -- (40,-26.7);
\draw (37.65,-26.7) node [below] {$b$};
\draw [black] (42.477,-23.52) arc (234:-54:2.25);
\draw (43.8,-18.95) node [above] {$b$};
\fill [black] (45.12,-23.52) -- (46,-23.17) -- (45.19,-22.58);
\end{tikzpicture}
```

### Transition Complement

|state|a|b|
|-|-|-|
|q0|q1|q3|
|q1|q2|q1|
|q2*|q2|q2|
|q3*|q3|q3|
