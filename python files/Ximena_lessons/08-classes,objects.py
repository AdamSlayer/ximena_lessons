class things:
    pass
class animate(things):
    pass
class inanimate(things):
    pass
class sidewalks(inanimate):
    pass
class animals(animate):
    def breathe(self):
        print("Breathing", self)
    def move(self):
        print("Moving")
    def eat_food(self):
        print("Eattting")
    def dance(self):
        
class mammals(animals):
    pass
class giraffes(mammals):
    pass
reginald = giraffes()
reginald.breathe()
herold = giraffes()
