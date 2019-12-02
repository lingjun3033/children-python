'''
程序：莫尔斯码，支持字母、数字和标点符号
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
codes = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..',
         'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
         'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
         'M':'--', 'N':'-.', 'O':'---', 'P':'.--.',
         'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
         'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
         'Y':'-.--', 'Z':'--..',
         '0':'-----', '1':'.----', '2':'..---', '3':'...--',
         '4':'....-', '5':'.....', '6':'-....', '7':'--...',
         '8':'---..', '9':'----.',
         '.':'.-.-.-', ':':'---...', ',':'--..--', ';':'-.-.-.',
         '?':'..--..', '=':'-...-', '\'':'.----.', '/':'-..-.',
         '!':'-.-.--', '-':'-....-', '_':'..--.-', '"':'.-..-.',
         '(':'-.--.', ')':'-.--.-', '$':'...-..-', '&':'....',
         '@':'.--.-.', '+':'.-.-.',
         }

words = input('请输入一句英文:')
for s in words:
    code = codes.get(s.upper(), s)
    print(code, end=' ')
