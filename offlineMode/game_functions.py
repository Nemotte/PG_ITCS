import pygame
import sys
import random
from pointer import CheckPokemon01sPointer, PrizePointer, StorePointer, PokemonPointer

def update_screen(p_setting, screen, menubar, menubarText, clock, *images):
    # images  除屏幕背景之外 需要绘制到屏幕上的
    # images的顺序
    # pokemons、skillImages
    # nowbar
    # pointer
    # statebar、healthbar次序不重要
    screen.blit(p_setting.screen_bg, (0, 0))
    for image in images:
        image.blitme()
    if menubarText:
        menubar.draw_text(menubarText)
    pygame.display.update()
    clock.tick_busy_loop(400) 


def draw_text(screen, font_name, font_size, text, text_topleft, text_color):
    typeface = pygame.font.Font(font_name, font_size)
    text_image = typeface.render(text, True, text_color)
    text_rect = text_image.get_rect()
    text_rect.topleft = text_topleft
    screen.blit(text_image, text_rect)


def checkDeath(pokemon, p_setting, screen, nowbar, menubar, statebar,
               statebar01, healthbar, healthbar01, clock):
    # 检查 pokemon 是否死亡
    if pokemon.health <= 0:
        pokemon.alive = False
        update_screen(p_setting, screen, menubar, pokemon.name + " 倒下了！", clock,
                      statebar, statebar01, healthbar, healthbar01,
                      pokemon.target, nowbar)
        pygame.time.delay(1000)
        return -1


def setFight(pokemon01, pokemon02):
    # 设定 对战的两个宝可梦
    pokemon01.target = pokemon02
    pokemon02.target = pokemon01
    for skill in pokemon01.skills:
        skill.pokemon = pokemon01
        skill.target = pokemon02
    for skill in pokemon02.skills:
        skill.pokemon = pokemon02
        skill.target = pokemon01


