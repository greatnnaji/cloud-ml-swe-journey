Questions to think about:
Why is a machine learning model being used here instead of writing explicit rules?
writing explicit rules would be inefficient and wouldn't leverage the power of ML and we would not be able to efficiently/effectively created accurate rules for unseen data, training a model allows us to be able to predict on new unseen data (accurately)
Note: Explicit rules would require knowing all contributing factors ahead of time, which we don’t

What assumptions does a linear model make about the relationship between GDP per capita and life satisfaction?
That the features/data points follow a linear fashion. i.e a linear line of best fit would best describe the underlying pattern
Note: The relationship is monotonic (more GDP → higher satisfaction)
- monotonic: moves in one direction (either increasing or decreasing)

In what real-world situations would this model give misleading or incorrect predictions? if the data points did not closely follow a linear fashion, this would cause us to have a very low accuracy on new unseen data and the predictions would be way off
Note: Even if the relationship looks linear, ignoring factors like inequality, culture, or social support would skew predictions.
