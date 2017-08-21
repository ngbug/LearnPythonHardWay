#字典是另一种可变容器模型，且可存储任意类型对象。字典的每个键值（key=>value)对用冒号(:)分割，
# 每个对之间用(,)分割，整个字典包括在花括号{}中，格式如下：

#d = { key1 : value1 , key2 : value2 }

#定义访问字典

student = { 1:'jack', 2:'bob',3:'marry',4:'micle'}
print(student[3])

#添加元素

#增加新的键值对
student[5]='51zxw'
print(student)

#修改元素
student[2]= 'harry'
print(student)

#删除元素

#修改字典
student[2]='harry'
print(student)

#删除某一个键值对
del student[1]
print (student)

#q清空字典全部字典
student.clear()
print (student)

#s删除字典
del student
