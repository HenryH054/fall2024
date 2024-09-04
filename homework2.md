# Homework 2

## Problem 1

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (19.2,-23.6) circle (3);
\draw (19.2,-23.6) node {$q0$};
\draw [black] (31.5,-23.6) circle (3);
\draw (31.5,-23.6) node {$q1$};
\draw [black] (41.9,-23.7) circle (3);
\draw (41.9,-23.7) node {$q2*$};
\draw [black] (52,-23.9) circle (3);
\draw (52,-23.9) node {$q3$};
\draw [black] (62.2,-23.9) circle (3);
\draw (62.2,-23.9) node {$q4$};
\draw [black] (17.877,-20.92) arc (234:-54:2.25);
\draw (19.2,-16.35) node [above] {$a$};
\fill [black] (20.52,-20.92) -- (21.4,-20.57) -- (20.59,-19.98);
\draw [black] (22.2,-23.6) -- (28.5,-23.6);
\fill [black] (28.5,-23.6) -- (27.7,-23.1) -- (27.7,-24.1);
\draw (25.35,-24.1) node [below] {$b$};
\draw [black] (30.177,-20.92) arc (234:-54:2.25);
\draw (31.5,-16.35) node [above] {$a$};
\fill [black] (32.82,-20.92) -- (33.7,-20.57) -- (32.89,-19.98);
\draw [black] (39.577,-25.557) arc (-64.4259:-116.6759:6.575);
\fill [black] (39.58,-25.56) -- (38.64,-25.45) -- (39.07,-26.35);
\draw (36.67,-26.71) node [below] {$b$};
\draw [black] (33.612,-21.513) arc (120.42239:58.4758:6.039);
\fill [black] (33.61,-21.51) -- (34.56,-21.54) -- (34.05,-20.68);
\draw (36.73,-20.17) node [above] {$a$};
\draw [black] (49.673,-25.748) arc (-65.17273:-117.09612:6.307);
\fill [black] (49.67,-25.75) -- (48.74,-25.63) -- (49.16,-26.54);
\draw (46.89,-26.85) node [below] {$a$};
\draw [black] (44.172,-21.786) arc (116.13268:61.59848:6.15);
\fill [black] (44.17,-21.79) -- (45.11,-21.88) -- (44.67,-20.99);
\draw (47.01,-20.64) node [above] {$a$};
\draw [black] (59.838,-25.708) arc (-65.55882:-114.44118:6.617);
\fill [black] (59.84,-25.71) -- (58.9,-25.58) -- (59.32,-26.49);
\draw (57.1,-26.8) node [below] {$b$};
\draw [black] (60.877,-21.22) arc (234:-54:2.25);
\draw (62.2,-16.65) node [above] {$b$};
\fill [black] (63.52,-21.22) -- (64.4,-20.87) -- (63.59,-20.28);
\draw [black] (54.107,-21.809) arc (120.29334:59.70666:5.934);
\fill [black] (54.11,-21.81) -- (55.05,-21.84) -- (54.55,-20.97);
\draw (57.1,-20.5) node [above] {$a$};
\end{tikzpicture}
```

## Problem 2

### Part a

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (19.2,-23.6) circle (3);
\draw (19.2,-23.6) node {$q0$};
\draw [black] (19.2,-12.1) circle (3);
\draw (19.2,-12.1) node {$q1$};
\draw [black] (32.4,-23.6) circle (3);
\draw (32.4,-23.6) node {$q2$};
\draw [black] (46.5,-23.6) circle (3);
\draw (46.5,-23.6) node {$q3*$};
\draw [black] (22.2,-23.6) -- (29.4,-23.6);
\fill [black] (29.4,-23.6) -- (28.6,-23.1) -- (28.6,-24.1);
\draw (25.8,-23.1) node [above] {$1$};
\draw [black] (19.2,-20.6) -- (19.2,-15.1);
\fill [black] (19.2,-15.1) -- (18.7,-15.9) -- (19.7,-15.9);
\draw (19.7,-17.85) node [right] {$0$};
\draw [black] (17.877,-9.42) arc (234:-54:2.25);
\draw (19.2,-4.85) node [above] {$0,1$};
\fill [black] (20.52,-9.42) -- (21.4,-9.07) -- (20.59,-8.48);
\draw [black] (43.772,-24.835) arc (-71.83579:-108.16421:13.866);
\fill [black] (43.77,-24.84) -- (42.86,-24.61) -- (43.17,-25.56);
\draw (39.45,-26.03) node [below] {$0$};
\draw [black] (34.96,-22.053) arc (113.50866:66.49134:11.256);
\fill [black] (34.96,-22.05) -- (35.89,-22.19) -- (35.49,-21.28);
\draw (39.45,-20.62) node [above] {$1$};
\draw [black] (31.077,-20.92) arc (234:-54:2.25);
\draw (32.4,-16.35) node [above] {$1$};
\fill [black] (33.72,-20.92) -- (34.6,-20.57) -- (33.79,-19.98);
\end{tikzpicture}
```

