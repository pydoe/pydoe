# Statistical Significance

*Formal statistical methods*
Formal statistical methods to answer the question of statistical
significance commonly involve the use of

- ANOVA (analysis of variance); and
   - $t$-based confidence intervals for the effects.

*ANOVA*
The virtue of ANOVA is that it is a powerful, flexible tool with
many applications.  The drawback of ANOVA is that

- it is heavily quantitative and non-intuitive;
   - it must have an assumed underlying model; and
   - its validity depends on assumptions of a constant error variance
        and normality of the errors.

*t confidence intervals*
$T$ confidence intervals for the effects, using the
$t$-distribution,
are also heavily used for determining factor significance.  As part
of the $t$ approach, one first needs to determine
*sd*(*effect*), the standard deviation of an effect.  For
2-level full and fractional factorial designs, such a standard deviation
is related to *σ*, the standard deviation of an observation
under fixed conditions, via the formula:

   $\mbox{sd(effect)} = \frac{2 \sigma}{\sqrt{n}}$ which in turn leads to forming 95% confidence
intervals for an effect via

$c$ * *sd*(*effect*)

for an appropriate multiple $c$ (from the $t$ distribution).
Thus in the context of the |effects| plot, "drawing the line" at
$c$ * *sd*(*effect*) would serve to separate, as desired,
the list of effects into 2 domains:

- significant (that is, important); and
   - not significant (that is, unimportant).

*Estimating sd(effect)*
The key in the above approach is to determine an estimate for
*sd*(*effect*).  Three statistical approaches are common:

- Prior knowledge about *σ*:

If *σ* is known, we can compute *sd*(*effect*)
       from the above expression and make use of a conservative
       (normal-based) 95% confidence interval by drawing the line at

$\mbox{2 sd(effect)} = 2 \left( \frac{2 \sigma}{\sqrt{n}}
             \right)$ This method is rarely used in practice because
       *σ* is rarely known.

- Replication in the experimental design:

Replication will allow *σ&*
       to be estimated from the data without depending on the
       correctness of a deterministic model.  This is a real
       benefit.  On the other hand, the downside of such replication
       is that it increases the number of runs, time, and expense of
       the experiment.  If replication can be afforded, this
       method should be used.  In such a case, the analyst separates
       important from unimportant terms by drawing the line at

$t \mbox{*sd(effect)} = t \mbox{*} \left(              \frac{2\hat{\sigma}}{\sqrt{n}} \right)$ with $t$ denoting the 97.5 percent point from the
       appropriate
       Student's-$t$
       distribution.

- Assume 3-factor interactions and higher are zero:

This approach "assumes away" all 3-factor interactions and higher
       and uses the data pertaining to these interactions to estimate
       *σ*.  Specifically,

$\hat{\sigma} = \sqrt{\frac{\mbox{SSQ}}{h}}$ with $h$ denoting the number of 3-factor interactions and
       higher, and SSQ is the sum of squares for these higher-order
       effects.  The analyst separates important from unimportant
       effects by drawing the line at

$t \mbox{*sd(effect)} = t \mbox{*}
          \left( \frac{2 \hat{\sigma}}{\sqrt{n}} \right)$ with $t$ denoting the 97.5 percent point from the
       appropriate (with $h$ degrees of freedom)        Student's-$t$
       distribution.

This method warrants caution:

- it involves an untestable assumption (that such
              interactions = 0);
          - it can result in an estimate for *sd*(*effect*)
              based on few terms (even a single term); and
          - it is virtually unusable for highly-fractionated
              designs (since high-order interactions are not
              directly estimable).

*Non-statistical considerations*
The above statistical methods can and should be used.  Additionally,
the non-statistical considerations discussed in the next few
sections are frequently insightful in practice and have their place in
the EDA approach as advocated here.
