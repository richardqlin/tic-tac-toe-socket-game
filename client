import socket, pygame, time
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((540, 540))
font = pygame.font.Font('freesansbold.ttf', 32)
pygame.display.set_caption("server")
window.fill((0,0,0))
black=(0,0,0)

d={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}

host = ''
port = 12345
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.bind((host, port))
conn.listen(10)
print("listening...")
client, address = conn.accept()
print("Client has connected with address: {}".format(address))
score = 0

pygame.draw.line(window, (255, 255, 255), (180, 0), (180, 540), 1)
pygame.draw.line(window, (255, 255, 255), (360, 0), (360, 540), 1)
pygame.draw.line(window, (255, 255, 255), (0, 180), (540, 180), 1)
pygame.draw.line(window, (255, 255, 255), (0, 360), (540, 360), 1)
pygame.display.update()

done=True
def drawX(x,y):
    pygame.draw.line(window, (0, 0, 255), (x-45, y-45), (x+45, y+45), 1)
    pygame.draw.line(window, (0, 0, 255), (x-45, y+45), (x+45, y-45), 1)

def drawO(x,y):
    pygame.draw.circle(window, (0, 255, 0), (x, y), 40, 1)

def message_display(text, textx, texty):
    textcontent = font.render(text, True, (255, 0, 0))
    textRect = textcontent.get_rect()
    textRect.center = (textx, texty)
    window.blit(textcontent, textRect)

def checkwin(d):
    # Checking Each Row for x
    if d[3] == d[1] == d[2] == 'x' or d[6] == d[4] == d[5] == 'x' or d[9] == d[7] == d[8] == 'x':
        show_x()
        quit()
    elif d[3] == d[1] == d[2] == 'o' or d[6] == d[4] == d[5] == 'o' or d[9] == d[7] == d[8] == 'o':
        show_o()
        quit()
    elif d[1] == d[4] == d[7] == 'x' or d[2] == d[5] == d[8] == 'x' or d[1] == d[3] == d[9] == 'x':
        show_x()
        quit()
    elif d[1] == d[5] == d[9] == 'x' or d[3] == d[5] == d[7] == 'x':
        show_x()
        quit()
    elif d[3] == d[6] == d[9] == 'o' or d[1] == d[4] == d[7] == 'o' or d[2] == d[5] == d[8] == 'o':
        show_o()
        quit()
    elif d[1] == d[5] == d[9] == 'o' or d[3] == d[5] == d[7] == 'o':
        show_o()
        quit()

def show_x():
    time.sleep(0.5)
    window.fill(black)
    message_display('x win.', 540/2.5, 540/3)
    pygame.display.update()
    time.sleep(5)
    global done
    done = False

def show_o():
    time.sleep(0.5)
    window.fill(black)
    message_display('o win.', 540/2.5, 540/3)
    pygame.display.update()
    time.sleep(5)
    global done
    done = False

count = 0
turnX, turnO='x','o'

x=-70
y=-80

while done:
    if turnX=='x':
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                done = False
            if event.type == MOUSEBUTTONDOWN:
                print ("Turn X:",turnX,"Turn O:",turnO)
                x,y = event.pos
                client.sendall((str(x)+','+str(y)).encode())
                print ("switch", x,y)
                turnX,turnO = turnO,turnX
                print ("Turn X:",turnX,"Turn O:",turnO)

    elif turnX=='o':
        clientpos = client.recv(1024).decode()
        clientpos = clientpos.split(',')
        x=int(clientpos[0])
        y=int(clientpos[1])
        print(x,y)
        turnX, turnO = turnO, turnX


    if 0 < x < 180 and 0< y < 180 and d[1] == '':
        if turnO=="x":
            drawX(90, 90)
            d[1] = 'x'
        elif turnO== 'o':
            drawO(90,90)
            d[1]='o'

    elif 0 < x < 180 and 180 < y < 360 and d[2] == '':
        if turnO=="x":
            drawX(90, 270)
            d[2] = 'x'
        elif turnO == 'o':
            drawO(90, 270)
            d[2] = 'o'

    elif 0 < x < 180 and 360 < y and d[3] == '':
        if turnO=="x":
            drawX(90, 450)
            d[3] = 'x'
        elif turnO == 'o':
            drawO(90, 450)
            d[3] = 'o'
    elif 180 < x < 360 and y < 180 and d[4] == '':
        if turnO=="x":
            drawX(270, 90)
            d[4] = 'x'
        elif turnO == 'o':
            drawO(270, 90)
            d[4] = 'o'

    elif 180 < x < 360 and 180 < y < 360 and d[5] == '':
        if turnO=="x":
            drawX(270, 270)
            d[5] = 'x'
        elif turnO == 'o':
            drawO(270, 270)
            d[5] = 'o'
    elif 180 < x < 360 and 360 < y and d[6] == '':
        if turnO=="x":
            drawX(270, 450)
            d[6] = 'x'
        elif turnO == 'o':
            drawO(270, 450)
            d[6] = 'o'

    elif 360 < x and y < 180 and d[7] == '':
        if turnO=="x":
            drawX(450, 90)
            d[7] = 'x'
        elif turnO == 'o':
            drawO(450, 90)
            d[7] = 'o'
    elif 360 < x and 180 < y < 360 and d[8] == '':
        if turnO=="x":
            drawX(450, 270)
            d[8] = 'x'
        elif turnO == 'o':
            drawO(450, 270)
            d[8] = 'o'
    elif 360 < x and 360 < y and d[9] == '':
        if turnO=="x":
            drawX(450, 450)
            d[9] = 'x'
        elif turnO == 'o':
            drawO(450, 450)
            d[9] = 'o'

    pygame.display.update()
