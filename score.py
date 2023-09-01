from turtle import Turtle
import board

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, board.BOARD_HEIGHT // 2 - board.UP_MARGIN // 2 - 10)
        self.write(f"{self.left_score}     Score     {self.right_score}", False, "center", ("Arial", 14, "bold"))

    def add_left_score(self):
        self.left_score += 1

    def add_right_score(self):
        self.right_score += 1

    def update_score(self):
        self.clear()
        self.write(f"{self.left_score}     Score     {self.right_score}", False, "center", ("Arial", 14, "bold"))

    def game_over_board(self):
        g_o_board = Turtle()
        g_o_board.hideturtle()
        g_o_board.penup()
        g_o_board.color("white")
        g_o_board.goto(-110, -60)
        g_o_board.pendown()
        g_o_board.goto(-110, 40)
        g_o_board.goto(110, 40)
        g_o_board.goto(110, -60)
        g_o_board.goto(-110, -60)
        g_o_board.penup()
        # g_o_board.goto(0, 0)
        # g_o_board.color("black")
        # g_o_board.shape("square")
        # g_o_board.shapesize(stretch_wid=4.9, stretch_len=9.9)
        # g_o_board.showturtle()

    def game_over(self):
        self.clear()
        self.game_over_board()
        self.goto(1, - 45)
        self.color("white")
        self.write(f" GAME OVER\n  {self.left_score}   Score   {self.right_score}", False, "center", ("Arial", 22, "bold"))
