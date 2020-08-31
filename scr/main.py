import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720], pygame.RESIZABLE)
window_title = pygame.display.set_caption('Football Pong')

field = pygame.image.load("assets/field.png")

player1 = pygame.image.load('assets/player1.png')
player1_y = 287
player1_move_up = False
player1_move_down = False

player2 = pygame.image.load('assets/player2.png')
player2_y = 287

ball = pygame.image.load('assets/ball.png')
ball_x = 617
ball_y = 337


def draw():
    window.blit(field, (0, 0))
    window.blit(player1, (50, player1_y))
    window.blit(player2, (1152, player2_y))
    window.blit(ball, (ball_x, ball_y))

    move_ball()


def move_player1():
    global player1_y
    if player1_move_up:
        player1_y -= 10
    elif player1_move_down:
        player1_y += 10


def move_ball():
    global ball_x
    global ball_y
    ball_x += 1


loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_move_up = True
            if event.key == pygame.K_s:
                player1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_move_up = False
            if event.key == pygame.K_s:
                player1_move_down = False





    draw()

    pygame.display.update()
