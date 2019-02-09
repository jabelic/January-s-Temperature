import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
 
sns.set()
 
df = pd.read_csv("data_high_low.csv",encoding="shift_jis",skiprows=[0,1,2,4,5],index_col=0)
 
df = df.drop(df.columns[[1,2]],axis=1)

x = np.linspace(1, 31, num = 31, endpoint = True, retstep = False, dtype = None)

Low2019 = np.array(df.loc["2019/1/1":"2019/1/31","C_low"])
High2019 = np.array(df.loc["2019/1/1":"2019/1/31","C_high"])

data = pd.DataFrame({
    "Highest temperature of the day":High2019,
    "Lowest temperature of the day":Low2019
})


ax = sns.jointplot(x = data.columns[0], y = data.columns[1],data = data,color="GREEN", kind="kde", shade_lowest=False)
ax.plot_joint(plt.scatter, c="c", s=30, linewidth=1, marker="+")

plt.show()
