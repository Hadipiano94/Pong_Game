from turtle import Screen
from racket import Racket
from ball import Ball
from score import ScoreBoard
import board
import time

screen = Screen()
screen.setup(board.BOARD_WIDTH, board.BOARD_HEIGHT)
screen.bgcolor("black")
screen.register_shape("square_2", ((-5, -1), (-5, 1), (5, 1), (5, -1)))
screen.tracer(0)
screen.listen()

pong_screen = board.PongScreen()
score_board = ScoreBoard()

left_racket = Racket(- (board.BOARD_WIDTH // 2 - 30))
right_racket = Racket(board.BOARD_WIDTH // 2 - 30)
screen.update()
screen.onkeypress(right_racket.move_up, "Up")
screen.onkeypress(right_racket.move_down, "Down")
screen.onkeypress(left_racket.move_up, "w")
screen.onkeypress(left_racket.move_down, "s")

ball = Ball(left_racket, right_racket, screen)
screen.update()
time.sleep(1)

if 90 < ball.heading() < 270:
    left_racket.turn = True
else:
    right_racket.turn = True


game_is_on = True
while game_is_on:

    if ball.out_of_board():
        game_is_on = False

    ball.move(2)
    ball.bounce_up()
    ball.bounce_down()
    ball.hit_left()
    ball.hit_right()

    if ball.hit_left() or ball.hit_right():
        ball.move(4)

    if ball.hit_left() and left_racket.turn:
        score_board.add_left_score()
        left_racket.turn = False
        right_racket.turn = True
    if ball.hit_right() and right_racket.turn:
        score_board.add_right_score()
        left_racket.turn = True
        right_racket.turn = False

    score_board.update_score()
    screen.update()

if not game_is_on:
    pong_screen.wipe_g_o_board()
    if left_racket.turn:
        score_board.add_right_score()
    else:
        score_board.add_left_score()
    score_board.game_over()
    screen.update()

screen.exitonclick()
