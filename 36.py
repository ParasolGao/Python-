class Animal(object):
    pass

##??
class Dog(Animal):

    def __init__(self, name):
        self.name = name

class Cat(Animal):

    def __init__(self,name):
        self.name = name

class Person(object):

    def __init__(self,name):
        self.name = name
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(object):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
#这就用到了“类即是对象”的概念。他们决定用小写的“object”这个词作为一个类，
#让你在创建新类时从它继承下来。有点晕了吧？一个类从另一个类继承，而后者
#虽然是个类，但名字却叫“object”……不过在定义类的时候，别忘记要从 object
#继承就好了。
#的确如此。一个词的不同就让这个概念变得更难理解，让我不得不现在才讲给你。
#现在你可以试着去理解“一个是对象的类”这个概念了，如果你感兴趣的话。
#不过我还是建议你别去理解了，干脆完全忘记旧格式和新格式类的区别吧，就假
#设 Python 的 class 永远都要求你加上 (object) 好了，你的脑力要留着思考更
#重要的问题。