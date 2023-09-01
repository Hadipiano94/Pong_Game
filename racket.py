from turtle import Turtle, Screen
import board

class Racket(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.turn = False
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.color("white")
        self.goto(x_cor, - (board.UP_MARGIN - board.DOWN_MARGIN - 10))
        self.showturtle()

    def move_up(self):
        if self.ycor() < (board.BOARD_HEIGHT // 2 - board.UP_MARGIN - 20):

            self.goto(self.xcor(), self.ycor() + 10)
            self.screen.update()

    def move_down(self):
        if self.ycor() > - (board.BOARD_HEIGHT // 2 - board.DOWN_MARGIN - 20):
            self.goto(self.xcor(), self.ycor() - 10)

    def get_position(self):
        return self.ycor()