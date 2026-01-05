Machine Learning is the science (or art) of programming computers so they can learn from data

Data Mining: applying ML techniques to dig into large amounts of data that can help discover patterns that were not immediately obvious

Supervised Learning: training set given to the algorithm, include solutions/labels
    - Regression: predict a target value given a set of features/predictors. ex. car model, mileage,... (features), car price (target/label/output) (continuous quantity)

feature = data type plus its value, feature = data type, both are used interchangeably

logistic regression: used for classification, outputs a value correspoding to the probability of belonging to a given class (e.g 20% chance of being spam)
    - classification algorithm despite the "regression" portion of name
        e.g. spam/not spam (discrete quantity)

Unsupervised Learning: training set given to the algorithm, without solutions/labels

dimensionality reduction: goal is to simplify data without losing too much information
 - a way to do is to merge several correlated features into one feature -> feature extraction
 - better performance and makes data take up less memory space (good idea to use on training data after proper cleaning)
 
 Semisupervised Learning: labeling is time consuming and costly, hence make most of the data unlabeled and the other parts labeled

 Reinforcement Learning: learning system (agent) observes environment, perform actions and gets rewards in return, it learns to maximize rewards over time

 Batch vs Online Learning
 Batch Learning: system is incapable of learning incrementally, must be trained on all available data
 - this takes time so it must be done offline
 - if new data comes in, must create a new system and train on old data and new (repeat as needed)
    - inefficient and costly most of the time, consider trying to learn stock market (attempting this would be very costly) 

Online Learning: system learns by feeding it data instances incrementally
- can be done on live systems (online) e.g. stock price prediction
- if learning rate set too high, system adapts rapidly to new data but tends to forget old data quicker
- if learning rate set too low, system learns slowly but is less sensitive to noise and outliers in new data

Instance-based learning vs Model-based learning
Instance-based learning: system learns by heart and generalizes to new cases by using a similarity measure to compare them to learned examples (or subset of them)
Model-based learning: build a model from set of examples and use model to make predictions

Utility/Fitness function: measures how good your model is
Cost function: measures how bad your model is
- want to minimize cost function -> minimize loss function

training a model means running an algorithm to find the model parameters (choosing model type and specfifying its architecture)
that will best fit the training data (and hopefully make good predictions on new data) 

AI vs ML vs DL
ML is a subset of AI, not all AI is ML
- ex. of AI not ML are chess engines made with long hardcoded rules
- Deep Learning is a subset of AI, that uses multi-layered aritificial neural networks to automatically learn complex patterns from vast amounts of data
Note: Multilayered Perceptron (MLP) is a feed forward neural network with multiple neurons, where each layer is fully connected to the next