### Part b

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (19.2,-23.6) circle (3);
\draw (19.2,-23.6) node {$q0$};
\draw [black] (32.4,-23.6) circle (3);
\draw (32.4,-23.6) node {$q1$};
\draw [black] (43.8,-23.6) circle (3);
\draw (43.8,-23.6) node {$q2$};
\draw [black] (32.4,-35.5) circle (3);
\draw (32.4,-35.5) node {$q3$};
\draw [black] (43.8,-35.5) circle (3);
\draw (43.8,-35.5) node {$q4$};
\draw [black] (21.867,-22.245) arc (109.6027:70.3973:11.722);
\fill [black] (29.73,-22.24) -- (29.15,-21.51) -- (28.81,-22.45);
\draw (25.8,-21.07) node [above] {$a$};
\draw [black] (35.4,-23.6) -- (40.8,-23.6);
\fill [black] (40.8,-23.6) -- (40,-23.1) -- (40,-24.1);
\draw (38.1,-23.1) node [above] {$a$};
\draw [black] (17.555,-21.105) arc (241.12502:-46.87498:2.25);
\draw (18.05,-16.3) node [above] {$b$};
\fill [black] (20.18,-20.78) -- (21,-20.32) -- (20.13,-19.83);
\draw [black] (29.933,-25.286) arc (-64.58366:-115.41634:9.63);
\fill [black] (21.67,-25.29) -- (22.18,-26.08) -- (22.6,-25.18);
\draw (25.8,-26.72) node [below] {$b$};
\draw [black] (42.477,-20.92) arc (234:-54:2.25);
\draw (43.8,-16.35) node [above] {$b$};
\fill [black] (45.12,-20.92) -- (46,-20.57) -- (45.19,-19.98);
\draw [black] (33.505,-32.715) arc (153.65151:118.80716:18.249);
\fill [black] (33.51,-32.71) -- (34.31,-32.22) -- (33.41,-31.78);
\draw (36.15,-26.72) node [left] {$a$};
\draw [black] (35.4,-35.5) -- (40.8,-35.5);
\fill [black] (40.8,-35.5) -- (40,-35) -- (40,-36);
\draw (38.1,-36) node [below] {$a$};
\draw [black] (45.445,-37.995) arc (61.12502:-226.87498:2.25);
\draw (45.17,-42.87) node [below] {$a,b$};
\fill [black] (42.82,-38.32) -- (42,-38.78) -- (42.87,-39.27);
\draw [black] (42.534,-26.317) arc (-29.03223:-58.5091:21.233);
\fill [black] (42.53,-26.32) -- (41.71,-26.77) -- (42.58,-27.26);
\draw (39.83,-32.17) node [right] {$b$};
\end{tikzpicture}
```

### Part C

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (19.2,-23.6) circle (3);
\draw (19.2,-23.6) node {$q0*$};
\draw [black] (30,-23.6) circle (3);
\draw (30,-23.6) node {$q1$};
\draw [black] (24.6,-10.7) circle (3);
\draw (24.6,-10.7) node {$q2$};
\draw [black] (17.877,-20.92) arc (234:-54:2.25);
\draw (19.2,-16.35) node [above] {$a,c$};
\fill [black] (20.52,-20.92) -- (21.4,-20.57) -- (20.59,-19.98);
\draw [black] (21.82,-22.169) arc (108.72013:71.27987:8.663);
\fill [black] (27.38,-22.17) -- (26.78,-21.44) -- (26.46,-22.39);
\draw (24.6,-21.21) node [above] {$b$};
\draw [black] (27.435,-25.124) arc (-69.7644:-110.2356:8.197);
\fill [black] (21.76,-25.12) -- (22.34,-25.87) -- (22.69,-24.93);
\draw (24.6,-26.13) node [below] {$c$};
\draw [black] (28.84,-20.83) -- (25.76,-13.47);
\fill [black] (25.76,-13.47) -- (25.61,-14.4) -- (26.53,-14.01);
\draw (28.04,-16.22) node [right] {$a,b$};
\draw [black] (23.277,-8.02) arc (234:-54:2.25);
\draw (24.6,-3.45) node [above] {$a,b,c$};
\fill [black] (25.92,-8.02) -- (26.8,-7.67) -- (25.99,-7.08);
\end{tikzpicture}
```

