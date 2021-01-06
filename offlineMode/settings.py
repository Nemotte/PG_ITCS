import pygame


class Setting():
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 304
        self.screen_bg = pygame.image.load("../othersource/Pic/background01.png")
        self.selection_bg = pygame.image.load("../othersource/Pic/selection_bg.png")
        self.selection = [pygame.image.load("../othersource/Pic/selection_01.jpg"), pygame.image.load("../othersource/Pic/selection_02.jpg"), pygame.image.load(
            "../othersource/Pic/selection_03.jpg"), pygame.image.load("../othersource/Pic/selection_04.jpg"), pygame.image.load("../othersource/Pic/selection_05.jpg")]
        self.mode_bg = pygame.image.load("../othersource/Pic/select_mode.jpg")
        self.loadingPage = pygame.image.load("../othersource/Pic/loadingPage.png")
        self.loadPage = [pygame.image.load("../othersource/Pic/loadingPage01.png"), pygame.image.load("../othersource/Pic/loadingPage02.png"), pygame.image.load(
            "../othersource/Pic/loadingPage03.png"), pygame.image.load("../othersource/Pic/loadingPage04.png"), pygame.image.load("../othersource/Pic/loadingPage05.png"), ]

        self.mainFont = "../othersource/font/SiYuanMedium.otf"

        self.menubarTextPos = (41, 232)             # 记录menubar上文字 左上角坐标
        self.menubarFontSize = 16                   # 记录menubar上 文字大小
        self.menubarTextColor = (255, 255, 255)     # 记录menubar上 文字颜色

        self.statebarNamePos = (31, 31)             # 记录statebar上 名字  左上角坐标
        self.statebarLvPos = (178, 29)              # 记录statebar上 等级  左上角坐标
        self.statebarFontSize = 18                  # 记录statebar上 文字大小
        self.statebarTextColor = (100, 100, 100)    # 记录statebar上 文字颜色

        self.statebar01NamePos = (278, 151)         # 记录statebar01上 名字  左上角坐标
        self.statebar01LvPos = (430, 151)           # 记录statebar01上 等级  左上角坐标
        self.statebar01HealthPos = (383, 193)       # 记录statebar01上 血量  左上角坐标
        self.statebar01FontSize = 18                # 记录statebar01上 文字大小
        self.statebar01TextColor = (100, 100, 100)  # 记录statebar上 文字颜色

        self.skillbarTypePos = (410, 265)           # 记录skillbar上 属性  左上角坐标
        self.skillbarNamePos0 = (37, 236)            # 记录skillbar上 技能0名字  左上角坐标
        # 记录skillbar上 技能1名字  左上角坐标
        self.skillbarNamePos1 = (200, 236)
        self.skillbarNamePos2 = (37, 265)           # 记录skillbar上 技能2名字  左上角坐标
        self.skillbarNamePos3 = (200, 265)           # 记录skillbar上 技能3名字  左上角坐标

        self.skillbarPpPos = (379, 235)             # 记录skillbar上 PP  左上角坐标
        self.skillbarFontSize = 20                  # 记录skillbar上 文字大小
        self.skillbarTextColor = (100, 100, 100)    # 记录skillbar上 文字颜色

        self.healthbar01Pos = (315, 175)            # 记录 我方宠物血条 左上角坐标
        self.healthbarPos = (53, 50)                # 记录 敌方宠物血条 左上角坐标

        # 记录 menubar上pointer 的初始 左上角坐标
        self.menubarInitPointer = (295, 228)
        # 记录 skillbar上pointer 的初始 左上角坐标
        self.skillbarInitPointer = (11, 228)
