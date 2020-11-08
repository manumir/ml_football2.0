import pandas as pd
import glob

names=glob.glob('./*.csv')

cols='Date,HomeTeam,AwayTeam,HS,AS,HST,AST,HC,AC,HF,AF,HY,AY,HR,AR,B365H,B365D,B365A,FTHG,FTAG,FTR'

file=open('all_data.txt','w')

wrote_header=0
for name in names:
	print(name)
	data=pd.read_csv(name)
	data=data[cols.split(',')]
	data.to_csv(name,index=False)
	with open(name,'r') as f:
		lines=f.readlines()
		if wrote_header==0:
			wrote_header=1
			file.write(lines[0])
		for line in lines[1:]:
			file.write(line)

file.close()

