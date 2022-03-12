from GameObject import GameObject
import math

class Defense(GameObject):
    def __init__(self, screen):
        self.position = (0, 0)
        self.screen = screen
        self.shootingSpeed = 20

    def onUpdate(self):
        self.setPositionInDirection(self.screen.getValue("MousePosition")[0], self.screen.getValue("MousePosition")[1], 50)

        #calculates the collissions between the defense and the attacker from the screen object
        for attacker in self.screen.attacker:
            #calculates the length of the vector between the attacker and the defense
            vec = (attacker.position[0] - self.position[0], attacker.position[1] - self.position[1])
            length = math.sqrt(vec[0]**2 + vec[1]**2)

            if length < 25:
                attacker.randomizePosition()
                #increases the points of the screen
                self.screen.increment("Points")

    def show(self, screen, pygame):
        #draw circle at position
        pygame.draw.circle(screen, (255, 0, 0), self.position, 10)

    def onClick(self, x, y):
        pass

    def onRelease(self, x, y):
        pass

    #Sets the position in a specified offset from the center towards the x and y position
    def setPositionInDirection(self, x, y, r):
        mouseVec = (x - 240, y - 240)
        length = math.sqrt(mouseVec[0]**2 + mouseVec[1]**2)
        if length > 0:
            mouseVec = (mouseVec[0] / length, mouseVec[1] / length)
            self.position = (int(240 + mouseVec[0] * r), int(240 + mouseVec[1] * r))
