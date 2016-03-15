#!/usr/bin/python
# -*-coding:UTF-8-*-

# 商品价格字典
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# 商品库存字典
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

# 循环输出商品的价格和库存
for key in prices:
    print key
    # 此处使用格式化输出，%s代表字符串
    # 格式化输出的格式为 print "%s%s%s" % (arg1, arg2, arg3)
    print "price:%s" % prices[key]
    print "stock:%s" % stock[key]

#计算账单的方法
def compute_bill(food):
    total = 0
    for key in food:
        #此处首先要判断库存中是否有购买的商品,购买成功后将库存数量-1
        if stock[key] > 0:
            total += prices[key]
            stock[key] = stock[key] - 1
    return total

print "您的账单是: %d元" % compute_bill(["banana","pear"])
