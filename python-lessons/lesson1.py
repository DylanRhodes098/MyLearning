class animal:
    def __init__ (self, name):
        self.name = name

class dog (animal):
    def __init__ (self, name, sound):
        super().__init__(name)
        self.sound = sound

      
    def speak (self):
        print(f"{self.sound}, my name is {self.name}")
    
class cat (animal):
    def __init__ (self, name, sound):
        super().__init__ (name)
        self.sound = sound
    
    def speak (self):
        print(f"{self.sound}, my name is {self.name}")

if __name__ == "__main__":
    d = dog("jerry", "woof!")
    c = cat("simon", "meow")
    d.speak()
    c.speak()