## Problem 3

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (18.8,-23.3) circle (3);
\draw (18.8,-23.3) node {$q0$};
\draw [black] (30.7,-23.3) circle (3);
\draw (30.7,-23.3) node {$q1$};
\draw [black] (42.6,-23.3) circle (3);
\draw (42.6,-23.3) node {$q2$};
\draw [black] (54.3,-23.3) circle (3);
\draw (54.3,-23.3) node {$q3*$};
\draw [black] (42.6,-37.7) circle (3);
\draw (42.6,-37.7) node {$q4$};
\draw [black] (17.477,-20.62) arc (234:-54:2.25);
\draw (18.8,-16.05) node [above] {$a$};
\fill [black] (20.12,-20.62) -- (21,-20.27) -- (20.19,-19.68);
\draw [black] (21.8,-23.3) -- (27.7,-23.3);
\fill [black] (27.7,-23.3) -- (26.9,-22.8) -- (26.9,-23.8);
\draw (24.75,-23.8) node [below] {$b$};
\draw [black] (33.7,-23.3) -- (39.6,-23.3);
\fill [black] (39.6,-23.3) -- (38.8,-22.8) -- (38.8,-23.8);
\draw (36.65,-23.8) node [below] {$a$};
\draw [black] (45.6,-23.3) -- (51.3,-23.3);
\fill [black] (51.3,-23.3) -- (50.5,-22.8) -- (50.5,-23.8);
\draw (48.45,-23.8) node [below] {$b$};
\draw [black] (52.977,-20.62) arc (234:-54:2.25);
\draw (54.3,-16.05) node [above] {$a$};
\fill [black] (55.62,-20.62) -- (56.5,-20.27) -- (55.69,-19.68);
\draw [black] (32.61,-25.61) -- (40.69,-35.39);
\fill [black] (40.69,-35.39) -- (40.56,-34.45) -- (39.79,-35.09);
\draw (36.1,-31.93) node [left] {$b$};
\draw [black] (42.6,-26.3) -- (42.6,-34.7);
\fill [black] (42.6,-34.7) -- (43.1,-33.9) -- (42.1,-33.9);
\draw (42.1,-30.5) node [left] {$a$};
\draw [black] (52.41,-25.63) -- (44.49,-35.37);
\fill [black] (44.49,-35.37) -- (45.38,-35.07) -- (44.61,-34.44);
\draw (47.89,-29.07) node [left] {$b$};
\draw [black] (43.923,-40.38) arc (54:-234:2.25);
\draw (42.6,-44.95) node [below] {$a,b$};
\fill [black] (41.28,-40.38) -- (40.4,-40.73) -- (41.21,-41.32);
\end{tikzpicture}
```

## Problem 4

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (18.8,-23.3) circle (3);
\draw (18.8,-23.3) node {$q0*$};
\draw [black] (30.7,-23.3) circle (3);
\draw (30.7,-23.3) node {$q1*$};
\draw [black] (42.6,-23.3) circle (3);
\draw (42.6,-23.3) node {$q2$};
\draw [black] (17.477,-20.62) arc (234:-54:2.25);
\draw (18.8,-16.05) node [above] {$a$};
\fill [black] (20.12,-20.62) -- (21,-20.27) -- (20.19,-19.68);
\draw [black] (21.3,-21.669) arc (113.27389:66.72611:8.731);
\fill [black] (28.2,-21.67) -- (27.66,-20.89) -- (27.27,-21.81);
\draw (24.75,-20.46) node [above] {$b$};
\draw [black] (33.7,-23.3) -- (39.6,-23.3);
\fill [black] (39.6,-23.3) -- (38.8,-22.8) -- (38.8,-23.8);
\draw (36.65,-23.8) node [below] {$b$};
\draw [black] (41.277,-20.62) arc (234:-54:2.25);
\draw (42.6,-16.05) node [above] {$a,b$};
\fill [black] (43.92,-20.62) -- (44.8,-20.27) -- (43.99,-19.68);
\draw [black] (28.076,-24.729) arc (-70.18393:-109.81607:9.81);
\fill [black] (21.42,-24.73) -- (22.01,-25.47) -- (22.35,-24.53);
\draw (24.75,-25.81) node [below] {$a$};
\end{tikzpicture}
```

