#!/usr/bin/python
# -*-coding:UTF-8-*-
# 面向对象编程，将对象属性，行为抽象成一个类
# object类是所有类的基类，所有其他类最终都是从object类继承而来
# __somefun__这种类型的方法，是object中已有的
#__init__ ()方法在类对象被实例化时便会自动执行，参数既是实例化时传入的
# self是这个类当前被实例化的对象的引用，方法被调用时，self会被自动传入方法


class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
        print "This is a %s %s with %s MPG."%(self.color,self.model,self.mpg)

    def drive_car(self):
        self.condition = "used"



class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = "like new"

my_car = ElectricCar("BWM","red",88,"molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition