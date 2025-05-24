def product(a, b,c):
    return a * b * c
print(product(1, 2, 3))

def divide(a, b):
    return a / b
print(divide(10, 2))

division=lambda x,y: x / y
print(division(10, 2))
cube=lambda x : x**3
print(cube(3))
greetings= lambda first,second : first + second
print(greetings("Hi, ", "Guys!"))
even= lambda x: x if x%2==0 else "Odd"
print(even(1))
pupil_check=lambda x: "Olevel" if x<=17 and x>=13 else "Alevel"
print(pupil_check(15))
#write a program to handle errrors 
# ask prog to ask for two numbers using input and then divide them use infinite looop 
#to keep asking valid input until user enters valid numbers