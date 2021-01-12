import pygame
from pygame.sprite import Group
from pokemons import Pokemon, Pokemons
from settings import Setting
from menubar import Menubar
from pointer import Pointer, SelectionPointer, ModePointer, PokemonPointer
from skills import Knock, ShadowBall, Powerup, Lightning, FireBeam, Kirin, Tsunami, Hypnotism, Protection, FireKick, DragonClaw, SabreDance, BulletFist, Yeokrin, Waterfall, IceBeam
from statebar import Statebar, Statebar01, Healthbar
from skillmenu import Skillbar
from prizes import UpgradeHp, UpgradeAtt, UpgradeDam, UpgradeDef, HealAll, UpgradeStr, DegradeHp, DegradeAtt, DegradeDef, CoinsPrize
import game_functions as gf
import random
import sys
import os

# import socket


def mainFrameCall():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("../othersource/Music/mainFrame.mp3")
    pygame.mixer.music.play(-1, 0.0)
    screen = pygame.display.set_mode((649, 415))
    for i in range(160):
        bgImage = pygame.image.load(
            "../othersource/Pic/mainFrameBkg_"+str(i//10)+".png")
        screen.blit(bgImage, (0, 0))
        pygame.display.update()
    while True:
        flag = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    flag = 1
                    break
        if flag == 1:
            pygame.mixer.music.stop()
            break
        for i in range(140):
            bgImage = pygame.image.load(
                "../othersource/Pic/mainFrameBkg_loop"+str(i//10)+".png")
            screen.blit(bgImage, (0, 0))
            pygame.display.update()


def main():
    # mainFrameCall()
    '''
    s = socket.socket()
    s.connect(('42.192.86.230', 8712))
    print(s.recv(1024).decode(encoding='utf8'))
    state = int(s.recv(1024).decode())
    s.close()
    '''
    pygame.init()
    pygame.mixer.init()
    state = 0
    # 创建 设置 实例
    p_setting = Setting()

    clock = pygame.time.Clock()
    # 创建屏幕
    screen = pygame.display.set_mode(
        (p_setting.screen_width, p_setting.screen_height))
    # 绘制背景图像
    screen.blit(p_setting.screen_bg, (0, 0))
    # 创建菜单栏 对象
    menubar = Menubar(p_setting, screen)

    '''
    创建技能
    '''

    # 创建 撞击技能 对象（我方）
    knock01 = Knock(p_setting, screen, menubar)

    # 创建 撞击技能 对象（敌方）
    knock02 = Knock(p_setting, screen, menubar)

    # 创建 影子球技能 对象（我方）
    shadowBall01 = ShadowBall(p_setting, screen, menubar)

    # 创建 影子球技能 对象（敌方）
    shadowBall02 = ShadowBall(p_setting, screen, menubar)

    # 创建 力量提升技能 对象（我方）
    powerup01 = Powerup(p_setting, screen, menubar)

    # 创建 力量提升技能 对象（敌方）
    powerup02 = Powerup(p_setting, screen, menubar)

    # 创建 雷击技能 对象（我方）
    lightning01 = Lightning(p_setting, screen, menubar)

    # 创建 雷击技能 对象（敌方）
    lightning02 = Lightning(p_setting, screen, menubar)

    # 创建 大字爆技能 对象（我方）
    fireBeam01 = FireBeam(p_setting, screen, menubar)

    # 创建 大字爆技能 对象（敌方）
    fireBeam02 = FireBeam(p_setting, screen, menubar)

    # 创建 麒麟技能 对象（我方）
    kirin01 = Kirin(p_setting, screen, menubar)

    # 创建 麒麟技能 对象（敌方）
    kirin02 = Kirin(p_setting, screen, menubar)

    # 创建 海啸技能 对象（我方）
    tsunami01 = Tsunami(p_setting, screen, menubar)

    # 创建 海啸技能 对象（敌方）
    tsunami02 = Tsunami(p_setting, screen, menubar)

    # 创建 催眠术技能 对象（我方）
    hypnotism01 = Hypnotism(p_setting, screen, menubar)

    # 创建 保护技能 对象（我方）
    protection01 = Protection(p_setting, screen, menubar)

    # 创建 保护技能 对象（敌方）
    protection02 = Protection(p_setting, screen, menubar)

    # 创建 火焰踢技能 对象（我方）
    fireKick01 = FireKick(p_setting, screen, menubar)

    # 创建 火焰踢技能 对象（敌方）
    fireKick02 = FireKick(p_setting, screen, menubar)

    # 创建 龙之爪技能 对象（我方）
    dragonClaw01 = DragonClaw(p_setting, screen, menubar)

    # 创建 龙之爪技能 对象（敌方）
    dragonClaw02 = DragonClaw(p_setting, screen, menubar)

    # 创建 剑舞技能 对象（我方）
    sabreDance01 = SabreDance(p_setting, screen, menubar)

    # 创建 剑舞技能 对象（敌方）
    sabreDance02 = SabreDance(p_setting, screen, menubar)

    # 创建 子弹拳技能 对象（我方）
    bulletFist01 = BulletFist(p_setting, screen, menubar)

    # 创建 子弹拳技能 对象（敌方）
    bulletFist02 = BulletFist(p_setting, screen, menubar)

    # 创建 逆鳞技能 对象（我方）
    yeokrin01 = Yeokrin(p_setting, screen, menubar)

    # 创建 逆鳞技能 对象（敌方）
    yeokrin02 = Yeokrin(p_setting, screen, menubar)

    # 创建 攀瀑技能 对象（我方）
    waterfall01 = Waterfall(p_setting, screen, menubar)

    # 创建 攀瀑技能 对象（敌方）
    waterfall02 = Waterfall(p_setting, screen, menubar)

    # 创建 急冻光束技能 对象（我方）
    iceBeam01 = IceBeam(p_setting, screen, menubar)

    # 创建 急冻光束技能 对象（敌方）
    iceBeam02 = IceBeam(p_setting, screen, menubar)


    '''
    蛇纹熊初始化  0
    '''
    # 创建 我方蛇纹熊
    Zigzagoon01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Zigzagoon01.png", "../othersource/Pic/headPortraits/Zigzagoon01.png",
                          1, '蛇纹熊', 50, 100, 20, 20, 50, 0, 20, 70, 118)
    Zigzagoon01.orderPos = (50, 110)

    # 创建 野生蛇纹熊
    Zigzagoon02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Zigzagoon02.png", None,  2, '蛇纹熊',
                          200, 200, 50, 50, 50, 0, 20, 637, 50)

    # 创建 技能组 对象
    Zigzagoon01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Zigzagoon02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    裂空座初始化  1
    '''
    # 创建 我方裂空座
    Rayquaza01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Rayquaza01.png", "../othersource/Pic/headPortraits/Rayquaza01.png", 1, '裂空座',
                         400, 400, 150, 100, 150, 0, 60, 70, 80)
    Rayquaza01.orderPos = (174, 110)

    # 创建 野生裂空座
    Rayquaza02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Rayquaza02.png", None,  2, '裂空座',
                         900, 900, 160, 107, 150, 0, 70, 637, 10)

    # 创建 技能组 对象
    Rayquaza01.skills = (dragonClaw01, sabreDance01, yeokrin01, kirin01)
    Rayquaza02.skills = (dragonClaw02, sabreDance02, yeokrin02, kirin02)

    '''
    裂空座初始化结束
    '''

    '''
    火鸡战士初始化 2
    '''
    # 创建 我方火鸡战士
    Blaziken01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Blaziken01.png", "../othersource/Pic/headPortraits/Blaziken01.png", 1, '火鸡战士',
                         400, 400, 128, 83, 150, 0, 50, 60, 80)
    Blaziken01.orderPos = (298, 110)

    # 创建 野生火鸡战士（未作为BOSS）
    Blaziken02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Blaziken02.png", None,  2, '火鸡战士',
                         400, 400, 120, 100, 150, 0, 20, 637, 10)

    # 创建 技能组 对象
    Blaziken01.skills = (protection01, fireKick01, powerup01, fireBeam01)
    Blaziken02.skills = (protection02, fireKick02, powerup02, fireBeam02)

    '''
    火鸡战士初始化结束
    '''

    '''
    炎帝初始化   
    '''
    # 创建 野生炎帝
    Entei02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Entei02.png", None,  2, '炎帝',
                      400, 400, 122, 101, 150, 0, 80, 637, 10)

    # # 创建 我方炎帝     无图
    # Entei01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Entei01.png", 1, '炎帝',
    #                      400, 400, 120, 100, 150, 0, 20, 70, 80)

    # 创建 技能组 对象
    # Entei01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Entei02.skills = (protection02, fireKick02, powerup02, fireBeam02)

    '''
    炎帝初始化结束
    '''

    '''
    灾兽初始化   
    '''
    # 创建 野生灾兽
    Absol02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Absol02.png", None,  2, '灾兽',
                      400, 400, 128, 71, 150, 0, 20, 637, 10)

    # # 创建 我方灾兽     无图
    # Absol01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Absol01.png", 1, '灾兽',
    #                      400, 400, 120, 100, 150, 0, 20, 70, 80)

    # 创建 技能组 对象
    # Absol01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Absol02.skills = (sabreDance02, shadowBall02, iceBeam02, kirin02)

    '''
    灾兽初始化结束
    '''

    '''
    闪电鸟初始化  3
    '''
    # 创建 我方闪电鸟
    Zapdos01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Zapdos01.png", "../othersource/Pic/headPortraits/Zapdos01.png", 1, '闪电鸟',
                       400, 400, 120, 100, 150, 0, 20, 70, 80)
    Zapdos01.orderPos = (422, 110)

    # 创建 野生闪电鸟
    Zapdos02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Zapdos02.png", None,  2, '闪电鸟',
                       400, 400, 122, 101, 150, 0, 80, 637, 10)

    # 创建 技能组 对象
    Zapdos01.skills = (kirin01, fireBeam01, powerup01, lightning01)
    Zapdos02.skills = (kirin02, fireBeam02, powerup02, lightning02)

    '''
    闪电鸟初始化结束
    '''

    '''
    巨钳螳螂初始化 4
    '''
    # 创建 我方巨钳螳螂
    Scizor01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Scizor01.png",  "../othersource/Pic/headPortraits/Scizor01.png", 1, '巨钳螳螂',
                       400, 400, 140, 133, 150, 0, 50, 70, 80)
    Scizor01.orderPos = (50, 191)

    # 创建 野生巨钳螳螂
    Scizor02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Scizor02.png",  None, 2, '巨钳螳螂',
                       400, 400, 120, 100, 150, 0, 20, 637, 10)

    # 创建 技能组 对象
    Scizor01.skills = (sabreDance01, bulletFist01, iceBeam01, fireKick01)
    Scizor02.skills = (sabreDance02, bulletFist02, iceBeam02, fireKick02)

    '''
    巨钳螳螂初始化结束
    '''

    '''
    九尾初始化   
    '''
    # 创建 野生九尾
    Ninetails02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Ninetails02.png", None,  2, '九尾',
                          400, 400, 80, 89, 150, 0, 80, 637, 10)

    # # 创建 我方九尾     无图
    # Ninetails01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Ninetails01.png", 1, '九尾',
    #                      400, 400, 120, 100, 150, 0, 20, 70, 80)

    # 创建 技能组 对象
    # Ninetails01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Ninetails02.skills = (protection02, fireBeam02, powerup02, fireKick02)

    '''
    九尾初始化结束
    '''

    '''
    超梦初始化   
    '''
    # 创建 野生超梦
    Mewtwo02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Mewtwo02.png",  None, 2, '超梦',
                       4000, 4000, 181, 101, 150, 0, 100, 637, 10)

    # # 创建 我方超梦 无图
    # Mewtwo01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Mewtwo01.png", 1, '超梦',
    #                      400, 400, 120, 100, 150, 0, 20, 70, 80)

    # 创建 技能组 对象
    # Mewtwo01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Mewtwo02.skills = (kirin02, shadowBall02, iceBeam02, tsunami02)

    '''
    超梦初始化结束
    '''

    '''
    鲤鱼王初始化  
    '''
    # 创建 野生鲤鱼王
    Magikarp02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Magikarp02.png", None,  2, '鲤鱼王',
                         400, 400, 120, 100, 150, 0, 20, 637, 10)

    # # 创建 我方鲤鱼王    无图
    # Magikarp01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Magikarp01.png", 1, '鲤鱼王',
    #                      400, 400, 120, 100, 150, 0, 20, 70, 80)

    # 创建 技能组 对象
    # Magikarp01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Magikarp02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    鲤鱼王初始化结束
    '''

    ''' 
    暴鲤龙初始化  5
    '''
    # 创建 我方暴鲤龙
    Gyarados01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Gyarados01.png", "../othersource/Pic/headPortraits/Gyarados01.png", 1, '暴鲤龙',
                         400, 400, 110, 96, 150, 0, 20, 70, 80)
    Gyarados01.orderPos = (174, 191)

    # 创建 野生暴鲤龙
    Gyarados02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Gyarados02.png",  None, 2, '暴鲤龙',
                         400, 400, 120, 100, 150, 0, 20, 637, 10)

    # 创建 技能组 对象
    Gyarados01.skills = (dragonClaw01, tsunami01, sabreDance01, waterfall01)
    Gyarados02.skills = (dragonClaw02, tsunami02, sabreDance02, waterfall02)

    '''
    暴鲤龙初始化结束
    '''

    '''
    古拉顿初始化  6
    '''
    # 创建 我方古拉顿
    Groudon01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Groudon01.png", "../othersource/Pic/headPortraits/Groudon01.png", 1, '古拉顿',
                        400, 400, 176, 178, 150, 0, 80, 70, 80)
    Groudon01.orderPos = (298, 191)

    # 创建 野生古拉顿
    Groudon02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Groudon02.png",  None, 2, '古拉顿',
                        900, 900, 150, 160, 150, 0, 50, 637, 10)

    # 创建 技能组 对象
    Groudon01.skills = (fireKick01, fireBeam01, powerup01, protection01)
    Groudon02.skills = (fireKick02, fireBeam02, powerup02, protection02)

    '''
    古拉顿初始化结束
    '''

    '''
    沙奈朵初始化  7
    '''
    # # 创建 野生沙奈朵    无图
    # Gardevoir02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Gardevoir02.png", 2, '沙奈朵',
    #                    400, 400, 120, 100, 150, 0, 20, 637, 10)

    # 创建 我方沙奈朵
    Gardevoir01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Gardevoir01.png", "../othersource/Pic/headPortraits/Gardevoir01.png",  1, '沙奈朵',
                          400, 400, 80, 77, 150, 0, 40, 70, 80)
    Gardevoir01.orderPos = (422, 191)

    # 创建 技能组 对象
    Gardevoir01.skills = (hypnotism01, kirin01, powerup01, lightning01)
    # Gardevoir02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    沙奈朵初始化结束
    '''

    '''
    沙漠蜻蜓初始化 
    '''
    # 创建 野生沙漠蜻蜓
    Flygon02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Flygon02.png",  None, 2, '沙漠蜻蜓',
                       400, 400, 107, 95, 150, 0, 40, 637, 10)

    # # 创建 我方沙漠蜻蜓   无图
    # Flygon01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Flygon01.png", 1, '沙漠蜻蜓',
    #                      400, 400, 120, 100, 150, 0, 20, 70, 80)

    # 创建 技能组 对象
    # Flygon01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Flygon02.skills = (fireBeam02, iceBeam02, powerup02, dragonClaw02)

    '''
    沙漠蜻蜓初始化结束
    '''

    '''
    喷火龙初始化  8
    '''
    # 创建 我方喷火龙
    Charizard01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Charizard01.png", "../othersource/Pic/headPortraits/Charizard01.png", 1, '喷火龙',
                          400, 400, 90, 105, 150, 0, 20, 70, 80)
    Charizard01.orderPos = (50, 272)

    # 创建 野生喷火龙
    Charizard02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Charizard02.png", None,  2, '喷火龙',
                          400, 400, 100, 100, 150, 0, 30, 637, 10)

    # 创建 技能组 对象
    Charizard01.skills = (knock01, fireBeam01, powerup01, dragonClaw01)
    Charizard02.skills = (knock02, fireBeam02, powerup02, dragonClaw02)

    '''
    喷火龙初始化结束
    '''

    '''
    急冻鸟初始化  9
    '''
    # 创建 我方急冻鸟
    Articuno01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Articuno01.png", "../othersource/Pic/headPortraits/Articuno01.png", 1, '急冻鸟',
                         400, 400, 78, 102, 150, 0, 50, 70, 80)
    Articuno01.orderPos = (174, 272)

    # 创建 野生急冻鸟
    Articuno02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Articuno02.png", None,  2, '急冻鸟',
                         500, 500, 91, 109, 150, 0, 80, 637, 0)

    # 创建 技能组 对象
    Articuno01.skills = (dragonClaw01, kirin01, iceBeam01, lightning01)
    Articuno02.skills = (dragonClaw02, kirin02, iceBeam02, lightning02)

    '''
    海皇牙初始化  10
    '''
    # 创建 我方海皇牙
    Kyogre01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Kyogre01.png", "../othersource/Pic/headPortraits/Kyogre01.png", 1, '海皇牙',
                       400, 400, 133, 107, 150, 0, 80, 70, 80)
    Kyogre01.orderPos = (298, 272)

    # 创建 野生海皇牙
    Kyogre02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Kyogre02.png",  None, 2, '海皇牙',
                       1000, 1000, 130, 96, 150, 0, 60, 637, 10)

    # 创建 技能组 对象
    Kyogre01.skills = (iceBeam01, tsunami01, waterfall01, kirin01)
    Kyogre02.skills = (iceBeam02, tsunami02, waterfall02, kirin02)

    '''
    皮卡丘初始化  11
    '''
    # 创建 我方皮卡丘
    Pikachu01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Pikachu01.png", "../othersource/Pic/headPortraits/Pikachu01.png", 1, '皮卡丘',
                        230, 230, 85, 55, 150, 0, 40, 70, 80)
    Pikachu01.orderPos = (422, 272)

    # 创建 野生皮卡丘
    Pikachu02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Pikachu.png", None,  2, '皮卡丘',
                        230, 230, 80, 50, 150, 0, 30, 637, 10)

    # 创建 技能组 对象
    Pikachu01.skills = (knock01, kirin01, fireBeam01, lightning01)
    Pikachu02.skills = (knock02, kirin02, fireBeam02, lightning02)

    '''
    风速狗初始化  
    '''
    # 创建 野生风速狗 无图片
    # Arcanine02 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Arcanine02.png", 2, '风速狗',
    #                    400, 400, 120, 100, 150, 0, 20, 637, 10)

    # 创建 我方风速狗
    Arcanine01 = Pokemon(p_setting, screen, clock, menubar, "../othersource/Pic/Arcanine01.png", None, 1, '风速狗',
                         400, 400, 117, 100, 150, 0, 20, 70, 80)

    # 创建 技能组 对象
    Arcanine01.skills = (tsunami01, fireBeam01, kirin01, lightning01)
    # Arcanine02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    风速狗初始化结束
    '''

    pygame.mixer.music.load("../othersource/Music/select.mp3")
    pygame.mixer.music.play(-1, 0.0)

    # 创建 选择模式界面的 指针
    modePointer = ModePointer(screen)
    '''#玩家选择游戏模式   '''
    mode = gf.selectMode(p_setting, screen, modePointer, clock)
    if mode == 2:
        pygame.quit()
        os.system('python ../onlineMode/main.py')
        sys.exit()
    if mode == 3:
        pygame.quit()
        os.system('python ../trainingMode/main.py')
        sys.exit()
    if mode == 4:
        pygame.quit()
        os.system("python ../hidingMode/main.py")
        sys.exit()

    # 我方可选的 pokemons
    opt_pokemon01s = ((Charizard01, Gyarados01), (Pikachu01, Gardevoir01),
                      (Scizor01, Articuno01), (Rayquaza01, Blaziken01), (Groudon01, Kyogre01))
    # 存放玩家选择的 pokemons
    myPokemon01s = Pokemons([])

    '''改动！！！！！！！！'''
    maxLevel = 8
    level = 1   # 记录玩家所在关卡
    # 每一关对应的boss，嵌套列表
    bosses = [[Zigzagoon02], [Pikachu02, Charizard02],
              [Flygon02], [Groudon02], [Kyogre02], [Rayquaza02],
              [Articuno02, Ninetails02, Zapdos02, Entei02], [Mewtwo02]]
    enemyPokemon02s = bosses[level-1]
    ''''''
    # 存储玩家的金币
    coins = 0
    selectTime = 0
    # 创建 选择界面的 指针
    pokemonPointer = PokemonPointer(screen)
    # 玩家选择 pokemon 设定 对战的两个宝可梦
    gf.selectPokemonBetFight(p_setting, screen, opt_pokemon01s[selectTime],
                             pokemonPointer, myPokemon01s.myPokemon01s, selectTime, clock, coins)
    selectTime += 1
    # myPokemon01s.updateSkills()        #存放我方pokemons的所有技能

    pokemon01 = myPokemon01s.myPokemon01s[0]  # 我方pokemon

    pokemon02 = enemyPokemon02s[0]  # 敌方pokemon
    gf.setFight(pokemon01, pokemon02)



    '''
    初始化奖励
    '''
    upgradeHp = UpgradeHp(screen, myPokemon01s)
    upgradeAtt = UpgradeAtt(screen, myPokemon01s)
    upgradeDam = UpgradeDam(screen, myPokemon01s)
    upgradeDef = UpgradeDef(screen, myPokemon01s)
    healAll = HealAll(screen, myPokemon01s)
    upgradeStr = UpgradeStr(screen, myPokemon01s.skills)
    degradeHp = DegradeHp(screen, enemyPokemon02s)
    degradeAtt = DegradeAtt(screen, enemyPokemon02s)
    degradeDef = DegradeDef(screen, enemyPokemon02s)
    coinsPrize = CoinsPrize(screen)

    # 每关可能获得的奖励
    prizes = (upgradeHp, upgradeAtt, upgradeDam, upgradeDef, healAll,upgradeStr, degradeHp, degradeAtt, degradeDef, coinsPrize)

    # 商店售卖的商品
    storeGoods = (upgradeHp, upgradeAtt, upgradeDam, upgradeDef,
                  healAll, upgradeStr, degradeHp, degradeAtt, degradeDef)

    # 创建 双方状态栏 对象
    statebar02 = Statebar(p_setting, screen, pokemon02)
    statebar01 = Statebar01(p_setting, screen, pokemon01)
    healthbar02 = Healthbar(
        p_setting, screen, pokemon02, p_setting.healthbarPos)
    healthbar01 = Healthbar(p_setting, screen, pokemon01,
                            p_setting.healthbar01Pos)
    healthbar01.update()
    healthbar02.update()
    # 创建 指针 对象
    pointer = Pointer(p_setting, screen, menubar, pokemon02,
                      pokemon01, statebar02, statebar01, healthbar02, healthbar01, clock)

    # 创建 技能栏 对象
    skillbar = Skillbar(p_setting, screen, pointer)
    skillbar.skills = pokemon01.skills

    # 记录现在该显示在屏幕下方的 菜单栏or技能栏
    pointer.nowbar = menubar

    pygame.mixer.music.stop()

    pygame.mixer.music.load("../othersource/Music/battle01.mp3")
    pygame.mixer.music.play(-1, 0.0)

    # 游戏开始 菜单栏右移进入  野生pokemon左移进入
    for i in range(140):
        p_setting.screen_bg = pygame.image.load(
            "../othersource/Pic/background"+str(i//10+1)+".png")
        gf.update_screen(p_setting, screen, menubar,
                         None, clock, pokemon02, pointer.nowbar)
    while menubar.rect.x < 0:
        menubar.rect.x += 2
        if pokemon02.rect.x >= 300:
            pokemon02.rect.x -= 2
        gf.update_screen(p_setting, screen, menubar,
                         None, clock, pokemon02, pointer.nowbar)

    # 文本提示 ”野生的蛇纹熊出现了！“
    gf.update_screen(p_setting, screen, menubar,
                     pokemon02.name + " 出现了！", clock, pokemon02, pointer.nowbar)
    pygame.time.delay(1000)

    # 文本提示 ”去吧 蛇纹熊！“
    screen.blit(menubar.image, menubar.rect)  # 覆盖上一个文本
    gf.update_screen(p_setting, screen, menubar, "去吧 " +
                     pokemon01.name + " ！", clock, pokemon02, pointer.nowbar)
    pygame.time.delay(1000)

    sleepCount = 2

    # 游戏主循环
    while True:
        clock.tick_busy_loop(400)
        if state == 0:
            # 我方 选择 “战斗”       menubar切换至 skillbar
            pointer.nowbar = menubar
            pointer.update()
            gf.update_screen(p_setting, screen, menubar, pokemon01.name +
                             " 想要干什么？", clock, statebar02, statebar01,
                             healthbar02, healthbar01, pokemon02, pokemon01,
                             pointer.nowbar, pointer)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pointer.nowbar = skillbar
                        state = 1
                        pointer.update()
                        gf.update_screen(p_setting, screen, menubar, None, clock,
                                         statebar02, statebar01, healthbar02,
                                         healthbar01, pokemon02, pokemon01,
                                         pointer.nowbar, pointer)

        if state == 1:
            # 我方 出招
            '''
            s = socket.socket()
            s.connect(('42.192.86.230', 8712))
            '''
            quiT = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        pointer.moveUp()
                    if event.key == pygame.K_DOWN:
                        pointer.moveDown()
                    if event.key == pygame.K_LEFT:
                        pointer.moveLeft()
                    if event.key == pygame.K_RIGHT:
                        pointer.moveRight()
                    if event.key == pygame.K_RETURN:
                        pointer.nowbar = menubar

                        state = 2
                        skillNum = pointer.flag

                        '''
                        s.send(str(skillNum).encode())
                        s.close()
                        '''
                        quiT = 1
            if quiT == 1:
                if pokemon01.skills[skillNum].nowPP <= 0:
                    pokemon01.state = 1
                    gf.update_screen(p_setting, screen, menubar,
                                     pokemon01.name + " 使用了" +
                                     pokemon01.skills[skillNum].name
                                     + "！", clock, statebar02,
                                     statebar01, healthbar02, healthbar01,
                                     pokemon02, pokemon01, pointer.nowbar)
                    pygame.time.delay(1000)

                if pokemon02.state != 2 and pokemon01.state != 1:
                    pokemon01.useSkill(skillNum)  # 我方出招
                    healthbar02.update()  # 更新 敌方血条
                    gf.update_screen(p_setting, screen, menubar,
                                     pokemon01.name + " 使用了" +
                                     pokemon01.skills[skillNum].name
                                     + "！", clock, statebar02,
                                     statebar01, healthbar02, healthbar01,
                                     pokemon02, pokemon01, pointer.nowbar)
                    pygame.time.delay(1000)
                elif pokemon01.state != 1:
                    pokemon02.state = 0
                    gf.update_screen(p_setting, screen, menubar,
                                     pokemon01.name + " 使用了" +
                                     pokemon01.skills[skillNum].name
                                     + "！", clock, statebar02,
                                     statebar01, healthbar02, healthbar01,
                                     pokemon02, pokemon01, pointer.nowbar)
                    pygame.time.delay(1000)
                    gf.update_screen(p_setting, screen, menubar,
                                     pokemon01.name + " 的技能无效化了"
                                     + "！", clock, statebar02,
                                     statebar01, healthbar02, healthbar01,
                                     pokemon02, pokemon01, pointer.nowbar)
                    pygame.time.delay(1000)

                if pokemon01.state == 1:
                    gf.update_screen(p_setting, screen, menubar,
                                     "但是它失败了！", clock, statebar02,
                                     statebar01, healthbar02, healthbar01,
                                     pokemon02, pokemon01, pointer.nowbar)
                    pokemon01.state = 0

                if pokemon01.state == 2:
                    gf.update_screen(p_setting, screen, menubar,
                                     pokemon01.name + " 保护了自己"
                                     + "！", clock, statebar02,
                                     statebar01, healthbar02, healthbar01,
                                     pokemon02, pokemon01, pointer.nowbar)
                pygame.time.delay(1000)
                pointer.flag = 0

        if gf.checkDeath(pokemon02, p_setting, screen, pointer.nowbar, menubar,
                         statebar02, statebar01, healthbar02, healthbar01, clock) == -1:
            '''
            s = socket.socket()
            s.connect(('42.192.86.230', 8712))
            s.send('-1'.encode())
            s.close()
            '''
            enemyPokemon02s.remove(enemyPokemon02s[0])
            if len(enemyPokemon02s) == 0:
                # 通过一关
                # 音乐、文字提示
                pygame.mixer.music.stop()
                pygame.mixer.music.load("../othersource/Music/normalwin.mp3")
                pygame.mixer.music.play(1, 0.0)
                gf.update_screen(p_setting, screen, menubar, "胜利了" + "！", clock, statebar02,
                                 statebar01, healthbar02, healthbar01, pokemon01, pointer.nowbar)
                pygame.time.delay(1000)

                level += 1

                # 治疗玩家的宠物 恢复技能pp 重置pokemon的各项属性
                myPokemon01s.reset()
                gf.healPokemons(myPokemon01s.myPokemon01s)
                pokemon01.initSkills()

                print(pokemon01.attack)

                if level < maxLevel+1:
                    enemyPokemon02s = bosses[level - 1]

                    # 金币奖励
                    coins = gf.drawGetCoins(screen, level, coins, clock)  # 硬币数待定
                    pygame.time.delay(1000)

                    # 选奖励or查看pokemons
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("../othersource/Music/Prize.mp3")
                    pygame.mixer.music.play(-1, 0.0)
                    getMoney = gf.choosePrize(
                        screen, prizes, myPokemon01s.myPokemon01s, enemyPokemon02s, coins, clock)
                    # 如果选了100金币奖励
                    if getMoney:
                        coins += getMoney

                    # 每三关进商店买东西
                    cost = gf.store(screen, level, coins,
                                    storeGoods, myPokemon01s.myPokemon01s, clock)
                    if cost: coins -= cost

                    if selectTime < 5:
                        tmpPokemons = Pokemons([])
                        # 创建 选择界面的 指针
                        pokemonPointer = PokemonPointer(screen)
                        # 玩家选择 pokemon 设定 对战的两个宝可梦
                        gf.selectPokemonBetFight(p_setting, screen, opt_pokemon01s[selectTime],
                                                 pokemonPointer, tmpPokemons.myPokemon01s, selectTime, clock, coins)
                        myPokemon01s.myPokemon01s.append(
                            tmpPokemons.myPokemon01s[0])
                        selectTime += 1
                    # 下一关or查看pokemons
                    gf.drawNextLevel(
                        screen, level, myPokemon01s.myPokemon01s, coins, clock)
                    pygame.time.delay(1500)
                    pokemon01 = myPokemon01s.myPokemon01s[0]
                    pokemon02 = enemyPokemon02s[0]
                    gf.setFight(pokemon01, pokemon02)
                    # 更新技能栏、血条、状态栏信息
                    statebar02.pokemon = pokemon02
                    statebar01.pokemon = pokemon01
                    healthbar02.pokemon = pokemon02
                    healthbar01.pokemon = pokemon01
                    healthbar02.update()
                    healthbar01.update()
                    skillbar.skills = pokemon01.skills
                    pointer.pokemon02 = pokemon02
                    pointer.pokemon01 = pokemon01
                    menubar.rect.x = -500

                    pygame.mixer.music.load("../othersource/Music/battle0"+str(level)+".mp3")
                    pygame.mixer.music.play(-1, 0.0)
                    # 下一关开始 菜单栏右移进入  野生pokemon左移进入
                    for i in range(140):
                        p_setting.screen_bg = pygame.image.load(
                            "../othersource/Pic/background" + str(i // 10 + 1) + ".png")
                        gf.update_screen(p_setting, screen, menubar,
                                         None, clock, pokemon02, pointer.nowbar)
                    while menubar.rect.x < 0:
                        menubar.rect.x += 2
                        if pokemon02.rect.x >= 300:
                            pokemon02.rect.x -= 2
                        gf.update_screen(p_setting, screen, menubar,
                                         None, clock, pokemon02, pointer.nowbar)

                    # 文本提示 ”野生的蛇纹熊出现了！“
                    gf.update_screen(p_setting, screen, menubar,
                                     pokemon02.name + " 出现了！", clock, pokemon02, pointer.nowbar)
                    pygame.time.delay(1000)
                    state = 0

                else:
                    # 通过了最后一关
                    screen.blit(pygame.image.load(
                        "../othersource/Pic/game_over.jpg"), (0, 0))
                    pygame.mixer.music.load("../othersource/Music/finalWin.mp3")
                    pygame.mixer.music.play(1, 0.0)
                    pygame.display.update()
                    pygame.time.delay(7000)
                    sys.exit()
            else:
                # 这一关的boss不只一个，换下一个boss
                pokemon02 = enemyPokemon02s[0]
                gf.setFight(pokemon01, pokemon02)
                pokemon02.rect.x = 300

                # 更新技能栏、血条、状态栏信息
                statebar02.pokemon = pokemon02
                healthbar02.pokemon = pokemon02
                healthbar02.update()
                pointer.pokemon02 = pokemon02
                gf.update_screen(p_setting, screen, menubar,
                                 pokemon02.name + " 出现了！", clock, pokemon02, pokemon01, pointer.nowbar)
                state = 0
                pygame.time.delay(1000)

        if state == 2:
            # 敌方 出招
            state = 0
            if pokemon02.state < 0:
                pokemon02.state += 1
                gf.update_screen(p_setting, screen, menubar,
                                 pokemon02.name + " 睡着了" +
                                 "！", clock, statebar02, statebar01,
                                 healthbar02, healthbar01, pokemon02,
                                 pokemon01, pointer.nowbar)
                pygame.time.delay(1000)
                continue

            skillNum = random.randint(0, 3)
            '''
            while True:
                choice = 0
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            s = socket.socket()
                            s.connect(('42.192.86.230', 8712))
                            skillNum = int(s.recv(1024).decode())
                            s.close()
                            choice = 1
                            break
                if choice == 1:
                    break
            '''
            # if skillNum != -1:
            if pokemon02.skills[skillNum].nowPP <= 0:
                pokemon02.state = 1
                gf.update_screen(p_setting, screen, menubar,
                                 pokemon02.name + " 使用了" +
                                 pokemon02.skills[skillNum].name +
                                 "！", clock, statebar02, statebar01,
                                 healthbar02, healthbar01, pokemon02,
                                 pokemon01, pointer.nowbar)
                pygame.time.delay(1000)

            if pokemon01.state != 2 and pokemon02.state != 1:
                pokemon02.useSkill(skillNum)  # 敌方 出招
                healthbar01.update()  # 更新 我方血条
                gf.update_screen(p_setting, screen, menubar,
                                 pokemon02.name + " 使用了" +
                                 pokemon02.skills[skillNum].name +
                                 "！", clock, statebar02, statebar01,
                                 healthbar02, healthbar01, pokemon02,
                                 pokemon01, pointer.nowbar)
                pygame.time.delay(1000)
            elif pokemon02.state != 1:
                pokemon01.state = 0
                gf.update_screen(p_setting, screen, menubar,
                                 pokemon02.name + " 使用了" +
                                 pokemon02.skills[skillNum].name +
                                 "！", clock, statebar02, statebar01,
                                 healthbar02, healthbar01, pokemon02,
                                 pokemon01, pointer.nowbar)
                pygame.time.delay(1000)
                gf.update_screen(p_setting, screen, menubar,
                                 pokemon02.name + " 的技能无效化了" +
                                 "！", clock, statebar02, statebar01,
                                 healthbar02, healthbar01, pokemon02,
                                 pokemon01, pointer.nowbar)
                pygame.time.delay(1000)

            if pokemon02.state == 1:
                gf.update_screen(p_setting, screen, menubar,
                                 "但是它失败了！", clock, statebar02,
                                 statebar01, healthbar02, healthbar01,
                                 pokemon02, pokemon01, pointer.nowbar)
                pokemon02.state = 0
                pygame.time.delay(1000)

        if gf.checkDeath(pokemon01, p_setting, screen, pointer.nowbar, menubar,
                         statebar02, statebar01, healthbar02, healthbar01, clock) == -1:
            '''
            s = socket.socket()
            s.connect(('42.192.86.230', 8712))
            s.send('-1'.encode())
            s.close()
            '''
            # myPokemon01s.myPokemon01s.remove(myPokemon01s.myPokemon01s[0])
            pokemon01.alive = False
            pokemon01.initSkills()              # 恢复被当前pokemon使用过的技能
            if myPokemon01s.allFailed():
                # 玩家失败
                sys.exit()
            else:
                for pokemon in myPokemon01s.myPokemon01s:
                    if pokemon.alive:
                        pokemon01 = pokemon
                        break

                gf.setFight(pokemon01, pokemon02)

                # 更新状态栏、血条、技能栏信息
                statebar01.pokemon = pokemon01
                healthbar01.pokemon = pokemon01
                healthbar01.update()
                pointer.pokemon01 = pokemon01
                skillbar.skills = pokemon01.skills

                gf.update_screen(p_setting, screen, menubar, "去吧 " +
                                 pokemon01.name + " ！", clock, pokemon02, pointer.nowbar)
                pygame.time.delay(1000)


if __name__ == "__main__":
    main()
