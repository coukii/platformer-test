# game options/settingsS
TITLE = "Platformer"
WIDTH = 720
HEIGHT = 480
FPS = 60
FONT_NAME = 'arial-bold'

# player properties
PLAYER_ACC = 1.1
PLAYER_FRICTION = -0.2
PLAYER_TOPSPEED = 6
PLAYER_GRAVITY = 0.9

# starting platforms

PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT / 2 + 50, 100, 20)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (122, 215, 205)
DARKGREEN = (35, 45, 45)
BGCOLOR = LIGHTBLUE
