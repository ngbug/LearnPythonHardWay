#Python编程中if语句用于控制程序的执行，基本形式为：
#if 判断语句：
#    执行语句...

#else为可选语句，当需要在条件不成立时执行内容则可以执行相关语句
#if判断语句：
#    判断语句...
#else:
#    判断语句...

#案例1：根据分数来判断学生成绩是否为优秀，80分及以上为优秀，评级为A
score = 80
if score >= 80:
    print("score is A")
else:
    print("score is not A")


#注意：print语句要注意缩进，不要Tab和空格混用，否则会编译报错

#案例2：成绩80分以上为评级A,60-79分为B，60分以下为C
score = 90
if score >=80:
    print("score is A")
elif score >=60:
    print("score is B")
else:
    print("score is c")

#tips:elif是else if的缩写，完全可以有多个elif



