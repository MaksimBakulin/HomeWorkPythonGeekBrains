import pygame
import sys

def Check_win(massive, symbol):
    zeroes = 0
    for row in massive:
        zeroes += row.count(0)
        if row.count(symbol) == 3:
            return f"Победили - {symbol}"
    for col in range(3):
        if massive[0][col] == symbol and massive[1][col] == symbol and massive[2][col] == symbol:
            return f"Победили - {symbol}"
    if massive[0][0] == symbol and massive[1][1] == symbol and massive[2][2] == symbol:
        return f"Победили - {symbol}"
    if massive[0][2] == symbol and massive[1][1] == symbol and massive[2][0] == symbol:
        return f"Победили - {symbol}"
    if zeroes == 0:
        return "Победила дружба!"
    return False

pygame.init()
size_block = 100
size_margin = 15
width = height = size_block * 3 + size_margin * 4

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики-нолики")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + size_margin)
            row = y_mouse // (size_block + size_margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = "x"
                else:
                    mas[row][col] = "o"
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == "x":
                    color = red
                elif mas[row][col] == "o":
                    color = green
                else:
                    color = white
                x = col * size_block + (col + 1) * size_margin
                y = row * size_block + (row + 1) * size_margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 3)
                    pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 3)
    if (query - 1) % 2 == 0:
        game_over = Check_win(mas, "x")
    else:
        game_over = Check_win(mas, "o")

    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont("stxingkai", 50)
        text_1 = font.render(game_over, True, white)
        text_rect = text_1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text_1, [text_x, text_y])

    pygame.display.update()