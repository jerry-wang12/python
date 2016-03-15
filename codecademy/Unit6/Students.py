#!/usr/bin/python
# -*-coding:UTF-8-*-

# 数据存储在 列表，字典中,；分别可以根据其键值，index取得对应数据
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


# 求平均数的方法,传入一个数字list作为参数
# 使用自带方法 sum() float() len()
# 此处float()将int转为float再运算，否则计算结果默认为整数类型
def average(numbers):
    total = sum(numbers)
    return float(total) / len(numbers)


# 计算加权平均数,传入学生字典为参数,调用已定义的方法
def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    return homework * 0.1 + quizzes * 0.3 + tests * 0.6


#返回学生成绩等级， if~elif~else 选择分支
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print get_letter_grade(get_average(lloyd))


#计算班级平均分，以学生列表为参数
# lists.append() 给列表添加一条记录
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)


print get_class_average([lloyd, alice, tyler])
