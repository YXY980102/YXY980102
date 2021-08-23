'''

运算符	描述	        实例
==	    等于 - 比较对象是否相等	(a == b) 返回 False。
!=	    不等于 - 比较两个对象是否不相等	(a != b) 返回 True。
>	    大于 - 返回x是否大于y	(a > b) 返回 False。
<	    小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 True。
>=	    大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
<=	    小于等于 - 返回x是否小于等于y。	(a <= b) 返回 True。

注:比较运算符最后返回的只能是bool值(即True和False)

'''
a=10
b=20

# ==等于
print(a==b)
# !=不等于
print(a!=b)
# >大于
print(a>b)
# <小于
print(a<b)
# >=大于等于
print(a>=b)
# <=小于等于
print(a<=b)