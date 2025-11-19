# 一、理解函数调用和变量概念

"""
1、概念：以.py结尾的文件为python程序
2、print为输出打印函数
3、# 为单行注释
4、""" """或''' '''为多行注释
5、print+括号引号里边的内容“原样输出”，没有引号的内容输出它的值
6、参数：参数是传递给函数的输入，某种程度上影响其行为。
"""
# print("hello，world")
# print("hello.py")

# 课后习题：编写第一个Python程序，打印“Hello World”
# print("Hello World")

# 二、掌握函数定义和调用方法

# 1、概念：需要一个函数用来获取用户输入的值———输入函数input（）

# input("What's your name ?") # 使用input函数获取用户输入的内容，且为字符串类型
# print("Hello MeiXin") # 原样输出引号中的内容，和用户实际输入的值无关
"""
1、实现返回用户输入的内容
2、功能：函数的返回值
3、变量：变量可以存储一个值（存储到内存中），数字、文本、图片或者是视频
4、赋值运算符：X = 1 ，将1的值符给变量X
"""
# name = input("What’s your name? ")  # 将用户输入的内容赋值给变量name（字符串型）
# print('hello,')
# print(name)   # name没有加引号则打印输出它的值，为用户输入的内容

# name = input (" What's your name ? ")
# hello()   # hello（）函数没有被定义，所以会产生“名称错误：hello没有定义”是不存在的
# print(name)

"""
1、定义、创建、发明自己的函数，使用关键字def（def——定义的缩写、str字符串的缩写，int整型的缩写）
2、def hello()自定义函数，以冒号结尾，且换行后产生缩进，缩进下方所有的内容都成为这个函数的一部分
3、函数名称为hello()，且括号中没有任何值或参数
4、
"""

# def hello():
#     print("hello") # 自动缩进为4个空格；确保所有代码，缩进对齐。
# name = input("What's your name? ")
# hello()
# print(name)
"""
1、将上方相同的函数hello（）进行函数参数化
2、自定义hello，让它接受用户的名字作为输入
3、# 调用def定义的函数hello，且将name的值传递给to（将名称变量作为参数输入）
4、hello（name）的值被复制了一份传递给hello（to）
"""
# def hello(to):
#     print("hello,",to)  # 原样打印引号里边的内容，to代表获取hello的值，hello的值为用户输入的name的值
# name = input("What is your name? ")
# hello(name) # 调用def定义的函数hello，且将name的值传递给to（将name变量作为参数输入给to）

"""
1、给参数设置默认值
2、print，sep的默认值用于分隔符；end的默认值是行结束符
3、定义hello的函数，参数为to，给to赋值为world，防止程序员不带任何参数调用hello
4、定义了hello，即使在最顶部或者不同文件中，都可以调用它
"""
# def hello(to="world"): # 定义函数hello， 参数为to，给to赋默认值为world，防止程序员不带任何参数调用hello
#     print("hello,",to)
# hello() # 简单的调用hello，没有参数
# name = input("What's your name? ") # 获取用户的姓名
# hello(name) # 调用函数，参数为name
"""
1、将代码的主要部分放在文件的顶部
2、进一步定义函数，Main（）——主函数
"""
def main():   # main 主函数，程序的主要部分
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,",to)
main()  # 调用主函数 main
hello(name)
# 练习：创建计算器函数（加减乘除）
# 三、熟练使用不同类型变量
# 练习：编写程序计算圆的面积和周长

















