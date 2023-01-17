class Guitar:

    def __init__(self, maker, model):
        self.maker = maker
        self.model = model

    def play_chord(self,x):
        print("That" , x, " chord sounds great on this ", self.maker, " ", self.model)
    def what_guitar(self):
        print("This guitar is a ", self.maker, self.model, "!")


#guitar1 = Guitar("fender", "stratocaster")
#guitar2 = Guitar("gibson", "SG")

#guitar1.play_chord("A")
#guitar2.what_guitar()