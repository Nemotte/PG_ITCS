import pygame
import game_functions as gf


class Statebar():
    def __init__(self, p_setting, screen, pokemon):
        self.image = pygame.image.load("../othersource/Pic/stateBar.png")
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        self.screen = screen
        self.p_setting = p_setting
        # 状态栏上显示当前 野生pokemon 的信息
        self.pokemon = pokemon
        # 记录statebar上 名字 的 左上角 坐标
        self.namePos = self.p_setting.statebarNamePos
        # 记录statebar上 等级 的 左上角 坐标
        self.lvPos = self.p_setting.statebarLvPos
        # 记录statebar上 文字大小
        self.fontSize = self.p_setting.statebarFontSize
        # 记录statebar上 文字颜色
        self.textColor = self.p_setting.statebarTextColor

    def blitme(self):
        # 绘制 野生pokemon的 状态栏
        self.screen.blit(self.image, self.rect)
        # 绘制 野生pokemon的 名字
        gf.draw_text(self.screen, self.p_setting.mainFont, self.fontSize,
                     self.pokemon.name, self.namePos, self.textColor)
        # 绘制 野生pokemon的 等级
        gf.draw_text(self.screen, self.p_setting.mainFont, self.fontSize, "LV "
                     + str(self.pokemon.level), self.lvPos, self.textColor)


class Statebar01():
    def __init__(self, p_setting, screen, pokemon):
        self.image = pygame.image.load("../othersource/Pic/stateBar01.png")
        self.rect = self.image.get_rect()
        self.rect.x = 270
        self.rect.y = 139
        self.screen = screen
        self.p_setting = p_setting
        # 状态栏上显示当前 我方pokemon 的信息
        self.pokemon = pokemon
        # 记录statebar上 名字 左上角坐标
        self.namePos = p_setting.statebar01NamePos
        # 记录statebar上 等级 左上角坐标
        self.lvPos = p_setting.statebar01LvPos
        # 记录statebar上 血量 左上角坐标
        self.healthPos = p_setting.statebar01HealthPos
        # 记录statebar上 文字大小
        self.fontSize = p_setting.statebar01FontSize
        # 记录statebar上 文字颜色
        self.textColor = p_setting.statebar01TextColor

    def blitme(self):
        # 绘制 我方pokemon 状态栏
        self.screen.blit(self.image, self.rect)
        # 绘制 我方pokemon的 名字
        gf.draw_text(self.screen, self.p_setting.mainFont, self.fontSize,
                     self.pokemon.name, self.namePos, self.textColor)
        # 绘制 我方pokemon的 等级
        gf.draw_text(self.screen, self.p_setting.mainFont, self.fontSize,
                     "LV " + str(self.pokemon.level), self.lvPos,
                     self.textColor)
        # 绘制 我方pokemon的 血量
        gf.draw_text(self.screen, self.p_setting.mainFont, self.fontSize, str(
            self.pokemon.health) + " / " + str(self.pokemon.maxHealth),
            self.healthPos, self.textColor)


class Healthbar():
    def __init__(self, p_setting, screen, pokemon, topleft):
        self.image = pygame.image.load("../othersource/Pic/healthBar100.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.screen = screen
        self.p_setting = p_setting
        self.pokemon = pokemon

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.pokemon.maxHealth == 0:
            healthPer = 0
            self.image = pygame.image.load(
                "../othersource/Pic/healthBar" + str(healthPer) + ".png")
            return
        healthPer = int(self.pokemon.health /
                        self.pokemon.maxHealth * 100) // 10 * 10
        if healthPer < 0:
            healthPer = 0
        self.image = pygame.image.load(
            "../othersource/Pic/healthBar" + str(healthPer) + ".png")
