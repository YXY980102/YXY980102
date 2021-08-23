'''

函数	                返回值 ( 描述 )
abs(x)	        返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	        返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)       如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃，使用 (x>y)-(x<y) 替换。
exp(x)	        返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	        返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	    返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	        如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	    返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	        返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	    x**y 运算后的值。
round(x [,n])   返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。其实准确的说是保留值将保留到离上一位更近的一端。
sqrt(x)	        返回数字x的平方根。

'''
import math

# abs()
print(abs(-12))

# ceil(x)
print(math.ceil(4.1))

# exp(x)
print(math.exp(1))

# fabs(x)
print(math.fabs(-12))

# floor(x)
print(math.floor(4.3))

# log()
print(math.log(100,10))

# log10(x)
print(math.log10(100))

# max(x1, x2,...)
print(max(100,1000,10000))

# min(x1, x2,...)
print(min(100,1000,10000))

# modf(x)
print(math.modf(12.3))

# pow(x, y)
print(pow(2,3))

# round(x [,n])
print(round(72.2344))

# sqrt(x)
print(math.sqrt(16))