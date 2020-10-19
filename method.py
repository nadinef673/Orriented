class rectangle:

    def area1(self):
        self.answer = self.length * self.width
        print(self.answer)

objtable = rectangle()
objtable.length = int(input("Enter Length"))
objtable.width = int(input("Enter Width"))
objtable.area1()