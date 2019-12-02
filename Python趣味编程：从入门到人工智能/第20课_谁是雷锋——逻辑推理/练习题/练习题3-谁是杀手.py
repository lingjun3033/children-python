'''
程序：谁是杀手，逻辑推理
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

用1~4分别表示4个嫌疑犯，用枚举法列举杀手编号。
判断如果4个人说的话有3句成立，则找到答案。
提示：该题的编程思路可参考《Scratch趣味编程进阶》中的相同问题。
'''
def main():
    '''谁是杀手'''
    for k in range(1, 5):
        a = k != 1
        b = k == 3
        c = k == 4
        d = k != 4
        if a + b + c + d == 3:
            print('杀手的编号是', k)
            return

if __name__ == '__main__':
    main()
