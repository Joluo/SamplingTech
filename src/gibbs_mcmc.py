#coding:utf-8
# refer to: http://blog.csdn.net/Dark_Scope/article/details/70992266

import numpy as np
import math
import matplotlib.pyplot as plt

PI = math.pi

def domain_random(): #计算定义域一个随机值
    return np.random.random()*3.8-1.9
def get_tilde_p(x):
    # 模拟不知道怎么计算Z的PI，20这个值对于外部采样算法来说是未知的，对外只暴露这个函数结果
    return get_p(x)*20

def get_p(x):
    # 模拟pi函数
    return 1/(2*PI)*np.exp(- x[0]**2 - x[1]**2)

def partialSampler(x,dim):
    xes = []
    for t in range(10): #随机选择10个点
        xes.append(domain_random())
    tilde_ps = []
    for t in range(10): #计算这10个点的未归一化的概率密度值
        tmpx = x[:]
        tmpx[dim] = xes[t]
        tilde_ps.append(get_tilde_p(tmpx))
    #在这10个点上进行归一化操作，然后按照概率进行选择。
    norm_tilde_ps = np.asarray(tilde_ps)/sum(tilde_ps)
    u = np.random.random()
    sums = 0.0
    for t in range(10):
        sums += norm_tilde_ps[t]
        if sums>=u:
            return xes[t]

def gibbs(x):
    rst = np.asarray(x)[:]
    path = [(x[0],x[1])]
    for dim in range(2): #维度轮询，这里加入随机也是可以的。
        new_value = partialSampler(rst,dim)
        rst[dim] = new_value
        path.append([rst[0],rst[1]])
    #这里最终只画出一轮轮询之后的点，但会把路径都画出来
    return rst,path

def testGibbs(counts = 100,drawPath = False):
    #plotContour()

    x = (domain_random(),domain_random())
    xs = [x]
    paths = [x]
    for i in range(counts):
        xs.append([x[0],x[1]])
        x,path = gibbs(x)
        paths.extend(path) #存储路径
    if drawPath:
        plt.plot(map(lambda x:x[0],paths),map(lambda x:x[1],paths),'k-',linewidth=0.5)
    plt.scatter(map(lambda x:x[0],xs),map(lambda x:x[1],xs),c = 'g',marker='.')
    plt.show()

testGibbs(5000, False)
