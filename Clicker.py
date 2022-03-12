from GameObject import GameObject
import random
import math

class Clicker(GameObject):
    def __init__(self, screen):
        super().__init__(screen)
        self.timeLeft = 2000
        self.randomizePosition()

    def randomizePosition(self):
        self.timeLeft = max(2000 - self.screen.getValue("passedFrames") / 100, 200)
        while True:
            self.position = (random.randint(0, 480), random.randint(0, 480))
            distance = math.sqrt((240 - self.position[0])**2 + (240 - self.position[1])**2)
            if distance < 200 and distance > 20:
                break

    def onUpdate(self):
        self.timeLeft -= 1

    def show(self, screen, pygame):
        r = min(255 - (self.timeLeft / 2000) * 255, 255)
        g = max((self.timeLeft / 2000) * 255, 0)
        b = 0
        pygame.draw.circle(screen, (r, g, b), self.position, 20)

    def onClick(self, x, y):
        distance = math.sqrt((x - self.position[0])**2 + (y - self.position[1])**2)
        if distance < 40: 
            self.randomizePosition()
            self.screen.increment("Points")

    def onRelease(self, x, y):
        pass