def selectPokemon(p_setting, screen, opt_pokemon01s, selectionPointer, myPokemon01s, clock):
    # 玩家选择 pokemon
    while True:
        screen.blit(p_setting.selection_bg, (0, 0))
        selectionPointer.blitme()
        for i in range(len(myPokemon01s)):
            draw_text(screen, p_setting.mainFont, 16, str(i + 1), myPokemon01s[i].orderPos, (100, 100, 100))
        pygame.display.update()
        clock.tick_busy_loop(400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if (opt_pokemon01s[selectionPointer.flag] not in myPokemon01s) and len(myPokemon01s) < 6:
                        myPokemon01s.append(opt_pokemon01s[selectionPointer.flag])

                    elif ((opt_pokemon01s[selectionPointer.flag] not in myPokemon01s) and len(myPokemon01s) >= 6):
                        # 玩家选择多于 6 只
                        screen.blit(p_setting.loadingPage, (0, 0))
                        draw_text(screen, p_setting.mainFont, 13, "最多只能选择 6 只 pokemon", (170, 137), (100, 100, 100))
                        draw_text(screen, p_setting.mainFont, 13, "按 F 键开始游戏", (170, 157), (100, 100, 100))
                        pygame.display.update()
                        clock.tick_busy_loop(400) 
                        pygame.time.delay(1300)

                    elif (opt_pokemon01s[selectionPointer.flag] in myPokemon01s):
                        # 不允许重复选择，选择同一只 作 取消选择
                        myPokemon01s.remove(opt_pokemon01s[selectionPointer.flag])

                elif event.key == ord('f'):
                    # 玩家 结束选择
                    if (myPokemon01s):
                        screen.blit(p_setting.loadingPage, (0, 0))
                        draw_text(screen, p_setting.mainFont, 13, "已选择 %d 只 pokemon" % len(myPokemon01s), (185, 137),
                                  (100, 100, 100))
                        draw_text(screen, p_setting.mainFont, 13, "游戏马上开始...", (185, 157), (100, 100, 100))
                        pygame.display.update()
                        clock.tick_busy_loop(400) 
                        pygame.time.delay(1300)
                        return
                    else:
                        # 不允许不选择 pokemon
                        screen.blit(p_setting.loadingPage, (0, 0))
                        draw_text(screen, p_setting.mainFont, 13, "还未选择 pokemon ！", (185, 137), (100, 100, 100))
                        draw_text(screen, p_setting.mainFont, 13, "按 Enter 键进行选择", (185, 157), (100, 100, 100))
                        pygame.display.update()
                        clock.tick_busy_loop(400) 
                        pygame.time.delay(1500)

                elif event.key == pygame.K_UP:
                    selectionPointer.moveUp()
                elif event.key == pygame.K_DOWN:
                    selectionPointer.moveDown()
                elif event.key == pygame.K_LEFT:
                    selectionPointer.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    selectionPointer.moveRight()


def selectMode(p_setting, screen, ModePointer, clock):
    while True:
        screen.blit(p_setting.mode_bg, (0, 0))
        ModePointer.blitme()
        pygame.display.update()
        clock.tick_busy_loop(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ModePointer.moveUp()
                elif event.key == pygame.K_DOWN:
                    ModePointer.moveDown()
                elif event.key == pygame.K_RETURN:
                    return ModePointer.flag



def drawGetCoins(screen, level, coins, clock):
    getCoinImage = pygame.image.load("../othersource/Pic/get_coins.png")
    screen.blit(getCoinImage, (0, 0))
    getCoins = int(level * 20 * random.uniform(1.1, 1.5))  # 本关获得的金币
    coins += getCoins
    draw_text(screen, "../othersource/font/SiYuanMedium.otf", 15, "游戏胜利！获得 %d 个金币!" % (getCoins), (165, 144),
              (74, 73, 74))  # 数据待测试
    pygame.display.update()
    clock.tick_busy_loop(400) 
    return coins


def choosePrize(screen, prizes, myPokemon01s, coins, clock):
    tempPrizes = random.sample(prizes, 3)
    prizePointer = PrizePointer(screen)
    prizePos = ((102, 123), (249, 123), (395, 123))  # 存放绘制奖励的位置信息（center坐标）
    prizeBg = pygame.image.load("../othersource/Pic/selectPrize_bg.jpg")
    pygame.event.pump()
    while True:
        screen.blit(prizeBg, (0, 0))
        drawCoins(screen, coins)
        prizePointer.blitme()
        for i in range(3):
            tempPrizes[i].rect.center = prizePos[i]
            tempPrizes[i].blitme()
        pygame.display.update()
        clock.tick_busy_loop(400) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    prizePointer.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    prizePointer.moveRight()
                elif event.key == pygame.K_RETURN:
                    screen.blit(pygame.image.load("../othersource/Pic/notes_bg.png"), (0, 0))
                    draw_text(screen, "../othersource/font/SiYuanMedium.otf", 13,
                                "您已选择 %s" % tempPrizes[prizePointer.flag].name, (185, 147), (100, 100, 100))
                    pygame.display.update()
                    clock.tick_busy_loop(400) 
                    pygame.time.delay(1500)

                    return tempPrizes[prizePointer.flag].useBuff()

                elif event.key == ord('p'):
                    checkPokemon01s(screen, myPokemon01s, clock)


def store(screen, level, coins, storeGoods, myPokemon01s, clock):
    # 这里的myPokemon01s是列表（不是对象）
    # cost = 0
    if level % 3!=1:
        return
    else:
        screen.blit(pygame.image.load("../othersource/Pic/store1.png"), (0, 0))
        # drawCoins(screen, coins)
        draw_text(screen, "../othersource/font/SiYuanMedium.otf", 12, str(coins), (227, 280), (200, 200, 200))
        pygame.display.update()
        clock.tick_busy_loop(400) 
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('n'):
                        return
                    elif event.key == ord('y'):
                        return drawStore(screen, storeGoods, coins, myPokemon01s, clock)

def drawStore(screen, storeGoods, coins, myPokemon01s, clock):
    # 这里的myPokemon01s是列表（不是对象）
    # 进入商店，返回花费的金币数
    cost = 0            # 花费的金币数
    tempGoods = random.sample(storeGoods, 3)
    storeBg = pygame.image.load("../othersource/Pic/storeBg.jpg")
    storePointer = StorePointer(screen)
    goodsPos = ((102, 123), (249, 123), (395, 123))
    while True:
        
        screen.blit(storeBg, (0, 0))
        drawCoins(screen, coins)
        storePointer.blitme()
        for i in range(3):
            tempGoods[i].rect.center = goodsPos[i]
            tempGoods[i].blitme()
            tempGoods[i].drawPrice()
        pygame.display.update()
        clock.tick_busy_loop(400) 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord('b'):
                    return cost
                elif event.key == ord('p'):
                    checkPokemon01s(screen, myPokemon01s)
                elif event.key == pygame.K_LEFT:
                    storePointer.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    storePointer.moveRight()
                elif event.key == pygame.K_RETURN:
                    if coins>=tempGoods[storePointer.flag].price:
                        tempGoods[storePointer.flag].useBuff()
                        coins -= tempGoods[storePointer.flag].price
                        cost += tempGoods[storePointer.flag].price
                        screen.blit(pygame.image.load("../othersource/Pic/notes_bg.png"), (0,0))
                        draw_text(screen, "../othersource/font/SiYuanMedium.otf", 13, "您购买了 %s"%tempGoods[storePointer.flag].name, (185,147), (100, 100, 100))
                        pygame.display.update()
                        clock.tick_busy_loop(400) 
                        pygame.time.delay(1000)
                    else:
                        # 玩家钱不够
                        screen.blit(pygame.image.load("../othersource/Pic/notes_bg.png"), (0,0))
                        draw_text(screen, "../othersource/font/SiYuanMedium.otf", 13, "您没有足够的金币!", (190,147), (100, 100, 100))
                        pygame.display.update()
                        clock.tick_busy_loop(400) 
                        pygame.time.delay(1000)


def drawCoins(screen, coins):
    draw_text(screen, "../othersource/font/SiYuanMedium.otf", 12, str(coins), (227, 280), (74, 73, 74))


def drawNextLevel(screen, level, myPokemon01s, coins, clock):
    nextLevelImage = pygame.image.load("../othersource/Pic/next_level.jpg")
    while True:
        
        screen.blit(nextLevelImage, (0, 0))
        drawCoins(screen, coins)
        draw_text(screen, "../othersource/font/迷你简剪纸.TTF", 40, "进入第%d关" % (level), (160, 140), (74, 73, 74))
        pygame.display.update()
        clock.tick_busy_loop(400) 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord("p"):
                    checkPokemon01s(screen, myPokemon01s, clock)
                if event.key == pygame.K_RETURN:
                    return
            pygame.event.pump()


def healPokemons(pokemons):
    # 每关恢复玩家pokemon的PP和血量（最大血量的一半）
    for pokemon in pokemons:
        pokemon.alive = True
        pokemon.health += pokemon.maxHealth / 2
        if pokemon.health > pokemon.maxHealth:
            pokemon.health = pokemon.maxHealth


def checkPokemon01s(screen, myPokemon01s, clock):
    # 这里的myPokemon01s是列表（不是对象）
    # 创建查看宠物界面的指针
    checkPokemon01sPointer = CheckPokemon01sPointer(screen, myPokemon01s)
    # 加载背景图片
    playerPokemonsImage = pygame.image.load("../othersource/Pic/playerPokemons.jpg")
    # 记录位置信息
    pokemonPos = [(22, 54), (110, 54), (22, 138), (110, 138), (22, 222), (110, 222)]
    skillPos = [(220, 183), (360, 183), (220, 244), (360, 244)]
    swap = []
    while True:
        
        pointedPokemon = myPokemon01s[checkPokemon01sPointer.flag]  # 此时指针指向的pokemon
        screen.blit(playerPokemonsImage, (0, 0))
        for i in range(len(myPokemon01s)):
            screen.blit(myPokemon01s[i].miniImage, pokemonPos[i])

        draw_text(screen, "../othersource/font/SiYuanMedium.otf", 14,
                  "%d / %d" % (pointedPokemon.health, pointedPokemon.maxHealth), (345, 82), (74, 73, 74))
        healthPer = int(pointedPokemon.health / pointedPokemon.maxHealth * 100) // 10 * 10
        screen.blit(pygame.image.load("../othersource/Pic/healthBar" + str(healthPer) + ".png"), (280, 62))

        for i in range(len(pointedPokemon.skills)):
            draw_text(screen, "../othersource/font/SiYuanMedium.otf", 14, pointedPokemon.skills[i].name, skillPos[i],
                      (74, 73, 74))
            draw_text(screen, "../othersource/font/SiYuanMedium.otf", 12,
                      "PP %d / %d" % (pointedPokemon.skills[i].nowPP, pointedPokemon.skills[i].maxPP),
                      (skillPos[i][0] + 59, skillPos[i][1] - 10), (74, 73, 74))
            draw_text(screen, "../othersource/font/SiYuanMedium.otf", 12, "属性 " + pointedPokemon.skills[i].attribute,
                      (skillPos[i][0] + 59, skillPos[i][1] + 10), (74, 73, 74))
        checkPokemon01sPointer.blitme()
        pygame.display.update()
        clock.tick_busy_loop(400) 

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.QUIT:
                    sys.exit()
                elif event.key == pygame.K_UP:
                    checkPokemon01sPointer.moveUp()
                elif event.key == pygame.K_DOWN:
                    checkPokemon01sPointer.moveDown()
                elif event.key == pygame.K_LEFT:
                    checkPokemon01sPointer.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    checkPokemon01sPointer.moveRight()
                elif event.key == pygame.K_RETURN:
                    if checkPokemon01sPointer.flag<len(myPokemon01s):
                        swap.append(checkPokemon01sPointer.flag)
                    if len(swap)>=2:
                        temp = myPokemon01s[swap[0]]
                        myPokemon01s[swap[0]] = myPokemon01s[swap[1]]
                        myPokemon01s[swap[1]] = temp
                        swap.pop()
                        swap.pop()
                        pygame.display.update()
                elif event.key == ord("b"):
                    # del checkPokemon01sPointer
                    return 
    # print(myPokemon01s)


def selectPokemonBetFight(p_setting, screen, opt_pokemon01s, selectionPointer, myPokemon01s, num, clock, coins):
    # 玩家选择 pokemon
    selection = None
    while True:
        screen.blit(p_setting.selection[num], (0, 0))
        selectionPointer.blitme()
        drawCoins(screen, coins)
        if selection:
            if selection%2:
                screen.blit(pygame.image.load("../othersource/Pic/tick.png"), (135, 201))

            else:
                screen.blit(pygame.image.load("../othersource/Pic/tick.png"), (322, 201))
        pygame.display.update()
        clock.tick_busy_loop(400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if selection==None:
                        selection = selectionPointer.flag+1
                    elif (selectionPointer.flag == selection-1):
                        selection = None
                    else:
                        selection = selectionPointer.flag+1
                elif event.key == ord('f'):
                    # 玩家 结束选择
                    if (selection):
                        myPokemon01s.append(opt_pokemon01s[selection-1])
                        screen.blit(p_setting.loadPage[num], (0, 0))
                        draw_text(screen, p_setting.mainFont, 13, "已选择 %s" % opt_pokemon01s[selection-1].name, (185, 137),
                                  (100, 100, 100))
                        draw_text(screen, p_setting.mainFont, 13, "游戏马上开始...", (185, 157), (100, 100, 100))
                        pygame.display.update()
                        clock.tick_busy_loop(400) 
                        pygame.time.delay(1300)
                        return
                    else:
                        # 不允许不选择 pokemon
                        screen.blit(p_setting.loadPage[num], (0, 0))
                        draw_text(screen, p_setting.mainFont, 13, "还未选择 pokemon ！", (185, 137), (100, 100, 100))
                        draw_text(screen, p_setting.mainFont, 13, "按 Enter 键进行选择", (185, 157), (100, 100, 100))
                        pygame.display.update()
                        clock.tick_busy_loop(400) 
                        pygame.time.delay(1500)

                elif event.key == pygame.K_LEFT:
                    # selected = False

                    selectionPointer.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    # selected = False

                    selectionPointer.moveRight()