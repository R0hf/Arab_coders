import turtle ;

def draw_square(haja) :
	for i in range(1,5) :
		haja.forward(100)
		haja.right(90)
def draw_triangle(haja) :
	for i in range(1,4) :
		haja.forward(100)
		haja.right(120)

def draw_art() :
	window = turtle.Screen() ;
	window.bgcolor("black") ;

	brad = turtle.Turtle() 
	brad.shape("turtle")
	brad.color("white")
	brad.speed(4)

	for y in range(1,20) :
		draw_triangle(brad)
		brad.right(10)

	#alvaro = turtle.Turtle()
	#alvaro.shape("arrow")
	#alvaro.color("white")
	#alvaro.circle(100)

	window.exitonclick();
draw_art()
	