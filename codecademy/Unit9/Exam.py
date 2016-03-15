#!/usr/bin/python
# -*-coding:UTF-8-*-

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

#打印所有分数
def print_grades(grades):
    for grade in grades:
        print grade

print "分数分别是\n ",print_grades(grades)


#计算分数和
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

print "总分是： ",grades_sum(grades)


#计算平均分，此处使用总分方法
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

print "平均分是： ",grades_average(grades)


#计算
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / float(len(scores))


print "方差是：",grades_variance(grades)


def grades_std_deviation(variance):
    return variance ** 0.5


variance = grades_variance(grades)
print "标准差是：",grades_std_deviation(variance)
