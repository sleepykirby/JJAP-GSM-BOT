#import
import random

LENGTH = 4

#함수 선언


def newBoard():
#     board=[
#         [0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0]]#보드 생성
#     board[random.randrange(0,4)][random.randrange(0,4)]=2#첫번째 숫자 생성
    board = [
        [0 for j in range(LENGTH)] for i in range(LENGTH)]
    board = newNum(newNum(board))
    printBoard(board)
    return board
    

def newNum(board):
#     tmp=random.randrange(0,4)#다음 숫자 세로 위치 생성
#     tmp2=random.randrange(0,4)#다음 숫자 가로 위치 생성
#     while(board[tmp][tmp2]!=0):#지정 위치에 숫자가 있을때
#         tmp=random.randrange(0,4)
#         tmp2=random.randrange(0,4)#위치 변경
#     board[tmp][tmp2]=(random.randrange(0,2)+1)*2#빈 위치에 2 or 4 생성
    empty = [
        i for i in range(LENGTH ** 2) if board[i // LENGTH][i % LENGTH] == 0]
    if len(empty) <= 0:
        return False
    put = random.choice(empty)
    board[put // LENGTH][put % LENGTH] = random.choice([2, 2, 2, 2, 4])
    return board

def pressW(board):
    for k in range(4):#어쨌든 끝까지 이동
        for i in range(1,4):#2,3,4줄
            for j in range(0,4):#1,2,3,4칸
                if(board[i-1][j]==0):
                    board[i-1][j]=board[i][j]
                    board[i][j]=0
                elif(board[i-1][j]==board[i][j]):
                    board[i-1][j]=board[i-1][j]*2
                    board[i][j]=0
    newNum(board)#새로운 숫자 생성
    printBoard(board)#콘솔에 출력
    return board#보드 반환

def pressA(board):
    for k in range(4):#어쨌든 끝까지 이동
        for i in range(0,4):#1,2,3,4줄
            for j in range(1,4):#2,3,4칸
                if(board[i][j-1]==0):
                    board[i][j-1]=board[i][j]
                    board[i][j]=0
                elif(board[i][j-1]==board[i][j]):
                    board[i][j-1]=board[i][j-1]*2
                    board[i][j]=0
    newNum(board)#새로운 숫자 생성
    printBoard(board)#콘솔에 출력
    return board#보드 반환


def pressS(board):
    for k in range(4):#어쨌든 끝까지 이동
        for i in range(0,3):#1,2,3줄
            for j in range(0,4):#1,2,3,4칸
                if(board[i+1][j]==0):
                    board[i+1][j]=board[i][j]
                    board[i][j]=0
                elif(board[i+1][j]==board[i][j]):
                    board[i+1][j]=board[i+1][j]*2
                    board[i][j]=0
    newNum(board)#새로운 숫자 생성
    printBoard(board)#콘솔에 출력
    return board#보드 반환

def pressD(board):
    for k in range(4):#어쨌든 끝까지 이동
        for i in range(0,4):#1,2,3,4줄
            for j in range(0,3):#1,2,3칸
                if(board[i][j+1]==0):
                    board[i][j+1]=board[i][j]
                    board[i][j]=0
                elif(board[i][j+1]==board[i][j]):
                    board[i][j+1]=board[i][j+1]*2
                    board[i][j]=0
    newNum(board)#새로운 숫자 생성
    printBoard(board)#콘솔에 출력
    return board#보드 반환

def printBoard(board):
    s=''
    for line in board:
        print(line[0],line[1],line[2],line[3])
        s+=str(line[0])+' '+str(line[1])+' '+str(line[2])+' '+str(line[3])
        s+='\n'
    print('------')
    return s



#함수 테스트
b=newBoard()
pressW(b)
pressA(b)
pressS(b)
pressD(b)
