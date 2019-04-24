#import
import random

#함수 선언
board=[[],[],[],[]]


def newBoard():
    board=[
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
    board[random.randrange(0,4)][random.randrange(0,4)]=2
    tmp=random.randrange(0,4)
    tmp2=random.randrange(0,4)
    while(board[tmp][tmp2]==2):
        tmp=random.randrange(0,4)
        tmp2=random.randrange(0,4)
    board[tmp][tmp2]=2
    printBoard()

# def pressW():


# def pressA():


# def pressS():


# def pressD():


def printBoard():
    for line in board:
        print(line)

# def numGen():


#함수 테스트
newBoard()