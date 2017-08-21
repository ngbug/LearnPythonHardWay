#元组Tuple
#Python的元组与列表类似，不同之处在于元组的元素一旦定于就不能修改。元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
course = ('chinese','math','english','computer')
print (course)
print(course[0])
print(course[1:3])
print(course[1:])
print(course[:1])

#len返回元素个数
print(len(course))

#要定义一个只有1个元素的元组，则只需要在元素后面加逗号，用来消除数学歧义
t = (1,)

#返回元组最大的值
score = (78,90,88,67,78)
print(max(score))
#返回元组最小的值
print(min(score))