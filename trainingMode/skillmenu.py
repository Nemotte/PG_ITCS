import pygame
import game_functions as gf


class Skillbar():
    skills = 0

    def __init__(self, p_setting, screen, pointer):
        self.image = pygame.image.load("../othersource/Pic/skillBar.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 215
        self.screen = screen
        self.p_setting = p_setting
        self.pointer = pointer

        # 记录skillbar上 属性 的 左上角 坐标
        self.typePos = self.p_setting.skillbarTypePos
        # 记录skillbar上 技能名字 的 左上角 坐标
        self.namePos0 = self.p_setting.skillbarNamePos0
        self.namePos1 = self.p_setting.skillbarNamePos1
        self.namePos2 = self.p_setting.skillbarNamePos2
        self.namePos3 = self.p_setting.skillbarNamePos3

        # 记录skillbar上 PP 的 左上角 坐标
        self.ppPos = self.p_setting.skillbarPpPos

        self.fontSize = self.p_setting.skillbarFontSize
        self.textColor = self.p_setting.skillbarTextColor
        self.initPointer = self.p_setting.skillbarInitPointer

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        gf.draw_text(self.screen, self.p_setting.mainFont, self.fontSize,
                     self.skills[0].name, self.namePos0, self.textColor)
        gf.draw_text(self.screen, self.p_setting.mainFont, self.fontSize,
                     self.skills[1].name, self.namePos1, self.textColor)
        gf.draw_text(self.screen, self.p_setting.mainFont, self.fontSize,
                     self.skills[2].name, self.namePos2, self.textColor)
        gf.draw_text(self.screen, self.p_setting.mainFont, self.fontSize,
                     self.skills[3].name, self.namePos3, self.textColor)

        gf.draw_text(self.screen, self.p_setting.mainFont, self.fontSize,
                     str(self.skills[self.pointer.flag].nowPP)+" / "
                     + str(self.skills[self.pointer.flag].maxPP), self.ppPos,
                     self.textColor)
        gf.draw_text(self.screen, self.p_setting.mainFont,
                     self.fontSize, self.skills[self.pointer.flag].attribute,
                     self.typePos, self.textColor)


