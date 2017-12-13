#!/usr/bin/python3
# python -m pip install -U pip
# python3 dugu_python.py
# python dugu_python.py
from sys import path
import sys
import math
import keyword
import random
import matplotlib
import scrapy
import numpy.random as nmr
from collections import deque
import dugu_lib as dugu
import pickle
import pprint as ppr

#python利用缩进编程，句尾没有分号
print("hello word")
print(1.2 * 2.3)

print(math.sin(math.pi / 2))  #这是一条注释
#python基础语法
print(keyword.kwlist)
if True:
    print(True)
    print(1.1 / 2)
elif False:
    pass
else:
    pass

#续航符：\

items = ['one', 'two', 'three', 'four']
print('\n')
print(items)

# py中有四种数据类型：整数、长整数、浮点数和复数
# py中使用单引号和双引号完全相同

wordStr = '这是一个字符串\n'
print(wordStr)

#py可以在同一行中使用多条语句，语句之间使用分号(;)分隔，以下是一个简单的实例
x = 'dugu'
print(x)
#py不换行输出
print(x, end=' ')
print(x, end=' ')
print(path.count(1))
#print(max.__doc__)

#py变量就是变量，所说的类型是变量所指内存中对象的类型
#py中有六个标准的数据类型：Number(数字)、String(字符串)
#List(列表)、Tuple(元组)、Sets(集合)、Dictionary(字典)
a, b, c, d = 20, True, 3.3, 1+2j 
print(type(a), type(b), type(c), type(d))
#isinstance和type的区别
#type()不会认为子类和父类是一种类型
#isinstance()会认为子类是一种父类类型
del x   #删除对象;
#加法，减法，乘法，除法，除法求模，乘方
print(5 + 4, 4.3 - 2, 3 * 7, 2 / 4, 2 // 4, 2 ** 5)
#复数的两种方式
fu = complex(2, 3)
strDuGu = 'Runoob'
 
print(strDuGu)          # 输出字符串
print(strDuGu[0:-1])    # 输出第一个到倒数第二个的所有字符
print(strDuGu[0])       # 输出字符串第一个字符
print(strDuGu[2:5])     # 输出从第三个开始到第五个的字符
print(strDuGu[2:])      # 输出从第三个开始的后的所有字符
print(strDuGu * 2)      # 输出字符串两次
print(strDuGu + "TEST") # 连接字符串
#但是字符串索引取字符串是只读的，只能读不能写
#word[0] = 'm'会导致错误。 

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
 
print(list)            # 输出完整列表
print(list[0])         # 输出列表第一个元素
print(list[1:3])       # 从第二个开始输出到第三个元素
print(list[2:])        # 输出从第三个元素开始的所有元素
print(tinylist * 2)    # 输出两次列表
print(list + tinylist) # 连接列表

#与Python字符串不一样的是，列表中的元素是可以改变的：
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')
 
print(tuple)             # 输出完整元组
print(tuple[0])          # 输出元组的第一个元素
print(tuple[1:3])        # 输出从第二个元素开始到第三个元素
print(tuple[2:])         # 输出从第三个元素开始的所有元素
print(tinytuple * 2)     # 输出两次元组
print(tuple + tinytuple) # 连接元组

#string、list和tuple都属于sequence（序列）。

#集合
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
 
print(student)   # 输出集合，重复的元素被自动去掉
 
# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
 
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集 
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素

#字典
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
 
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
 
 
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

print({x: x**2 for x in (2, 4, 6)})

print(str(dict))
# 注意下面只输出两个元素1代表索引1的元素，也就是第2个元素；
# 3代表第三个元素
listDu = ['abcd', 786, 2.23, 'runoob', 70.2]
print(listDu[1:3])       # 从第二个开始输出到第三个元素
print(listDu[2:3])

flag = True
if flag:
    print('ssss')
else:
    pass
'''
python逻辑运算符 and or not
'''
test = 2
if test < 2 and test >= 0:
    print(test)
tests = (2, 3, 4)
if test in tests:
    print(str(test) + 'is in tests')

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b,end=',')
    a, b = b, a+b
print("")
#py条件控制
var1 = 100
if var1:
    print(var1)

if var1 >= 99:
    print(99.99)

print(5 == 6)

print(2 % 3)
print(4 & 4)
print(random.choice(range(100)))

# py循环语句
guess = 1
sum_dugu = 0
while guess < 100:
    sum_dugu += guess
    guess += 1
    if guess == 88:
        break
else:
    print("循环结束啦")
print("和为:",sum)
languages = ["c", "c++", "c#", "Python"]
for lan in languages:
    print(lan,end=' ')
    print("")
languages = {"c", "c++", "c#", "Python"}
for lan in languages:
    print(lan,end=' ')
    print("")
languages = ("c", "c++", "c#", "Python")
for lan in languages:
    print(lan,end=' ')
    print("")

for letter in "DuGu":
    if letter == 'u':
        continue
    print("the letter is", letter)

varNum = 10
while varNum > 0:
    print("now the num is ",varNum)
    varNum -= 1
    if varNum == 5:
        break

print("good bye")

