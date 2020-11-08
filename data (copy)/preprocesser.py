import pandas as pd
import glob

names=glob.glob('./*.csv')

cols='Date,HomeTeam,AwayTeam,HS,AS,HST,AST,HC,AC,HF,AF,HY,AY,HR,AR,B365H,B365D,B365A,FTHG,FTAG,FTR'

file=open('all_data.txt',w)

for name in names:
	data=pd.read_csv(name)
	data=data[cols.split(',')]
	data.to_csv(name,index=false)
	with open(name,'r') as f:
		lines=f.readlines()
		file.write(lines[1:])

file.close()

data=pd.read_csv('all_data.txt')

# booking points (number of red and yellow cards)
def faltas_score(yellow,red):
	new=[]
	
	if (len(yellow)!=len(red)):
		print('different lengths')

	for x in range(len(yellow)):
		new.append(yellow[x]+red[x])
	return new


data['HBP']=faltas_score(data['HY'],data['HR'])
data=data.drop(['HY','HR'],1)

data['ABP']=faltas_score(data['AY'],data['AR'])
data=data.drop(['AY','AR'],1)


def result(result_column):
	new=[]
	for x in range(len(result_column)):
		if result_column[x]=='H':
			new.append(0)
		if result_column[x]=='D':
			new.append(1)
		if result_column[x]=='A':
			new.append(2)
	
	return new
data['FTR']=result(data['FTR'])


def date2int(date):
	new=[]
	for x in range(len(date)):
		day=date[x][:2]
		month=date[x][3:5]
		year=date[x][6:]

		new_date=year+month+day
		new.append(new_date)

	return new
data['Date']=date2int(data['Date'])


cols2avg_home='HS,HST,HC,HF,FTHG'
cols2avg_home=cols2avg_home.split(',')

cols2avg_away='AS,AST,AC,AF,FTAG'
cols2avg_away=cols2avg_away.split(',')

og=data.copy()
for x in range(len(data)):
	hometeam=data.at[x,'HomeTeam']
	date=data.at[x,'Date']
	
	df_date=og.loc[og['Date'] < date]
	df=df_date.loc[df_date['HomeTeam']==hometeam]
	df=df.tail(5)

	if len(df)>0:
		print(x)
		for col in cols2avg_home:
			y=0
			for value in df[col]:
				y=y+float(value)
			avg=y/len(df)
			data.at[x,col]==avg
		
		y=0
		for value in df['FTR']:
			if value == 0:
				y=y+1
		data.at[x,'winrate20_home']=y/len(df)

	awayteam=data.at[x,'AwayTeam']
	df=df_date.loc[df_date['AwayTeam']==awayteam]
	df=df.tail(5)

	if len(df)>0:
		print(x)
		for col in cols2avg_away:
			y=0
			for value in df[col]:
				y=y+float(value)
			avg=y/len(df)
			data.at[x,col]==avg
		
		y=0
		for value in df['FTR']:
			if value == 2:
				y=y+1
		data.at[x,'winrate20_away']=y/len(df)


print(data)


