import sys
def greeting(greeted="World"):
    return "Hello " + greeted + "!"

if len(sys.argv) > 1:
    print(greeting(sys.argv[1]))
else:
    print(greeting())
