from turtle import Turtle, Screen
import board
import racket
import random
import time


class Ball(Turtle):

    def __init__(self,racket_left, racket_right, screen=Screen()):
        super().__init__()
        self.racket_right = racket_right
        self.racket_left = racket_left
        self.hideturtle()
        self.penup()
        self.shape("circle")
        self.color("white")
        # self.goto(random.randint(- (board.BOARD_WIDTH // 2 - board.SIDE_MARGIN), (board.BOARD_WIDTH // 2 - board.SIDE_MARGIN)), random.randint(- (board.BOARD_HEIGHT // 2 - board.DOWN_MARGIN), (board.BOARD_HEIGHT // 2 - board.UP_MARGIN)))
        self.goto(0, - (board.UP_MARGIN - board.DOWN_MARGIN - 10))
        self.showturtle()
        self.setheading(random.choice([45, 135, 225, 315]))
        # self.move()

    def out_of_board(self):
        if self.xcor() <= (board.BOARD_WIDTH // 2 - board.SIDE_MARGIN) and self.xcor() >= - (
                board.BOARD_WIDTH // 2 - board.SIDE_MARGIN):
            return False
        return True

    def bounce_up(self):
        if self.ycor() >= (board.BOARD_HEIGHT // 2 - board.UP_MARGIN - 10):
            self.setheading(360 - self.heading())

    def bounce_down(self):
        if self.ycor() <= - (board.BOARD_HEIGHT // 2 - board.DOWN_MARGIN - 10):
            self.setheading(360 - self.heading())

    def hit_left(self):
        if self.xcor() <= - (board.BOARD_WIDTH // 2 - board.SIDE_MARGIN - 20) and abs(self.racket_left.get_position() - self.ycor()) < 38:
            self.setheading(180 - self.heading())
            print(self.heading())
            return True

    def hit_right(self):
        if self.xcor() >= (board.BOARD_WIDTH // 2 - board.SIDE_MARGIN - 20) and abs(self.racket_right.get_position() - self.ycor()) < 38:
            self.setheading(180 - self.heading())
            print(self.heading())
            return True

    def move(self, pace):
        self.forward(pace)

