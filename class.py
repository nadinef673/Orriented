#cerating a class

class rectangle:

    def rect_oop(self):
        print("My length is", self.length)
        print("My width is", self.width)
        print("My area is", self.area)

obj_rec = rectangle()

obj_rec.length = 16
obj_rec.width = 20
obj_rec.area = obj_rec.length * obj_rec.width
obj_rec.rect_oop()

