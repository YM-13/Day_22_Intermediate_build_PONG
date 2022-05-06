from turtle import Turtle

class Ball(Turtle):

	def __init__(self, position): # class Ball((0, 0)) - position
		super().__init__()
		self.color("white")
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_wid=1, stretch_len=1)
		self.goto(position)
		self.x_move = 10
		self.y_move = 10
		self.speed_move = 0.1


	def speed_up(self):
		self.speed_move *= 0.9


	def ball_move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce_y(self):
		self.y_move *= -1

	def bounce_x(self):
		self.x_move *= -1

	def reset_the_position(self):
		self.goto(0, 0)
		self.bounce_x()
		self.speed_move = 0.1
