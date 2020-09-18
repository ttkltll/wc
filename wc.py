### 需求:写一个计算器命令行程序：
"""
在命令行输出如下：
请输出命令：
wc.exe -c file.python: char count

思路：
先读取一个文件
然后对这个文件对象操作
如何统计它的字数多少呢
python应该有一个内置函数。
也可以自己遍历这个字符，然后统计

"""


def count(file_path):
    with open(file_path, 'r') as f:
        string = f.read()
        return len(string)


# 给定一个文本文件的路径，返回它的行数
def count_lines(file_path):
    if file_path == '*.py':
        #那么这个文件夹下所有.py的文件都要统计

    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

def count_words(file_path):
    with open(file_path, 'r') as file:
        string = file.read()
        return len(string.split())




if __name__ == "__main__":
    while True:
        print("请输入命令和文件:")
        a, b = input().split(' ')
        if a == '-c':
            print(count(b))
        elif a == '-w':
            print(count_words(b))
        else:
            print(count_lines(b))