#while语句和for循环语句都可以加else(另外加break)
cards = ["A", "B", "C", "D"]
for card in cards:
    if card == "C":
        print(card)
        break
    print("card is", card)
else:
    print("no card be found")
# range()函数
# 相当于matlab中的1:2:10
for j in range(1,10,2): 
    print("this num 1 is ", j)

#可以结合range函数和len函数遍历集合的索引
words = ["google", "microsoft", "facebook", "???", "??"]
for i in range(len(words)):
    print(i, words[i])

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)
# 或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。 

# 查询质数的例子

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        print(n, '是质数')

# 使用 enumerate ,好使
dugustrs = ["?", "??", "???", "????"]
for i, o in enumerate(dugustrs):
    print(i, o)

## py3迭代器与生成器
#迭代器 iter
NUM_LIST = [1, 2, 3, 4]
it = iter(NUM_LIST)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
for x in it:
    print(x, end=' ')

it2 = iter(NUM_LIST)
print(next(it2), end=' ')
print(next(it2), end=' ')
print(next(it2), end=' ')
print(next(it2), end=' ')

#生成器 yield
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)
print(next(f), end=' ')
print(next(f), end=' ')
print(next(f), end=' ')
print(next(f), end=' ')
print(next(f), end=' ')
print(next(f), end=' ')
print(next(f), end=' ')
print(next(f), end=' ')

# python3 函数
# def 函数名（参数列表）:
#    函数体
## py3函数
def hello():
    print("hello world")

hello()
# 元组是值类型，列表，字典是引用类型
#可写函数说明
def printme( str = "dugu"):
   "打印任何传入的字符串"
   print (str);
   return;
 
#调用printme函数
printme( str = "hello me");
printme()

# 不定长参数
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;
 
# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );

# lambda
sum = lambda arg1, arg2 : arg1 + arg2;
print(sum(12.3, 23.5))

X = int(2.7)
print(X)
# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域

total = 0; # 这是一个全局变量
# 可写函数说明
def sum2( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2; # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total;

#调用sum函数
total = sum2( 10, 20 );
print ("函数外是全局变量 : ", total)

# global 和 nonlocal关键字可以改变作用域

print(nmr.laplace(1.1))

## python3 数据结构
#列表list可以修改，tuple和字符串不行
A = [12,3,45.6]
print(A.count('str'))
A.append(17.9)
print(A)
A.sort(reverse=False)
print(A)
A.sort(reverse=True)
print(A)
queue_me = deque(['1', 'aeee', 'dugu'])
print(queue_me.popleft())
queue_me.append('ssss')
queue_me.append('sad')
print(queue_me)

#列表推导式
Y = [12, 23, 45]
print([[y, y ** 2] for y in Y]) 
wepon = [' sd   ', 'sss   ', '  assa']
print([[w, str(w).strip()] for w in wepon])
VET1 = [1, 2, 3]
VET2 = [4, 5, 6, 7]
print([[v1, v2] for v1 in VET1 for v2 in VET2])

#通过嵌套列表构成矩阵Matrix
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(M)

# del 删除语句
C = [1,2,3,4,'23','232',[1,2,3]]
del C[2]
print(C)

# 元组和序列
T = 12, 23, 45
U = 12,T
print(U)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
dic_me = {str(x): x**2 for x in (2, 4, 6)} # 推导式创建字典
print(dic_me)
for k, v in dic_me.items():
    print(k, v)
i = 0
for k, v in enumerate(dic_me):
    print(i, k, v)
    i += 1
print('')
for k, v in enumerate(C):
    print(k, v)
print('')
for i in reversed(range(1, 10, 3)):
    print(i)
print('')
for i, j in zip(dic_me, C):
    print(i, j)

## python3 模块
for p in sys.argv:
    print(p)
print(sys.path)

dugu.print_func('dugu')

## python3 输入和输出
S = 'hello dugu\n'
print(repr(S))
print(str(S))
for i in range(1,11):
    print(repr(i).rjust(2), repr(i * i).rjust(3), end=' ')
    print(repr(i * i * i).rjust(4))
print('')
for i in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(i, i * i, i * i * i))
print('12'.zfill(5), '123456'.zfill(6))
print('{} {} {other}'.format(123, 345, other='1233333'))
#'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
PI = math.pi
print('{!a} {!s} {!r}'.format(PI, PI, PI))
print('the pi is %3.5f' % PI)
#键盘读入 input
#文件读入 open
myfile = open('file_test.txt','w')
myfile.write("123\n")
myfile.write("123\n")
print(myfile.write("'123444'\n"))
myfile.flush()
myfile.close()

dufile = open('file_test.txt','r')
print(dufile.readlines())
dufile.close()

# 相当于c#中的using
with open('file_test.txt', 'w') as f:
    f.write('1233333')
#pickle模块实现了对象的序列化和反序列化
data = {'key' : 123, 'value' : 'sdd'}
print(str(data))
with open('data.ini', 'wb') as wb:
    pickle.dump(data, wb)
with open('data.ini', 'rb') as rb:
    data_read = pickle.load(rb)
    ppr.pprint(data_read)
## pyhton3 OS

print('')

