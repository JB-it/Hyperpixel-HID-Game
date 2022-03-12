from GameObject import GameObject

class MouseFollower(GameObject):
    def __init__(self, screen):
        super().__init__(screen)

    def updatePosition(self, pos):
        self.position = pos

    def show(self, screen, pygame):
        pygame.draw.circle(screen, (255, 255, 255), self.position, 10)