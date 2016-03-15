#!/usr/bin/python
# -*-coding:UTF-8-*-

# 构建了一个简单战舰游戏，点阵上有随机位置坐标的战舰，玩家猜位置
# 从random包中引入randint方法,生成随机整数
from random import randint
# 点阵数组 5*5 range(start, end ,step) 生成[start, end)，间隔step的list
#本质就是一个二维数组
board = []
for i in range(5):
    board.append(["O"] * 5)


# join()方法将参数插入数组，返回字符串
def print_board(board):
    for row in board:
        print " ".join(row)


print "Let`s play BattleShip!!"
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board) - 1)


ship_row = random_col(board)
ship_cow = random_col(board)

print "作弊 船的坐标为(%d,%d)" % (ship_row, ship_cow)

#以上是游戏初始化部分，以下是玩家游戏部分,玩家可以玩四次
for turn in range(4):
    print "这是第 %d 次游戏：" % (turn+1)
    #玩家猜坐标，raw_input() 方法返回值是一个字符串，需要将它转换成int类型
    guess_row = int(raw_input("Guess Row:"))
    guess_cow = int(raw_input("Guess Cow:"))

    #游戏判断胜负部分
    if guess_cow == ship_cow and guess_row == ship_row:
        #玩家获得胜利后，游戏应该结束，break跳出循环
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if guess_row not in range(5) or guess_row not in range(5):
            #如果玩家猜的坐标不再棋盘坐标范围内
            print "Oops, that`s not even in the ocean"
        elif board[guess_row][guess_cow] == "X":
            #如果玩家猜的坐标已被标记为X，则告诉玩家已经猜过了
            print "You guessed that one already."
        else:
            print "You missed my battleship"
            #如果没有猜对，将猜的坐标标记为X，已猜过
            board[guess_row][guess_cow] = "X"
            print_board(board)
    #此处等于 turn+1==4，游戏执行四次以后结束
    if( turn==3 ):
        print "Game Over!"
        break


