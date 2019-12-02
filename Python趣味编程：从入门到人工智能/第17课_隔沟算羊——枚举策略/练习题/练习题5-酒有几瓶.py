'''
程序：酒有几瓶
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

根据题意得出两个等式：
    x + y = 19
    3 * x + y / 3 = 33
采用枚举法，用单重循环列举x的值，y的值可由等量关系计算得到。
判断如果等式成立，则可求得答案。
'''
def main():
    '''酒有几瓶'''
    x = 1
    while True:
        y = 19 - x
        if 3 * x + y / 3 == 33:
            print('醇酒、醨酒数量分别是:', x, y)
            break
        else:
            x = x + 1

if __name__ == '__main__':
    main()
