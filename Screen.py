class Screen:
    def __init__(self, game):
        self.game = game
        self.running = True
        self.gameObjects = []
        self.variables = {
            "MousePosition": (0, 0),
            "passedFrames": 0,
        }

    def start(self):
        pass

    def stop(self):
        pass

    def onUpdate(self):
        self.setVariable("MousePosition", self.game.mousePosition)
        for gameObject in self.gameObjects:
            gameObject.onUpdate()

    def onUpdateScreen(self):
        for gameObject in self.gameObjects:
            gameObject.show(self.game.pygameScreen, self.game.pygame)

    def onClick(self, x, y):
        for gameObject in self.gameObjects:
            gameObject.onClick(x, y)

    def onRelease(self, x, y):
        for gameObject in self.gameObjects:
            gameObject.onRelease(x, y)

    def updateVariable(self, key, value):
        self.variables[key] = value

    def setVariable(self, key, value):
        self.variables[key] = value

    def getValue(self, key):
        return self.variables[key]

    def increment(self, key, amount=1):
        self.variables[key] = self.variables[key] + amount

    def addGameObject(self, obj):
        self.gameObjects.append(obj)

    def removeGameObject(self, obj):
        self.gameObjects.remove(obj)
