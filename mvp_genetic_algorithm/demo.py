from tpot import TPOTClassifier 
from sklearn.cross_validation import train_test_split
import pandas as pd 
import numpy as np

#load the data
telescope = pd.read_csv("datac.csv")

#clean the data
telescope_shuffle=telescope.iloc[np.random.permutation(len(telescope))]
tele=telescope_shuffle.reset_index(drop=True)

#store 2 classes
tele['MVP']=tele['MVP'].map({'h':0, 'm':1})
tele_class = tele['MVP'].values

#split training, testing, and validation data
training_indices, validation_indices = training_indices, testing_indices = train_test_split(tele.index, stratify=tele_class, train_size=0.75, test_size=0.25)

#let genetic programming find best ML model and hyperparameters

tpot = TPOTClassifier(generations=5, verbosity=2)
tpot.fit(tele.drop('MVP', axis=1).loc[training_indices].values, tele.loc[training_indices, 'MVP'].values)

tpot.score(tele.drop('MVP', axis=1).loc[validation_indices].values,
	tele.loc[validation_indices, 'MVP'].values)

tpot.export('pipeline.py')