#creating a class
class intro:

    #adding a method
    def intro_oop(self):
        print("I am a", self.name)
        print("my color is", self.color)

#creating an object
objshape1 = intro_oop()
objshape1.lw = "Triangle"
objshape1.color = "Black"
objshape1.intro_oop()