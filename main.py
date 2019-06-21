import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # init game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game loop - update
        self.all_sprites.update()

        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if self.player.pos.y > hits[0].rect.top + 20:
                print("can collide")
                if self.player.vel.x > 0:
                    print("hitting left")
                    self.player.pos.x = hits[0].rect.left - 20
                if self.player.vel.x < 0:
                    print("hitting right")
                    self.player.pos.x = hits[0].rect.right + 20

        # check if player is falling to collide
        
        if self.player.vel.y > 0:
            
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            
            if hits:
                if self.player.pos.y < hits[0].rect.top + 20:
                    self.player.pos.y = hits[0].rect.top + 1
                    self.player.vel.y = 0
        # check if player is rising to collide
        if self.player.vel.y < 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.bottom + 40
                self.player.vel.y = 0
        # if player reaches right 1/4 of screen
        if self.player.rect.right >= WIDTH * 3/4:
            # if self.player.vel.x > 0:
            self.player.pos.x -= max(abs(self.player.vel.x),2)
            for plat in self.platforms:
                plat.rect.right-= max(abs(self.player.vel.x),2)
                if plat.rect.right <= 0:
                    print("kill")
                    plat.kill()

        # # if player reaches left 1/4 of screen
        # if self.player.rect.left <= WIDTH * 1/4:
        #     # if self.player.vel.x > 0:
        #     self.player.pos.x += max(abs(self.player.vel.x),2)
        #     for plat in self.platforms:
        #         plat.rect.right += max(abs(self.player.vel.x),2)

        # Death
        if self.player.rect.top > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

        #spawn new platforms
        while len(self.platforms) < 3 and self.player.rect.top < HEIGHT:
            print("spawning")
            width = random.randrange(50,100)
            p = Platform(random.randrange(WIDTH + 10, WIDTH + 20), random.randrange(HEIGHT / 2,  HEIGHT - 40), width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        # game loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # game loop - draw
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, DARKGREEN, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Arrows to move, Space to jump", 22, DARKGREEN, WIDTH / 2, HEIGHT / 2)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        pass

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()

g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
