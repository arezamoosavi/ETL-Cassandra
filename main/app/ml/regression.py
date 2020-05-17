import pickle
import numpy as np
import pandas as pd 
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

def preprocess(df):
    df.sort_values("date", axis = 0, ascending = True, 
                 inplace = True, na_position ='last')
    df.reset_index(drop=True, inplace=True)

    df['date'] = df['date'].astype('datetime64[ns]')
    df.set_index('date',inplace=True)
    df['high_low_change']=(df['adj_high']-df['adj_close'])/df['adj_close']*100.0
    df['change_perc']=(df['adj_close']-df['adj_open'])/df['adj_open']*100.0
    df=df[['adj_close','high_low_change','change_perc','adj_volume']]
    df.fillna(-9999,inplace=True)
    df['price_monthly']=df['adj_close'].shift(-30)

    return df


def adj_close_model(df):

    df = preprocess(df)


    #Features
    X=np.array(df.drop(['price_monthly'],1))
    X=preprocessing.scale(X)
    X=X[:-30]    
    df.dropna(inplace=True)
    
    # Output
    y=np.array(df['price_monthly'])

    #Splitting the data set for training and testin
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4)


    clf=LinearRegression()
    clf.fit(X_train,y_train)

    accuracy=clf.score(X_test,y_test)
    accuracy=accuracy*100
    accuracy = float("{0:.2f}".format(accuracy))
    print('\n'*2,'Test Accuracy is: ',accuracy,'%', '\n'*2)

    # Save the trained model as a pickle string.
    modelPath = 'app/ml/reg_model.pickle'

    with open(modelPath, 'wb') as handle:
        pickle.dump(clf, handle, protocol=pickle.HIGHEST_PROTOCOL)
