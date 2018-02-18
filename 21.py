from sys import argv
script, filename = argv

def print_all(f):
    print f.read()

def print_a_line(line, f):
    print line,f.readfile()

def rewind(f):
    f.seek(0)

print "First let's print the whole file:"
f = open(filename)
print_all(f)

print "Now let's rewind, kind of like a tape."
rewind(f)
print f.readline()
print f.readline()
print f.readline()

