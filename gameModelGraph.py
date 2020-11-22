import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import math

""" 
在这个程序中，以第一次抽到的次数为变量绘制
概率质量函数和累积分布函数的图像 
"""


def increasePro():
    """ 绘制概率增加模型的概率质量函数和累积分布函数 """
    p = 0.01       # probability in the beginning
    alpha = 0.01   # increment of each round

    """ 生成概率列表和横坐标列表 """
    pro = []
    index = []

    failPro = 1         # PI(1-p-alpha*i) from 0 to n
    currPro = 0         # store the current index probability
    expectation = 1*p   # E[X]
    expectSquare = 1*p  # E[X**2]

    print('{0:.6f}'.format(currPro))
    for i in range(0, 50):
        currPro = failPro*(p+i*alpha)
        pro.append(currPro)
        index.append(i+1)
        failPro = failPro * (1 - p - i*alpha)
        expectation = expectation + (i+1)*currPro
        expectSquare = expectSquare + ((i+1)**2) * currPro

    maxPro = max(pro)
    maxidx = pro.index(maxPro)+1
    variance = expectSquare - expectation**2
    print("The expectation is {0:.4f}".format(expectation))
    print("The variance is {0:.4f}".format(variance))
    mu = maxidx
    sigma = 1 / (maxPro * np.sqrt(2*np.pi))

    """ 概率质量函数的绘制 """
    x = np.linspace(mu - 2*sigma, mu + 4*sigma, 50)
    y_sig = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / \
        (math.sqrt(2*math.pi)*sigma)
    plt.subplot(1, 2, 1)
    plt.plot(x, y_sig, "r-", label='Normal', linewidth=2)
    plt.plot(index, pro, label='Increasing Probability', linewidth=2)
    plt.vlines(maxidx, 0, maxPro, colors='g', linestyles="dotted")
    plt.legend()
    plt.title('Increasing Probability: E[X]:%.2f\nNormal: $\mu = %.2f, $sigma=%.2f' % (
        expectation, mu, sigma))
    plt.grid(True)

    """ 累积分布函数的绘制 """
    cdf = []
    temp1 = 0
    for p in pro:
        temp1 += p
        cdf.append(temp1)

    plt.subplot(1, 2, 2)
    plt.plot(index, cdf, label="Increasing model", linewidth=2)
    plt.plot(x, st.norm.cdf(x, loc=mu, scale=sigma),
             label='Normal', linewidth=2)
    plt.title('CDF Graph')
    plt.legend()
    plt.grid()


def tenthGuaranteeProPMF():
    """十连保底的概率质量函数图像的绘制 """
    p = 0.1
    index = [i for i in range(1, 11)]
    pro = [(1-p)**i*p for i in range(9)]
    pro.append((1-p)**9)
    cdf = []
    temp = 0
    for p in pro:
        temp += p
        cdf.append(temp)
    expectation = 0
    for i in range(10):
        expectation = expectation + (i+1)*pro[i]

    plt.rcParams['font.family'] = ['SimHei']
    plt.subplot(1, 2, 1)
    plt.bar(index, pro, label='TenthGuarantee')
    plt.title('minimum tenth guarantee: E[X]:%.4f' % (expectation))
    plt.subplot(1, 2, 2)
    plt.bar(index, cdf, label='CDF')
    plt.title('CDF of minimum tenth guarantee')


def extendedModel():
    p = 0.02
    pro = []
    idx = []
    failPro = (1 - p)   # probabilty that the previous draws all fail
    expectation = 0     # E[X]
    expectSquare = 0    # E[X**2]
    for i in range(0, 100):  # the index of the list represents the index+1 times drawal
        if i <= 49:
            pro.append(((1-p)**i) * p)
            failPro = failPro * (1 - p)
        elif 49 < i < 100:
            pro.append(failPro*(p + p * (i - 49)))
            failPro = failPro * (1 - p - p * (i - 49))
        idx.append(i+1)
        expectation += (i+1) * pro[i]
        expectSquare += (i+1) ** 2 * pro[i]


    variance = expectSquare - expectation ** 2
    maxPro = max(pro)
    maxIdx = pro.index(maxPro)+1


    plt.subplot(1, 2, 1)
    plt.plot(idx, pro, label="extended model", linewidth=2)
    plt.xlabel('Times')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.title("Extended Model:\nE[X]: %.2f, Var[X]: %.1f" % (
        expectation, variance))
    plt.vlines(maxIdx, 0, maxPro, color='c', linestyles='dotted')
    plt.legend()

    idx0 = [(i+1) for i in range(len(pro))]
    cdf = []
    temp = 0
    for p in pro:
        temp += p
        cdf.append(temp)

    plt.subplot(1, 2, 2)
    plt.title('CDF of extended model')
    plt.plot(idx0, cdf, label='CDF of extended Model', linewidth = 2)
    plt.grid()
    plt.legend()

    """ 根据绘制的图像进行相应的计算 """
    print('At the first 50 draws, only %.2f%% players can get A' %(cdf[49]*100))
    print('%.2f%% players get A bewteen 40 draws and 70 draws'%((cdf[69]-cdf[39])*100))

def main():
    # increasePro()
    # tenthGuaranteeProPMF()
    extendedModel()
    plt.show()


if __name__ == '__main__':
    main()
