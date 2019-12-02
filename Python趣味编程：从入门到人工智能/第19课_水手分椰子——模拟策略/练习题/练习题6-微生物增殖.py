'''
程序：微生物增殖
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

提示：该题的编程思路可参考《Scratch趣味编程进阶》中的相同问题。
'''
def main():
    '''微生物增殖'''
    x, y = 10, 90
    t = 1
    while t <= 60:
        y = y - x
        if t % 2 == 0:
            y = y * 2
        if t % 3 == 0:
            x = x * 2
        t += 1
    print('60分钟后Y的数量是', y)

if __name__ == '__main__':
    main()
