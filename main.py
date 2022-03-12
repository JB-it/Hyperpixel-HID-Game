from hyperpixel2r import Touch
from Game import Game

touch = Touch(bus=11, i2c_addr=0x15, interrupt_pin=27)
game = Game()

@touch.on_touch
def handle_touch(touch_id, x, y, state):
    game.onHyperpixelTouch(touch_id, x, y, state)

if __name__ == "__main__":
    game.setup()
    game.run()