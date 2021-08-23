'''

函数	                描述
acos(x)	        返回x的反余弦弧度值。
asin(x)	        返回x的反正弦弧度值。
atan(x)	        返回x的反正切弧度值。
atan2(y, x)	    返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	        返回x的弧度的余弦值。
hypot(x, y)	    返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	        返回的x弧度的正弦值。
tan(x)	        返回x弧度的正切值。
degrees(x)	    将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	    将角度转换为弧度

'''
import math

# acos(x)
print(math.acos(0))

# asin(x)
print(math.asin(0))

# atan(x)
print(math.atan(0))

# sin(x)
print(math.sin(math.pi/6))

# cos(x)
print(math.cos(math.pi/3))

# tan(x)
print(math.tan(math.pi))


# hypot() 函数
print(math.hypot(0,2))

# degrees(x)
print(math.degrees(math.pi/2))

# radians(x)
print(math.radians(60.0))

