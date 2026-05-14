import pandas as pd

xd=pd.read_csv("data.csv")
y=pd.DataFrame([[1,2,3],[4,5,6]],columns=["A","B","C"],index=["X","Y"])
#y.to_csv("nose.csv")
print(y.describe())
#xd.index=["x","y","z"]
#print(xd)