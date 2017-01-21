# YASP
Yet Another Simple Predictor.

We implemented it to identify StarCraft 2 players from game data in a Kaggle in class competition. Our final score was **0.70801** using [F-measure](https://en.wikipedia.org/wiki/F1_score).
## Prerequisites

YASP is proudly powered by ***Python 2.7***

You need those python modules in order to install YASP:

- math
- functools
- random
- [sklearn](http://scikit-learn.org/stable/index.html)
- [matplotlib](http://matplotlib.org)

## How do I use it?

Execute one of those python scripts :

- yaspredictor.py

Our solution with the best F-mesure.
We experimented with decision trees before trying random forests, which gave much better results. We used several measures, from accuracy to [Jaccard similarity coefficient](https://en.wikipedia.org/wiki/Jaccard_index) or [cross evaluation score](https://en.wikipedia.org/wiki/Cross-validation_(statistics)). Details of the features are precised later in the document.

- random_tree_predictor_by_race.py

Another solution, using a Random Forest per race of avatar: it's assuming players behavior is correlated with their avatar race.



## How do we test it?

You can run all tests by executing this command at project root: ```python -m unittest discover```
Another way would be running the tests module by module following this format :  ```python -m unittest package.module_name```.

For example, here, we run all tests of the test_indexing module (tests package):

    python -m unittest tests.test_features

## How did we implement it?

### Cleaning the data
We removed the games without actions (only in the training set)
We tried training on the same proportion of each player but it wasn't really useful : we loose too much information.
### Strategy
Key points in our strategy:

- Find a meaningful measure : we started evaluating our model with accuracy scores. The problem is : it does not take in account false positives. We used [Jaccard similarity coefficient](https://en.wikipedia.org/wiki/Jaccard_index) before finally selecting the [cross evaluation score](https://en.wikipedia.org/wiki/Cross-validation_(statistics)) with 10 K-Folds for the evaluation. 
- Find the most successful model (Random Forest in our case) and fine tune its number of predictors.
- Select as few interesting features as possible. 
From a certain threshold, the more features you add, the worst is your model's prediction. 
We saw that empirically : with only 4 interesting features, we scored 0.6 in F-Measure. From that moment, we tried to limit our number of features.


In depth :

First, we extract the first 20 seconds from each game and we compute the trivial features ont it : we count how many times each key was pressed and how many selections they were. That's because in fact, in the first moments of the game, the players are doing some fingers warmup. Their warmup sequence is used to identify them

Then, we add features we selected (by empirically adding and removing them from the classifier and measuring the cross validation score). Here are our thoughts about other features we implemented:


### Additional Features
#### Selected
- Race of avatar (but that's cheating, right?)
- Used hotkeys distribution 
- Speed of player between far away hotkeys : we define a distance between successive pressed hotkeys. Then we compute how fast the player goes from a key to the other.
- Player APM : mean of player speed throughout the game


#### Not selected
- Used hotkeys relative frequency instead of distribution. It didn't seem to better have a significant effect.  
- Most used hotkey : same diagnostic.

## Where could we go from here ?
- We weren't able to use several tools like [recursive feature elimination with cross-validation](http://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html#sphx-glr-auto-examples-feature-selection-plot-rfe-with-cross-validation-py), [matplotlib](http://matplotlib.org) to have a real scientific approach to back our intuitions for the feature selection phase.    We didn't study features correlations either. That's what we'll try to address in the near future.
- We had an idea of assigning a weight to each feature depending on its relevance on the prediction. That needs more digging up.

Other ideas not implemented : 

- Create multiple decision trees with a small groups of features (grouping them by relevance) and affect a vote to each tree. The prediction with the most votes are selected.
- Identify patterns in sequences of key pressed in the first seconds of the game instead of just counting each of them
- Try to identify left-handed players from right-handed ones. Maybe by computing a speed in keystrokes in the right or left part of the keyboard.
- Identify patterns in the assignations of hotkeys before the first one is used.
-  Range of used hotkeys : a player uses the same set of hotkeys during a game. Thought we do not know if it can generalize well on multiple games. 
