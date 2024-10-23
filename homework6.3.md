# Homework 6.3

## Problem 1

```{=latex}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (8.5,-52.6) circle (3);
\draw (8.5,-52.6) node {$q0$};
\draw [black] (22.1,-52.6) circle (3);
\draw (22.1,-52.6) node {$q1$};
\draw [black] (39.4,-52.6) circle (3);
\draw (39.4,-52.6) node {$q2$};
\draw [black] (65.2,-52.6) circle (3);
\draw (65.2,-52.6) node {$q3$};
\draw [black] (65.2,-52.6) circle (2.4);
\draw [black] (39.4,-29.9) circle (3);
\draw (39.4,-29.9) node {$qA$};
\draw [black] (64.9,-89.8) circle (3);
\draw (64.9,-89.8) node {$qS$};
\draw [black] (22.1,-89.8) circle (3);
\draw (22.1,-89.8) node {$qB$};
\draw [black] (13.9,-29.4) circle (3);
\draw (13.9,-29.4) node {$q4$};
\draw [black] (64.9,-15.8) circle (3);
\draw (64.9,-15.8) node {$q5$};
\draw [black] (64.9,-29.4) circle (3);
\draw (64.9,-29.4) node {$q6$};
\draw [black] (3.2,-89.8) circle (3);
\draw (3.2,-89.8) node {$q7$};
\draw [black] (7.3,-108) circle (3);
\draw (7.3,-108) node {$q9$};
\draw [black] (22.1,-108) circle (3);
\draw (22.1,-108) node {$q8$};
\draw [black] (49,-89.8) circle (3);
\draw (49,-89.8) node {$q10$};
\draw [black] (64.9,-108) circle (3);
\draw (64.9,-108) node {$q11$};
\draw [black] (2.2,-52.6) -- (5.5,-52.6);
\fill [black] (5.5,-52.6) -- (4.7,-52.1) -- (4.7,-53.1);
\draw [black] (11.5,-52.6) -- (19.1,-52.6);
\fill [black] (19.1,-52.6) -- (18.3,-52.1) -- (18.3,-53.1);
\draw (15.3,-53.1) node [below] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }\$$};
\draw [black] (25.1,-52.6) -- (36.4,-52.6);
\fill [black] (36.4,-52.6) -- (35.6,-52.1) -- (35.6,-53.1);
\draw (30.75,-53.1) node [below] {$\lambda,\lambda\rightarrow\mbox{ }S$};
\draw [black] (42.4,-52.6) -- (62.2,-52.6);
\fill [black] (62.2,-52.6) -- (61.4,-52.1) -- (61.4,-53.1);
\draw (52.3,-53.1) node [below] {$\lambda,\mbox{ }\$\mbox{ }\rightarrow\mbox{ }\lambda$};
\draw [black] (40.723,-55.28) arc (54:-234:2.25);
\draw (39.4,-59.85) node [below] {$a,\mbox{ }a\mbox{ }\rightarrow\mbox{ }\lambda\mbox{ }|\mbox{ }b,\mbox{ }b\mbox{ }\rightarrow\mbox{ }\lambda$};
\fill [black] (38.08,-55.28) -- (37.2,-55.63) -- (38.01,-56.22);
\draw [black] (39.4,-32.9) -- (39.4,-49.6);
\fill [black] (39.4,-49.6) -- (39.9,-48.8) -- (38.9,-48.8);
\draw (38.9,-41.25) node [left] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }\lambda$};
\draw [black] (39.4,-49.6) -- (39.4,-32.9);
\fill [black] (39.4,-32.9) -- (38.9,-33.7) -- (39.9,-33.7);
\draw (39.9,-41.25) node [right] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }\lambda$};
\draw [black] (42.14,-53.821) arc (63.86691:4.99311:40.683);
\fill [black] (64.75,-86.8) -- (65.18,-85.96) -- (64.18,-86.05);
\draw (58.38,-65.99) node [right] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }\lambda$};
\draw [black] (41.75,-54.464) arc (50.38033:18.47968:71.629);
\fill [black] (41.75,-54.46) -- (42.05,-55.36) -- (42.69,-54.59);
\draw (55.76,-67.79) node [right] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }\lambda$};
\draw [black] (22.286,-86.806) arc (174.80696:135.31111:52.444);
\fill [black] (22.29,-86.81) -- (22.86,-86.05) -- (21.86,-85.96);
\draw (26.25,-68.4) node [left] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }\lambda$};
\draw [black] (21.325,-86.903) arc (-167.87023:-242.01169:30.214);
\fill [black] (36.69,-53.87) -- (35.74,-53.81) -- (36.21,-54.69);
\draw (22.75,-66.78) node [left] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }\lambda$};
\draw [black] (42.03,-28.45) -- (62.27,-17.25);
\fill [black] (62.27,-17.25) -- (61.33,-17.2) -- (61.82,-18.08);
\draw (60.05,-23.37) node [below] {$\lambda,\mbox{ }A\mbox{ }\rightarrow\mbox{ }A$};
\draw [black] (64.9,-18.8) -- (64.9,-26.4);
\fill [black] (64.9,-26.4) -- (65.4,-25.6) -- (64.4,-25.6);
\draw (65.4,-22.6) node [right] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }A$};
\draw [black] (61.9,-29.46) -- (42.4,-29.84);
\fill [black] (42.4,-29.84) -- (43.21,-30.33) -- (43.19,-29.33);
\draw (52.09,-29) node [above] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }b$};
\draw [black] (16.601,-28.099) arc (112.3295:65.42389:25.32);
\fill [black] (16.6,-28.1) -- (17.53,-28.26) -- (17.15,-27.33);
\draw (26.78,-25.55) node [above] {$\lambda,\mbox{ }A\mbox{ }\rightarrow\mbox{ }S$};
\draw [black] (36.771,-31.341) arc (-65.00068:-117.24592:23.058);
\fill [black] (36.77,-31.34) -- (35.83,-31.23) -- (36.26,-32.13);
\draw (26.51,-34.14) node [below] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }a$};
\draw [black] (5.887,-88.473) arc (111.59958:68.40042:18.372);
\fill [black] (5.89,-88.47) -- (6.81,-88.64) -- (6.45,-87.71);
\draw (12.65,-86.68) node [above] {$\lambda,\mbox{ }B\mbox{ }\rightarrow\mbox{ }S$};
\draw [black] (19.199,-90.56) arc (-78.0428:-101.9572:31.61);
\fill [black] (19.2,-90.56) -- (18.31,-90.24) -- (18.52,-91.21);
\draw (12.65,-91.75) node [below] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }b$};
\draw [black] (22.1,-92.8) -- (22.1,-105);
\fill [black] (22.1,-105) -- (22.6,-104.2) -- (21.6,-104.2);
\draw (22.6,-98.9) node [right] {$\lambda,\mbox{ }B\mbox{ }\rightarrow\mbox{ }B$};
\draw [black] (19.1,-108) -- (10.3,-108);
\fill [black] (10.3,-108) -- (11.1,-108.5) -- (11.1,-107.5);
\draw (14.7,-107.5) node [above] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }B$};
\draw [black] (9.19,-105.67) -- (20.21,-92.13);
\fill [black] (20.21,-92.13) -- (19.31,-92.43) -- (20.09,-93.06);
\draw (15.26,-100.33) node [right] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }a$};
\draw [black] (67.58,-88.477) arc (144:-144:2.25);
\draw (72.15,-89.8) node [right] {$\lambda,\mbox{ }S\mbox{ }\rightarrow\mbox{ }\lambda$};
\fill [black] (67.58,-91.12) -- (67.93,-92) -- (68.52,-91.19);
\draw [black] (65.868,-92.637) arc (15.23067:-15.23067:23.839);
\fill [black] (65.87,-105.16) -- (66.56,-104.52) -- (65.6,-104.26);
\draw (67.21,-98.9) node [right] {$\lambda,\mbox{ }S\mbox{ }\rightarrow\mbox{ }A$};
\draw [black] (64.191,-105.086) arc (-168.98172:-191.01828:32.367);
\fill [black] (64.19,-92.71) -- (63.55,-93.4) -- (64.53,-93.59);
\draw (63.09,-98.9) node [left] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }b$};
\draw [black] (51.44,-88.069) arc (118.01627:61.98373:11.729);
\fill [black] (51.44,-88.07) -- (52.38,-88.13) -- (51.91,-87.25);
\draw (56.95,-86.19) node [above] {$\lambda,\mbox{ }S\mbox{ }\rightarrow\mbox{ }B$};
\draw [black] (62.223,-91.144) arc (-69.14365:-110.85635:14.812);
\fill [black] (62.22,-91.14) -- (61.3,-90.96) -- (61.65,-91.9);
\draw (56.95,-92.61) node [below] {$\lambda,\mbox{ }\lambda\mbox{ }\rightarrow\mbox{ }a$};
\end{tikzpicture}
```

## Problem 2

S $\rightarrow$ aXX | SS
X $\rightarrow$ b

## Problem 3

First normalize the PDA

in this instance it essentially means to add a whole host of q1 $\rightarrow$ q1 transitions so that all $\lambda$ -pop transitions are accounted for essentially ensuring that a can always add an X and b can always add a Y

Afterwards we notate transitions in the form of start node, pop symbol, end node $\rightarrow$ read symbole, start node, push symbold, end node which yields

Then we can simplify by removing the node information

$\lambda, \lambda \rightarrow$

a, $\lambda \rightarrow$ X

a, X $\rightarrow$ XX

a, Y $\rightarrow$ XY

b, $\lambda \rightarrow$ Y

b, X $\rightarrow$ YX

b, Y $\rightarrow$ YY

a, Y $\rightarrow \lambda$
  
b, X $\rightarrow \lambda$

We can then group and simplify

S $\rightarrow$ X

L $\rightarrow \lambda ,$ | aX | bY
