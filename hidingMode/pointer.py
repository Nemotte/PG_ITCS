import pygame
import game_functions as gf


class Pointer():
    flag = 0            # pointer指向的技能

    def __init__(self, p_setting, screen, nowbar, pokemon02, pokemon01, statebar,
                 statebar01, healthbar, healthbar01):
        self.image = pygame.image.load("../othersource/Pic/pointer.png")
        self.rect = self.image.get_rect()
        self.p_setting = p_setting
        self.rect.topleft = self.p_setting.menubarInitPointer
        self.screen = screen
        self.nowbar = nowbar
        self.pokemon02 = pokemon02
        self.pokemon01 = pokemon01
        self.statebar = statebar
        self.statebar01 = statebar01
        self.healthbar = healthbar
        self.healthbar01 = healthbar01

    def update(self):
        # 菜单切换时，改变pointer的初始位置
        self.rect.topleft = self.nowbar.initPointer

    def moveUp(self):
        if self.rect.y > 230:
            self.rect.y = 228
            self.flag -=2
            gf.update_screen(self.p_setting, self.screen, self.nowbar,
                             None, self.pokemon02,  self.pokemon01,
                             self.statebar, self.statebar01,
                             self.healthbar, self.healthbar01,
                             self.nowbar, self)
            # 这里nowbar传入的是skillbar,但因为menubarText = None所以没有报错


    def moveDown(self):
        if self.rect.y < 230:
            self.rect.y = 260
            self.flag +=2
            gf.update_screen(self.p_setting, self.screen, self.nowbar,
                             None, self.pokemon02,  self.pokemon01,
                             self.statebar, self.statebar01,
                             self.healthbar, self.healthbar01,
                             self.nowbar, self)
            # 这里nowbar传入的是skillbar,但因为menubarText = None所以没有报错


    def moveLeft(self):
        if self.rect.x > 20:
            self.rect.x = 11
            self.flag -= 1
            gf.update_screen(self.p_setting, self.screen, self.nowbar,
                             None, self.pokemon02,  self.pokemon01,
                             self.statebar, self.statebar01,
                             self.healthbar, self.healthbar01,
                             self.nowbar, self)
            # 这里nowbar传入的是skillbar,但因为menubarText = None所以没有报错


    def moveRight(self):
        if self.rect.x < 20:
            self.rect.x = 170
            self.flag += 1
            gf.update_screen(self.p_setting, self.screen, self.nowbar,
                             None, self.pokemon02, self.pokemon01,
                             self.statebar, self.statebar01,
                             self.healthbar, self.healthbar01,
                             self.nowbar, self)
            # 这里nowbar传入的是skillbar,但因为menubarText = None所以没有报错


    def blitme(self):
        self.screen.blit(self.image, self.rect)



class SelectionPointer():
    def __init__(self, p_setting, screen):
        self.p_setting = p_setting
        self.screen = screen
        self.image = pygame.image.load("../othersource/Pic/pointerUp.png")
        self.rect = self.image.get_rect()
        self.flag = 0
        self.rect.topleft=(82, 110)
    def moveUp(self):
        if self.rect.y>110:
            self.rect.y -= 81
            self.flag -= 4

    def moveDown(self):
        if self.rect.y < 205:
            self.rect.y += 81
            self.flag += 4

    def moveLeft(self):
        if self.rect.x > 82:
            self.rect.x -= 124
            self.flag -= 1

    def moveRight(self):
        if self.rect.x < 454:
            self.rect.x += 124
            self.flag += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
