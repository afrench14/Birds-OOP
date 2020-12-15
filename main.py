# driver code for testing duck & canary classes
import bird

aQuack = bird.Duck("Bob")

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