# Defining multiplication
def multiply(a,b):
	return a * b

# Defining division
def divide(a,b):
	return a / b

# Defining addition
def add(a,b):
	return a + b

# Defining subtraction
def substract(a,b):
	return a - b

print("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)

#Defining squaring
def square(a):
	return a * a
print("I'm going to use the calculator function to square 4")
y = square(4)
print(y)

#Defining cubing
def cube(a):
	return a * a * a 

print("I'm going to use the calculator function to cube 5")
z = cube(5)
print(z)

#Define square_n_times
def square_n_times(number,n):
	return multiply((number * number),n)

print("I'm going to use the calculator function to square 4 two times")
w = square_n_times(4,2)
print(w)
