#!/usr/bin/python
# -*-coding:UTF-8-*-

#错误的方法
def is_int(x):
    if int(x)==x:
        return True
    else:
        return False

#isinstance(p_object, class_or_type_or_tuple) 标准库函数
def is_int_two(x):
    return isinstance(x,int)

print "is_int",is_int(1.0)
print "is_int_two",is_int_two(1.0)

#转成str循环，再转成int相加
def digit_sum(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total

print "digit_sum",digit_sum(1234)

#range(start,end,step) [start, end)
def factorial(x):
    sums = 1
    for i in range(1,x+1):
        sums*=i
    return sums

print "factorial",factorial(4)


#反转字符串 此处使用字符串的截取方法  string(start:end:step) 不填既是默认值，-1代表反向截取
def reverse(text):
    print text[::-1]

print "reverse",reverse("abcd")

#遍历字符串，如果字符不再范围内，则组成新的字符串返回
def anti_vowel(text):
    temp = ""
    for s in text:
        if s not in "aeiouAEIOU":
            temp+=s
    return  temp

#参见Hint 先用split()方法以word分割text，生成不包含word的列表
#在用 ***与列表组合成新字符串
def censor(text,word):
    list = text.split(word)
    string = ("*"*len(word)).join(list)
    return string

#创建新的list存放不重复的元素
def remove_duplicates(lists):
    new_list = []
    for i in lists:
        if i not in new_list:
            new_list.append(i)
    return  new_list

#求中位数的方法
#sorted方法将列表排序
#注意列表下标是从 0 开始的
def median(nums):
    new_list = sorted(nums)
    if len(nums)%2 != 0:
        return new_list[len(nums)/2]
    else:
        temp = len(nums)/2
        return float(new_list[temp]+new_list[temp-1])/2

print "median :",median([9,5,6,7,1,8,3])