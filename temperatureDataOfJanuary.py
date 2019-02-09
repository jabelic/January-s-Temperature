import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
 
sns.set()
 
df = pd.read_csv("data.csv",encoding="shift_jis",skiprows=[0,1,2,4,5],index_col=0)
 
df = df.drop(df.columns[[1,2]],axis=1)

x = np.linspace(1, 31, num = 31, endpoint = True, retstep = False, dtype = None)

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


dataframe = pd.DataFrame({
    "x":x,
    "2009":Y2009,
    "2010":Y2010,
    "2011":Y2011,
    "2012":Y2012,
    "2013":Y2013,
    "2014":Y2014,
    "2015":Y2015,
    "2016":Y2016,
    "2017":Y2017,
    "2018":Y2018
})

Data2 = pd.DataFrame({
        "2009":Y2009,
        "2010":Y2010,
        "2011":Y2011,
        "2012":Y2012,
        "2013":Y2013,
        "2014":Y2014,
        "2015":Y2015,
        "2016":Y2016,
        "2017":Y2017,
        "2018":Y2018
})




fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot('x', '2009', data=dataframe, label='2009',
        marker='o', linewidth=1, markersize=2.0)
ax.plot('x', '2010', data=dataframe, label='2010',
        marker='o', linewidth=1, markersize=2.0)
ax.plot('x', '2011', data=dataframe, label='2011',
        marker='o', linewidth=1, markersize=2.0)
ax.plot('x', '2012', data=dataframe, label='2012',
        marker='o', linewidth=1, markersize=2.0)
ax.plot('x', '2013', data=dataframe, label='2013',
        marker='o', linewidth=1, markersize=2.0)
ax.plot('x', '2014', data=dataframe, label='2014',
        marker='o', linewidth=1, markersize=2.0)
ax.plot('x', '2015', data=dataframe, label='2015',
        marker='o', linewidth=1, markersize=2.0)
ax.plot('x', '2016', data=dataframe, label='2016',
        marker='o', linewidth=1, markersize=2.0)
ax.plot('x', '2017', data=dataframe, label='2017',
        marker='o', linewidth=1, markersize=2.0)
ax.plot('x', '2018', data=dataframe, label='2018',
        marker='o', linewidth=1, markersize=2.0)

ax.legend()
ax.set_xlabel("date")  # 軸ラベル
ax.set_ylabel("temperature")
ax.set_ylim(-10,10)
#plt.show()
Data2.plot( kind='kde', figsize=(6, 5), fontsize=10 )


plt.show()
