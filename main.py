#def greet():
#   return "Hello Alfred"
#print(greet())
#============================

'''
Function with parameters
'''
#def greet(name):
#   '''
#   Greets a person passed in as argumrnt name: a name of a person to greet
#   '''
#   return f"Hello {name}, Good morning"
    
#print(greet("Felix"))
#print(greet("Arlo"))
#print(greet("Arien"))

#help(print)
#Function with parameters above
'''
Arbirtary parameters
'''
#def fruits (*names):
#   '''
#   Accepts unknown number of fruti names and prints each of them
#   *name: list of fruits
#   '''
   
   #names are tuples
#   for fruit in names:
#       print(fruit)
   
#fruits("Orange", "Banana", "Apple", "Grapes)")
#Means you can accept one or many with arbitary paramaters
#====================================

'''
Keyword paramters
'''

#def greet(name, msg):
#   '''
#   This function greets a person with a given message
#   name: person to greet
#   msg: message to greet person with
#   '''
   
#   return f"Hello {name}, {msg}"
   
#print(greet("Alfred", "Good afternoon!"))
#print(greet("Good afternoon", "Arlo!"))
#Function becomes more useful

#print(greet(name= "Alfred", msg="Good afternoon!'))'"))
#print(greet(msg="Good afternoon", name="Arlo!"))

#using keyword as name allows you to write it whichever way round

'''
Arbitary Keyword parameters
'''
#def person(**student):
#   print(type(student))

#person(fname="Alfred", lname="Banda")
#That comes in as a dictionary above

#def person(**student):
    #print(type(student))
    #print(student)
    #for key in student:
       #print(student[key])

#person(fname="Alfred", lname="Banda")
#person(fname="Alfred", lname="Banda", subject="Python")

'''
Default parameter 
'''

#def greet(name='Alfred'):
#   return f"Hello, {name}"
   
#print(greet())
#print(greet("Disa"))

'''
pass statement
'''

#def greet():
#   pass


'''
Recursion
'''

#A method calling itself

def factorial_recursive(n):
   '''
   Multiply given number by every number less than it down to 1 in factorial way e.g. if n is 5 then calculate 5*4*3*2*1 = 120
   '''

   if n == 1:
       return True
   else:
       return n * factorial_recursive(n -1)

print(factorial_recursive(50))