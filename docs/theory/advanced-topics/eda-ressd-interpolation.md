# Interpolation

Interpolation?

*Design table in original data units*
As for the mechanics of interpolation itself, consider a continuation of
the prior $k$ = 2 factor experiment.  Suppose temperature $T$
ranges from 300 to 350 and time $t$ ranges from 20 to 30, and the analyst can afford $n$ = 4 runs.  A 22 full factorial
design is run.  Forming the coded temperature as $X_1$ and the coded time as $X_2$, we have the usual:

| Temperature | Time | $X_1$ | $X_2$ | $Y$ |
| --- | --- | --- | --- | --- |
| 300 | 20 | - | - | 2 |
| 350 | 20 | + | - | 4 |
| 300 | 30 | - | + | 6 |
| 350 | 30 | + | + | 8 |

*Graphical representation*
Graphically the design and data are as follows:

![Diagram of design and response data in orignal data units](https://www.itl.nist.gov/div898/handbook/pri/section5/dpmacros/2x2des2.gif)

    30 +1 --------------
          |6          8|
     T    |            |
     i  X |            |
     m  2 |            |
     e    |            |
          |            |
          |2          4|
    20 -1 --------------
          -1    X1    +1
          300  Temp  350

*Typical interpolation question*
As before, from the data, the prediction equation is

$\hat{Y} = 5 + 2 X_{2} + X_{1}$ =
5 + 2*X_{2} + X_{1}

We now pose the following typical interpolation question:

   From the model, what is the predicted response
   at, say, temperature = 310 and time = 26?

In short:

   $\hat{Y}(T = 310, t = 26) = \mbox{?}$ (T = 310,
   t = 26) = ?

To solve this problem, we first view the $k$ = 2 design and data
graphically, and note (via an "X") as to where the desired
($T$ = 310, $t$ = 26) interpolation point is:

![Diagram of design and response data with interpolation point in
 orignal data units](https://www.itl.nist.gov/div898/handbook/pri/section5/dpmacros/2x2des3.gif)

    30 +1 --------------
          |6          8|
     T    |            |
     i  X |  ?         |
     m  2 |            |
     e    |            |
          |            |
          |2          4|
    20 -1 --------------
          -1    X1    +1
          300  Temp  350

*Predicting the response for the interpolated point*
The important next step is to convert the raw (in units of the
original factors $T$ and $t$) interpolation point into a coded (in units of $X_1$ and $X_2$) interpolation point.  From
the graph or otherwise, we note that a linear translation between
$T$ and $X_1$, and between $t$ and $X_2$ yields

$T$ = 300 => $X_1$ = -1

$T$ = 350 => $X_1$ = +1

thus

$X_1$ = 0 is at $T$ = 325

        |-------------|-------------|
       -1     ?       0            +1
       300   310     325           350

which in turn implies that

$T$ = 310 => $X_1$ = -0.6

Similarly,

$t$ = 20 => $X_2$ = -1

$t$ = 30 => $X_2$ = +1

therefore,

$X_2$ = 0 is at $t$ = 25

        |-------------|-------------|
       -1             0   ?        +1
       20             25 26        30

thus

$t$ = 26 => $X_2$ = +0.2

Substituting $X_1$ = -0.6 and $X_2$ = +0.2 into the prediction
equation

$\hat{Y} = 5 + 2 X_{2} + X_{1}$ =
5 + 2*X_{2} + X_{1}

yields a predicted value of 4.8.

*Graphical representation of response value for interpolated data point*
Thus

![Diagram of design and response data with response for interpolated
 point in orignal data units](https://www.itl.nist.gov/div898/handbook/pri/section5/dpmacros/2x2des4.gif)

    30 +1 --------------
          |6          8|
     T    |            |
     i  X | 4.8        |
     m  2 |            |
     e    |            |
          |            |
          |2          4|
    20 -1 --------------
          -1    X1    +1
          300  Temp  350
