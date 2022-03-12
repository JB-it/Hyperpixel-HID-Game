import pygame
from EmptyScreen import Empty
from MainGameScreen import MainGameScreen
from DefenderGameScreen import DefenderGameScreen
from MenuScreen import Menu

class Game():
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.font.init()
        pygame.init()
        diameter = 480
        self.pygameScreen = pygame.display.set_mode((diameter, diameter), pygame.FULLSCREEN)
        pygame.display.set_caption('Hyperpixel Game')#
        self.running = True
        self.mousePosition = (0, 0)
        self.mousePressed = False
        self.lastPressed = False
        self.screens = []
        self.currentScreen = 0
        self.pygame = pygame

    def setup(self):
        self.screens.append(Menu(self))
        self.screens.append(MainGameScreen(self))
        self.screens.append(DefenderGameScreen(self))

        self.getCurrentScreen().start()

    def run(self):
        while self.running:
            self.handleEvents()
            self.update()
            self.updateScreen()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    def update(self):
        #self.mousePosition = pygame.mouse.get_pos()
        #self.mousePressed = pygame.mouse.get_pressed()[0]

        if not self.mousePressed is self.lastPressed:
            if self.mousePressed:
                self.getCurrentScreen().onClick(self.mousePosition[0], self.mousePosition[1])
            else:
                self.getCurrentScreen().onRelease(self.mousePosition[0], self.mousePosition[1])
        self.lastPressed = self.mousePressed

        self.getCurrentScreen().onUpdate()

    def updateScreen(self):
        self.pygameScreen.fill((0, 0, 0))

        # Draw the screen
        self.getCurrentScreen().onUpdateScreen()

        pygame.display.flip()

    def onHyperpixelTouch(self, touch_id, x, y, state):
        self.mousePosition = (x, y)
        self.mousePressed = state

    def getCurrentScreen(self):
        return self.screens[self.currentScreen]

    def loadScreen(self, screenIndex):
        self.getCurrentScreen().stop()
        self.currentScreen = screenIndex
        self.getCurrentScreen().start()

    def end(self):
        self.running = False