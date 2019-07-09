'''
The purpose of this program is to take one of 6 different unknown variables, along with any other given values, and solve one
of the three kinematic equations.
They are as follows:
v = v_i + at
x = x_i + v_i*t + 1/2 * a * t^2
v^2 = v_i^2 + 2a(x - x_i)
Depending on the values known, one or sometimes more of them can be used to solve for it.
'''

# Variable assignment below
variables = []

print(" ")
print("- - -")
print(" ")
print ("When inputting values put an 'n/a' in the place of any non-given.")
print ("Also remember to put a 'find' in the place of your target.")
print(" ")
print ("- - -")
print (" ")
v_i = input("Enter your initial velocity. (m/s): ") #initial velocity (m/s)
if v_i != "find" and v_i != "n/a":
    v_i = int(v_i)
elif v_i != "n/a": # Adding the variable to the list of givens
    variables.append(v_i)

v = input("Enter your final velocity. (m/s): ") #velocity (m/s)
if v != "find" and v != "n/a":
    v = int(v)
elif v != "n/a":
    variables.append(v)

t = input("Enter the time elapsed. (s): ") #time (sec)
if t != "find" and t != "n/a":
    t = int(t)
elif t != "n/a":
    variables.append(t)

a = input("Enter your constant acceleration. (m/s/s): ") #constant acceleration (m/s/s)
if a != "find" and a != "n/a":
    a = int(a)
elif a != "n/a":
    variables.append(a)

x_i = input("Enter your initial position. (m): ") #initial displacement(m)
if x_i != "find" and x_i != "n/a":
    x_i = int(x_i)
elif x_i != "n/a":
    variables.append(x_i)

x = input("Enter your final position. (m): ") #final displacement (m)
if x != "find" and x != "n/a":
    x = int(x)
elif x != "n/a":
    variables.append(x)

print(" ")

# Defining functions below

ans = 0

def first(): # Has v, v_i, a, & t
    if a == "find":
        ans = v - v_i
        return ans / t
    elif v == "find":
        ans = a * t
        return ans + v_i
    elif v_i == "find":
        ans = a * t
        return v / ans
    elif t == "find":
        ans = v - v_i
        return ans / t

def second(): # Has x, x_i, v_i, t, & a
    if x == "find":
        ans = (.5 * a * (t**2)) + (v_i * t) + x_i
        return ans
    elif x_i == "find":
        ans = x - (v_i * t) + (.5 * a * (t**2))
        return ans
    elif v_i == "find":
        ans = x - x_i - (.5 * a * (t**2))
        return ans / t
    elif a == "find":
        ans = x - x_i - (v_i * t)
        return ans / (.5 * (t**2))
    elif t == "find":
        print("error")

def third(): # Has v, v_i, a, x, & x_i
    if v == "find":
        ans = (v_i ** 2) + (2 * a * (x - x_i))
        return ans ** .5
    elif v_i == "find":
        ans = (v ** 2) - (2 * a * (x - x_i))
        return ans ** .5
    elif a == "find":
        ans = ((v ** 2) - (v_i ** 2)) / (2 * (x - x_i))
        return ans
    elif x == "find":
        ans = ((v ** 2) - (v_i ** 2)) / (2 * a)
        return ans + x_i
    elif x_i == "find":
        ans = ((v ** 2) - (v_i ** 2)) / (2 * a)
        return ans + x
def error():
    print("Error: You did not input enough givens.")
    print("Try to find any missing variables, or omit any unnecessary values before trying again.")

# Deciding which equation to use

if a == "find" and v != "n/a" and v_i != "n/a" and t != "n/a":
    print("a: " + str(float(first())) + " m/s/s")

elif a == "find" and x != "n/a" and x_i != "n/a" and v_i != "n/a" and t != "n/a":
    print("a: " + str(float(second())) + " m/s/s")

elif a == "find" and x != "n/a" and x_i != "n/a" and v_i != "n/a" and v != "n/a":
    print("a: " + str(float(third())) + " m/s/s")

elif v =="find" and v_i != "n/a" and a != "n/a" and t != "n/a":
    print("v: " + str(float(first())) + " m/s")

elif v == "find" and v_i != "n/a" and a != "n/a" and x != "n/a" and x_i != "n/a": # <--- HERE
    print("v: " + str(float(third())) + " m/s")

elif v_i == "find" and v != "n/a" and a != "n/a" and t != "n/a":
    print("v_i: " + str(float(first())) + " m/s")

elif v_i == "find" and x != "n/a" and x_i != "n/a" and t != "n/a" and a != "n/a":
    print("v_i: " + str(float(second())) + " m/s")

elif v_i == "find" and v != "n/a" and x != "n/a" and x_i != "n/a" and a != "n/a":
    print("v_i: " + str(float(third())) + " m/s")

elif t == "find" and a != "n/a" and v != "n/a" and v_i != "n/a":
    print("t: " + str(float(first())) + " sec")

elif t == "find" and x != "n/a" and x_i != "n/a" and v_i != "n/a" and a != "n/a":
    print("t: " + str(float(second())) + " sec")

elif x == "find" and x_i != "n/a" and v_i != "n/a" and a != "n/a" and t != "n/a":
    print(" x: " + str(float(second())) + " meters")

elif x == "find" and x_i != "n/a" and v != "n/a" and v_i != "n/a" and a != "n/a":
    print("x: " + str(float(third())) + " meters")

elif x_i == "find" and x != "n/a" and v_i != "n/a" and a != "n/a" and t != "n/a":
    print("x_i: " + str(float(second())) + " meters")

elif x_i == "find" and a != "n/a" and v != "n/a" and v_i != "n/a" and a != "n/a":
    print("x_i: " + str(float(third())) + " meters")

else:
    error()
