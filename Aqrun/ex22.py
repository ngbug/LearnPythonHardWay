# -- coding: utf-8 --
"""
习题 22: 到现在你学到了哪些东西?

完成一个表格，回顾你到现在学到的所有东西。
回到你的每一个习题的脚本里
把你碰到的每一个词和每一个符号 (symbol，character 的别名)写下来。
确保你的符号列表是完整的。
下一步，在每一个关键词和字符后面写出它的名字，并且说明它的作用
"""

# 井号注释代码
print("Hello World") # 控制台输出字符串

print("number: %s" % 3) # 字符串替换

print("\n Let\'s") # 转义字符

data = False # Bool

print("*" * 10) # 字符串乘一个整数表示字符串重复

print('a' + 'b') # 加号 字符串连接

print('%r' % 'a') # 调用repr() 替换

raw_input("从控制台读取字符串")
input("读取值再转换") ## 相当于 eval(raw_input(prompt))

##########
# 文件操作
# 引入扩展包
from sys import argv
from os.path import exists

# 定义一个函数
def handle_file(file_name):
    data_file = open(file_name) # 打开一个文件
    file_content = data_file.read() # 读取文件内容
    file_content.close() # 操作完成关闭文件

    file_write = open(file_name, 'w')  # 以写的方式打开一个文件
    file_write.wite("This is the content to write")
    file_write.close()


if len(argv) > 2:
    # 读取控制台参数 第一个参数是当前脚本文件名称 之后是用户参数
    file_name = argv[1]
    if exists(file_name):
        handle_file(file_name)

var_a = 1
var_a += 1 # 加赋运算 *= -= /=





