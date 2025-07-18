from turtle import Turtle
start=[(0,0),(-20,0),(-40,0)]
move=20
up=90
down=270
left=180
right=0

class Snake:

  def __init__(self):
    self.segments=[]
    self.create_snake()
    self.head=self.segments[0]

  def create_snake(self):
    for position in start:
      self.add_segment(position)


  def move(self):
    for seg in range(len(self.segments)-1,0,-1):
        x=self.segments[seg-1].xcor()
        y=self.segments[seg-1].ycor()
        self.segments[seg].goto(x,y)
    self.segments[0].forward(move)


  def add_segment(self,position):
    new_seg=Turtle("square")
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(position)
    self.segments.append(new_seg)
    
    
  def extend(self):
    last_segment_pos = self.segments[-1].position()  # get (x, y) tuple
    self.add_segment(last_segment_pos)
    

  def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

  def down(self):
      if self.head.heading() != 90:
            self.head.setheading(270)

  def left(self):
     if self.head.heading() != 0:
            self.head.setheading(180)

  def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

  def reset(self):
      for seg in self.segments:
          seg.goto(1000, 1000)  # Move off screen
      self.segments.clear()
      self.create_snake()
      self.head = self.segments[0]