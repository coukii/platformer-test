# sprite classes for platform game
import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((40, 40))
        self.image.fill(DARKGREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.jumpcounter = 0
        self.onground = True

    def jump(self):
        # jump only if standing on a platform
        # self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        # self.rect.x -= 1
        if hits:
            self.jumpcounter = 0
            self.vel.y = -20
        elif self.jumpcounter < 1:
            self.vel.y = -20
            self.jumpcounter += 1



    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        # apply friction

        keys = pg.key.get_pressed()
        if self.onground == True:
            if keys[pg.K_LEFT]:
                self.acc.x = -PLAYER_ACC
                # print("moving")
            elif keys[pg.K_RIGHT]:
                self.acc.x = PLAYER_ACC
                # print("moving")
            else:
                self.acc.x += self.vel.x * PLAYER_FRICTION
                # print("stopped/slowing")

        self.vel += self.acc #v = u + at

        # limit speed
        if self.vel.x > PLAYER_TOPSPEED:
            self.vel.x = PLAYER_TOPSPEED
        if self.vel.x < PLAYER_TOPSPEED * -1:
            self.vel.x = PLAYER_TOPSPEED * -1


        # equations of motion
        self.vel = self.vel + 0.5 * self.acc #v = ut + 1/2at^2
        self.pos += self.vel

        if self.pos.x <= 20:
            self.pos.x = 20

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(DARKGREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
