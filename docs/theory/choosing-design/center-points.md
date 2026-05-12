# Adding Centerpoints

## Center Point, or 'Control' Runs

*Centerpoint runs provide a check for both process stability and possible curvature*

As mentioned earlier in this section, we add centerpoint runs interspersed among the experimental setting runs for two purposes:

- To provide a measure of process stability and inherent variability
- To check for curvature.

*Centerpoint runs are not randomized*

Centerpoint runs should begin and end the experiment, and should be dispersed as evenly as possible throughout the design matrix. The centerpoint runs are not randomized! There would be no reason to randomize them as they are there as guardians against process instability and the best way to find instability is to sample the process on a regular basis.

*Rough rule of thumb is to add 3 to 5 center point runs to your design*

With this in mind, we have to decide on how many centerpoint runs to do. This is a tradeoff between the resources we have, the need for enough runs to see if there is process instability, and the desire to get the experiment over with as quickly as possible. *As a rough guide, you should generally add approximately 3 to 5 centerpoint runs to a full or fractional factorial design.*

*Table of randomized, replicated $2^3$ full factorial design with centerpoints*

In the following Table we have added three centerpoint runs to the otherwise randomized design matrix, making a total of nineteen runs.

**TABLE 3.32: Randomized, Replicated $2^3$ Full Factorial Design Matrix with Centerpoint Control Runs Added**

| | Random Order | Standard Order | SPEED | FEED | DEPTH |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | not applicable | not applicable | 0 | 0 | 0 |
| 2 | 1 | 5 | -1 | -1 | 1 |
| 3 | 2 | 15 | -1 | 1 | 1 |
| 4 | 3 | 9 | -1 | -1 | -1 |
| 5 | 4 | 7 | -1 | 1 | 1 |
| 6 | 5 | 3 | -1 | 1 | -1 |
| 7 | 6 | 12 | 1 | 1 | -1 |
| 8 | 7 | 6 | 1 | -1 | 1 |
| 9 | 8 | 4 | 1 | 1 | -1 |
| 10 | not applicable | not applicable | 0 | 0 | 0 |
| 11 | 9 | 2 | 1 | -1 | -1 |
| 12 | 10 | 13 | -1 | -1 | 1 |
| 13 | 11 | 8 | 1 | 1 | 1 |
| 14 | 12 | 16 | 1 | 1 | 1 |
| 15 | 13 | 1 | -1 | -1 | -1 |
| 16 | 14 | 14 | 1 | -1 | 1 |
| 17 | 15 | 11 | -1 | 1 | -1 |
| 18 | 16 | 10 | 1 | -1 | -1 |
| 19 | not applicable | not applicable | 0 | 0 | 0 |

*Preparing a worksheet for operator of experiment*

To prepare a worksheet for an operator to use when running the experiment, delete the columns 'RandOrd' and 'Standard Order.' Add an additional column for the output (Yield) on the right, and change all '-1', '0', and '1' to original factor levels as follows.

*Operator worksheet*

**TABLE 3.33: DOE Worksheet Ready to Run**

| Sequence Number | Speed | Feed | Depth | Yield |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 20 | 0.003 | 0.015 | |
| 2 | 16 | 0.001 | 0.02 | |
| 3 | 16 | 0.005 | 0.02 | |
| 4 | 16 | 0.001 | 0.01 | |
| 5 | 16 | 0.005 | 0.02 | |
| 6 | 16 | 0.005 | 0.01 | |
| 7 | 24 | 0.005 | 0.01 | |
| 8 | 24 | 0.001 | 0.02 | |
| 9 | 24 | 0.005 | 0.01 | |
| 10 | 20 | 0.003 | 0.015 | |
| 11 | 24 | 0.001 | 0.01 | |
| 12 | 16 | 0.001 | 0.02 | |
| 13 | 24 | 0.005 | 0.02 | |
| 14 | 24 | 0.005 | 0.02 | |
| 15 | 16 | 0.001 | 0.01 | |
| 16 | 24 | 0.001 | 0.02 | |
| 17 | 16 | 0.005 | 0.01 | |
| 18 | 24 | 0.001 | 0.01 | |
| 19 | 20 | 0.003 | 0.015 | |

Note that the control (centerpoint) runs appear at rows 1, 10, and 19.

This worksheet can be given to the person who is going to do the runs/measurements and asked to proceed through it from first row to last in that order, filling in the Yield values as they are obtained.

## Pseudo Center Points

*Center points for discrete factors*

One often runs experiments in which some factors are nominal. For example, Catalyst "A" might be the (-1) setting, catalyst "B" might be coded (+1). The choice of which is "high" and which is "low" is arbitrary, but one must have some way of deciding which catalyst setting is the "standard" one.

These standard settings for the discrete input factors together with center points for the continuous input factors, will be regarded as the "center points" for purposes of design.

## Center Points in Response Surface Designs

*Uniform precision*

In an unblocked response surface design, the number of center points controls other properties of the design matrix. The number of center points can make the design orthogonal or have "uniform precision." We will only focus on uniform precision here as classical quadratic designs were set up to have this property.

*Variance of prediction*

Uniform precision ensures that the variance of prediction is the same at the center of the experimental space as it is at a unit distance away from the center.

*Protection against bias*

In a response surface context, to contrast the virtue of uniform precision designs over replicated center-point orthogonal designs one should also consider the following guidance from Montgomery ("Design and Analysis of Experiments," Wiley, 1991, page 547), "*A uniform precision design offers more protection against bias in the regression coefficients than does an orthogonal design because of the presence of third-order and higher terms in the true surface.*"

*Controlling $\alpha$ and the number of center points*

Myers, Vining, et al, ["Variance Dispersion of Response Surface Designs," *Journal of Quality Technology*, 24, pp. 1-11 (1992)] have explored the options regarding the number of center points and the value of $\alpha$ somewhat further: An investigator may control two parameters, $\alpha$ and the number of center points ($n_c$), given $k$ factors. Either set $\alpha = 2^{(k/4)}$ (for rotatability) or $\sqrt{k}$ — an axial point on perimeter of design region. Designs are similar in performance with $\sqrt{k}$ preferable as $k$ increases. Findings indicate that the best overall design performance occurs with $\alpha \approx \sqrt{k}$ and $2 \leq n_c \leq 5$.
