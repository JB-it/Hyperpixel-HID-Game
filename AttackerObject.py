from GameObject import GameObject
import random
import math

class Attacker(GameObject):
    def __init__(self, screen):
        self.position = self.randomOnCircle(240)
        self.velocity = (0, 0)
        self.goal = (240, 240)
        self.screen = screen
        self.speedMultiplier = 0.001

    def onUpdate(self):
        direction = (self.goal[0] - self.position[0], self.goal[1] - self.position[1])
        length = math.sqrt(direction[0]**2 + direction[1]**2)
        if length > 0:
            if(length < self.screen.centerRadius):
                self.screen.removeGameObject(self)
                self.screen.attacker.remove(self)
                self.screen.looseHP()
                return

            direction = (direction[0] / length, direction[1] / length)
            self.velocity = (self.velocity[0] + direction[0] * self.speedMultiplier, self.velocity[1] + direction[1] * self.speedMultiplier)
            self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

    def randomizePosition(self):
        self.velocity = (0, 0)
        self.position = self.randomOnCircle(random.randint(200, 300))

    def show(self, screen, pygame):
        #draws a circle at the position of the attacker
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position[0]), int(self.position[1])), 10)

    def onClick(self, x, y):
        pass

    def onRelease(self, x, y):
        pass

    def randomOnCircle(self, radius):
        angle = random.random() * 2 * math.pi
        x = int(math.cos(angle) * radius) + 240
        y = int(math.sin(angle) * radius) + 240
        return (x, y)