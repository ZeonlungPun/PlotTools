# Libraries

import pandas as pd
from math import pi
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt

data=pd.read_excel('D:\codes\matlab_code\\alloy\w1000\\alldata.xlsx',engine='openpyxl')
df=data.iloc[:,9::]

df=df.apply(lambda x:(x-min(x))/(max(x)-min(x)),axis=0)
df=np.array(df)
#要展示的指标
#sel_col = ['Al','Ti','Cr','Co','Ni','Nb','Mo','Ta','W']
sel_col=['Y1','Y2','Y3','Y4','Y5','Y6','Y7']

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

name = sel_col  #标签

theta = np.linspace(0,2*np.pi,len(name),endpoint=False)    #将圆根据标签的个数等比分
theta = np.concatenate((theta, [theta[0]]))  # 闭合
name=name+['Y1']  #闭合坐标
#value = np.random.randint(50,100,size=9)   #在60-120内，随机取5个数
for value in df:

    value = np.concatenate((value,[value[0]]))  #闭合

    #print(len(theta),len(value))
    ax = plt.subplot(111,projection = 'polar')      #构建图例
    ax.plot(theta,value,'m-',lw=1,alpha = 0.75)    #绘图
    ax.fill(theta,value,'m',alpha = 0.75)           #填充
    ax.set_thetagrids(theta*180/np.pi,name)         #替换标签
    ax.set_theta_zero_location('N')         #设置极轴方向
ax.set_ylim(0,1)     #设置极轴的区间
ax.set_title('W1000',fontsize = 20)   #添加图描述
plt.show()