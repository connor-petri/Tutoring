# Game.start
Game.debug = True

Game.player = Player()
Platform()
Platform().y = -100
Platform().y = -200
floor(-600, -250, 50)


# Game.loop
if key_was_pressed('b'):
    Game.debug = False if Game.debug else True
