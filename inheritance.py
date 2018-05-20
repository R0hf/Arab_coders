class Parent():
	
	def __init__(self, last_name , eye_color):
		print ('Parent created')
		self.last_name = last_name 
		self.eye_color = eye_color
	def show_info(self) :
		print ("last name : "+self.last_name)
		print ('eye color : '+self.eye_color)	
		
class Child(Parent) :
	def __init__(self , last_name, eye_color ,number_of_toys ):
		print ('child created')
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

titi = Parent("tiouche" , "black")
titi.show_info()
#alvaro = Child("tiouche" , "brown" , 5)
#print alvaro.last_name
#print alvaro.number_of_toys						