## Problem 5

|Current State|A|B|
|--|--|--|
|q0*|q0|q1|
|q1*|q0|q2|
|q2|q2|q2|

## Problem 6

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (18.8,-23.3) circle (3);
\draw (18.8,-23.3) node {$q0*$};
\draw [black] (30.4,-16.3) circle (3);
\draw (30.4,-16.3) node {$q1*$};
\draw [black] (30,-30.2) circle (3);
\draw (30,-30.2) node {$q2*$};
\draw [black] (43.2,-24.5) circle (3);
\draw (43.2,-24.5) node {$q3$};
\draw [black] (21.37,-21.75) -- (27.83,-17.85);
\fill [black] (27.83,-17.85) -- (26.89,-17.84) -- (27.4,-18.69);
\draw (25.66,-20.3) node [below] {$a$};
\draw [black] (21.35,-24.87) -- (27.45,-28.63);
\fill [black] (27.45,-28.63) -- (27.03,-27.78) -- (26.5,-28.63);
\draw (23.29,-27.25) node [below] {$b$};
\draw [black] (28.839,-27.44) arc (-163.51835:-199.77834:13.586);
\fill [black] (29.08,-18.99) -- (28.34,-19.57) -- (29.28,-19.91);
\draw (27.74,-23.19) node [left] {$a$};
\draw [black] (31.531,-19.072) arc (16.01315:-19.30984:13.891);
\fill [black] (31.29,-27.5) -- (32.03,-26.91) -- (31.08,-26.58);
\draw (32.61,-23.31) node [right] {$b$};
\draw [black] (32.93,-17.92) -- (40.67,-22.88);
\fill [black] (40.67,-22.88) -- (40.27,-22.03) -- (39.73,-22.87);
\draw (35.74,-20.9) node [below] {$a$};
\draw [black] (32.75,-29.01) -- (40.45,-25.69);
\fill [black] (40.45,-25.69) -- (39.51,-25.55) -- (39.91,-26.47);
\draw (37.68,-27.86) node [below] {$b$};
\draw [black] (45.88,-23.177) arc (144:-144:2.25);
\draw (50.45,-24.5) node [right] {$a,b$};
\fill [black] (45.88,-25.82) -- (46.23,-26.7) -- (46.82,-25.89);
\end{tikzpicture}
```

## Problem 7

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (18.4,-23.1) circle (3);
\draw (18.4,-23.1) node {$q0$};
\draw [black] (30,-15.7) circle (3);
\draw (30,-15.7) node {$q1$};
\draw [black] (30,-30.2) circle (3);
\draw (30,-30.2) node {$q2$};
\draw [black] (42.4,-22.5) circle (3);
\draw (42.4,-22.5) node {$q3$};
\draw [black] (19.549,-20.341) arc (148.79801:96.27213:10.005);
\fill [black] (27.01,-15.58) -- (26.16,-15.17) -- (26.27,-16.16);
\draw (21.66,-16.59) node [above] {$a$};
\draw [black] (27.021,-30.433) arc (-94.44609:-148.49292:9.642);
\fill [black] (27.02,-30.43) -- (26.26,-29.87) -- (26.18,-30.87);
\draw (21.62,-29.54) node [below] {$b$};
\draw [black] (32.982,-15.479) arc (86.27409:36.24632:10.79);
\fill [black] (40.98,-19.87) -- (40.91,-18.93) -- (40.11,-19.52);
\draw (38.58,-16.28) node [above] {$b$};
\draw [black] (27.47,-17.31) -- (20.93,-21.49);
\fill [black] (20.93,-21.49) -- (21.87,-21.48) -- (21.33,-20.63);
\draw (25.26,-19.9) node [below] {$a$};
\draw [black] (27.44,-28.63) -- (20.96,-24.67);
\fill [black] (20.96,-24.67) -- (21.38,-25.51) -- (21.9,-24.66);
\draw (25.31,-26.15) node [above] {$b$};
\draw [black] (41.378,-25.309) arc (-28.56796:-87.75415:10.02);
\fill [black] (41.38,-25.31) -- (40.56,-25.77) -- (41.43,-26.25);
\draw (38.93,-29.53) node [below] {$a$};
\draw [black] (39.77,-21.06) -- (32.63,-17.14);
\fill [black] (32.63,-17.14) -- (33.09,-17.97) -- (33.57,-17.09);
\draw (35.09,-19.6) node [below] {$b$};
\draw [black] (39.85,-24.08) -- (32.55,-28.62);
\fill [black] (32.55,-28.62) -- (33.49,-28.62) -- (32.96,-27.77);
\draw (35.14,-25.85) node [above] {$a$};
\end{tikzpicture}
```

