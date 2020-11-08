def myacc(preds2,test):
  preds=[]
  for i in range(len(preds2)):
    if preds2[i] < 0.5:
      preds.append(0)
    else:
      preds.append(1)

  test=list(test)
  count=0
  for i in range(len(test)):
    if preds[i]==test[i]:
      count=count+1

  return count/len(test)

