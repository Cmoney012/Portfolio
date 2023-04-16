import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Faerie Tale")
game_active = True

pygame.mouse.get_pos()

title_font = pygame.font.Font('Font/roman_font_7.ttf', 50)
title_text = title_font.render("'Faerie Tale'", False, "#ab41e0")
tt_rect = title_text.get_rect(center=(480, 130))
start_text = title_font.render("Start", False, "#ab41e0")
start_rect = start_text.get_rect(center=(480, 450))


title1 = pygame.image.load('Assets/Medieval_Castle_Asset_Pack/Background/layer_1.png')
title1 = pygame.transform.scale(title1, (960, 540))
t1rect = title1.get_rect(midbottom=(480, 540))
title2 = pygame.image.load('Assets/Medieval_Castle_Asset_Pack/Background/layer_2.png')
title2 = pygame.transform.scale(title2, (960, 393))
t2rect = title2.get_rect(midbottom=(480, 540))
title3 = pygame.image.load('Assets/Medieval_Castle_Asset_Pack/Background/layer_3.png')
title3 = pygame.transform.scale(title3, (960, 120))
t3rect = title3.get_rect(midbottom=(480, 540))


def start():
    screen.fill('Black')
    # screen.blit(title1, t1rect)
    # screen.blit(title2, t2rect)
    # screen.blit(title3, t3rect)





def title_screen():
    screen.blit(title1, t1rect)
    screen.blit(title2, t2rect)
    screen.blit(title3, t3rect)
    screen.blit(title_text, tt_rect)
    screen.blit(start_text, start_rect)


while True:
    title_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(pygame.mouse.get_pos()):
                Start()

    pygame.display.update()



