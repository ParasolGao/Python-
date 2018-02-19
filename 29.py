i = 0
numbers = []

def whileloop():
    numbers = []
    i = 0
    a = 4
    while i < a:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i    
    return numbers

numbers = whileloop()
print "The numbers: "

for num in numbers:
    print num