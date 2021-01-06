import pygame
from pygame.sprite import Group
from pokemons import Pokemon
from settings import Setting
from menubar import Menubar
from pointer import Pointer
from pointer import SelectionPointer
from skills import Knock, ShadowBall, Powerup, Lightning, FireBeam, Kirin, Tsunami, Hypnotism
from statebar import Statebar, Statebar01, Healthbar
from skillmenu import Skillbar
import game_functions as gf
import random
import sys
import socket


def main():
    s = socket.socket()
    s.connect(('42.192.86.230', 8712))
    print(s.recv(1024).decode(encoding='utf8'))
    state = int(s.recv(1024).decode())
    s.close()

    pygame.init()
    pygame.mixer.init()
    # 创建 设置 实例
    p_setting = Setting()

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

    # 创建 催眠术技能 对象（敌方）
    hypnotism02 = Hypnotism(p_setting, screen, menubar)

    '''
    蛇纹熊初始化  0
    '''
    # 创建 我方蛇纹熊
    Zigzagoon01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Zigzagoon01.png",
                          1, '蛇纹熊', 100, 100, 20, 20, 50, 0, 20, "Zigzagoon01", 70, 118)
    Zigzagoon01.orderPos = (50, 110)

    # 创建 野生蛇纹熊
    Zigzagoon02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Zigzagoon02.png", 2, '蛇纹熊',
                          100, 100, 20, 20, 50, 0, 20, "Zigzagoon02", 637, 50)

    # 创建 技能组 对象
    Zigzagoon01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Zigzagoon02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    裂空座初始化  1
    '''
    # 创建 我方裂空座
    Rayquaza01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Rayquaza01.png", 1, '裂空座',
                         400, 400, 120, 100, 150, 0, 20, "Rayquaza01", 70, 80)
    Rayquaza01.orderPos = (174, 110)

    # 创建 野生裂空座
    Rayquaza02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Rayquaza02.png", 2, '裂空座',
                         400, 400, 120, 100, 150, 0, 20, "Rayquaza02", 637, 10)

    # 创建 技能组 对象
    Rayquaza01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Rayquaza02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    裂空座初始化结束
    '''

    '''
    火鸡战士初始化 2
    '''
    # 创建 我方火鸡战士
    Blaziken01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Blaziken01.png", 1, '火鸡战士',
                         400, 400, 120, 100, 150, 0, 20, "Blaziken01", 70, 80)
    Blaziken01.orderPos = (298, 110)

    # 创建 野生火鸡战士
    Blaziken02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Blaziken02.png", 2, '火鸡战士',
                         400, 400, 120, 100, 150, 0, 20, "Blaziken02", 637, 10)

    # 创建 技能组 对象
    Blaziken01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Blaziken02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    火鸡战士初始化结束
    '''

    '''
    炎帝初始化   
    '''
    # 创建 野生炎帝
    Entei02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Entei02.png", 2, '炎帝',
                      400, 400, 120, 100, 150, 0, 20, "Entei02", 637, 10)

    # # 创建 我方炎帝     无图
    # Entei01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Entei01.png", 1, '炎帝',
    #                      400, 400, 120, 100, 150, 0, 20, 70, 80)

    # 创建 技能组 对象
    # Entei01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Entei02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    炎帝初始化结束
    '''

    '''
    灾兽初始化   
    '''
    # 创建 野生灾兽
    Absol02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Absol02.png", 2, '灾兽',
                      400, 400, 120, 100, 150, 0, 20, "Absol02", 637, 10)

    # # 创建 我方灾兽     无图
    # Absol01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Absol01.png", 1, '灾兽',
    #                      400, 400, 120, 100, 150, 0, 20, 70, 80)

    # 创建 技能组 对象
    # Absol01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Absol02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    灾兽初始化结束
    '''

    '''
    闪电鸟初始化  3
    '''
    # 创建 我方闪电鸟
    Zapdos01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Zapdos01.png", 1, '闪电鸟',
                       400, 400, 120, 100, 150, 0, 20, "Zapdos01", 70, 80)
    Zapdos01.orderPos = (422, 110)

    # 创建 野生闪电鸟
    Zapdos02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Zapdos02.png", 2, '闪电鸟',
                       400, 400, 120, 100, 150, 0, 20, "Zapdos02", 637, 10)

    # 创建 技能组 对象
    Zapdos01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Zapdos02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    闪电鸟初始化结束
    '''

    '''
    巨钳螳螂初始化 4
    '''
    # 创建 我方巨钳螳螂
    Scizor01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Scizor01.png", 1, '巨钳螳螂',
                       400, 400, 120, 100, 150, 0, 20, "Scizor01", 70, 80)
    Scizor01.orderPos = (50, 191)

    # 创建 野生巨钳螳螂
    Scizor02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Scizor02.png", 2, '巨钳螳螂',
                       400, 400, 120, 100, 150, 0, 20, "Scizor02", 637, 10)

    # 创建 技能组 对象
    Scizor01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Scizor02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    巨钳螳螂初始化结束
    '''

    '''
    九尾初始化   
    '''
    # 创建 野生九尾
    Ninetails02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Ninetails02.png", 2, '九尾',
                          400, 400, 120, 100, 150, 0, 20, "Ninetails02", 637, 10)

    # # 创建 我方九尾     无图
    # Ninetails01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Ninetails01.png", 1, '九尾',
    #                      400, 400, 120, 100, 150, 0, 20, 70, 80)

    # 创建 技能组 对象
    # Ninetails01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Ninetails02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    九尾初始化结束
    '''

    '''
    超梦初始化   
    '''
    # 创建 野生超梦
    Mewtwo02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Mewtwo02.png", 2, '超梦',
                       400, 400, 120, 100, 150, 0, 20, "Mewtwo02", 637, 10)

    # # 创建 我方超梦 无图
    # Mewtwo01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Mewtwo01.png", 1, '超梦',
    #                      400, 400, 120, 100, 150, 0, 20, 70, 80)

    # 创建 技能组 对象
    # Mewtwo01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Mewtwo02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    超梦初始化结束
    '''

    '''
    鲤鱼王初始化  
    '''
    # 创建 野生鲤鱼王
    Magikarp02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Magikarp02.png", 2, '鲤鱼王',
                         400, 400, 120, 100, 150, 0, 20, "Magikarp02", 637, 10)

    # # 创建 我方鲤鱼王    无图
    # Magikarp01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Magikarp01.png", 1, '鲤鱼王',
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
    Gyarados01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Gyarados01.png", 1, '暴鲤龙',
                         400, 400, 120, 100, 150, 0, 20, "Gyarados01", 70, 80)
    Gyarados01.orderPos = (174, 191)

    # 创建 野生暴鲤龙
    Gyarados02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Gyarados02.png", 2, '暴鲤龙',
                         400, 400, 120, 100, 150, 0, 20, "Gyarados02", 637, 10)

    # 创建 技能组 对象
    Gyarados01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Gyarados02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    暴鲤龙初始化结束
    '''

    '''
    古拉顿初始化  6
    '''
    # 创建 我方古拉顿
    Groudon01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Groudon01.png", 1, '古拉顿',
                        400, 400, 120, 100, 150, 0, 20, "Groudon01", 70, 80)
    Groudon01.orderPos = (298, 191)

    # 创建 野生古拉顿
    Groudon02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Groudon02.png", 2, '古拉顿',
                        400, 400, 120, 100, 150, 0, 20, "Groudon02", 637, 10)

    # 创建 技能组 对象
    Groudon01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Groudon02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    古拉顿初始化结束
    '''

    '''
    沙奈朵初始化  7
    '''
    # # 创建 野生沙奈朵    无图
    # Gardevoir02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Gardevoir02.png", 2, '沙奈朵',
    #                    400, 400, 120, 100, 150, 0, 20, 637, 10)

    # 创建 我方沙奈朵
    Gardevoir01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Gardevoir01.png", 1, '沙奈朵',
                          400, 400, 120, 100, 150, 0, 100, "Gardevoir01", 70, 80)
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
    Flygon02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Flygon02.png", 2, '沙漠蜻蜓',
                       400, 400, 120, 100, 150, 0, 20, "Flygon02", 637, 10)

    # # 创建 我方沙漠蜻蜓   无图
    # Flygon01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Flygon01.png", 1, '沙漠蜻蜓',
    #                      400, 400, 120, 100, 150, 0, 20, 70, 80)

    # 创建 技能组 对象
    # Flygon01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Flygon02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    沙漠蜻蜓初始化结束
    '''

    '''
    喷火龙初始化  8
    '''
    # 创建 我方喷火龙
    Charizard01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Charizard01.png", 1, '喷火龙',
                          400, 400, 120, 100, 150, 0, 20, "Charizard01", 70, 80)
    Charizard01.orderPos = (50, 272)

    # 创建 野生喷火龙
    Charizard02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Charizard02.png", 2, '喷火龙',
                          400, 400, 120, 100, 150, 0, 20, "Charizard02", 637, 10)

    # 创建 技能组 对象
    Charizard01.skills = (knock01, shadowBall01, powerup01, lightning01)
    Charizard02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    喷火龙初始化结束
    '''

    '''
    急冻鸟初始化  9
    '''
    # 创建 我方急冻鸟
    Articuno01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Articuno01.png", 1, '急冻鸟',
                         400, 400, 120, 100, 150, 0, 100, "Articuno01", 70, 80)
    Articuno01.orderPos = (174, 272)

    # 创建 野生急冻鸟
    Articuno02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Articuno02.png", 2, '急冻鸟',
                         400, 400, 120, 100, 150, 0, 100, "Articuno02", 637, 0)

    # 创建 技能组 对象
    Articuno01.skills = (knock01, shadowBall01, fireBeam01, lightning01)
    Articuno02.skills = (knock02, shadowBall02, fireBeam02, lightning02)

    '''
    海皇牙初始化  10
    '''
    # 创建 我方海皇牙
    Kyogre01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Kyogre01.png", 1, '海皇牙',
                       400, 400, 120, 100, 150, 0, 100, "Kyogre01", 70, 80)
    Kyogre01.orderPos = (298, 272)

    # 创建 野生海皇牙
    Kyogre02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Kyogre02.png", 2, '海皇牙',
                       400, 400, 120, 100, 150, 0, 100, "Kyogre02", 637, 10)

    # 创建 技能组 对象
    Kyogre01.skills = (knock01, shadowBall01, fireBeam01, lightning01)
    Kyogre02.skills = (knock02, shadowBall02, fireBeam02, lightning02)

    '''
    皮卡丘初始化  11
    '''
    # 创建 我方皮卡丘
    Pikachu01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Pikachu01.png", 1, '皮卡丘',
                        400, 400, 120, 100, 150, 0, 100, "Pikachu01", 70, 80)
    Pikachu01.orderPos = (422, 272)

    # 创建 野生皮卡丘
    Pikachu02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Pikachu.png", 2, '皮卡丘',
                        400, 400, 120, 100, 150, 0, 100, "Pikachu02", 637, 10)

    # 创建 技能组 对象
    Pikachu01.skills = (knock01, shadowBall01, fireBeam01, lightning01)
    Pikachu02.skills = (knock02, kirin02, fireBeam02, lightning02)

    '''
    风速狗初始化  
    '''
    # 创建 野生风速狗 无图片
    # Rayquaza02 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Rayquaza.png", 2, '风速狗',
    #                    400, 400, 120, 100, 150, 0, 20, 637, 10)

    # 创建 我方风速狗
    Arcanine01 = Pokemon(p_setting, screen, menubar, "../othersource/Pic/Arcanine01.png", 1, '风速狗',
                         400, 400, 120, 100, 150, 0, 20, "Arcanine01", 70, 80)

    # 创建 技能组 对象
    Arcanine01.skills = (tsunami01, fireBeam01, kirin01, lightning01)
    # Rayquaza02.skills = (knock02, shadowBall02, powerup02, lightning02)

    '''
    风速狗初始化结束
    '''

    # 我方可选的 pokemons
    opt_pokemon01s = (Zigzagoon01, Rayquaza01, Blaziken01, Zapdos01, Scizor01, Gyarados01,
                      Groudon01, Gardevoir01, Charizard01, Articuno01, Kyogre01, Pikachu01)
    # 存放玩家选择的 pokemons
    myPokemon01s = []

    # 创建 选择界面的 指针
    selectionPointer = SelectionPointer(p_setting, screen)

    varStri = ''

    while True:
        if state == 0:
            s = socket.socket()
            s.connect(('42.192.86.230', 8712))
            gf.selectPokemon(p_setting, screen, opt_pokemon01s,
                             selectionPointer, myPokemon01s)
            pokemon01 = myPokemon01s[0]  # 我方pokemon
            varStr = pokemon01.variable[:-1]+'2'
            varStri = ''
            s.send(str(varStr).encode())
            s.close()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            s = socket.socket()
                            s.connect(('42.192.86.230', 8712))
                            varStri = str(s.recv(1024).decode())
                            s.close()
                            break
                if varStri != '':
                    break
        if state == 2:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            varStri = ''
                            s = socket.socket()
                            s.connect(('42.192.86.230', 8712))
                            varStri = str(s.recv(1024).decode())
                            s.close()
                            break
                if varStri != '':
                    break
            s = socket.socket()
            s.connect(('42.192.86.230', 8712))
            gf.selectPokemon(p_setting, screen, opt_pokemon01s,
                     selectionPointer, myPokemon01s)
            pokemon01 = myPokemon01s[0]  # 我方pokemon
            varStr = pokemon01.variable[:-1]+'2'
            s.send(str(varStr).encode())
            s.close()
        if varStri != '':
            break
    # 敌方pokemon
    if varStri == "Rayquaza02":
        enemyPokemon02s = [Rayquaza02]
    if varStri == "Blaziken02":
        enemyPokemon02s = [Blaziken02]
    if varStri == "Zapdos02":
        enemyPokemon02s = [Zapdos02]
    if varStri == "Gyarados02":
        enemyPokemon02s = [Gyarados02]
    if varStri == "Groudon02":
        enemyPokemon02s = [Groudon02]
    if varStri == "Charizard02":
        enemyPokemon02s = [Rayquaza02]
    if varStri == "Articuno02":
        enemyPokemon02s = [Articuno02]
    if varStri == "Kyogre02":
        enemyPokemon02s = [Kyogre02]
    if varStri == "Pikachu02":
        enemyPokemon02s = [Pikachu02]

    pokemon02 = enemyPokemon02s[0]
    gf.setFight(pokemon01, pokemon02)

    # 创建 双方状态栏 对象
    statebar02 = Statebar(p_setting, screen, pokemon02)
    statebar01 = Statebar01(p_setting, screen, pokemon01)
    healthbar02 = Healthbar(
        p_setting, screen, pokemon02, p_setting.healthbarPos)
    healthbar01 = Healthbar(p_setting, screen, pokemon01,
                            p_setting.healthbar01Pos)

    # 创建 指针 对象
    pointer = Pointer(p_setting, screen, menubar, pokemon02,
                      pokemon01, statebar02, statebar01, healthbar02, healthbar01)

    # 创建 技能栏 对象
    skillbar = Skillbar(p_setting, screen, pointer)
    skillbar.skills = pokemon01.skills

    # 记录现在该显示在屏幕下方的 菜单栏or技能栏
    pointer.nowbar = menubar

    pygame.mixer.music.load("../othersource/Music/battle01.mp3")
    pygame.mixer.music.play(-1, 0.0)

    # 游戏开始 菜单栏右移进入  野生pokemon左移进入
    for i in range(140):
        p_setting.screen_bg = pygame.image.load(
            "../othersource/Pic/background"+str(i//10+1)+".png")
        gf.update_screen(p_setting, screen, menubar,
                         None, pokemon02, pointer.nowbar)
    while menubar.rect.x < 0:
        menubar.rect.x += 2
        if pokemon02.rect.x >= 300:
            pokemon02.rect.x -= 2
        gf.update_screen(p_setting, screen, menubar,
                         None, pokemon02, pointer.nowbar)

    # 文本提示 ”野生的蛇纹熊出现了！“
    gf.update_screen(p_setting, screen, menubar,
                     pokemon02.name + " 出现了！", pokemon02, pointer.nowbar)
    pygame.time.delay(1000)

    # 文本提示 ”去吧 蛇纹熊！“
    screen.blit(menubar.image, menubar.rect)  # 覆盖上一个文本
    gf.update_screen(p_setting, screen, menubar, "去吧 " +
                     pokemon01.name + " ！", pokemon02, pointer.nowbar)
    pygame.time.delay(1000)

    sleepCount = 2

    # 游戏主循环
    while True:
        if state == 0:
            # 我方 选择 “战斗”       menubar切换至 skillbar
            pointer.nowbar = menubar
            pointer.update()
            gf.update_screen(p_setting, screen, menubar, pokemon01.name +
                             " 想要干什么？", statebar02, statebar01,
                             healthbar02, healthbar01, pokemon02, pokemon01,
                             pointer.nowbar, pointer)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pointer.nowbar = skillbar
                        state = 1
                        pointer.update()
                        gf.update_screen(p_setting, screen, menubar, None,
                                         statebar02, statebar01, healthbar02,
                                         healthbar01, pokemon02, pokemon01,
                                         pointer.nowbar, pointer)

        if state == 1:
            # 我方 出招
            s = socket.socket()
            s.connect(('42.192.86.230', 8712))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
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
                        s.send(str(skillNum).encode())
                        s.close()
                        pokemon01.useSkill(skillNum)  # 我方出招
                        healthbar02.update()  # 更新 敌方血条
                        gf.update_screen(p_setting, screen, menubar,
                                         pokemon01.name + " 使用了" +
                                         pokemon01.skills[skillNum].name
                                         + "！", statebar02,
                                         statebar01, healthbar02, healthbar01,
                                         pokemon02, pokemon01, pointer.nowbar)
                        pygame.time.delay(1000)
                        if pokemon01.state == 1:
                            gf.update_screen(p_setting, screen, menubar,
                                             "但是它失败了！", statebar02,
                                             statebar01, healthbar02, healthbar01,
                                             pokemon02, pokemon01, pointer.nowbar)
                            pokemon01.state = 0
                        pygame.time.delay(1000)
                        pointer.flag = 0

        if gf.checkDeath(pokemon02, p_setting, screen, pointer.nowbar, menubar,
                         statebar02, statebar01, healthbar02, healthbar01) == -1:
            s = socket.socket()
            s.connect(('42.192.86.230', 8712))
            s.send('-1'.encode())
            s.close()
            enemyPokemon02s.remove(enemyPokemon02s[0])
            if len(enemyPokemon02s) == 0:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("../othersource/Music/normalwin.mp3")
                pygame.mixer.music.play(1, 0.0)
                gf.update_screen(p_setting, screen, menubar,
                                 "你 赢得了比赛！", statebar02,
                                 statebar01, healthbar02, healthbar01,
                                 pokemon01, pointer.nowbar)
                pygame.time.delay(2000)
                sys.exit()
            else:
                pokemon02 = enemyPokemon02s[0]
                gf.setFight(pokemon01, pokemon02)
                pokemon02.rect.x = 300
                # 创建 双方状态栏 对象
                statebar02 = Statebar(p_setting, screen, pokemon02)
                statebar01 = Statebar01(p_setting, screen, pokemon01)
                healthbar02 = Healthbar(
                    p_setting, screen, pokemon02, p_setting.healthbarPos)
                healthbar01 = Healthbar(p_setting, screen, pokemon01,
                                        p_setting.healthbar01Pos)
                healthbar02.update()
                healthbar01.update()
                # 创建 指针 对象
                pointer = Pointer(p_setting, screen, menubar, pokemon02,
                                  pokemon01, statebar02, statebar01, healthbar02, healthbar01)

                # 创建 技能栏 对象
                skillbar = Skillbar(p_setting, screen, pointer)
                skillbar.skills = pokemon01.skills

                # 记录现在该显示在屏幕下方的 菜单栏or技能栏
                pointer.nowbar = menubar
                screen.blit(menubar.image, menubar.rect)  # 覆盖上一个文本
                gf.update_screen(p_setting, screen, menubar,
                                 pokemon02.name + " 出现了！", pokemon02, pokemon01, pointer.nowbar)
                state = 0
                pygame.time.delay(1000)

        if state == 2:
            # 敌方 出招
            state = 0
            skillNum = -1
            if pokemon02.state < 0:
                pokemon02.state += 1
                gf.update_screen(p_setting, screen, menubar,
                                 pokemon02.name + " 睡着了" +
                                 "！", statebar02, statebar01,
                                 healthbar02, healthbar01, pokemon02,
                                 pokemon01, pointer.nowbar)
                pygame.time.delay(1000)
                continue
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
            if skillNum != -1:
                pokemon02.useSkill(skillNum)  # 敌方 出招
                healthbar01.update()  # 更新 我方血条
                gf.update_screen(p_setting, screen, menubar,
                                 pokemon02.name + " 使用了" +
                                 pokemon02.skills[skillNum].name +
                                 "！", statebar02, statebar01,
                                 healthbar02, healthbar01, pokemon02,
                                 pokemon01, pointer.nowbar)
                pygame.time.delay(1000)

        if gf.checkDeath(pokemon01, p_setting, screen, pointer.nowbar, menubar,
                         statebar02, statebar01, healthbar02, healthbar01) == -1:
            s = socket.socket()
            s.connect(('42.192.86.230', 8712))
            s.send('-1'.encode())
            s.close()
            myPokemon01s.remove(myPokemon01s[0])
            if len(myPokemon01s) == 0:
                sys.exit()
            else:
                pokemon01 = myPokemon01s[0]
                gf.setFight(pokemon01, pokemon02)
                for skill in pokemon01.skills:
                    skill.nowPP = skill.maxPP
                # 创建 双方状态栏 对象
                statebar02 = Statebar(p_setting, screen, pokemon02)
                statebar01 = Statebar01(p_setting, screen, pokemon01)
                healthbar02 = Healthbar(
                    p_setting, screen, pokemon02, p_setting.healthbarPos)
                healthbar01 = Healthbar(p_setting, screen, pokemon01,
                                        p_setting.healthbar01Pos)

                # 创建 指针 对象
                pointer = Pointer(p_setting, screen, menubar, pokemon02,
                                  pokemon01, statebar02, statebar01, healthbar02, healthbar01)

                # 创建 技能栏 对象
                skillbar = Skillbar(p_setting, screen, pointer)
                skillbar.skills = pokemon01.skills

                # 记录现在该显示在屏幕下方的 菜单栏or技能栏
                pointer.nowbar = menubar
                healthbar01.update()
                healthbar02.update()
                screen.blit(menubar.image, menubar.rect)  # 覆盖上一个文本
                gf.update_screen(p_setting, screen, menubar, "去吧 " +
                                 pokemon01.name + " ！", pokemon02, pointer.nowbar)
                pygame.time.delay(1000)


if __name__ == "__main__":
    main()
