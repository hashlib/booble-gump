import os
import pygame
from enum import Enum


DATA_DIR = "./data"

HIGH_SCORE_PATH = os.path.join(DATA_DIR, "high_score.txt")

PACK_NAME = "blue"
PACK_DIR = os.path.join(DATA_DIR, PACK_NAME)

PLAYER_DIR = os.path.join(PACK_DIR, "player")

PLAYER_IMAGES_DIR = os.path.join(PLAYER_DIR, "images")
PLAYER_SOUNDS_DIR = os.path.join(PLAYER_DIR, "sounds")
SHOOT_SOUND_NAME = "blaster"
DEATH_SOUND_NAME = "crash"
FALL_DOWN_SOUND_NAME = "whistle"

PLATFORMS_DIR = os.path.join(PACK_DIR, "platforms")
P_SOUNDS_DIR = os.path.join(PLATFORMS_DIR, "sounds")
P_IMAGES_DIR = os.path.join(PLATFORMS_DIR, "images")
P_INITIAL_WEIGHTS = (80, 20, 0, 0)
P_ALIVE_COEFFICIENT = 2
P_FALL_SPEED = -1000

MONSTERS_DIR = os.path.join(PACK_DIR, "monsters")
M_SOUNDS_DIR = os.path.join(MONSTERS_DIR, "sounds")
M_IMAGES_DIR = os.path.join(MONSTERS_DIR, "images")
M_INITIAL_WEIGHTS = tuple(1 for _ in range(9))

BACKGROUND = pygame.image.load(os.path.join(PACK_DIR, "background.png"))
SCORE_BAR = pygame.image.load(os.path.join(PACK_DIR, "score_bar.png"))
INVITATION = pygame.image.load(os.path.join(PACK_DIR, "invitation.png"))

MAIN_FONT_PATH = os.path.join(PACK_DIR, "IndieFlower-Regular.ttf")
SCORE_COLOR = "#2E4600"
HIGH_SCORE_COLOR = LAST_SCORE_COLOR = "#000000"
FPS = 60

LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
SHOOT_KEYS = (pygame.K_SPACE, pygame.K_UP)
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 320, 512
WORLD_BOUNDINGS = (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
LEVEL_LINE = WINDOW_HEIGHT // 2
GRAVITATION = 1300

PLATFORMS_JUMP_FORCE = 600
PLATFORM_MOVE_SPEED = 100
PLATFORM_SIZE = PLATFORM_WIDTH, PLATFORM_HEIGHT = 57, 14

PLAYER_WEIGHT = 1
PLAYER_HORIZONTAL_FORCE = 350
PLAYER_BOUNCE_ANIMATION_STEPS = 20
PLAYER_SHOOT_ANIMATION_STEPS = 20
PLAYER_SIZE = PLAYER_WIDTH, PLAYER_HEIGHT = 46, 45
PLAYER_LEGS_LENGTH = 10

LEFT_NOSE_POS = (16, 1)
RIGHT_NOSE_POS = (32, 1)
SHELLS_SPEED = -1000

MAX_PLAYER_SPEED = PLATFORMS_JUMP_FORCE / PLAYER_WEIGHT
MAX_PLAYER_JUMP_HEIGHT = \
    int(MAX_PLAYER_SPEED ** 2 / (2 * GRAVITATION) - PLAYER_HEIGHT)

MAX_DIFFICULT = 21

MONSTER_TOP_LEVEL = 5
MONSTER_FALL_SPEED = 500
MONSTER_JUMP_FORCE = 800


START_PLATFORM_JUMP_FORCE = 1800
MENU_PLATFORM_HEIGHT = WORLD_BOUNDINGS[3] - 100


class Direction(Enum):
    STALL = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
