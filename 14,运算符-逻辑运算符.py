'''

运算符	逻辑表达式	        描述	                                                                    实例
and	    x and y	    布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值。	    (a and b) 返回 20。
or	    x or y	    布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	        (a or b) 返回 10。
not	    not x	    布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False

'''
# and
a=10
b=20
print(a and b)

# or
print(a or b)

# not
print(not b)