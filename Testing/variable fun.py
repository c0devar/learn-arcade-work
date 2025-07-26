#in this file we are testing out variables
"""
x = 3
x = x + 1

x = x + 1

x = x + 1
print(x)

variable_name_one = x + 1
print (variable_name_one, "fucka")

# more example code
# This works, and prints "3"
x = 3
print(x)

# Make x bigger by one using the regular
# assignment operator.
x = x + 1
print(x)

# Make x bigger by one, using the +=
# assignment operator.
x += 1
print(x)

# Make x smaller by six using the -=
# operator.
x -= 6
print(x)


import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHTH = 800

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHTH, "drawing no.2")

arcade.set_background_color((29, 229, 211, 0))

arcade.start_render()

arcade.draw_circle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHTH/4, 80, (248, 140, 187))

arcade.finish_render()
arcade.run()


#we are printing an answer unsing a formatted string (note the f in front of the quotation marks)
answer =  42
print(f"The answer is {answer}.")

#learning to define a function
"""

def print_hello():
    """ This is a comment that describes the function. """
    print("Hello!")

# This calls our function twice.
print_hello()
print_hello()

# Add two numbers and return the results e
def sum_two_numbers(a, b):
    e = a + b
    return e

# This doesn't do much, because we don't capture the result
sum_two_numbers(5, 15)

my_result = sum_two_numbers(5, 15) #<--- This line CAPTURES the return value

print(my_result)


# abstraction to make me understand using banana bread example
def make_banana_bread (milk, flour, eggs, bananas):
    banana_bread = milk + flour + eggs + bananas
    return banana_bread
"""
i am defining the recipe for banana bread and 
the ingredients, I am defining what the final product will look like using the banana_bread variable
and I am defining to return this product when done. BUT I am not defining what to do with this product >
banana bread cannot be handed anywhere
"""

final_baked_good = make_banana_bread(1, 2, 3, 4)

print(final_baked_good)

"""
# example six-pack volume calculation
def volume_cylinder(radius, height):
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume

six_pack_volume = volume_cylinder(2.5, 5) * 6
# See how the value returned from volume_cylinder goes into the equation and is multiplied by six.
# We would not be able to chain together calculations like that if all we could do was print, instead of return.
"""


# This function will print the result
def sum_print(a, b):
    result = a + b
    print(result)


# This function will return the result
def sum_return(a, b):
    result = a + b
    return result


# This code prints the sum of 4+4, because the function has a print
sum_print(4, 4)

# This code prints nothing, because the function returns, and doesn't print
sum_return(4, 4)

# This code will not set x1 to the sum.
# The sum_print function does not have a return statement, so it returns
# nothing!
# x1 actually gets a value of 'None' because nothing was returned
x1 = sum_print(4, 4)
print("x1 =", x1)

# This will set x2 to the sum and print it properly.
x2 = sum_return(4, 4)
print("x2 =", x2)


def calculate_average(a, b):
    """ Calculate an average of two numbers """
    result = (a + b) / 2
    return result


# Pretend you have some code here
x = 45
y = 56

# Wait, how do I print the result of this?
calculate_average(x, y)

average_result = calculate_average(x, y)
print (average_result)


# Create the x variable and set to 44
x = 44


# Define a simple function that prints x
def f():
    print(x)


# Call the function
f()


# Define a simple function that prints x
def f(x):
    x += 1
    print(x)

f(8)
y = 50
f(y)

# Example 15
# New concept!
# Covered in more detail in a later chapter
def a(my_list):
    print("function a, list =  ", my_list)
    my_list[0] = 1000
    print("function a, list =  ", my_list)


my_list = [5, 2, 4]

print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)