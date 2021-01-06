import pygame
import game_functions as gf
import random
from skillImage import SkillImage


class Knock(object):
    def __init__(self, p_setting, screen, menubar):
        self.p_setting = p_setting
        self.screen = screen
        self.menubar = menubar

        self.name = "撞击"
        self.attribute = '普通'
        self.damage = 20
        self.skillType = 0
        self.maxPP = 25
        self.nowPP = 25
        self.num = 0

        self.pokemon = None
        self.target = None

    def knockMove(self):
        if self.pokemon.label == 1:
            self.pokemon.leftMove(1, 20)
            pygame.time.delay(500)
            self.pokemon.rightMove(2, 50)
            pygame.time.delay(500)
            self.pokemon.leftMove(1, 30)
        else:
            self.pokemon.rightMove(1, 20)
            pygame.time.delay(500)
            self.pokemon.leftMove(2, 50)
            pygame.time.delay(500)
            self.pokemon.rightMove(1, 30)

    def use(self):
        self.knockMove()
        self.target.attackedMove()
        self.nowPP -= 1
        self.target.health -= self.pokemon.attack * \
            (1 + self.damage / 100) * \
            (1 - (self.target.defence / (100+self.target.defence)))
        self.target.health = round(self.target.health, 2)


class ShadowBall(object):
    def __init__(self, p_setting, screen, menubar):
        self.p_setting = p_setting
        self.screen = screen
        self.menubar = menubar

        self.name = "影子球"
        self.attribute = '暗'
        self.damage = 20
        self.skillType = 0
        self.maxPP = 15
        self.nowPP = 15
        self.num = 1

        self.pokemon = None
        self.target = None

        self.skillImage = SkillImage(pygame.image.load(
            "../othersource/SkillsImage/ShadowBall.png"), 150, 140, p_setting,
            screen)


    def shadowBallMove(self):
        if self.pokemon.label == 1:
            self.skillImage.rect_x = 150
            self.skillImage.rect_y = 140
            self.pokemon.leftMove(1, 20)
            pygame.time.delay(200)
            for i in range(25):
                self.pokemon.rightMove(2, 2)
                self.skillImage.rect_x += 2
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
                # 这里nowbar = menubar
            while(self.skillImage.rect_x <= 300
                  or self.skillImage.rect_y >= 57):
                self.skillImage.rect_x += 1.5
                self.skillImage.rect_y -= 1
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
                # 这里nowbar = menubar
            pygame.time.delay(300)
            self.pokemon.leftMove(1, 30)
            self.skillImage.rect_x = 150
            self.skillImage.rect_y = 140
        else:
            self.skillImage.rect_x = 300
            self.skillImage.rect_y = 57
            self.pokemon.rightMove(1, 20)
            pygame.time.delay(200)
            for i in range(25):
                self.pokemon.leftMove(2, 2)
                self.skillImage.rect_x -= 2
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
                # 这里nowbar = menubar
            while(self.skillImage.rect_x >= 150
                  or self.skillImage.rect_y <= 140):
                self.skillImage.rect_x -= 1.5
                self.skillImage.rect_y += 1
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
                # 这里nowbar = menubar
            pygame.time.delay(300)
            self.pokemon.rightMove(1, 30)
            self.skillImage.rect_x = 300
            self.skillImage.rect_y = 57

    def use(self):
        self.shadowBallMove()
        self.target.attackedMove()
        self.nowPP -= 1
        self.target.health -= self.pokemon.attack * \
            (1 + self.damage / 100) * \
            (1 - (self.target.defence / (100+self.target.defence)))
        self.target.health = round(self.target.health, 2)


