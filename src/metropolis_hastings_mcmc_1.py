#coding:utf-8
# refer to: http://blog.csdn.net/Dark_Scope/article/details/70992266

import numpy as np
import math
import matplotlib.pyplot as plt

PI = math.pi

def domain_ramdon_2(x):
    x_star = np.random.normal(x, 1)
    return x_star

def domain_random(): #计算定义域一个随机值
    return np.random.random()*3.8-1.9
def metropolis(x):
    new_x = domain_ramdon_2(x) #(domain_random(),domain_random()) #新状态
    #计算接收概率
    acc = min(1,get_tilde_p((new_x[0],new_x[1]))/get_tilde_p((x[0],x[1])))
    #使用一个随机数判断是否接受
    u = np.random.random()
    if u<acc:
        return new_x
    return x

def get_p(x):
    # 模拟pi函数
    return 1/(2*PI)*np.exp(- x[0]**2 - x[1]**2)
def get_tilde_p(x):
    # 模拟不知道怎么计算Z的PI，20这个值对于外部采样算法来说是未知的，对外只暴露这个函数结果
    return get_p(x)*20

def testMetropolis(counts = 100,drawPath = False):
    #plotContour() #可视化
    #主要逻辑
    x = (domain_random(),domain_random()) #x0
    xs = [x] #采样状态序列
    for i in range(counts):
        xs.append(x)
        x = metropolis(x) #采样并判断是否接受
    #在各个状态之间绘制跳转的线条帮助可视化
    if drawPath:
        plt.plot(map(lambda x:x[0],xs),map(lambda x:x[1],xs),'k-',linewidth=0.5)
    ##绘制采样的点
    plt.scatter(map(lambda x:x[0],xs),map(lambda x:x[1],xs),c = 'g',marker='.')
    plt.show()
    pass

testMetropolis(100, True)
