import pygame


def update_screen(p_setting, screen, menubar, menubarText, *images):
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


def draw_text(screen, font_name, font_size, text, text_topleft, text_color):
    typeface = pygame.font.Font(font_name, font_size)
    text_image = typeface.render(text, True, text_color)
    text_rect = text_image.get_rect()
    text_rect.topleft = text_topleft
    screen.blit(text_image, text_rect)


def checkDeath(pokemon, p_setting, screen, nowbar, menubar, statebar,
               statebar01, healthbar, healthbar01):
    # 检查 pokemon 是否死亡
    if pokemon.health <= 0:
        update_screen(p_setting, screen, menubar, pokemon.name + " 倒下了！",
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


def selectPokemon(p_setting, screen, opt_pokemon01s, selectionPointer, myPokemon01s):
    # 玩家选择 pokemon
    while True:
        for event in pygame.event.get():

            screen.blit(p_setting.selection_bg, (0, 0))
            selectionPointer.blitme()
            for i in range(len(myPokemon01s)):
                draw_text(screen, p_setting.mainFont, 16, str(i + 1), myPokemon01s[i].orderPos, (100, 100, 100))
            pygame.display.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                        if (opt_pokemon01s[selectionPointer.flag] not in myPokemon01s) and len(myPokemon01s)<6:
                            myPokemon01s.append(opt_pokemon01s[selectionPointer.flag])

                        elif ((opt_pokemon01s[selectionPointer.flag] not in myPokemon01s) and len(myPokemon01s)>=6):
                            # 玩家选择多于 6 只
                            screen.blit(p_setting.loadingPage, (0, 0))
                            draw_text(screen, p_setting.mainFont, 13, "最多只能选择 6 只 pokemon", (170, 137), (100, 100, 100))
                            draw_text(screen, p_setting.mainFont, 13, "按 F 键开始游戏", (170, 157), (100, 100, 100))
                            pygame.display.update()
                            pygame.time.delay(1300)

                        elif (opt_pokemon01s[selectionPointer.flag] in myPokemon01s):
                            # 不允许重复选择，选择同一只 作 取消选择
                            myPokemon01s.remove(opt_pokemon01s[selectionPointer.flag])

                elif event.key == ord('f'):
                    # 玩家 结束选择
                    if(myPokemon01s):
                        screen.blit(p_setting.loadingPage, (0, 0))
                        draw_text(screen, p_setting.mainFont, 13, "已选择 %d 只 pokemon" % len(myPokemon01s), (185, 137),
                                  (100, 100, 100))
                        draw_text(screen, p_setting.mainFont, 13, "游戏马上开始...", (185, 157), (100, 100, 100))
                        pygame.display.update()
                        pygame.time.delay(1300)
                        return
                    else:
                        # 不允许不选择 pokemon
                        screen.blit(p_setting.loadingPage, (0,0))
                        draw_text(screen, p_setting.mainFont, 13, "还未选择 pokemon ！", (185, 137), (100, 100, 100))
                        draw_text(screen, p_setting.mainFont, 13, "按 Enter 键进行选择", (185, 157), (100, 100, 100))
                        pygame.display.update()
                        pygame.time.delay(1500)

                elif event.key == pygame.K_UP:
                    selectionPointer.moveUp()
                elif event.key == pygame.K_DOWN:
                    selectionPointer.moveDown()
                elif event.key == pygame.K_LEFT:
                    selectionPointer.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    selectionPointer.moveRight()