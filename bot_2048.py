#import
import random as r

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
    newNum(board)
    newNum(board)
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
    put = r.choice(empty)
    board[put // LENGTH][put % LENGTH] = r.choice([2, 2, 2, 2, 4])
    return True 

def pressW(board):
    added=[[False for j in range(LENGTH)] for i in range(LENGTH)]
    for k in range(3):#어쨌든 끝까지 이동
        for i in range(1,4):#2,3,4줄
            for j in range(0,4):#1,2,3,4칸
                if(board[i-1][j]==0):
                    board[i-1][j]=board[i][j]
                    board[i][j]=0
                elif(board[i-1][j]==board[i][j]&added[i-1][j]==False):
                    board[i-1][j]=board[i-1][j]*2
                    board[i][j]=0
                    added[i-1][j]=True
    newNum(board)#새로운 숫자 생성
    printBoard(board)#콘솔에 출력
    return board#보드 반환

def pressA(board):
    added=[[0 for j in range(LENGTH)]for i in range(LENGTH)]
    for k in range(4):#어쨌든 끝까지 이동
        for i in range(0,4):#1,2,3,4줄
            for j in range(1,4):#2,3,4칸
                if(board[i][j-1]==0):
                    board[i][j-1]=board[i][j]
                    board[i][j]=0
                elif(board[i][j-1]==board[i][j]&added[i][j-1]==0):
                    board[i][j-1]=board[i][j-1]*2
                    board[i][j]=0
                    added[i][j-1]=1
    newNum(board)#새로운 숫자 생성
    printBoard(board)#콘솔에 출력
    return board#보드 반환


def pressS(board):
    added=[[0 for j in range(LENGTH)]for i in range(LENGTH)]
    for k in range(4):#어쨌든 끝까지 이동
        for i in range(0,3):#1,2,3줄
            for j in range(0,4):#1,2,3,4칸
                if(board[i+1][j]==0):
                    board[i+1][j]=board[i][j]
                    board[i][j]=0
                elif(board[i+1][j]==board[i][j]&added[i+1][j]==0):
                    board[i+1][j]=board[i+1][j]*2
                    board[i][j]=0
                    added[i+1][j]=1
    newNum(board)#새로운 숫자 생성
    printBoard(board)#콘솔에 출력
    return board#보드 반환

def pressD(board):
    added=[[0 for j in range(LENGTH)]for i in range(LENGTH)]
    for k in range(4):#어쨌든 끝까지 이동
        for i in range(0,4):#1,2,3,4줄
            for j in range(0,3):#1,2,3칸
                if(board[i][j+1]==0):
                    board[i][j+1]=board[i][j]
                    board[i][j]=0
                elif(board[i][j+1]==board[i][j]&added[i][j+1]==0):
                    board[i][j+1]=board[i][j+1]*2
                    board[i][j]=0
                    added[i][j+1]=1
    newNum(board)#새로운 숫자 생성
    printBoard(board)#콘솔에 출력
    return board#보드 반환

def printBoard(board):
    for i in range(LENGTH):
        print("-" * (LENGTH * 6 + 1))
        for j in range(LENGTH):
            print("|%5d" % board[i][j], end="")
        print("|")
    print("-" * (LENGTH * 6 + 1))


    s = ''
    for line in board:
        s += ' '.join(str(line[i]) for i in range(LENGTH))
        s += '\n'
    return s

def gravity(board, way):
    if way == 'a':  # 왼쪽
        pass  # 아래 처리 문장은 왼쪽이 기준, 그래서 나머지 방향은 왼쪽 방향 이동에 맞춰 대칭이동
    elif way == 'd':  # 오른쪽
        board = [
            [board[i][LENGTH - 1 - j]
                for j in range(LENGTH)]
            for i in range(LENGTH)
        ]
    elif way == 'w':  # 위쪽
        board = [
            [board[j][i] for j in range(LENGTH)]
            for i in range(LENGTH)
        ]
    elif way == 's':  # 아래쪽
        board = [
            [board[LENGTH - 1 - j][LENGTH - 1 - i]
                for j in range(LENGTH)]
            for i in range(LENGTH)
        ]
    else:
        print("Input error!")
        return board

    for i in range(LENGTH):
        zeroCnt = board[i].count(0)
        for z in range(zeroCnt):
            board[i].remove(0)
            board[i].append(0)
        for j in range(LENGTH - 1):
            if board[i][j] > 0 and board[i][j] == board[i][j + 1]:
                board[i][j] *= 2
                board[i].pop(j + 1)
                board[i].append(0)

    if way == 'd':  # 오른쪽
        board = [
            [board[i][LENGTH - 1 - j] for j in range(LENGTH)]
            for i in range(LENGTH)
        ]
    elif way == 'w':  # 위쪽
        board = [
            [board[j][i] for j in range(LENGTH)]
            for i in range(LENGTH)
        ]
    elif way == 's':  # 아래쪽
        board = [
            [board[LENGTH - 1 - j][LENGTH - 1 - i]
                for j in range(LENGTH)]
            for i in range(LENGTH)
        ]
    return board


#함수 테스트
# b=newBoard()
# b=gravity(b,'w')
# b=gravity(b,'s')
# b=gravity(b,'a')
# b=gravity(b,'d')

board = newBoard()
board = gravity(board, 'w')
newNum(board)
printBoard(board)
board = gravity(board, 'a')
newNum(board)
printBoard(board)
board = gravity(board, 'd')
newNum(board)
printBoard(board)
board = gravity(board, 's')
