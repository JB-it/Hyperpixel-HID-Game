from Screen import Screen
from AttackerObject import Attacker
from DefenseGameObject import Defense
import random

class DefenderGameScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.font = self.game.pygame.font.SysFont('Comic Sans MS', 50)
        self.attacker = []
        self.centerRadius = 30

    def start(self):
        super().start()
        self.setVariable("Points", 0)
        self.setVariable("OldPoints", 0)
        self.setVariable("passedFrames", 0)
        self.setVariable("looseWaitFrames", -1)
        self.setVariable("hp", 2)
        self.setVariable("hpColors", [(255,0,0), (255,255,0), (0,255,0)])
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
        self.addGameObject(Defense(self))
        self.addNewAttacker()

    def stop(self):
        self.gameObjects.clear()
        self.attacker.clear()
        super().stop()


    def onUpdate(self):
        if len(self.attacker) == 0:
            self.addNewAttacker()

        if self.getValue("looseWaitFrames") > 0:
            self.increment("looseWaitFrames", -1)
            return
        if self.getValue("looseWaitFrames") == 0:
            self.game.loadScreen(0)
            return

        super().onUpdate()

        if self.getValue("Points") > self.getValue("OldPoints"):
            sound = None
            if self.getValue("Points") // 10 > self.getValue("OldPoints") // 10:
                sound = self.getValue("levelUpSound")
                self.addNewAttacker()
            else:
                sound = self.getValue("clickSounds")[random.randint(0, 4)]
            
            if sound is not None:
                self.game.pygame.mixer.Sound.play(sound)
        
        self.setVariable("OldPoints", self.getValue("Points"))

    def onUpdateScreen(self):
        super().onUpdateScreen()

        if self.getValue("looseWaitFrames") > 0:
            s = self.game.pygame.Surface((480,480))  # the size of your rect
            s.set_alpha(128)                # alpha level
            s.fill((255,0,0))           # this fills the entire surface
            self.game.pygameScreen.blit(s, (0,0))    # (0,0) are the top-left coordinates


        #draws a circle in the center of the screen
        self.game.pygame.draw.circle(self.game.pygameScreen, self.getCenterColor(), (240,240), self.centerRadius)
        
        text = self.font.render(str(self.getValue("Points")), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (240, 240)
        self.game.pygameScreen.blit(text, textRect)


    def onClick(self, x, y):
        super().onClick(x, y)

    def onRelease(self, x, y):
        super().onRelease(x, y)

    def getCenterColor(self):
        return self.getValue("hpColors")[self.getValue("hp")]

    def addNewAttacker(self):
        atk = Attacker(self)
        self.addGameObject(atk)
        self.attacker.append(atk)

    def looseHP(self):
        self.increment("hp", -1)
        if self.getValue("hp") == 0:
            self.setVariable("looseWaitFrames", 300)
            self.game.pygame.mixer.Sound.play(self.getValue("loose"))
        else:
            self.game.pygame.mixer.Sound.play(self.getValue("specialSounds")[self.getValue("hp")])