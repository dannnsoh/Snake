from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        # * Create starting snake body
        start_x = -60
        for _ in range(3):
            seg = Turtle(shape="square")
            seg.penup()
            seg.color("white")
            seg.goto(start_x, 0)
            start_x += 20
            self.segments.append(seg)

    def move(self):
        # movement: last seg move to 2nd seg's position, 2nd seg move to 1st, 1st move to new position, and so on...
        # so instead of first seg moving first, last seg will move first
        # so index will be from 2 -> 1 -> 0 in a snake body of 3 segments
        # range will start will last index and step to first index
        for seg in range(len(self.segments) - 1, 0, -1):
            next_seg_position = self.segments[seg - 1].position()
            self.segments[seg].goto(next_seg_position)
        self.segments[0].forward(20)
