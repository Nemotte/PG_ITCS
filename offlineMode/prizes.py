'''奖励类'''
import pygame
import game_functions as gf


class UpgradeHp():
    def __init__(self, screen, pokemons):
        self.image = pygame.image.load("../othersource/Pic/prizeImages/血量提升药水.png")
        self.rect = self.image.get_rect()
        self.pokemons = pokemons.myPokemon01s  # 使用buff的pokemons
        self.screen = screen
        self.isPos = True  # 是正面buff
        self.name = "血量提升药水"
        self.price = 100   # 商店中售卖价格 具体数字待定
    def useBuff(self):
        for pokemon in self.pokemons:
            pokemon.maxHealth += int(pokemon.maxHealth * 0.05)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 18, "血量提升药水",
                     (self.rect.x - 41, self.rect.y + 62), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "所有pokemon",
                     (self.rect.x - 36, self.rect.y + 90), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "血量提升5%",
                     (self.rect.x - 28, self.rect.y + 110), (74, 73, 74))
    def drawPrice(self):
        self.screen.blit(pygame.image.load("../othersource/Pic/coinSmall.png"), (self.rect.x-2, self.rect.y+135))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 10, str(self.price), (self.rect.x+8, self.rect.y+133), (74,73,74))

class UpgradeAtt():
    def __init__(self, screen, pokemons):
        self.image = pygame.image.load("../othersource/Pic/prizeImages/攻击提升药水.png")
        self.rect = self.image.get_rect()
        self.pokemons = pokemons.myPokemon01s  # 使用buff的pokemons
        self.screen = screen
        self.isPos = True  # 是正面buff
        self.name = "攻击提升药水"
        self.price = 120

    def useBuff(self):
        for pokemon in self.pokemons:
            pokemon.attack += int(pokemon.attack * 0.05)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 18, "攻击提升药水",
                     (self.rect.x - 41, self.rect.y + 62), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "所有pokemon",
                     (self.rect.x - 36, self.rect.y + 90), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "攻击提升5%",
                     (self.rect.x - 27, self.rect.y + 110), (74, 73, 74))
    def drawPrice(self):
        self.screen.blit(pygame.image.load("../othersource/Pic/coinSmall.png"), (self.rect.x-2, self.rect.y+135))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 10, str(self.price), (self.rect.x+8, self.rect.y+133), (74,73,74))

class UpgradeDam():
    def __init__(self, screen, pokemons):
        self.image = pygame.image.load("../othersource/Pic/prizeImages/技能强化药水.png")
        self.rect = self.image.get_rect()
        self.pokemons = pokemons  # 使用buff的pokemons
        self.screen = screen
        self.isPos = True  # 是正面buff
        self.name = "技能强化药水"
        self.price = 120

    def useBuff(self):
        for skill in self.pokemons.skills:
            skill.damage = int(skill.damage*1.1)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 18, "技能强化药水",
                     (self.rect.x - 40, self.rect.y + 62), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "所有pokemon技",
                     (self.rect.x-43, self.rect.y + 90), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "能威力提升10%",
                     (self.rect.x-41, self.rect.y + 110), (74, 73, 74))
    def drawPrice(self):
        self.screen.blit(pygame.image.load("../othersource/Pic/coinSmall.png"), (self.rect.x-2, self.rect.y+135))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 10, str(self.price), (self.rect.x+8, self.rect.y+133), (74,73,74))

class UpgradeDef():
    def __init__(self, screen, pokemons):
        self.image = pygame.image.load("../othersource/Pic/prizeImages/防御提升药水.png")
        self.rect = self.image.get_rect()
        self.pokemons = pokemons.myPokemon01s  # 使用buff的pokemons
        self.screen = screen
        self.isPos = True  # 是正面buff
        self.name = "防御提升药水"
        self.price = 130

    def useBuff(self):
        for pokemon in self.pokemons:
            pokemon.defence += int(pokemon.defence * 0.05)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 18, "防御提升药水",
                     (self.rect.x - 41, self.rect.y + 62), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "所有pokemon",
                     (self.rect.x -37, self.rect.y + 90), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "防御提升5%",
                     (self.rect.x - 30, self.rect.y + 110), (74, 73, 74))
    def drawPrice(self):
        self.screen.blit(pygame.image.load("../othersource/Pic/coinSmall.png"), (self.rect.x-2, self.rect.y+135))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 10, str(self.price), (self.rect.x+8, self.rect.y+133), (74,73,74))

class HealAll():
    def __init__(self, screen, pokemons):
        self.image = pygame.image.load("../othersource/Pic/prizeImages/全满药.png")
        self.rect = self.image.get_rect()
        self.pokemons = pokemons.myPokemon01s  # 使用buff的pokemons
        self.screen = screen
        self.isPos = True  # 是正面buff
        self.name = "全满药"
        self.price = 200

    def useBuff(self):
        for pokemon in self.pokemons:
            pokemon.health = pokemon.maxHealth

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 18, "全满药",
                     (self.rect.x -15, self.rect.y + 62), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "所有pokemon",
                     (self.rect.x -35, self.rect.y + 90), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "回复至满血",
                     (self.rect.x - 25, self.rect.y + 110), (74, 73, 74))
    def drawPrice(self):
        self.screen.blit(pygame.image.load("../othersource/Pic/coinSmall.png"), (self.rect.x-2, self.rect.y+135))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 10, str(self.price), (self.rect.x+8, self.rect.y+133), (74,73,74))

