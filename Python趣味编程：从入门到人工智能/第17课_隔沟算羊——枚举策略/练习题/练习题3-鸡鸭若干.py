'''
程序：鸡鸭若干
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

根据题意得出两个等式：
    x = y / 2
    y - 8 = 3 * (x - 6)
采用枚举法，用单重循环列举x的值，y的值可由等量关系计算得到。
判断如果等式成立，则可求得答案。
'''
def main():
    '''鸡鸭若干'''
    x = 1
    while True:
        y = 2 * x
        if y - 8 == 3 * (x - 6):
            print('鸡、鸭数量分别是:', x, y)
            break
        else:
            x = x + 1

if __name__ == '__main__':
    main()
