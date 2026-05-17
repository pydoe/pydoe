# When to Stop Adding Terms

Terms?

*Cumulative residual standard deviation plot typically has a
hockey stick appearance*
Proceeding left to right, as we add more terms to the model, the
cumulative residual standard deviation "curve" will typically decrease.
At the beginning (on the left), as we add large-effect terms, the
decrease from one residual standard deviation to the next residual
standard deviation will be large.  The incremental improvement
(decrease) then tends to drop off slightly.  At some point the
incremental improvement will typically slacken off considerably.
Appearance-wise, it is thus very typical for such a curve to have a
"hockey stick" appearance:

- starting with a series of large decrements between successive
       residual standard deviations; then

- hitting an elbow; then

- having a series of gradual decrements thereafter.

*Stopping rule*
The cumulative residual standard deviation plot provides a visual
answer to the question:

   What is a good model?

by answering the related question:

   When do we stop adding terms to the cumulative model?

Graphically, the most common stopping rule for adding terms is
to cease immediately upon encountering the "elbow".  We include all
terms up to and including the elbow point since each of these terms
decreased the residual standard deviation by a large amount.  However,
we exclude any terms afterward since these terms do not decrease the
residual standard deviation fast enough to warrant inclusion in
the model.
