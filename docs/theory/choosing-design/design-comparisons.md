# Comparisons of Response Surface Designs

**Choosing a Response Surface Design**

*Various CCD designs and Box-Behnken designs are compared and their properties discussed*

Table 3.24 contrasts the structures of four common quadratic designs one might use when investigating three factors. The table combines CCC and CCI designs because they are structurally identical.

For three factors, the Box-Behnken design offers some advantage in requiring a fewer number of runs. For 4 or more factors, this advantage disappears.

*Structural comparisons of CCC (CCI), CCF, and Box-Behnken designs for three factors*

**TABLE 3.24: Structural Comparisons of CCC (CCI), CCF, and Box-Behnken Designs for Three Factors**

| CCC (CCI) | | | | CCF | | | | Box-Behnken | | | |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Rep | *X*1 | *X*2 | *X*3 | Rep | *X*1 | *X*2 | *X*3 | Rep | *X*1 | *X*2 | *X*3 |
| 1 | -1 | -1 | -1 | 1 | -1 | -1 | -1 | 1 | -1 | -1 | 0 |
| 1 | +1 | -1 | -1 | 1 | +1 | -1 | -1 | 1 | +1 | -1 | 0 |
| 1 | -1 | +1 | -1 | 1 | -1 | +1 | -1 | 1 | -1 | +1 | 0 |
| 1 | +1 | +1 | -1 | 1 | +1 | +1 | -1 | 1 | +1 | +1 | 0 |
| 1 | -1 | -1 | +1 | 1 | -1 | -1 | +1 | 1 | -1 | 0 | -1 |
| 1 | +1 | -1 | +1 | 1 | +1 | -1 | +1 | 1 | +1 | 0 | -1 |
| 1 | -1 | +1 | +1 | 1 | -1 | +1 | +1 | 1 | -1 | 0 | +1 |
| 1 | +1 | +1 | +1 | 1 | +1 | +1 | +1 | 1 | +1 | 0 | +1 |
| 1 | -1.682 | 0 | 0 | 1 | -1 | 0 | 0 | 1 | 0 | -1 | -1 |
| 1 | 1.682 | 0 | 0 | 1 | +1 | 0 | 0 | 1 | 0 | +1 | -1 |
| 1 | 0 | -1.682 | 0 | 1 | 0 | -1 | 0 | 1 | 0 | -1 | +1 |
| 1 | 0 | 1.682 | 0 | 1 | 0 | +1 | 0 | 1 | 0 | +1 | +1 |
| 1 | 0 | 0 | -1.682 | 1 | 0 | 0 | -1 | 3 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1.682 | 1 | 0 | 0 | +1 | | | | |
| 6 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | | | | |
| **Total Runs = 20** | | | | **Total Runs = 20** | | | | **Total Runs = 15** | | | |

*Factor settings for CCC and CCI three factor designs*

Table 3.25 illustrates the factor settings required for a central composite circumscribed (CCC) design and for a central composite inscribed (CCI) design (standard order), assuming three factors, each with low and high settings of 10 and 20, respectively. Because the CCC design generates new extremes for all factors, the investigator must inspect any worksheet generated for such a design to make certain that the factor settings called for are reasonable.

In Table 3.25, treatments 1 to 8 in each case are the factorial points in the design; treatments 9 to 14 are the star points; and 15 to 20 are the system-recommended center points. Notice in the CCC design how the low and high values of each factor have been extended to create the star points. In the CCI design, the specified low and high values become the star points, and the system computes appropriate settings for the factorial part of the design inside those boundaries.

**TABLE 3.25: Factor Settings for CCC and CCI Designs for Three Factors**

| Central Composite Circumscribed CCC | | | | | Central Composite Inscribed CCI | | | |
|---|:---:|:---:|:---:|---|---|:---:|:---:|:---:|
| Sequence Number | *X*1 | *X*2 | *X*3 | | Sequence Number | *X*1 | *X*2 | *X*3 |
| 1 | 10 | 10 | 10 | | 1 | 12 | 12 | 12 |
| 2 | 20 | 10 | 10 | | 2 | 18 | 12 | 12 |
| 3 | 10 | 20 | 10 | | 3 | 12 | 18 | 12 |
| 4 | 20 | 20 | 10 | | 4 | 18 | 18 | 12 |
| 5 | 10 | 10 | 20 | | 5 | 12 | 12 | 18 |
| 6 | 20 | 10 | 20 | | 6 | 18 | 12 | 18 |
| 7 | 10 | 20 | 20 | | 7 | 12 | 12 | 18 |
| 8 | 20 | 20 | 20 | | 8 | 18 | 18 | 18 |
| 9 * | 6.6 | 15 | 15 | | 9 * | 10 | 15 | 15 |
| 10 * | 23.4 | 15 | 15 | | 10 * | 20 | 15 | 15 |
| 11 * | 15 | 6.6 | 15 | | 11 * | 15 | 10 | 15 |
| 12 * | 15 | 23.4 | 15 | | 12 * | 15 | 20 | 15 |
| 13 * | 15 | 15 | 6.6 | | 13 * | 15 | 15 | 10 |
| 14 * | 15 | 15 | 23.4 | | 14 * | 15 | 15 | 20 |
| 15 | 15 | 15 | 15 | | 15 | 15 | 15 | 15 |
| 16 | 15 | 15 | 15 | | 16 | 15 | 15 | 15 |
| 17 | 15 | 15 | 15 | | 17 | 15 | 15 | 15 |
| 18 | 15 | 15 | 15 | | 18 | 15 | 15 | 15 |
| 19 | 15 | 15 | 15 | | 19 | 15 | 15 | 15 |
| 20 | 15 | 15 | 15 | | 20 | 15 | 15 | 15 |

