import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
 
sns.set()
 
df = pd.read_csv("data.csv",encoding="shift_jis",skiprows=[0,1,2,4,5],index_col=0)
 
df = df.drop(df.columns[[1,2]],axis=1)

list_day = [i for i in range(1,32)]
x = np.array(list_day)

Y2009 = np.array(df.loc["2009/1/1":"2009/1/31","C"])
Y2010 = np.array(df.loc["2010/1/1":"2010/1/31","C"])
Y2011 = np.array(df.loc["2011/1/1":"2011/1/31","C"])
Y2012 = np.array(df.loc["2012/1/1":"2012/1/31","C"])
Y2013 = np.array(df.loc["2013/1/1":"2013/1/31","C"])
Y2014 = np.array(df.loc["2014/1/1":"2014/1/31","C"])
Y2015 = np.array(df.loc["2015/1/1":"2015/1/31","C"])
Y2016 = np.array(df.loc["2016/1/1":"2016/1/31","C"])
Y2017 = np.array(df.loc["2017/1/1":"2017/1/31","C"])
Y2018 = np.array(df.loc["2018/1/1":"2018/1/31","C"])

plt.plot(Y2009)
plt.plot(Y2010)
plt.plot(Y2011)
plt.plot(Y2012)
plt.plot(Y2013)
plt.plot(Y2014)
plt.plot(Y2015)
plt.plot(Y2016)
plt.plot(Y2017)
plt.plot(Y2018)
plt.show()