## Problem 8

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (17.1,-19.2) circle (3);
\draw (17.1,-19.2) node {$q0$};
\draw [black] (32.7,-21.4) circle (3);
\draw (32.7,-21.4) node {$q2$};
\draw [black] (45.6,-33.9) circle (3);
\draw (45.6,-33.9) node {$q3$};
\draw [black] (45.6,-33.9) circle (2.4);
\draw [black] (15.777,-16.52) arc (234:-54:2.25);
\draw (17.1,-11.95) node [above] {$0$};
\fill [black] (18.42,-16.52) -- (19.3,-16.17) -- (18.49,-15.58);
\draw [black] (20.07,-19.62) -- (29.73,-20.98);
\fill [black] (29.73,-20.98) -- (29.01,-20.37) -- (28.87,-21.36);
\draw (24.54,-20.9) node [below] {$1$};
\draw [black] (34.85,-23.49) -- (43.45,-31.81);
\fill [black] (43.45,-31.81) -- (43.22,-30.9) -- (42.52,-31.61);
\draw (38.07,-28.13) node [below] {$1$};
\draw [black] (19.562,-17.505) arc (116.06709:47.87843:10.126);
\fill [black] (19.56,-17.5) -- (20.5,-17.6) -- (20.06,-16.7);
\draw (25.78,-15.98) node [above] {$0$};
\draw [black] (19.096,-16.966) arc (132.93253:-7.50095:16.243);
\fill [black] (19.1,-16.97) -- (20.02,-16.79) -- (19.34,-16.05);
\draw (38.66,-13.92) node [above] {$0$};
\end{tikzpicture}
```
