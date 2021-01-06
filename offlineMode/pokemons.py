import pygame
import game_functions as gf


class Pokemon(pygame.sprite.Sprite):
    def __init__(self, p_setting, screen, clock, menubar, image_path, miniImage_path, label, name,
                 health, maxHealth, attack, defence, speed, skills, level,
                 rect_x=0, rect_y=0, state=0):
        super().__init__()
        self.image = pygame.image.load(image_path)
        if miniImage_path:
            self.miniImage = pygame.image.load(miniImage_path)      #查看pokemon界面的头像
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
            gf.update_screen(self.p_setting, self.screen, self.menubar, None, self.clock, 
                             self.target, self, self.menubar)
            # 这里的nowbar是menubar

    def rightMove(self, move_speed, move_len):
        while move_len > 0:
            self.rect.x += move_speed
            move_len -= move_speed
            gf.update_screen(self.p_setting, self.screen, self.menubar, None, self.clock, 
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
            skill.nowPP=skill.maxPP


class Pokemons():
    # 玩家所持的pokemons     类似玩家的宠物背包
    def __init__(self, myPokemon01s):
        self.myPokemon01s = myPokemon01s        #列表
        self.skills = []                        #玩家pokemon的所有技能
        self.updateSkills()

    def updateSkills(self):
        for pokemon in self.myPokemon01s:
            self.skills.extend(pokemon.skills)
        self.skills = list(set(self.skills))

    def allFailed(self):
        # 查看是否玩家的所有pokemon都死了
        for pokemon in self.myPokemon01s:
            if pokemon.alive:
                return False
        return True

    # def useHpBuff(self):
    #     for pokemon in self.myPokemon01s:
    #         pokemon.maxHealth = int(pokemon.maxHealth*0.05)
    # def useAttBuff(self):
    #     for pokemon in self.myPokemon01s:
    #         pokemon.normalAtt = int(pokemon.normalAtt*0.05)