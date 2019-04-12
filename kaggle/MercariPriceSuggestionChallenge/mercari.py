# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from datetime import datetime, timedelta
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.

from sklearn.metrics import make_scorer
from sklearn import datasets, svm, tree, preprocessing, metrics
import  sklearn.model_selection as ms
import sklearn.ensemble as ske
#import tensorflow as tf
from sklearn.metrics import mean_squared_error , accuracy_score
import math
from math import sqrt
import time
# Perform the necessary imports
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt


import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)


test_data = "test.tsv"
train_data = "train.tsv"


# 1. Extract 3 category related features 
def cat_split(row):
    try:
        text = row
        txt1, txt2, txt3 = text.split('/')
        return txt1, txt2, txt3
    except:
        return "empty", "empty", "empty" #np.nan, np.nan, np.nan
        

     
logging.info("START - Reading data into DF")
train_df = pd.read_csv(train_data, sep='\t').sample(1000)
test_df = pd.read_csv(test_data, sep='\t').sample(200)
logging.info("END - Data loadedin DF")


logging.info ("START - get log of price")
train_df["log_price"] = np.log10(train_df["price"]+1) 
logging.info ("END - get log of price")

logging.info("START - explode category column into subcategories")
train_df["cat_1"], train_df["cat_2"], train_df["cat_3"] = zip(*train_df.category_name.apply(lambda val: cat_split(val)))
test_df["cat_1"], test_df["cat_2"], test_df["cat_3"] = zip(*test_df.category_name.apply(lambda val: cat_split(val)))
logging.info("End - explode category column into subcategories")

logging.info ("START - fill NAN values with No Brand where brand is missing")
train_df.brand_name = train_df.brand_name.fillna("no-brand")
test_df.brand_name = test_df.brand_name.fillna("no-brand")
logging.info ("END - fill NAN values with No Brand where brand is missing")


logging.info ("START - fill NAN values with no-description where item_description is missing")
train_df.item_description = train_df.item_description.fillna("no-description")
test_df.item_description = test_df.item_description.fillna("no-description")
logging.info ("END - fill NAN values with No Brand where brand is missing")


train_df.cat_1 = train_df.cat_1.fillna("no-category")
train_df.cat_2 = train_df.cat_2.fillna("no-category")
train_df.cat_3 = train_df.cat_3.fillna("no-category")

test_df.cat_1 = test_df.cat_1.fillna("no-category")
test_df.cat_2 = test_df.cat_2.fillna("no-category")
test_df.cat_3 = test_df.cat_3.fillna("no-category")


logging.info("START - making dictionaries for different categories ")
keys = train_df.cat_1.unique().tolist() + test_df.cat_1.unique().tolist()
keys = list(set(keys))
values = list(range(keys.__len__()))
cat1_dict = dict(zip(keys, values))

keys2 = train_df.cat_2.unique().tolist() + test_df.cat_2.unique().tolist()
keys2 = list(set(keys2))
values2 = list(range(keys2.__len__()))
cat2_dict = dict(zip(keys2, values2))

keys3 = train_df.cat_3.unique().tolist() + test_df.cat_3.unique().tolist()
keys3 = list(set(keys3))
values3 = list(range(keys3.__len__()))
cat3_dict = dict(zip(keys3, values3))

# making dictionaries for different brand names 
keys4 = train_df.brand_name.unique().tolist() + test_df.brand_name.unique().tolist()
keys4 = list(set(keys4))
values4 = list(range(keys4.__len__()))
brand_dict = dict(zip(keys4, values4))
logging.info("END- making dictionaries for different categories ")

logging.info("START- Replacing categories and brand names with token ")
train_df['cat_1'] = train_df['cat_1'].map(cat1_dict)
train_df['cat_2'] = train_df['cat_2'].map(cat2_dict)
train_df['cat_3'] = train_df['cat_3'].map(cat3_dict)
train_df['brand_name'] = train_df['brand_name'].map(brand_dict)


test_df['cat_1'] = test_df['cat_1'].map(cat1_dict)
test_df['cat_2'] = test_df['cat_2'].map(cat2_dict)
test_df['cat_3'] = test_df['cat_3'].map(cat3_dict)
test_df['brand_name'] = test_df['brand_name'].map(brand_dict)

logging.info("END- Replacing categories and brand names with token ")


logging.info("START- Replacing name and item_description with token ")
#text feature extraction from name
svd = TruncatedSVD(n_components=50)

from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english', vocabulary=None, norm='l2')
name_data = vectorizer.fit_transform(train_df.name)
item_desc_data = vectorizer.fit_transform(train_df.item_description)


# Create a TruncatedSVD instance: svd
name_reduction = svd.fit_transform(name_data)
item_desc_reduction = svd.fit_transform(item_desc_data)

