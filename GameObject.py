class GameObject:
    def __init__(self, screen):
        self.position = (0, 0)
        self.screen = screen

    def onUpdate(self):
        pass

    def show(self, screen, pygame):
        pass

    def onClick(self, x, y):
        pass

    def onRelease(self, x, y):
        pass