# import pygame
# import time
# import random
#
# # Pygame ni initsializatsiya qilish
# pygame.init()
#
# # Ranglar
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)
#
# # Oyna oʻlchamlari
# display_width = 800
# display_height = 600
#
# # Displeyni yaratish
# dis = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Ilon Oʻyini')
#
# # Vaqtni boshqarish uchun clock
# clock = pygame.time.Clock()
#
# # Ilonning boshlangʻich tezligi va hujayra oʻlchami
# snake_block = 10
# snake_speed = 15
#
# # Fontlar
# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)
#
#
# def your_score(score):
#     value = score_font.render("Hisob: " + str(score), True, black)
#     dis.blit(value, [0, 0])
#
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
#
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [display_width / 6, display_height / 3])
#
# def gameLoop():
#     game_over = False
#     game_close = False
#
#     # Ilonning boshlangʻich pozitsiyasi
#     x1 = display_width / 2
#     y1 = display_height / 2
#
#     # Harakatlarni saqlash uchun oʻzgaruvchilar
#     x1_change = 0
#     y1_change = 0
#
#     # Ilon tanasi
#     snake_List = []
#     Length_of_snake = 1
#
#     # Ovqat pozitsiyasi
#     foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
#
#     while not game_over:
#
#         while game_close == True:
#             dis.fill(white)
#             message("Siz yutqazdingiz! C-ni bosib qayta oʻyna yoki Q-ni bosib chiqing", red)
#             your_score(Length_of_snake - 1)
#             pygame.display.update()
#
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
#
#         # Chegaralardan chiqib ketishni tekshirish
#         if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(white)
#         pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
#         snake_Head = []
#         snake_Head.append(x1)
#         snake_Head.append(y1)
#         snake_List.append(snake_Head)
#         if len(snake_List) > Length_of_snake:
#             del snake_List[0]
#
#         # Ilon oʻzini yeb qoʻysa
#         for x in snake_List[:-1]:
#             if x == snake_Head:
#                 game_close = True
#
#         our_snake(snake_block, snake_List)
#         your_score(Length_of_snake - 1)
#
#         pygame.display.update()
#
#         # Ovqatni yeganlikni tekshirish
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
#             Length_of_snake += 1
#
#         clock.tick(snake_speed)
#
#     pygame.quit()
#     quit()
#
# gameLoop()













# import pygame
# import random
# import sys
#
# # Oʻyin sozlamalari
# pygame.init()
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Tovushqon va Olma")
#
# clock = pygame.time.Clock()
#
#
# # Ranglar
# white = (255, 255, 255)
# red = (255, 0, 0)
# green = (0, 255, 0)
# brown = (139, 69, 19)
#
#
# # Tovushqon
# rabbit_img = pygame.Surface((60, 80))
# rabbit_img.fill(brown)
# rabbit_x = width // 2
# rabbit_y = height - 100
# rabbit_speed = 10
#
# # Olma
# apple_img = pygame.Surface((30, 30))
# apple_img.fill(red)
# apple_x = random.randint(0, width - 30)
# apple_y = 0
# apple_speed = 5
#
#
# # Hisob
# score = 0
# font = pygame.font.SysFont(None, 36)
#
# def show_score():
#     text = font.render(f"Hisob: {score}", True, green)
#     screen.blit(text, (10, 10))
#
# # Asosiy oʻyin tsikli
# running = True
# while running:
#     screen.fill(white)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Tovushqonni boshqarish
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and rabbit_x > 0:
#         rabbit_x -= rabbit_speed
#     if keys[pygame.K_RIGHT] and rabbit_x < width - 60:
#         rabbit_x += rabbit_speed
#
#     # Olma tushadi
#     apple_y += apple_speed
#     if apple_y > height:
#         apple_y = 0
#         apple_x = random.randint(0, width - 30)
#         score -= 1  # Agar tushsa, ochko kamayadi
#
#     # Tovushqon olmani ushlashi
#     if (rabbit_x < apple_x + 30 and
#         rabbit_x + 60 > apple_x and
#         rabbit_y < apple_y + 30 and
#         rabbit_y + 80 > apple_y):
#         score += 1
#         apple_y = 0
#         apple_x = random.randint(0, width - 30)
#
#     # Objektlarni chizish
#     screen.blit(rabbit_img, (rabbit_x, rabbit_y))
#     screen.blit(apple_img, (apple_x, apple_y))
#     show_score()
#
#     pygame.display.flip()
#     clock.tick(30)
#
# pygame.quit()
# sys.exit()


def decarator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.perf_counter()
        result=func



















