#for 循环
#案例1：将Student数组值全部打印出来

student = ['jack','bob','marry','micle']
for stu in student:
     print(stu)

#案例2：计算 1+2+3+...10的值
#python提供一个range()的函数，可以生成一个整数序列，比如rang(10)生成的序列是从0开始小于10的整数

sum = 0
for i in range(11):
    sum = sum + i
print(sum)

#while循环
#while循环，只要满足条件，就不断循环，条件不满足时退出循环。

n = 10
while n>0:
    n = n-1
    print(n)
print ('over!')

