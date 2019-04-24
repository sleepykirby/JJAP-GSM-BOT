#import
import random

#함수 선언


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
    printBoard(board)
    return board

def pressW(board):
    for i in range(0,4):
        for j in range(0,4):
            

# def pressA():


# def pressS():


# def pressD():


def printBoard(board):
    for line in board:
        print(line[0],line[1],line[2],line[3])

# def numGen():


#함수 테스트
newBoard()