class SkillImage(object):
    def __init__(self, image, rect_x, rect_y, p_setting, screen):
        self.image = image
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.p_setting = p_setting
        self.screen = screen

    def blitme(self):
        self.screen.blit(self.image, (self.rect_x, self.rect_y))
