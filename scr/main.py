import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720], pygame.RESIZABLE)
window_title = pygame.display.set_caption('Football Pong')

win = pygame.image.load('assets/win.png')

field = pygame.image.load('assets/field.png')

score1 = 0
score1_image = pygame.image.load('assets/score/' + str(score1) + '.png')
score2 = 0
score2_image = pygame.image.load('assets/score/' + str(score2) + '.png')

player1 = pygame.image.load('assets/player1.png')
player1_y: int = 287
player1_move_up = False
player1_move_down = False

player2 = pygame.image.load('assets/player2.png')
player2_y = 287

ball = pygame.image.load('assets/ball.png')
ball_x = 617
ball_y = 337
ball_dir_x = -6
ball_dir_y = -1
ball_speed_x = -6
ball_speed_y = 1


def draw():
    if score1 or score2 < 9:
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1152, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_image, (500, 50))
        window.blit(score2_image, (710, 50))

        move_player1()
        move_ball()
    else:
        window.blit(score1_image, (500, 50))
        window.blit(score2_image, (710, 50))
        window.blit(win, (300, 330))


def move_player1():
    global player1_y, player1_move_down, player1_move_up, player2_y

    if player1_move_up:
        player1_y -= 5
    else:
        player1_move_up += 0

    if player1_move_down:
        player1_y += 5
    else:
        player1_move_down += 0

    if player1_y < 0:
        player1_y = 0
    elif player1_y > 550:
        player1_y = 550

    player2_y = ball_y - 73


def move_ball():
    global ball_x, ball_y, ball_dir_x, ball_dir_y, player1_y
    global ball_speed_y, ball_speed_x, score2, score1, score2_image, score1_image

    ball_x += ball_dir_x
    ball_y += ball_dir_y

    if ball_x < 120 and player1_y < ball_y + 23 < player1_y + 146:
        ball_dir_x *= -1
        ball_dir_x += 1
        ball_dir_y += 1

    if ball_x > 1100 and player2_y < ball_y + 23 < player2_y + 146:
        ball_dir_x *= -1
        ball_dir_x += -1
        ball_dir_y += 1

    if ball_y < 0:
        ball_dir_y *= -1
    elif ball_y > 670:
        ball_dir_y *= -1

    if ball_x < 0:
        score2 += 1
        ball_x = 617
        ball_y = 337
        ball_dir_x *= -1
        ball_dir_y *= -1
        ball_dir_x = ball_speed_x
        ball_dir_y = ball_speed_y
        score2_image = pygame.image.load('assets/score/' + str(score2) + '.png')

    elif ball_x > 1326:
        score1 += 1
        ball_x = 617
        ball_y = 337
        ball_dir_x *= -1
        ball_dir_y *= -1
        ball_dir_x = ball_speed_x
        ball_dir_y = ball_speed_y
        score1_image = pygame.image.load('assets/score/' + str(score1) + '.png')


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
