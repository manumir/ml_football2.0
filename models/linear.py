import pandas as pd
import numpy as np
from functions import myacc
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df=pd.read_csv('../data/train_all.txt')
df=df.drop(['Date','HomeTeam','AwayTeam','FTHG','FTAG'],1)
df=df.dropna()

Y=df.pop('FTR')
X=df

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=1)

clf=LinearRegression(n_jobs=-1)

clf.fit(x_train,y_train)

print(clf.score(x_test,y_test))
preds=clf.predict(x_test)
print(myacc(preds,y_test))

df=pd.read_csv('../data/train_all.txt')
df=df.sort_values(by=['Date'])

teams=['West Brom','Tottenham']
home=teams[0]
away=teams[1]

df_away=df.loc[df['AwayTeam']==away].tail(1)
df_home=df.loc[df['HomeTeam']==home].tail(1)

df_home=df_home[['HS','HST','HC','HF','B365H','B365D','FTR','HBP','winrate20_home']]
df_away=df_away[['AS','AST','AC','AF','B365A','ABP','winrate20_away']]

df_home=df_home.reset_index(drop=True)
df_away=df_away.reset_index(drop=True)

df=df_home.join(df_away)
df=df[['HS','AS','HST','AST','HC','AC','HF','AF','B365H','B365D','B365A','HBP','ABP','winrate20_away','winrate20_home','FTR']]
df=df.dropna()

Y=df.pop('FTR')
X=df

#x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=1)

print(home+','+away+',',clf.predict(X))


