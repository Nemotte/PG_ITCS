import pygame
import game_functions as gf


class Pokemon(pygame.sprite.Sprite):
    def __init__(self, p_setting, screen, menubar, image_path, label, name,
                 health, maxHealth, attack, defence, speed, skills, level, variable,
                 rect_x=0, rect_y=0, state=0):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.label = label                          #1代表我方 0代表敌方
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.attack = attack
        self.defence = defence
        self.speed = speed

        self.skills = skills                    # skills 为 元组
        self.state = state
        self.level = level
        self.screen = screen
        self.p_setting = p_setting
        self.menubar = menubar
        self.target = None

        self.variable = variable

        # self.selectedOrder = 0
        self.orderPos = (0, 0)

    # def appear(self):
    #     if self.label == 0:
    #         self.rect.x = 637
    #         self.rect.y = 50

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
