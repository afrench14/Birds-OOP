class Bird:
    '''constructor'''
    def __init__(self, name = "", life = None, alive = True, birdType = None):
        self.name = name
        self.lifeSpan = life
        self.__age = 0
        self.__alive = alive
        self.type = birdType
        
    def makeSound(self):
        raise NotImplementedError

    def getAge(self):
        ''' returns integer of birds age '''
        return self.__age
         
    def growOld(self):
        ''' increments the Bird.age by 1 '''
        if self.__alive:
            self.__age += 1
            if self.__age > self.lifeSpan:
                self.__alive = False
        return None

    def isAlive(self):
        return self.__alive

    def __str__ (self):
        return "{0} is a {1} and is {2} years old (staus: {3}).".format (self.name, self.type, self.__age, self.__alive)


class Canary(Bird):
    def __init__(self, birdName):
        super().__init__(name = birdName)
        self.lifeSpan = 15
        self.type = "Canary"

    def makeSound(self):
        ''' returns string of "tweet" '''
        return "tweet"

class Crow(Bird):
		def __init__(self, birdName):
			super().__init__(name = birdName)
			self.lifeSpan = 4
			self.type = "Crow"

		def makeSound(self):
			''' returns string of "caw caw" '''
			return "caw caw"

class Duck(Bird):
    def __init__(self, birdName):
        super().__init__(name = birdName)
        self.type = "Duck"
        self.lifeSpan = 10
        
    def makeSound(self):
        ''' returns string of "quack" '''
        return "quack"



#driver code t run the above classes and child classes
aDuck = bird.Duck("Bob")
for i in range(0,4):
    aDuck.growOld()
print(aDuck.makeSound())
print(aDuck.__str__())

aCanary = bird.Canary("TweetiePie")
for i in range(0,10):
    aCanary.growOld()
print(aCanary.makeSound())
print(aCanary.__str__())

aCrow = bird.Crow("Evil Bob")
for i in range(0,10):
    aCrow.growOld()
print(aCrow.makeSound())
print(aCrow.__str__())