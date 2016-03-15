#!/usr/bin/python
# -*-coding:UTF-8-*-

#主要讲了些python自带方法用法

#创建list的语法
# [x for x in range() if statements]

doubles_by_3 = [x*2 for x in range(1,6) if (x*2)%3==0]

print "doubles_by_3",doubles_by_3

even_squares = [x**2 for x in range(1,11) if x%2==0]

print "even_squares:", even_squares

#list截取语法 lists[start :end :step] 【start,end)
#包括开始下标，但不包括结束下标，step是步长
lists = [i**2 for i in range(1,11)]
#此处将lists 下标从2到9之间数输出，间隔为2
print lists[2:9:2]
print "lists的反转，步长为-1:",lists[::-1]


#lambda 函数式编程语法
# filter ( lambda x: x>30 and x<70, squares )
#filter将第二个参数列表遍历并依次传给lambda函数
#lambda 函数 == def xx(x) return condition
nums = [1,2,3,4,56,7,8,9]

print "lambda:",filter(lambda x: x>5 ,nums)
#等同于
def temp_fun(nums):
    new_list = []
    for x in nums:
        if x>5:
            new_list.append(x)
    return new_list
print "temp_fun:" ,temp_fun(nums)