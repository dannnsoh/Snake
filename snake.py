from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for position in STARTING_POSITIONS:
            seg = Turtle("square")
            seg.penup()
            seg.color("white")
            seg.goto(position)
            self.segments.append(seg)

    def move(self):
        # * snake movement:
        # last seg move to 2nd seg's position, 2nd seg move to 1st, 1st move to new position, and so on...
        # so instead of first seg moving first, last seg will move first
        # so index will be from 2 -> 1 -> 0 in a snake body of 3 segments
        # ? range will start start from last index and to first index
        for seg in range(len(self.segments) - 1, 0, -1):
            next_seg_position = self.segments[seg - 1].position()
            self.segments[seg].goto(next_seg_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
