class Tower:

    def drawPole(self):
            for x in range(1,5,1):
                print('      |')

    def drawBase(self):
            print('------------------')

    def drawTitle(self, title):
            print(f"   {title}")

    def draw(self, title):
            self.drawPole()
            self.drawBase()
            self.drawTitle(title)

 # object A
towerA = Tower()
towerA.draw("Tower-A")

    # object B
towerB = Tower()
towerB.draw("Tower-B")

    # object C
towerC = Tower()
towerC.draw("Tower-C") 

