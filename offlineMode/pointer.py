import pygame
import game_functions as gf


class Pointer():
    # 技能选择界面的指针
    flag = 0            # pointer指向的技能

    def __init__(self, p_setting, screen, nowbar, pokemon02, pokemon01, statebar,
                 statebar01, healthbar, healthbar01, clock):
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
        self.clock = clock

    def update(self):
        # 菜单切换时，改变pointer的初始位置
        self.rect.topleft = self.nowbar.initPointer

    def moveUp(self):
        if self.rect.y > 230:
            self.rect.y = 228
            self.flag -=2
            gf.update_screen(self.p_setting, self.screen, self.nowbar,
                             None, self.clock, self.pokemon02,  self.pokemon01,
                             self.statebar, self.statebar01,
                             self.healthbar, self.healthbar01,
                             self.nowbar, self)
            # 这里nowbar传入的是skillbar,但因为menubarText = None所以没有报错


    def moveDown(self):
        if self.rect.y < 230:
            self.rect.y = 260
            self.flag +=2
            gf.update_screen(self.p_setting, self.screen, self.nowbar,
                             None, self.clock, self.pokemon02,  self.pokemon01,
                             self.statebar, self.statebar01,
                             self.healthbar, self.healthbar01,
                             self.nowbar, self)
            # 这里nowbar传入的是skillbar,但因为menubarText = None所以没有报错


    def moveLeft(self):
        if self.rect.x > 20:
            self.rect.x = 11
            self.flag -= 1
            gf.update_screen(self.p_setting, self.screen, self.nowbar,
                             None, self.clock, self.pokemon02,  self.pokemon01,
                             self.statebar, self.statebar01,
                             self.healthbar, self.healthbar01,
                             self.nowbar, self)
            # 这里nowbar传入的是skillbar,但因为menubarText = None所以没有报错


    def moveRight(self):
        if self.rect.x < 20:
            self.rect.x = 170
            self.flag += 1
            gf.update_screen(self.p_setting, self.screen, self.nowbar,
                             None, self.clock, self.pokemon02, self.pokemon01,
                             self.statebar, self.statebar01,
                             self.healthbar, self.healthbar01,
                             self.nowbar, self)
            # 这里nowbar传入的是skillbar,但因为menubarText = None所以没有报错


    def blitme(self):
        self.screen.blit(self.image, self.rect)



class SelectionPointer():
    #pokemon选择界面的指针
    def __init__(self,screen):
        # self.p_setting = p_setting
        self.screen = screen
        self.image = pygame.image.load("../othersource/Pic/pointerUp.png")
        self.rect = self.image.get_rect()
        self.flag = 0
        self.rect.topleft=(82, 200)
    # def moveUp(self):
    #     if self.rect.y>110:
    #         self.rect.y -= 81
    #         self.flag -= 4
    #
    # def moveDown(self):
    #     if self.rect.y < 205:
    #         self.rect.y += 81
    #         self.flag += 4

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

class ModePointer():
    def __init__(self, screen):
        # self.p_setting = p_setting
        self.screen = screen
        self.image = pygame.image.load("../othersource/Pic/modePointer.png")
        self.rect = self.image.get_rect()
        self.flag = 1                   # 1；单击模式    2：联机模式  3：训练场
        self.rect.topleft=(50, 87)
    def moveUp(self):
        if self.flag == 4:
            self.flag -= 1
        if self.rect.y>100:
            self.rect.y -= 65
            self.flag -= 1

    def moveDown(self):
        if self.rect.y < 205:
            self.rect.y += 65
            self.flag += 1
        elif self.rect.y < 270:
            self.flag += 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)
        if self.flag == 1:
            gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 20, "规则：", (270, 100), (200, 100, 100))
            gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "共设九关", (285, 140), (200, 100, 100))
            gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "获胜后会有金币奖励", (285, 180), (200, 100, 100))
            gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "每过三关可去商店购买buff", (285, 220), (200, 100, 100))
        elif self.flag == 2:
            gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 20, "规则：", (270, 100), (200, 100, 100))
            gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "实时双人对战", (285, 140), (200, 100, 100))
            gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "可自行选择精灵", (285, 180), (200, 100, 100))
            gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "上限为6只", (285, 220), (200, 100, 100))
        else:
            gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 20, "规则：", (270, 100), (200, 100, 100))
            gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "训练你的精灵", (300, 140), (200, 100, 100))
            gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "让ta变得更强！", (300, 180), (200, 100, 100))

class CheckPokemon01sPointer():
    # 查看pokemon界面的pointer
    def __init__(self, screen, myPokemon01s):
        self.screen = screen
        self.myPokemon01s = myPokemon01s
        self.maxFlag = len(myPokemon01s)-1
        self.flag = 0
        self.image = pygame.image.load("../othersource/Pic/pointerup2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft=(42,111)

    def moveUp(self):
        if self.rect.y>111:
            self.rect.y -= 84
            self.flag -= 2

    def moveDown(self):
        if self.rect.y < 279 and self.flag +2<=self.maxFlag:
            self.rect.y += 84
            self.flag += 2

    def moveLeft(self):
        if self.rect.x > 42:
            self.rect.x -= 88
            self.flag -= 1

    def moveRight(self):
        if self.rect.x < 130 and self.flag +1<=self.maxFlag:
            self.rect.x += 88
            self.flag += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class PrizePointer():
    # 选奖励的指针
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("../othersource/Pic/prizePointer.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (42,80) # ori=37
        self.flag = 0
    def moveLeft(self):
        if self.rect.x>20:
            self.rect.x -= 147
            self.flag -=1
    def moveRight(self):
        if self.rect.x<500:
            self.rect.x += 147
            self.flag += 1
    def blitme(self):
        self.screen.blit(self.image, self.rect)


class StorePointer():
    # 商店场景里的指针
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("../othersource/Pic/prizePointer.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (42,80) # ori=37
        self.flag = 0
    def moveLeft(self):
        if self.rect.x>20:
            self.rect.x -= 146
            self.flag -=1
    def moveRight(self):
        if self.rect.x<500:
            self.rect.x += 146
            self.flag += 1
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class PokemonPointer():
    def __init__(self,screen):
        # self.p_setting = p_setting
        self.screen = screen
        self.image = pygame.image.load("../othersource/Pic/pointer.png")
        self.rect = self.image.get_rect()
        self.flag = 0
        self.rect.topleft=(85, 150)

    def moveLeft(self):
        if self.rect.x > 85:
            self.rect.x -= 190
            self.flag -= 1

    def moveRight(self):
        if self.rect.x < 275:
            self.rect.x += 190
            self.flag += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)