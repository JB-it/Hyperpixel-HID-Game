from Screen import Screen
from Button import Button

class Menu(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.addGameObject(Button(self, (140, 145, 200, 75), "Clickers", self.startClickerGame))
        self.addGameObject(Button(self, (140, 235, 200, 75), "Defenders", self.startDefenderGame))
        self.addGameObject(Button(self, (165, 325, 150, 50), "End", self.endGame))
        self.font = self.game.pygame.font.SysFont('Comic Sans MS', 50)

    def onUpdate(self):
        super().onUpdate()

    def onUpdateScreen(self):
        super().onUpdateScreen()

    def onClick(self, x, y):
        super().onClick(x, y)

    def onRelease(self, x, y):
        super().onRelease(x, y)

    def startClickerGame(self):
        self.game.loadScreen(1)

    def startDefenderGame(self):
        self.game.loadScreen(2)

    def backtoMenu(self):
        self.game.loadScreen(0)

    def endGame(self):
        self.game.end()
