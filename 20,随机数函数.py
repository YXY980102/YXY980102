'''

随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
函数	                        描述
choice(seq)	    从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange       ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
random()	    随机生成下一个实数，它在[0,1)范围内。
seed([x])	    改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

'''
import random

# choice(seq)
a=random.choice(range(10))  # 从0到9中随机挑选一个整数。
print(a)

# randrange
# 从 1-100 中选取一个奇数
print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
# 从 0-99 选取一个随机数
print("randrange(100) : ", random.randrange(100))

# random()
c=random.random()
print(c)

# seed() 函数
random.seed()
print ("使用默认种子生成随机数：", random.random())
print ("使用默认种子生成随机数：", random.random())

random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())

random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())


# shuffle() 函数
list = [20, 16, 10, 5]
random.shuffle(list)
print ("随机排序列表 : ", list)


# uniform() 函数
print(random.uniform(1,100))