class Powerup(object):
    def __init__(self, p_setting, screen, menubar):
        self.p_setting = p_setting
        self.screen = screen
        self.menubar = menubar

        self.name = "力量提升"
        self.attribute = '格斗'
        self.damage = 0
        self.skillType = 1
        self.maxPP = 15
        self.nowPP = 15
        self.num = 2

        self.pokemon = None
        self.target = None


    def powerupMove(self):
        m = 1           # 存储图像缩放倍数
        temp_image = self.pokemon.image         # 存初始大小的图像
        for i in range(20):
            m *= 1.01
            self.pokemon.image = pygame.transform.rotozoom(temp_image, 0, m)
            gf.update_screen(self.p_setting, self.screen, self.menubar,
                             None, self.target, self.pokemon, self.menubar)
            # 这里nowbar = menubar
        pygame.time.delay(500)
        for i in range(20):
            m /= 1.01
            self.pokemon.image = pygame.transform.rotozoom(
                temp_image, 0, m)
            gf.update_screen(self.p_setting, self.screen, self.menubar,
                             None, self.target, self.pokemon, self.menubar)
            # 这里nowbar = menubar
        self.pokemon.image = temp_image

    def use(self):
        self.powerupMove()
        self.nowPP -= 1
        if self.pokemon.attack < self.pokemon.level * 5:
            self.pokemon.attack *= 2.5
        if self.pokemon.defence < self.pokemon.level * 5:
            self.pokemon.defence *= 1.4


class Lightning(object):
    def __init__(self, p_setting, screen, menubar):
        self.p_setting = p_setting
        self.screen = screen
        self.menubar = menubar

        self.name = "雷击"
        self.attribute = '电'
        self.damage = 60
        self.skillType = 0
        self.maxPP = 10
        self.nowPP = 10
        self.num = 1

        self.pokemon = None
        self.target = None

        self.skillImage = SkillImage(pygame.image.load(
            "../othersource/SkillsImage/lightning/lightning01.png"), 150, 130,
            p_setting, screen)



    def lightningMove(self):
        if self.pokemon.label == 1:
            self.skillImage.rect_x = 330
            self.skillImage.rect_y = 35
            for i in range(180):
                self.skillImage.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//20)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
        else:
            self.skillImage.rect_x = 150
            self.skillImage.rect_y = 120
            for i in range(180):
                self.skillImage.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//20)+1)+".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)

    def use(self):
        self.lightningMove()
        self.target.attackedMove()
        self.nowPP -= 1
        self.target.health -= self.pokemon.attack * \
            (1 + self.damage / 100) * \
            (1 - (self.target.defence / (100+self.target.defence)))
        self.target.health = round(self.target.health, 2)


