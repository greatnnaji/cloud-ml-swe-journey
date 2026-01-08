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
opposite of overfitting, occurs when model is too simple to learn the underlying structure of data
possible solutions include:
- select more powerful model with more parameters
- feed better features to learning algorithm (feature engineering)
- reduce model constraints via regularization hyperparameter

Way to find out if your model generalizes well:
Testing and Validation:
could just push model to production and see how well it performs -> not good if model is bad, customers will complain
Hence, split data set into training set and test set, i.e train on train set, test on test set, error that occurs in new cases is called generalization error (or out-of-sample error), by evaluating model on test set you get an estimate of this error (this value tells you how well your model will perform on never seen before instances)
- if training error low but generalization error high -> overfitting
Note: common to use 80% of data for training and 20% of data for testing

When choosing the value of the regularization hyperparameter we could train 100 different models using 100 different hyperparameter values and pick the one with the lowest generalization error, but it gives an even higher generalization error in production
- This is because running generalization error multiple times on test set causes the model to adapt and produce the best hyperparameters for that set

Fix this with holdout validation, where we hold out part of the training set (will be our validation set) to evaluate several candidate models and select the best one, the steps are as follows:
- train multiple models on the reduced training set (i.e train set without validation set) and pick the best one
- train best model on full training set (including validation set), this gives final model
- evaluate final model on the test set to get an estimate of the generalization error
if val set too small -> may end up selecting a suboptimal model instead
if val set too large -> then training set is too small (analogy: selecting the fastest sprinter to run in a different marathon)
Solve this val set size problem by doing repeated cross-validation (using many small validation sets), here each model is evaluated once per validation set after it is trained on the rest of the data, by avergaing out all evaluations we get a more accurate measure of performance, con: takes more time (no. of val sets)

No Free Lunch Theorem: states averaged across all possible problems, every learning algorithm performs equally well (or poorly) i.e. there is no universally superior algorithm that works best for every problem
- an algorithm will perform well if your problem's structure happens to match the assumptions that the algorithm makes
