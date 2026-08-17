from pygame import *
from player import *
from enemy import *
from level import *
from items.coin import *
from camera import *
from src import level
from ui import UI

init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

player = Player()
platforms = level.create_level()
enemies = level.enemies
coins = level.coins
camera = Camera()
ui = UI()

running = True

while running:

    player.update(platforms)

    for enemy in enemies:
        enemy.update()

    for coin in coins:
        coin.update(player)

    camera.update(player)

    platforms.draw(window)
    player.draw(window)
    for enemy in enemies:
        enemy.draw(window)
    for coin in coins:
        coin.draw(window)

    ui.draw(window)