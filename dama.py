#numeric python (numpy) velmi silna kniznica na vektorove vypocty, matrixi...

# def createchessboard():
#     global chessboard
#     row=[0]*8
#     chessboard=[row]*8
#
# createchessboard()
# chessboard[2][2]=1
# print(chessboard) ---TAKTO TO NIKDY NEROBIT

from PIL import Image, ImageDraw

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


def nakresli_sachovnicu():
    velkost_policka = 60
    velkost_sachovnice = 8 * velkost_policka

    img = Image.new("RGB", (velkost_sachovnice, velkost_sachovnice))
    kreslenie = ImageDraw.Draw(img)

    for riadok in range(8):
        for stlpec in range(8):
            x1 = stlpec * velkost_policka
            y1 = riadok * velkost_policka
            x2 = x1 + velkost_policka
            y2 = y1 + velkost_policka

            if (riadok + stlpec) % 2 == 0:
                farba = (255, 255, 255)  #biela
            else:
                farba = (67, 67, 67)  #cierna

            kreslenie.rectangle([x1, y1, x2, y2], fill=farba)

    return img


def vytvor_obrazok(kombinacia_cislo):

    img = nakresli_sachovnicu()
    kreslenie = ImageDraw.Draw(img)

    velkost_policka = 60

    for riadok in range(8):
        for stlpec in range(8):
            if chessboard[riadok][stlpec] == 1:
                x1 = stlpec * velkost_policka
                y1 = riadok * velkost_policka

                okraj = 8

                kruh_x1 = x1 + okraj
                kruh_y1 = y1 + okraj
                kruh_x2 = x1 + velkost_policka - okraj
                kruh_y2 = y1 + velkost_policka - okraj

                kreslenie.ellipse([kruh_x1, kruh_y1, kruh_x2, kruh_y2], fill="red", outline="darkred", width=2)

    nazov_suboru =f"dama{kombinacia_cislo}.png"
    img.save(nazov_suboru)


def queens(n):
    global chessboard
    global counter
    if n==8:
        counter+=1
        print(chessboard)
        print("----------------------------------")
        print(counter)

        vytvor_obrazok(counter)
    else:
        for i in range(8):
            if checkit(i,n):
                chessboard[n][i]=1
                queens(n+1)
                chessboard[n][i]=0


createchessboard()
queens(0)
