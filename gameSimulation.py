import random
import matplotlib.pyplot as plt
import math


def randomDraw(p):
    if random.random() < p:
        return True
    else:
        return False


def drawInModel1(p, alpha):
    drawResult = []
    """ 抽卡直到抽中的次数 """
    # for i in range(10000):
    #     pro = p
    #     times = 0
    #     while not successfulDraw:
    #         if randomDraw(pro):
    #             successfulDraw = True
    #         else:
    #             pro += alpha
    #         times += 1
    #     drawResult.append(times)

    """ 100抽中抽中的次数 """
    for i in range(10000):
        pro = p
        times = 0
        for j in range(100):
            if randomDraw(pro):
                times += 1
                pro = p
            else:
                pro += alpha
        drawResult.append(times)

    drawDict = {}
    for key in drawResult:
        drawDict[key] = drawDict.get(key, 0) + 1

    for key in drawDict.keys():
        drawDict[key] /= 10000

    return drawDict


def drawInExtendedModel(p, alpha):
    drawResult = []
    for i in range(10000):
        pro = p
        times = 0
        numOfdraws = 0          # the number of draws before the successful draw
        for j in range(100):
            numOfdraws += 1
            if randomDraw(pro):  # if draw successfully
                times += 1      # reset the probability, numOfdraws, and increase the times
                numOfdraws = 0
                pro = p
            elif numOfdraws >= 50:
                pro += alpha

        drawResult.append(times)

    drawDict = {}
    for key in drawResult:
        drawDict[key] = drawDict.get(key, 0) + 1

    for key in drawDict.keys():
        drawDict[key] /= 10000

    return drawDict


def drawInPure(p):
    drawResult = []
    for i in range(10000):
        times = 0
        for j in range(100):
            if randomDraw(p):
                times += 1
        drawResult.append(times)

    drawDict = {}
    for key in drawResult:
        drawDict[key] = drawDict.get(key, 0) + 1

    for key in drawDict.keys():
        drawDict[key] /= 10000

    print(drawDict)
    return drawDict


def drawInTenthGuarantee(p):
    drawResult = []
    for i in range(10000):
        times = 0
        for j in range(10):
            for k in range(10):
                successfulDraw = False
                if randomDraw(p):
                    times += 1
                    successfulDraw = True
            if not successfulDraw:
                times += 1

        drawResult.append(times)

    drawDict = {}
    for key in drawResult:
        drawDict[key] = drawDict.get(key, 0) + 1

    for key in drawDict.keys():
        drawDict[key] /= 10000

    print(drawDict)
    return drawDict


def graph1():
    """ 概率增加模型模拟图像 """
    p = 0.01
    alpha = 0.01
    drawDict = drawInModel1(p, alpha)
    plt.title('Increasing model')
    plt.bar(drawDict.keys(), drawDict.values())
    plt.xlabel("Number successful draws in 100 draws")
    plt.show()


def graph2():
    """ 绘制纯随机模拟图像 """
    p = 0.05
    drawDict = drawInPure(p)
    plt.title('Pure Random Probability')
    plt.bar(drawDict.keys(), drawDict.values())
    plt.xlabel("Number successful draws in 100 draws")
    plt.show()


def graph3():
    """ 绘制十连保底模拟图像 """
    p = 0.05
    drawDict = drawInTenthGuarantee(p)
    plt.title('Ten Consecutive Draws with Minimum Guarantee')
    plt.bar(drawDict.keys(), drawDict.values())
    plt.xlabel("Number successful draws in 100 draws")
    plt.show()


def graph4():
    """ 绘制拓展模型模拟图像 """
    p = 0.02
    alpha = 0.02
    drawDict = drawInExtendedModel(p, alpha)
    plt.title('Extended Model')
    plt.bar(drawDict.keys(), drawDict.values())
    plt.xlabel("Number successful draws in 100 draws")
    plt.show()


def main():
    # graph1()
    # graph2()
    # graph3()
    graph4()


if __name__ == '__main__':
    main()
