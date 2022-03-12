from GameObject import GameObject

class Button(GameObject):
    def __init__(self, screen, transform, text, callback):
        self.rectTransform = transform
        self.screen = screen
        self.text = text
        self.callback = callback
        self.font = self.screen.game.pygame.font.SysFont('Comic Sans MS', 50)

    def onUpdate(self):
        pass

    def show(self, screen, pygame):
        #draws a rectangle on the screen
        pygame.draw.rect(screen, (255, 255, 255), self.rectTransform)
        #draws text centered on
        text = self.font.render(self.text, True, (0, 0, 0))
        textRect = text.get_rect(center=(self.rectTransform[0] + self.rectTransform[2]/2, self.rectTransform[1] + self.rectTransform[3]/2))
        self.screen.game.pygameScreen.blit(text, textRect)

    def onClick(self, x, y):
        #checks if click is in rect
        if self.rectTransform[0] < x < self.rectTransform[0] + self.rectTransform[2] and self.rectTransform[1] < y < self.rectTransform[1] + self.rectTransform[3]:
            if self.callback is not None:
                self.callback()

    def onRelease(self, x, y):
        pass