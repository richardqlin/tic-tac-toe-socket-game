import socket, pygame, random, pickle, atexit, time
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((540, 540))
pygame.display.set_caption("client")
font = pygame.font.Font('freesansbold.ttf', 32)
window.fill((0,0,0))

black = (0,0,0)

d={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}

host = 'localhost'
port = 12345
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host, port))

pygame.draw.line(window, (255, 255, 255), (180, 0), (180, 540), 1)
pygame.draw.line(window, (255, 255, 255), (360, 0), (360, 540), 1)
pygame.draw.line(window, (255, 255, 255), (0, 180), (540, 180), 1)
pygame.draw.line(window, (255, 255, 255), (0, 360), (540, 360), 1)


def message_display(text, textx, texty):
    textcontent = font.render(text, True, (255, 0, 0))
    textRect = textcontent.get_rect()
    textRect.center = (textx, texty)
    window.blit(textcontent, textRect)
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


def handle_exit():
    print("this runs after keyboard interrupt")
    conn.close()
atexit.register(handle_exit)

def drawX(x,y):
    pygame.draw.line(window, (0, 0, 255), ((x-45, y-45), (x+45, y+45)), 1)
    pygame.draw.line(window, (0, 0, 255), ((x-45, y+45), (x+45, y-45)), 1)

def checkwin(d):
    # Checking Each Row for x
    if d[3] == d[1] == d[2] == 'x' or d[6] == d[4] == d[5] == 'x' or d[9] == d[7] == d[8] == 'x':

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

def drawX(x,y):
    pygame.draw.line(window, (0, 0, 255), (x-45, y-45), (x+45, y+45), 1)
    pygame.draw.line(window, (0, 0, 255), (x-45, y+45), (x+45, y-45), 1)

def drawO(x,y):
    pygame.draw.circle(window, (0, 255, 0), (x, y), 40, 1)

turnX, turnO = 'o', 'x'
x = -900
y = -800
while True:
    if turnO == 'x':
        data = conn.recv(1024).decode()
        data = data.split(',')
        x = int(data[0])
        y = int(data[1])
        print(x, y)
        turnX, turnO = turnO, turnX
    elif turnO=='o':
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                print("Turn x:", turnX, "Turn o:", turnO)
                x,y = event.pos
                conn.send((str(x) + ',' + str(y)).encode())
                print("switch", x, y)
                turnX, turnO = turnO, turnX
                print("Turn x:", turnX, "Turn o:", turnO)



    if 0 < x < 180 and 0< y < 180 and d[1] == '':
        print ("hello")
        if turnX=='x':
            drawX(90, 90)
            d[1] = 'x'
        elif turnO== 'x':
            drawO(90,90)
            d[1]='o'

    elif 0 < x < 180 and 180 < y < 360 and d[2] == '':
        if turnX=="x":
            drawX(90, 270)
            d[2] = 'x'
        elif turnO == 'x':
            drawO(90, 270)
            d[2] = 'o'

    elif 0 < x < 180 and 360 < y and d[3] == '':
        if turnX=="x":
            drawX(90, 450)
            d[3] = 'x'
        elif turnX == 'o':
            drawO(90, 450)
            d[3] = 'o'
    elif 180 < x < 360 and y < 180 and d[4] == '':
        if turnX=="x":
            drawX(270, 90)
            d[4] = 'x'
        elif turnX == 'o':
            drawO(270, 90)
            d[4] = 'o'

    elif 180 < x < 360 and 180 < y < 360 and d[5] == '':
        if turnX=="x":
            drawX(270, 270)
            d[5] = 'x'
        elif turnX == 'o':
            drawO(270, 270)
            d[5] = 'o'
    elif 180 < x < 360 and 360 < y and d[6] == '':
        if turnX=="x":
            drawX(270, 450)
            d[6] = 'x'
        elif turnX == 'o':
            drawO(270, 450)
            d[6] = 'o'

    elif 360 < x and y < 180 and d[7] == '':
        if turnX=="x":
            drawX(450, 90)
            d[7] = 'x'
        elif turnX == 'o':
            drawO(450, 90)
            d[7] = 'o'
    elif 360 < x and 180 < y < 360 and d[8] == '':
        if turnX=="x":
            drawX(450, 270)
            d[8] = 'x'
        elif turnX == 'o':
            drawO(450, 270)
            d[8] = 'o'
    elif 360 < x and 360 < y and d[9] == '':
        if turnX=="x":
            drawX(450, 450)
            d[9] = 'x'
        elif turnX == 'o':
            drawO(450, 450)
            d[9] = 'o'

    pygame.display.update()
