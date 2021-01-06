import pygame
import game_functions as gf


class Menubar():
    def __init__(self, p_setting, screen):
        self.image = pygame.image.load("../othersource/Pic/fightMenu01.png")
        self.rect = self.image.get_rect()
        self.rect.x = -500
        self.rect.y = 215
        self.p_setting = p_setting
        self.textPos = self.p_setting.menubarTextPos
        self.fontSize = self.p_setting.menubarFontSize
        self.textColor = self.p_setting.menubarTextColor
        self.screen = screen
        self.initPointer = self.p_setting.menubarInitPointer

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def draw_text(self, text):
        # 在 menubar 上绘制文本
        gf.draw_text(self.screen, self.p_setting.mainFont,
                     self.fontSize, text, self.textPos, self.textColor)
