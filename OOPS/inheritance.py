class Bird:        #Parent class

    def __init__(self):
        print("Bird is ready")

    def whoisthis(self):
        print("Bird")
    
    def swim(self):
        print("Swim faster")
    
class Penguin(Bird):               #Child class

    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisthis(self):
        print("Penguin")
        super().whoisthis()
    
    def run(self):
        print("Run faster")

peggy = Penguin()  #Child class object
peggy.whoisthis()
peggy.swim()
peggy.run()