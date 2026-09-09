#numeric python (numpy) velmi silna kniznica na vektorove vypocty, matrixi...

# def createchessboard():
#     global chessboard
#     row=[0]*8
#     chessboard=[row]*8
#
# createchessboard()
# chessboard[2][2]=1
# print(chessboard) ---TAKTO TO NIKDY NEROBIT


chessboard=[]
counter=0

def createchessboard():
    global chessboard
    for i in range(8):
        row=[0]*8
        chessboard.append(row)


def checkit(x,y):
    global chessboard
    for i in range(0,8):
        if chessboard[y][i]==1: #suradnice idu vzdy naopak
            return False
        if chessboard[i][x]==1:
            return False
    for i in range(0,8): #i je y suradnica
        for j in range(0,8): #j je x suradnica
            if i+j==x+y:
                if chessboard[i][j]==1:
                    return False
            if i-j==y-x:
                if chessboard[i][j]==1:
                    return False
    return True

def queens(n):
    global chessboard
    global counter
    if n==8:
        counter+=1
        print(chessboard)
        print("----------------------------------")
        print(counter)
    else:
        for i in range(8):
            if checkit(i,n):
                chessboard[n][i]=1
                queens(n+1)
                chessboard[n][i]=0


createchessboard()
queens(0)
