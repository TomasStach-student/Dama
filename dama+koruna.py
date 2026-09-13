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


def vytvor_obrazok(counter):

    img = nakresli_sachovnicu()

    korunka_img = Image.open("korunka.png").convert("RGBA")
    korunka_img = korunka_img.resize((60, 60))

    velkost_policka = 60

    for riadok in range(8):
        for stlpec in range(8):
            if chessboard[riadok][stlpec] == 1:

                x1 = stlpec * velkost_policka
                y1 = riadok * velkost_policka

                img.paste(korunka_img, (x1, y1), korunka_img)

    nazov_suboru =f"dama{counter}.png"
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
