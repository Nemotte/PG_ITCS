import pygame
import game_functions as gf


class Pokemon(pygame.sprite.Sprite):
    def __init__(self, p_setting, screen, clock, menubar, image_path, miniImage_path, label, name,
                 health, maxHealth, attack, defence, speed, skills, level,
                 rect_x=0, rect_y=0, state=0):
        super().__init__()
        self.image = pygame.image.load(image_path)
        if miniImage_path:
            self.miniImage = pygame.image.load(
                miniImage_path)  # 查看pokemon界面的头像
        self.rect = self.image.get_rect()
        self.label = label  # 1代表我方 0代表敌方
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.normalAtt = attack
        self.attack = attack
        self.normalDef = defence
        self.defence = defence
        self.speed = speed

        self.skills = skills  # skills 为 元组
        self.state = state
        self.level = level
        self.screen = screen
        self.p_setting = p_setting
        self.menubar = menubar
        self.target = None

        self.orderPos = (0, 0)

        self.alive = True

        self.clock = clock

    def leftMove(self, move_speed, move_len):
        while move_len > 0:
            self.rect.x -= move_speed
            move_len -= move_speed
            pygame.display.update()
            gf.update_screen(self.p_setting, self.screen, self.menubar, None,
                             self.target, self, self.menubar)
            # 这里的nowbar是menubar

    def rightMove(self, move_speed, move_len):
        while move_len > 0:
            self.rect.x += move_speed
            move_len -= move_speed
            gf.update_screen(self.p_setting, self.screen, self.menubar, None,
                             self.target, self, self.menubar)
            # 这里的nowbar是menubar

    def attackedMove(self):
        self.leftMove(2, 4)
        self.rightMove(4, 8)
        self.leftMove(4, 8)
        self.rightMove(4, 8)
        self.leftMove(4, 8)
        self.rightMove(4, 8)
        self.leftMove(4, 8)
        self.rightMove(4, 8)
        self.leftMove(1, 4)

    def damaged(self, num):
        self.health -= num

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def useSkill(self, skillNum):
        self.skills[skillNum].use()

    def initSkills(self):
        for skill in self.skills:
            skill.nowPP = skill.maxPP


class Function(Pokemon):
    def __init__(self, p_setting, screen, clock, menubar, image_path, miniImage_path, label, name,
                 health, maxHealth, attack, defence, speed, skills, level, b,
                 rect_x=0, rect_y=0, state=0):
        super().__init__(p_setting, screen, clock, menubar, image_path, miniImage_path, label, name,
                 health, maxHealth, attack, defence, speed, skills, level)
        self.image = pygame.image.load(image_path)
        if miniImage_path:
            self.miniImage = pygame.image.load(
                miniImage_path)  # 查看pokemon界面的头像
        self.rect = self.image.get_rect()
        self.label = label  # 1代表我方 0代表敌方
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.normalAtt = attack
        self.attack = attack
        self.normalDef = defence
        self.defence = defence
        self.speed = speed

        self.skills = skills  # skills 为 元组
        self.state = state
        self.level = level
        self.screen = screen
        self.p_setting = p_setting
        self.menubar = menubar
        self.target = None

        self.orderPos = (0, 0)

        self.alive = True

        self.clock = clock
        self.b = b
        self.func = 'nx^'+str(self.b)
        self.maxHealth = b

    def derive(self):
        self.b -= 1
        self.func = 'nx^'+str(self.b)
        self.health -= 1
        self.maxHealth -= 1
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf",
                     60, str(self.func), (300, 40), (200, 100, 100))
        pygame.display.update()

    def intergral(self):
        self.b += 1
        self.func = 'nx^'+str(self.b)
        self.health += 1
        self.maxHealth += 1
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf",
                     60, str(self.func), (300, 40), (200, 100, 100))
        pygame.display.update()

    def leftMove(self, move_speed, move_len):
        while move_len > 0:
            self.rect.x -= move_speed
            move_len -= move_speed
            pygame.display.update()
            gf.update_screen(self.p_setting, self.screen, self.menubar, None,
                             self.target, self, self.menubar)
            # 这里的nowbar是menubar

    def rightMove(self, move_speed, move_len):
        while move_len > 0:
            self.rect.x += move_speed
            move_len -= move_speed
            gf.update_screen(self.p_setting, self.screen, self.menubar, None,
                             self.target, self, self.menubar)
            # 这里的nowbar是menubar

    def attackedMove(self):
        self.leftMove(2, 4)
        self.rightMove(4, 8)
        self.leftMove(4, 8)
        self.rightMove(4, 8)
        self.leftMove(4, 8)
        self.rightMove(4, 8)
        self.leftMove(4, 8)
        self.rightMove(4, 8)
        self.leftMove(1, 4)

    def damaged(self, num):
        self.health -= num

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def useSkill(self, skillNum):
        self.skills[skillNum].use()

    def initSkills(self):
        for skill in self.skills:
            skill.nowPP = skill.maxPP