\* are star points

*Factor settings for CCF and Box-Behnken three factor designs*

Table 3.26 illustrates the factor settings for the corresponding central composite face-centered (CCF) and Box-Behnken designs. Note that each of these designs provides three levels for each factor and that the Box-Behnken design requires fewer runs in the three-factor case.

**TABLE 3.26: Factor Settings for CCF and Box-Behnken Designs for Three Factors**

| Central Composite Face-Centered CCF | | | | | Box-Behnken | | | |
|---|:---:|:---:|:---:|---|---|:---:|:---:|:---:|
| Sequence Number | *X*1 | *X*2 | *X*3 | | Sequence Number | *X*1 | *X*2 | *X*3 |
| 1 | 10 | 10 | 10 | | 1 | 10 | 10 | 15 |
| 2 | 20 | 10 | 10 | | 2 | 20 | 10 | 15 |
| 3 | 10 | 20 | 10 | | 3 | 10 | 20 | 15 |
| 4 | 20 | 20 | 10 | | 4 | 20 | 20 | 15 |
| 5 | 10 | 10 | 20 | | 5 | 10 | 15 | 10 |
| 6 | 20 | 10 | 20 | | 6 | 20 | 15 | 10 |
| 7 | 10 | 20 | 20 | | 7 | 10 | 15 | 20 |
| 8 | 20 | 20 | 20 | | 8 | 20 | 15 | 20 |
| 9 * | 10 | 15 | 15 | | 9 | 15 | 10 | 10 |
| 10 * | 20 | 15 | 15 | | 10 | 15 | 20 | 10 |
| 11 * | 15 | 10 | 15 | | 11 | 15 | 10 | 20 |
| 12 * | 15 | 20 | 15 | | 12 | 15 | 20 | 20 |
| 13 * | 15 | 15 | 10 | | 13 | 15 | 15 | 15 |
| 14 * | 15 | 15 | 20 | | 14 | 15 | 15 | 15 |
| 15 | 15 | 15 | 15 | | 15 | 15 | 15 | 15 |
| 16 | 15 | 15 | 15 | | | | | |
| 17 | 15 | 15 | 15 | | | | | |
| 18 | 15 | 15 | 15 | | | | | |
| 19 | 15 | 15 | 15 | | | | | |
| 20 | 15 | 15 | 15 | | | | | |

\* are star points for the CCC

*Properties of classical response surface designs*

Table 3.27 summarizes properties of the classical quadratic designs. Use this table for broad guidelines when attempting to choose from among available designs.

**TABLE 3.27: Summary of Properties of Classical Response Surface Designs**

| Design Type | Comment |
|:---:|---|
| CCC | CCC designs provide high quality predictions over the entire design space, but require factor settings outside the range of the factors in the factorial part. **Note:** When the possibility of running a CCC design is recognized before starting a factorial experiment, factor spacings can be reduced to ensure that $\pm\alpha$ for each coded factor corresponds to feasible (reasonable) levels. Requires 5 levels for each factor. |
| CCI | CCI designs use only points within the factor ranges originally specified, but do not provide the same high quality prediction over the entire space compared to the CCC. Requires 5 levels of each factor. |
| CCF | CCF designs provide relatively high quality predictions over the entire design space and do not require using points outside the original factor range. However, they give poor precision for estimating pure quadratic coefficients. Requires 3 levels for each factor. |
| Box-Behnken | These designs require fewer treatment combinations than a central composite design in cases involving 3 or 4 factors. The Box-Behnken design is rotatable (or nearly so) but it contains regions of poor prediction quality like the CCI. Its "missing corners" may be useful when the experimenter should avoid combined factor extremes. This property prevents a potential loss of data in those cases. Requires 3 levels for each factor. |

*Number of runs required by central composite and Box-Behnken designs*

Table 3.28 compares the number of runs required for a given number of factors for various Central Composite and Box-Behnken designs.

**TABLE 3.28  Number of Runs Required by Central Composite and Box-Behnken Designs**

| Number of Factors | Central Composite | Box-Behnken |
|:---:|---|---|
| 2 | 13 (5 center points) | — |
| 3 | 20 (6 centerpoint runs) | 15 |
| 4 | 30 (6 centerpoint runs) | 27 |
| 5 | 33 (fractional factorial) or 52 (full factorial) | 46 |
| 6 | 54 (fractional factorial) or 91 (full factorial) | 54 |

**Desirable Features for Response Surface Designs**

*A summary of desirable properties for response surface designs*

G. E. P. Box and N. R. Draper in "Empirical Model Building and Response Surfaces," John Wiley and Sons, New York, 1987, page 477, identify desirable properties for a response surface design:

- Satisfactory distribution of information across the experimental region.
    - *rotatability*
- Fitted values are as close as possible to observed values.
    - *minimize residuals or error of prediction*
- Good lack of fit detection.
- Internal estimate of error.
- Constant variance check.
- Transformations can be estimated.
- Suitability for blocking.
- Sequential construction of higher order designs from simpler designs.
- Minimum number of treatment combinations.
- Good graphical analysis through simple data patterns.
- Good behavior when errors in settings of input variables occur.
