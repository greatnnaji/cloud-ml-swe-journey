How would you define Machine Learning? machine learning is the field (or art) of programming computers to learn from data

Can you name four types of problems where it shines? logistic regression, ex. spam or not spam, image classification, ex. dog vs cat, reinforcement learning, ex. chess game that learns, clustering, ex. customer segmentation

What is a labeled training set? this relates to supervised learning as the features/predictors are fed in with the solutions/labels in model training

What are the two most common supervised tasks? Classification and Regression
Regression
ex. car features like year,..., label is estimated car price, (idea is that both feature and label need to be fed into model during training)
Classification
ex. spam or not spam,..., features of emails that look like spam are fed in with whether or not they are spam

Can you name four common unsupervised tasks? Clustering, Dimensionality Reduction, Anomaly Detection, Association Rule Learning (e.g.identifying products commonly purchaed together in a market basket analysis)

What type of Machine Learning algorithm would you use to allow a robot to walk in various unknown 
terrains? reinforcement learning

What type of algorithm would you use to segment your customers into multiple groups? clustering(k-means) (for multiple groups)
Note: cannot be supervised learning nor logistic regression because mainly we dont know the groups ahead of time

Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem? supervised, see earlier

What is an online learning system? a learning system that allows learning to be done incrementally (adding new data) without putting the system offline. ex. very useful in stock market where changes happen a lot

What is out-of-core learning? used when the dataset is too large to fit into memory, so data is processed in small chunks from disk.

What type of learning algorithm relies on a similarity measure to make predictions? instance based learning (learning "by heart")

What is the difference between a model parameter and a learning algorithm’s hyperparameter?
Model parameters → learned from data. e.g., weights in linear regression
note: weights represent the strength of connection btw two neurons
Hyperparameters → set before training. e.g., learning rate

What do model-based learning algorithms search for? They search for the best model parameters that minimize a cost function.
What is the most common strategy they use to succeed? optimizations (e.g. gradient descent) 
How do they make predictions? by applying the learned model to new instances

Can you name four of the main challenges in Machine Learning? 
- bad algorithm (ML depends heavily on the model chosen, choosing a model that make assumptions that are not in line with the problem you aim to solve)
- sampling bias (examples used to train the model are not fully representative of the distribution)
- Overfitting (model overfits training data, making it unable to generalize well)
- Underfitting (model is oversimplified making it highly unlikely to recognize complex patterns)
- Bad data: if data is filled with noise and outliers, it makes it hard from the start for the model to generalize well, need data cleaning, also need a bunch of examples for any ml problem even simple ones

If your model performs great on the training data but generalizes poorly to new instances, what is happening? Overfitting Can you name three possible solutions? reduce model complexity (by constrining or reducing no. of features), add more training data, do feature engineering (i.e feature selection (select important features) and feature extraction -> combining multiple features into one feature (dimensionality reduction helps))

What is a test set, and why would you want to use it? A test set allows us to test and evaluate the models performance via the generalization error, we use it because we dont want to be testing in production and it helps us get and estimate via GE on how well our model will perform

What is the purpose of a validation set? it allows us to pick the best model without allowing us to use our test set for validation (this would cause the test set to adapt, making generalization in production very bad)

What is the train-dev set, when do you need it, and how do you use it? A train-dev set is used when training data and test data come from different distributions. It helps diagnose whether poor performance is due to overfitting or data mismatch

What can go wrong if you tune hyperparameters using the test set? model will get good at generalization for the test set (causing overfitting), making it perform badly when used on a never seen before dataset. i.e. production

Takeways: Reinforcement learning is neither supervised nor unsupervised learning