from Screen import Screen
from Clicker import Clicker
import random

class MainGameScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.clickerAmount = 3
        self.clickers = []
        self.variables["clickSounds"] = [
            self.game.pygame.mixer.Sound("Sounds/Click1.wav"),
            self.game.pygame.mixer.Sound("Sounds/Click2.wav"),
            self.game.pygame.mixer.Sound("Sounds/Click3.wav"),
            self.game.pygame.mixer.Sound("Sounds/Click4.wav"),
            self.game.pygame.mixer.Sound("Sounds/Click5.wav")
        ]
        self.variables["specialSounds"] = [
            self.game.pygame.mixer.Sound("Sounds/Special1.wav"),
            self.game.pygame.mixer.Sound("Sounds/Special2.wav"),
            self.game.pygame.mixer.Sound("Sounds/Special3.wav"),
        ]
        self.variables["levelUpSound"] = self.game.pygame.mixer.Sound("Sounds/upgrade.wav")
        self.variables["loose"] = self.game.pygame.mixer.Sound("Sounds/loose1.wav")
        self.font = self.game.pygame.font.SysFont('Comic Sans MS', 50)


    def start(self):
        super().start()
        self.setVariable("Points", 0)
        self.setVariable("OldPoints", 0)
        self.setVariable("passedFrames", 0)
        self.setVariable("looseWaitFrames", -1)
        for i in range(self.clickerAmount):
            self.addNewClicker()

    def stop(self):
        super().stop()
        self.gameObjects.clear()
        self.clickers.clear()


    def onUpdateScreen(self):
        super().onUpdateScreen()

        if self.getValue("looseWaitFrames") > 0:
            s = self.game.pygame.Surface((480,480))  # the size of your rect
            s.set_alpha(128)                # alpha level
            s.fill((255,0,0))           # this fills the entire surface
            self.game.pygameScreen.blit(s, (0,0))    # (0,0) are the top-left coordinates


        # draws the points variable centered on the screen
        text = self.font.render(str(self.getValue("Points")), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (240, 240)
        self.game.pygameScreen.blit(text, textRect)
        
    def onUpdate(self):
        if self.getValue("looseWaitFrames") > 0:
            self.increment("looseWaitFrames", -1)
            return
        if self.getValue("looseWaitFrames") == 0:
            self.game.loadScreen(0)
            return

        self.updateVariable("MousePosition", self.game.mousePosition)
        self.increment("passedFrames")
            
        if self.getValue("Points") > self.getValue("OldPoints"):
            sound = None
            if self.getValue("Points") // 50 > self.getValue("OldPoints") // 50:
                sound = self.getValue("levelUpSound")
                self.addNewClicker()
            elif self.getValue("Points") // 10 > self.getValue("OldPoints") // 10:
                sound = self.getValue("specialSounds")[random.randint(0, 2)]
            else:
                sound = self.getValue("clickSounds")[random.randint(0, 4)]
            
            if sound is not None:
                self.game.pygame.mixer.Sound.play(sound)

        self.setVariable("OldPoints", self.getValue("Points"))
                
        super().onUpdate()

        #checks clickers if lifetime variable is below 0
        for clicker in self.clickers:
            if clicker.timeLeft <= 0:
                self.game.pygame.mixer.Sound.play(self.getValue("loose"))
                self.setVariable("looseWaitFrames", 500)

    def addNewClicker(self):
        clk = Clicker(self)
        self.addGameObject(clk)
        self.clickers.append(clk)