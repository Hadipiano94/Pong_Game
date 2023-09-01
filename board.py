from turtle import Turtle, Screen

BOARD_WIDTH = 1000
BOARD_HEIGHT = 700
DOWN_MARGIN = 30
SIDE_MARGIN = DOWN_MARGIN
UP_MARGIN = DOWN_MARGIN + 30
MARGIN = DOWN_MARGIN + UP_MARGIN


class PongScreen:

    def __init__(self):
        self.board_width = BOARD_WIDTH
        self.board_height = BOARD_HEIGHT
        self.margin = MARGIN
        self.dotted_line_list = []
        self.draw_dotted_line()
        self.draw_outline()

    def draw_dotted_line(self):
        for i in range(((self.board_height -  self.margin) // 20) - 1):
            self.line = Turtle("square_2")
            self.line.penup()
            self.line.hideturtle()
            self.line.color("white")
            self.line.goto(0, - ((self.board_height // 2 - DOWN_MARGIN) - (((self.board_height - self.margin) % 20) // 2)) + ((i + 1) * 20))
            self.line.showturtle()
            self.dotted_line_list.append(self.line)

    def draw_outline(self):
        self.outline = Turtle()
        self.outline.color("white")
        self.outline.hideturtle()
        self.outline.penup()
        self.outline.goto(- (self.board_width // 2 - SIDE_MARGIN), -(self.board_height // 2 - DOWN_MARGIN))
        self.outline.pendown()
        self.outline.goto(- (self.board_width // 2 - SIDE_MARGIN),  (self.board_height // 2 - UP_MARGIN))
        self.outline.goto(  (self.board_width // 2 - SIDE_MARGIN),  (self.board_height // 2 - UP_MARGIN))
        self.outline.goto(  (self.board_width // 2 - SIDE_MARGIN), -(self.board_height // 2 - DOWN_MARGIN))
        self.outline.goto(- (self.board_width // 2 - SIDE_MARGIN), -(self.board_height // 2 - DOWN_MARGIN))
        self.outline.penup()

    def wipe_g_o_board(self):
        for i in range(int(len(self.dotted_line_list) // 2) - 2, int(len(self.dotted_line_list) // 2) + 3):
            self.dotted_line_list[i].hideturtle()