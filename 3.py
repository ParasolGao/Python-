# -- coding: utf-8 --
name = 'Parasol'
age = 23
height = 180
weight = 70
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %r." % name #使用%r的话会将框住字符串的单影号一并显示
print "He's %d cm tall." % height
print "He's %d kg heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair) 
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)