class UpgradeStr():
    # 强化提升
    def __init__(self, screen, skills):
        self.image = pygame.image.load("../othersource/Pic/prizeImages/强化提升药水.png")
        self.rect = self.image.get_rect()
        self.skills = skills
        self.effSkills = ['力量提升', "剑舞"]  # 该buff有效的技能
        self.screen = screen
        self.isPos = True  # 是正面buff
        self.name = "强化提升药水"
        self.price = 80

    def useBuff(self):
        for skill in self.skills:
            if skill.name in self.effSkills:
                skill.index *= 1.2

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 18, "强化提升药水",
                     (self.rect.x - 41, self.rect.y + 62), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "强化类技能",
                     (self.rect.x - 25, self.rect.y + 90), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "效果加强 5%",
                     (self.rect.x - 32, self.rect.y + 110), (74, 73, 74))
    def drawPrice(self):
        self.screen.blit(pygame.image.load("../othersource/Pic/coinSmall.png"), (self.rect.x-2, self.rect.y+135))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 10, str(self.price), (self.rect.x+8, self.rect.y+133), (74,73,74))

class DegradeHp():
    # 失血
    def __init__(self, screen, pokemons):
        self.image = pygame.image.load("../othersource/Pic/prizeImages/失血药剂.png")
        self.rect = self.image.get_rect()
        self.pokemons = pokemons  # 使用buff的pokemons
        self.screen = screen
        self.isPos = False  # 是负面buff
        self.name = "失血药剂"
        self.price = 150

    def useBuff(self):
        for pokemon in self.pokemons:
            pokemon.health -= int(pokemon.health * 0.05)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 18, "失血药剂",
                     (self.rect.x-24, self.rect.y + 62), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "下一关 Boss",
                     (self.rect.x-29, self.rect.y + 90), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "血量降低 5%",
                     (self.rect.x - 31, self.rect.y + 110), (74, 73, 74))
    def drawPrice(self):
        self.screen.blit(pygame.image.load("../othersource/Pic/coinSmall.png"), (self.rect.x-2, self.rect.y+135))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 10, str(self.price), (self.rect.x+8, self.rect.y+133), (74,73,74))

class DegradeAtt():
    # 攻击弱化
    def __init__(self, screen, pokemons):
        self.image = pygame.image.load("../othersource/Pic/prizeImages/攻击弱化药剂.png")
        self.rect = self.image.get_rect()
        self.pokemons = pokemons  # 使用buff的pokemons
        self.screen = screen
        self.isPos = False  # 是负面buff
        self.name = "攻击弱化药剂"
        self.price = 200

    def useBuff(self):
        for pokemon in self.pokemons:
            pokemon.attack -= int(pokemon.attack * 0.05)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 18, "攻击弱化药剂",
                     (self.rect.x - 42, self.rect.y + 62), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "下一关 Boss",
                     (self.rect.x - 29, self.rect.y + 90), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "攻击降低 5%",
                     (self.rect.x - 31, self.rect.y + 110), (74, 73, 74))
    def drawPrice(self):
        self.screen.blit(pygame.image.load("../othersource/Pic/coinSmall.png"), (self.rect.x-2, self.rect.y+135))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 10, str(self.price), (self.rect.x+8, self.rect.y+133), (74,73,74))


class DegradeDef():
    # 防御破除
    def __init__(self, screen, pokemons):
        self.image = pygame.image.load("../othersource/Pic/prizeImages/防御破除药剂.png")
        self.rect = self.image.get_rect()
        self.pokemons = pokemons  # 使用buff的pokemons
        self.screen = screen
        self.isPos = False  # 是负面buff
        self.name = "防御破除药剂"
        self.price = 200


    def useBuff(self):
        for pokemon in self.pokemons:
            pokemon.defence -= int(pokemon.defence * 0.05)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 18, "防御破除药剂",
                     (self.rect.x - 41, self.rect.y + 62), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "下一关 Boss",
                     (self.rect.x -30, self.rect.y + 90), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "防御降低 5%",
                     (self.rect.x -31, self.rect.y + 110), (74, 73, 74))
    def drawPrice(self):
        self.screen.blit(pygame.image.load("../othersource/Pic/coinSmall.png"), (self.rect.x-2, self.rect.y+135))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 10, str(self.price), (self.rect.x+8, self.rect.y+133), (74,73,74))

class CoinsPrize():
    # 好像不太好写，要不直接改成100金币？？
    def __init__(self, screen):
        self.image = pygame.image.load("../othersource/Pic/prizeImages/金币奖励.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        # self.coins = coins
        self.isPos = True  # 是正面buff
        self.name = "100 金币奖励"

    def useBuff(self):
        # global coins

        return 100

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 18, "金币奖励",
                     (self.rect.x - 10, self.rect.y + 62), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "恭喜获得",
                     (self.rect.x - 5, self.rect.y + 90), (74, 73, 74))
        gf.draw_text(self.screen, "../othersource/font/SiYuanMedium.otf", 15, "100 个金币",
                     (self.rect.x - 13, self.rect.y + 110), (74, 73, 74))
