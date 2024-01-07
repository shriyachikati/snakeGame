from turtle import Turtle

MOVE_DISTANCE = 20
TURN_ANGLE = 90
POSITIONS = [(0, 0), (0, -20), (0, -40)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]


    def new_segment(self, position):
        new_block = Turtle("square")
        new_block.penup()
        new_block.color("white")
        new_block.goto(position)
        self.blocks.append(new_block)

    def create_snake(self):
        for position in POSITIONS:
            self.new_segment(position)

    def grow(self):
        self.new_segment(self.blocks[-1].position())
    def move(self):
        for i in range(len(self.blocks) - 1, 0, -1):
            x = self.blocks[i - 1].xcor()
            y = self.blocks[i - 1].ycor()
            self.blocks[i].goto(x, y)
        self.blocks[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
