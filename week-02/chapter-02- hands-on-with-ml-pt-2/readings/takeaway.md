Since the main task of machine learning is to select a learning algorithm and train on it, 
the two main things that can go wrong are:
- bad algorithm
- bad data (due to errors, outliers and noise)
    - outliers -> extreme values
    - noise -> unexplained flunctuations in data points

Bad Data
- insufficient quantity of data: need lots of examples to train a model on a simple task

- non representative training data: It is crucial to use a training set that is representative of the 
cases you want to generalize to
    If sample is too small -> sampling noise (i.e. nonrepresentative data as a result of chance)
    If sample is large -> possibility of being nonrepresentative if sampling method is flawed
    This is called sampling bias
    ex. sample strategy could favor a group of people as opposed to an entire population (e.g wealthier people)
    we could also have nonresponse bias where out of the group being sampled some decided not to respond/participate

A critical part of success in a ML project is choosing a good set of features to train on, which is called feature engineering
which involves the following steps:
- feature selection: selecting the most useful features to train on
- feature extraction: merging multiple related features into one feature (dimensionality reduction can help)
- creating new features by adding new data

Bad Algorithms
Ovefitting the training data
- model performs well on training data but it does not generalize well

Note: complex models such as deep neaural networks can detect subtle patterns in training data, so if training data is noisy then the patterns will not generalize to new instances. ex. add country name as feature, might detect patterns in countries with letter w in name which may be irrelevant in the context of the new instances we want to generalize to

Overfitting happens when the model is too complex relative to the amount of noise in training data,
possible solutions include:
- simplify the model by selecting one with fewer parameters (e.g. linear model as opposed to higher-degree polynomial model) by reducing no. of features/attributes in training data, or constraining the model
- gather more training data
- reduce noise in training data (e.g. fix data errors and remove outliers)

Note: We want to find the balance between fitting the training data well and keeping the model simple enough so it will generalize well

Constraining a model to make it simpler and reduce the risk of overfitting is called regularization
- The amoount of regularization to apply during learning can be controlled by a hyperparameter
- A hyperparameter is a parameter of the learning algorithm (not of the model)
    - if large: no overfitting but less likely to find a good solution, makes model very simple and less complex

Underfitting the training data






