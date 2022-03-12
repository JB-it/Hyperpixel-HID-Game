from Screen import Screen

class Empty(Screen):
    def __init__(self, game):
        super().__init__(game)

    def onUpdate(self):
        super().onUpdate()

    def onUpdateScreen(self):
        super().onUpdateScreen()

    def onClick(self, x, y):
        super().onClick(x, y)

    def onRelease(self, x, y):
        super().onRelease(x, y)
