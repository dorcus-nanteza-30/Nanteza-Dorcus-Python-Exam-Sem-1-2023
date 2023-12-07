#Program that prints patterns
num = 5
for n in range (1, num):
    for x in range (1 + n +1):
        print(x, end ="")
    print("")

#Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 5

if num < 0:# check if the number is negative
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))



# FUnction that returns their sum test their function with a = 3 and b=4
def addition( a , b ):
   return a + b 
print( addition(3, 4 ) ) 


#Program that displays information about the car
class car():
     
    def __init__(self, model, color): # init method or constructor
        self.model = model
        self.color = color
         
    def show(self):
        print("Model is", self.model )
        print("color is", self.color )
         
audi = car("audi a4", "black")
 
audi.show()     # same output as car.show(audi)
 
print("Model for audi is ",audi.model)



#An instance of the class and display the information
class car():
     
    def __init__(self, model, color): # init method or constructor
        self.model = model
        self.color = color
         
    def show(self):
        print("Model is", self.model )
        print("color is", self.color )
         
audi = car("audi a4", "black")
 
audi.show()     # same output as car.show(audi)
 
print("Model for audi is ",audi.model)