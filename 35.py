class TheThing(object):

    def _init_(self):
        print "I got called."
        self.number = 0

  # def some_function(self):
    
    def add_me_up(self, more):
        self.number += more
        return self.number

a = TheThing()
b = TheThing()
a._init_()
b._init_()
##a.some_function()
#b.some_function()

print a.add_me_up(20)
print a.add_me_up(20)
print b.add_me_up(30)
print b.add_me_up(30)

print a.number
print b.number