name_columns = ["name_"+str(name_reduction[0].tolist().index(i)) for i in name_reduction[0].tolist()]
item_desc_columns = ["item_desc_"+str(item_desc_reduction[0].tolist().index(i)) for i in item_desc_reduction[0].tolist()]


train_df= pd.concat([train_df, pd.DataFrame (data=name_reduction, columns = name_columns , index=train_df.index) ], axis=1)
train_df= pd.concat([train_df, pd.DataFrame (data=item_desc_reduction, columns = item_desc_columns, index=train_df.index ) ], axis=1)

name_data = vectorizer.fit_transform(test_df.name)
item_desc_data = vectorizer.fit_transform(test_df.item_description)
name_reduction = svd.fit_transform(name_data)
item_desc_reduction = svd.fit_transform(item_desc_data)

name_columns = ["name_"+str(name_reduction[0].tolist().index(i)) for i in name_reduction[0].tolist()]
item_desc_columns = ["item_desc_"+str(item_desc_reduction[0].tolist().index(i)) for i in item_desc_reduction[0].tolist()]


test_df= pd.concat([test_df, pd.DataFrame (data=name_reduction, columns = name_columns,index=test_df.index ) ], axis=1)
test_df= pd.concat([test_df, pd.DataFrame (data=item_desc_reduction, columns = item_desc_columns ,index=test_df.index ) ], axis=1)

print(test_df.columns)

#train_df= pd.concat([train_df, pd.DataFrame (data=name_data.tocoo(copy=False).toarray(), columns=name_columns,  index=train_df.index) ], axis=1)
#train_df= pd.concat([train_df, pd.DataFrame (data=item_desc_data.tocoo(copy=False).toarray(), columns=item_desc_columns,  index=train_df.index) ], axis=1)
logging.info("END- Replacing name and item_description with token ")

logging.info("START- Create feature list ")
training_set= train_df.drop(["train_id","item_description", "name", "category_name", "brand_name","price"], axis=1).copy()
test_set= test_df.drop(["test_id","item_description", "name", "category_name", "brand_name"], axis=1).copy()

#print(len(training_set.columns))
#print(training_set.columns)

#print(len(test_set.columns))
#print(test_set.columns)

logging.info("START- apply Decision Tree Regressor Algorithm ")

#get all predictor variables in X
X = training_set.drop(['log_price'], axis=1).values
#get response variable in Y
y = training_set['log_price'].values



#split training dataset by 80/20. 80% of data will be used for prediction and compare against 20% of the remianing data 
X_train, X_test, y_train, y_test = ms.train_test_split(X,y)



#Apply decision tree algorithm over the data
clf_dt = tree.DecisionTreeRegressor()
res=clf_dt.fit (X_train, y_train)   
# get the prediction score. 
predicted=clf_dt.predict (test_set)

predictions = [[round(10**value, 3)-1] for value in predicted]

predicted_df = pd.DataFrame(data=predictions, columns=["prediction"])
predicted_df["test_id"]=predicted_df.index

print(predicted)
print("\n")
print(predicted_df)

sys.exit(0)


def test_classifier(clf):
    #iterate of test/train data set for n interattion and apply the decision tree regressor algorithm
    shuffle_validator = ms.ShuffleSplit(n_splits=10,  test_size=0.2, random_state=0)
    scores = ms.cross_val_score(clf, X, y, cv=shuffle_validator)
    print("Accuracy: %0.4f (+/- %0.2f)" % (scores.mean(), scores.std()))
   
test_classifier(clf_dt)

predicted = ms.cross_val_predict(clf_dt,X,y)





fig, ax = plt.subplots()
ax.scatter(y, predicted, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
#plt.show()


logging.info("End- apply DecisionTreeRegressor Algorithm ")

sys.exit(0)

logging.info("START- apply XGBoost Algorithm ")

import xgboost as xgb

model = xgb.XGBClassifier(missing=np.nan, max_depth=6, 
                        n_estimators=5, learning_rate=0.15,   nthread=-1)


# fitting
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
actuals = [round(10**value) for value in y_test]
predictions = [round(10**value) for value in y_pred]
# evaluate predictions
#print(actuals)
#print(predictions)

accuracy = accuracy_score(actuals, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

actuals =     [round(10**value,3) for value in y_test]
predictions = [round(10**value,3) for value in y_pred]

print(actuals[:10])
print(predictions[:10])

logging.info("Print Xboost performance ")
import numpy as np
import matplotlib.pyplot as pp
val = 0. # this is the value where you want the data to appear on the y-axis.
ar = np.arange(10) # just as an example array
#plt.plot(actuals, range(len(actuals)), 'x')
#plt.plot(predictions, range(len(predictions)), 'o')
#plt.show()

logging.info("END- apply XGBoost Algorithm ")