class FireBeam(object):
    def __init__(self, p_setting, screen, menubar):
        self.p_setting = p_setting
        self.screen = screen
        self.menubar = menubar

        self.name = "大字爆"
        self.attribute = '火'
        self.damage = 125
        self.skillType = 0
        self.maxPP = 5
        self.nowPP = 5
        self.num = 1

        self.pokemon = None
        self.target = None

        self.skillImage = SkillImage(pygame.image.load(
            "../othersource/SkillsImage/fireBeam/fireBeam01.png"), 150, 130,
            p_setting, screen)


    def fireBeamMove(self):
        if self.pokemon.label == 1:
            self.skillImage.rect_x = 150
            self.skillImage.rect_y = 30
            for i in range(60):
                self.skillImage.image = pygame.image.load(
                    "../othersource/SkillsImage/fireBeam/fireBeam0"
                    + str((i//10)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
            self.skillImage.rect_x = 270
            self.skillImage.rect_y = -15
            gf.update_screen(self.p_setting, self.screen, self.menubar,
                             None, self.target,
                             self.pokemon, self.menubar)
            pygame.time.delay(500)
            for i in range(40):
                self.skillImage.image = pygame.image.load(
                    "../othersource/SkillsImage/fireBeam/fireBeam00"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
            for i in range(40):
                self.skillImage.image = pygame.image.load(
                    "../othersource/SkillsImage/fireBeam/fireBeam00"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
            for i in range(40):
                self.skillImage.image = pygame.image.load(
                    "../othersource/SkillsImage/fireBeam/fireBeam00"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
            for i in range(40):
                self.skillImage.image = pygame.image.load(
                    "../othersource/SkillsImage/fireBeam/fireBeam00"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
        else:
            self.skillImage.rect_x = 150
            self.skillImage.rect_y = 30
            for i in range(60):
                self.skillImage.image = pygame.image.load(
                    "../othersource/SkillsImage/fireBeam/fireBeam1"
                    + str((i//10)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
            self.skillImage.rect_x = 50
            self.skillImage.rect_y = 50
            gf.update_screen(self.p_setting, self.screen, self.menubar,
                             None, self.target,
                             self.pokemon, self.menubar)
            pygame.time.delay(500)
            for i in range(40):
                self.skillImage.image = pygame.image.load(
                    "../othersource/SkillsImage/fireBeam/fireBeam00"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
            for i in range(40):
                self.skillImage.image = pygame.image.load(
                    "../othersource/SkillsImage/fireBeam/fireBeam00"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
            for i in range(40):
                self.skillImage.image = pygame.image.load(
                    "../othersource/SkillsImage/fireBeam/fireBeam00"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
            for i in range(40):
                self.skillImage.image = pygame.image.load(
                    "../othersource/SkillsImage/fireBeam/fireBeam00"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)

    def use(self):
        self.fireBeamMove()
        self.target.attackedMove()
        self.nowPP -= 1
        self.target.health -= self.pokemon.attack * \
            (1 + self.damage / 100) * \
            (1 - (self.target.defence / (100+self.target.defence)))
        self.target.health = round(self.target.health, 2)


class Kirin(object):
    def __init__(self, p_setting, screen, menubar):
        self.p_setting = p_setting
        self.screen = screen
        self.menubar = menubar

        self.name = "麒麟"
        self.attribute = '电'
        self.damage = 150
        self.skillType = 0
        self.maxPP = 5
        self.nowPP = 5
        self.num = 1

        self.pokemon = None
        self.target = None

        self.skillImage01 = SkillImage(pygame.image.load(
            "../othersource/SkillsImage/kirin/bkg01.png"), 0, 0,
            p_setting, screen)
        self.skillImage02 = SkillImage(pygame.image.load(
            "../othersource/SkillsImage/kirin/bkg01.png"), 0, 0,
            p_setting, screen)


    def kirinMove(self):
        self.skillImage01.rect_x = 0
        self.skillImage01.rect_y = 0
        for i in range(90):
            self.skillImage01.image = pygame.image.load(
                "../othersource/SkillsImage/kirin/bkg0"
                + str((i//10)+1) + ".png")
            gf.update_screen(self.p_setting, self.screen, self.menubar,
                             None, self.skillImage01, self.target,
                             self.pokemon, self.menubar)
        if self.pokemon.label == 2:
            for i in range(90):
                self.skillImage02.rect_x = 100
                self.skillImage02.rect_y = 120
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//10)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)
            for i in range(90):
                self.skillImage02.rect_x = 200
                self.skillImage02.rect_y = 120
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//10)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)
            for i in range(72):
                self.skillImage02.rect_x = 150
                self.skillImage02.rect_y = 120
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)
            for i in range(72):
                self.skillImage02.rect_x = 150
                self.skillImage02.rect_y = 120
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)
            for i in range(72):
                self.skillImage02.rect_x = 150
                self.skillImage02.rect_y = 120
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)
            for i in range(72):
                self.skillImage02.rect_x = 150
                self.skillImage02.rect_y = 120
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)
        else:
            for i in range(90):
                self.skillImage02.rect_x = 310
                self.skillImage02.rect_y = 35
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//10)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)
            for i in range(90):
                self.skillImage02.rect_x = 380
                self.skillImage02.rect_y = 35
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//10)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)
            for i in range(72):
                self.skillImage02.rect_x = 340
                self.skillImage02.rect_y = 35
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)
            for i in range(72):
                self.skillImage02.rect_x = 340
                self.skillImage02.rect_y = 35
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)
            for i in range(72):
                self.skillImage02.rect_x = 340
                self.skillImage02.rect_y = 35
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)
            for i in range(72):
                self.skillImage02.rect_x = 340
                self.skillImage02.rect_y = 35
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/lightning/lightning0"
                    + str((i//8)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)

    def use(self):
        self.kirinMove()
        self.target.attackedMove()
        self.nowPP -= 1
        self.target.health -= self.pokemon.attack * \
            (1 + self.damage / 100) * \
            (1 - (self.target.defence / (100+self.target.defence)))
        self.target.health = round(self.target.health, 2)


class Tsunami(object):
    def __init__(self, p_setting, screen, menubar):
        self.p_setting = p_setting
        self.screen = screen
        self.menubar = menubar

        self.name = "海啸"
        self.attribute = '水'
        self.damage = 100
        self.skillType = 0
        self.maxPP = 5
        self.nowPP = 5
        self.num = 1

        self.pokemon = None
        self.target = None

        self.skillImage = SkillImage(pygame.image.load(
            "../othersource/SkillsImage/Tsunami01.png"), 0, 0,
            p_setting, screen)


    def tsunamiMove(self):
        if self.pokemon.label == 1:
            self.skillImage.rect_x = -20
            self.skillImage.rect_y = 0
            for i in range(100):
                self.skillImage.rect_x += 1
                self.skillImage.rect_y -= 1
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)
        else:
            self.skillImage.image = pygame.image.load(
                "../othersource/SkillsImage/Tsunami02.png")
            self.skillImage.rect_x = 20
            self.skillImage.rect_y = -100
            for i in range(100):
                self.skillImage.rect_x -= 1
                self.skillImage.rect_y += 1
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None, self.target, self.skillImage,
                                 self.pokemon, self.menubar)

    def use(self):
        self.tsunamiMove()
        self.target.attackedMove()
        self.nowPP -= 1
        self.target.health -= self.pokemon.attack * \
            (1 + self.damage / 100) * \
            (1 - (self.target.defence / (100+self.target.defence)))
        self.target.health = round(self.target.health, 2)


class Hypnotism(object):
    def __init__(self, p_setting, screen, menubar):
        self.p_setting = p_setting
        self.screen = screen
        self.menubar = menubar

        self.name = "催眠术"
        self.attribute = '超能'
        self.damage = 0
        self.skillType = 0
        self.maxPP = 15
        self.nowPP = 15
        self.num = 1

        self.pokemon = None
        self.target = None

        self.skillImage01 = SkillImage(pygame.image.load(
            "../othersource/SkillsImage/hypnotism/bkg01.png"), 0, 0,
            p_setting, screen)
        self.skillImage02 = SkillImage(pygame.image.load(
            "../othersource/SkillsImage/hypnotism/bkg01.png"), 0, 0,
            p_setting, screen)

    def hypnotismMove(self):
        self.skillImage01.rect_x = 0
        self.skillImage01.rect_y = 0
        for i in range(90):
            self.skillImage01.image = pygame.image.load(
                "../othersource/SkillsImage/hypnotism/bkg0"
                + str((i//10)+1) + ".png")
            gf.update_screen(self.p_setting, self.screen, self.menubar,
                             None, self.skillImage01, self.target,
                             self.pokemon, self.menubar)
        if self.pokemon.label == 1:
            for i in range(40):
                self.skillImage02.rect_x = 0
                self.skillImage02.rect_y = 0
                self.skillImage02.image = pygame.image.load(
                    "../othersource/SkillsImage/hypnotism/Hypnotism0"
                    + str((i//10)+1) + ".png")
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)
            while(self.skillImage02.rect_x <= 150
                  or self.skillImage02.rect_y >= -100):
                self.skillImage02.rect_x += 1.5
                self.skillImage02.rect_y -= 1
                gf.update_screen(self.p_setting, self.screen, self.menubar,
                                 None,  self.skillImage01, self.target, self.skillImage02,
                                 self.pokemon, self.menubar)

    def use(self):
        i = random.randint(0, 9)
        if i < 7:
            self.hypnotismMove()
            self.target.attackedMove()
            self.target.state = -2
            self.nowPP -= 1
        else:
            self.pokemon.state = 1
            self.nowPP -= 1