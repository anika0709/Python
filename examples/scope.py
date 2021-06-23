
def outer_function():
    a = 20
    #print ("value of b is outer_function {}".format(b))
    print ("value of a  in outer_function is {}".format(a))
    def inner_func():
        c = 30
        a = 30
        print ("value of a  in inner_function is {}".format(a))
    inner_func()
    print ("value of a  in outer_function is {}".format(a))

a = 10
outer_function()
print ("value of a  in global scope is {}".format(a))

# global scope


def outerg_function():
    a = 20
    global g 
    g = 20
    #print ("value of b is outer_function {}".format(b))
    print ("value of g in outer_function is {}".format(g))
    def innerg_func():
        c = 30
        a = 30
        global g 
        g = 30
        print ("value of g in inner_function is {}".format(g))
    innerg_func()
    print ("value of g in outer_function is {}".format(g))


g = 10
print ("value of g in before func is {}".format(g))
outerg_function()
print ("value of g in global scope is {}".format(g))



