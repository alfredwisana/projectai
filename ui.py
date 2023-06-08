import pygame
import math
import genetic_algorithm as ga

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class ButtonImage(object):
    def __init__(self, position, size, path, path2):
        self.pos = position
        self.path2 = path2
        self.img = pygame.transform.scale(pygame.image.load(path), size)
        self.rect = pygame.Rect(position, size)
        screen.blit(self.img, position)
        self.size = size

    def draw(self, screen):
        screen.blit(self.img, self.pos)

    def is_hover(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

    def hover(self, screen):
        img2 = pygame.transform.scale(pygame.image.load(self.path2), self.size)
        screen.blit(img2, self.pos)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)


def draw_text(surface, message, y_cord, font_size, color):
    font = pygame.font.Font(None, font_size)
    text = font.render(message, 1, color)
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, y_cord/10))
    surface.blit(text, text_rect)


def startScreen(screen):
    SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
    pygame.display.set_caption('PROJECT KECERDASAN BUATAN')
    # Load image
    bg = pygame.image.load('projectai/assets/bg.png')
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_width = bg.get_width()
    bg_rect = bg.get_rect()
    # Scrolling background
    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    run = True
    while run:
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll
            pygame.draw.rect(screen, (0, 0, 0), bg_rect, 1)
            scroll -= 1
            if abs(scroll) > bg_width:
                scroll = 0
        start = ButtonImage((400, 200), (400, 100), 'projectai/assets/start1.png', 'projectai/assets/start2.png')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.is_clicked(event):
                    inputNMesinScreen(screen)

        pos = pygame.mouse.get_pos()

        if pos[0] >= 50 and pos[0] <= 250 and pos[1] >= 150 and pos[1] <= 210:
            start.hover(screen)
        else:
            start.draw(screen)

        pygame.display.update()


def inputNMesinScreen(screen):
    SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
    pygame.display.set_caption('PROJECT KECERDASAN BUATAN')
    WHITE = (255, 255, 255)
    # Load image
    bg = pygame.image.load('projectai/assets/bg.png')
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_width = bg.get_width()
    bg_rect = bg.get_rect()
    masukkanNMesin = pygame.transform.scale(pygame.image.load('projectai/assets/masukkanNMesin.png'), (700, 100))
    finish = ButtonImage((360, 360), (200, 60), 'projectai/assets/finish2.png', 'projectai/assets/finish1.png')
    # Input box properties
    input_box = pygame.Rect(200, 200, 300, 40)
    input_text = ""
    font = pygame.font.Font(None, 32)
    # Scrolling background
    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    run = True
    while run:
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll
            pygame.draw.rect(screen, (0, 0, 0), bg_rect, 1)
            scroll -= 1
            if abs(scroll) > bg_width:
                scroll = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RETURN:
                    print(input_text)
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if event.unicode.isnumeric():
                        input_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if finish.is_clicked(event):
                        # print("klik")
                        ga.jumlah = int(input_text)
                        # ga.printJumlah()
                        inputWattMaintenanceScreen(screen)
        # Draw the input box
        pygame.draw.rect(screen, WHITE, input_box, 2)
        # Render the input text
        text_surface = font.render(input_text, True, WHITE)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 10))

        screen.blit(masukkanNMesin, (200, 100))
        # ga.main(int(input_text))
        pos = pygame.mouse.get_pos()
        if pos[0] >= 360 and pos[0] <= 560 and pos[1] >= 360 and pos[1] <= 420:
            finish.hover(screen)
        else:
            finish.draw(screen)

        pygame.display.update()


def inputWattMaintenanceScreen(screen):
    SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
    pygame.display.set_caption('PROJECT KECERDASAN BUATAN')
    WHITE = (255, 255, 255)
    # Load image
    bg = pygame.image.load('projectai/assets/bg.png')
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_width = bg.get_width()
    bg_rect = bg.get_rect()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FONT = pygame.font.Font(None, 32)
    # Input box properties
    input_box1 = pygame.Rect(310, SCREEN_HEIGHT / 4, 300, 40)  # kotak pertama
    input_box2 = pygame.Rect(310, SCREEN_HEIGHT / 2, 300, 40)  # kotak kedua

    text1 = ""
    text2 = ""

    active_input = None

    font = pygame.font.Font(None, 32)
    # Scrolling background
    scroll = 0
    counter = ga.jumlah
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    run = True
    current_number = 1
    while run:
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll
            pygame.draw.rect(screen, (0, 0, 0), bg_rect, 1)
            scroll -= 1
            if abs(scroll) > bg_width:
                scroll = 0
        finish = ButtonImage((360, 360), (200, 60), 'projectai/assets/finish1.png', 'projectai/assets/finish2.png')
        inputNMesin = pygame.transform.scale(pygame.image.load('projectai/assets/inputFrame.png'), (550, 400))
        masukkanNWattMesin = pygame.transform.scale(pygame.image.load('projectai/assets/masukkanNWattMesin.png'),
                                                    (500, 80))
        masukkanNMinMaintenance = pygame.transform.scale(
            pygame.image.load('projectai/assets/masukkanNMinMaintenance.png'), (500, 80))
        # inputFrame = ButtonImage((190, 80), (550, 400), 'assets/inputFrame1.png', 'assets/inputFrame2.png')

        if counter > 0:
            draw_text(screen, "Inputan mesin ke-" + str(current_number), 300, 30, (WHITE))
        elif text1 == "" or text2 == "":
            draw_text("Kolom tidak boleh kosong")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif active_input:
                    if event.key == pygame.K_RETURN:
                        active_input = None
                    elif event.key == pygame.K_BACKSPACE:
                        if active_input == input_box1:
                            text1 = text1[:-1]
                        elif active_input == input_box2:
                            text2 = text2[:-1]
                    else:
                        if active_input == input_box1:
                            if event.unicode.isnumeric():
                                text1 += event.unicode
                        elif active_input == input_box2:
                            if event.unicode.isnumeric():
                                text2 += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box1.collidepoint(event.pos):
                    active_input = input_box1
                elif input_box2.collidepoint(event.pos):
                    active_input = input_box2
                elif finish.is_clicked:
                    if counter > 0:
                        if text1 == "" or text2 == "":
                            print("kolom tidak boleh kosong")
                        else:
                            ga.min_maintenance.append(int(text2))
                            ga.jumlah_watt.append(int(text1))
                            # print(counter)
                            counter -= 1
                            current_number += 1
                            text1 = ""
                            text2 = ""
                            if counter == 0:
                                print(ga.min_maintenance)
                                inputNMinWattScreen(screen)
                else:
                    active_input = None

        pygame.draw.rect(screen, WHITE, input_box1, 2)
        pygame.draw.rect(screen, WHITE, input_box2, 2)

        input_text1 = FONT.render(text1, True, WHITE)
        input_text2 = FONT.render(text2, True, WHITE)

        screen.blit(input_text1, (input_box1.x + 5, input_box1.y + 5))
        screen.blit(input_text2, (input_box2.x + 5, input_box2.y + 5))

        # pygame.display.flip()

        pos = pygame.mouse.get_pos()
        # print(pos)
        if pos[0] >= 360 and pos[0] <= 560 and pos[1] >= 360 and pos[1] <= 420:
            finish.hover(screen)
        else:
            finish.draw(screen)
        screen.blit(inputNMesin, (190, 80))
        screen.blit(masukkanNWattMesin, (220, 80))
        screen.blit(masukkanNMinMaintenance, (220, 212))

        pygame.display.update()


def inputNMinWattScreen(screen):
    SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
    pygame.display.set_caption('PROJECT KECERDASAN BUATAN')
    WHITE = (255, 255, 255)
    # Load image
    bg = pygame.image.load('projectai/assets/bg.png')
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_width = bg.get_width()
    bg_rect = bg.get_rect()
    masukkanNWattDibutuhkan = pygame.transform.scale(pygame.image.load('projectai/assets/masukkanNWattDibutuhkan.png'),
                                                     (700, 100))
    finish = ButtonImage((360, 360), (200, 60), 'projectai/assets/finish2.png', 'projectai/assets/finish1.png')
    # Input box properties
    input_box = pygame.Rect(200, 200, 300, 40)
    input_text = ""
    font = pygame.font.Font(None, 32)
    # Scrolling background
    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    run = True
    while run:
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll
            pygame.draw.rect(screen, (0, 0, 0), bg_rect, 1)
            scroll -= 1
            if abs(scroll) > bg_width:
                scroll = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(input_text)
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                # biar cuma bisa input angka
                else:
                    if event.unicode.isnumeric():
                        input_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if finish.is_clicked(event):
                    # print("klik")
                    ga.min_watt = int(input_text)
                    ga.hitung_total()
                    if ga.min_watt >= ga.total_watt:
                        # print(ga.min_watt)
                        print("Jumlah listrik minimal yang dihasilkan : %d "%ga.total_watt)
                        print("Jumlah listrik melebihi kapasitas")
                        inputNMinWattScreen(screen)
                    ga.main()
                    mutasiScreen(screen)
                    # Draw the input box
        pygame.draw.rect(screen, WHITE, input_box, 2)
        # Render the input text
        text_surface = font.render(input_text, True, WHITE)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 10))

        screen.blit(masukkanNWattDibutuhkan, (200, 100))
        pos = pygame.mouse.get_pos()
        if pos[0] >= 360 and pos[0] <= 560 and pos[1] >= 360 and pos[1] <= 420:
            finish.hover(screen)
        else:
            finish.draw(screen)

        pygame.display.update()


def mutasiScreen(screen):
    pygame.display.set_caption('PROJECT KECERDASAN BUATAN')
    SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
    table_width, table_height = 910, 490
    column_widths = [100] + [50] * 12
    rows_per_page = 5

    pygame.init()
    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Load background image
    bg = pygame.image.load('projectai/assets/bg.png')
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_width = bg.get_width()
    bg_rect = bg.get_rect()

    # Calculate table position
    table_x = 25
    table_y = 25

    # Define table data
    table_data = [
        ["FP", "Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"],
    ]
    for iterasi in ga.hasil_iterasi:
        for item in iterasi:
            tmp = []
            fp, ch = item
            tmp.append(str(fp))
            for x in ch:
                tmp.append(str(inner_list) for inner_list in x)
                print(tmp)
            table_data.append(item)

    row_per_page = 10
    columns_per_page = 13

    current_page = 0
    total_pages = len(table_data) // row_per_page
    font = pygame.font.Font(None, 30)

    # Scrolling background
    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    run = True
    while run:
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll
            pygame.draw.rect(screen, (0, 0, 0), bg_rect, 1)
            scroll -= 1
            if abs(scroll) > bg_width:
                scroll = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_page -= 1
                    if current_page < 0:
                        current_page = 0
                elif event.key == pygame.K_RIGHT:
                    current_page += 1
                    if current_page >= total_pages:
                        current_page = total_pages - 1
        start_row = current_page * row_per_page
        end_row = start_row + row_per_page
        current_data = table_data[start_row:end_row]

        pygame.draw.rect(screen, (255, 255, 255), (table_x, table_y, table_width, table_height))

        font = pygame.font.Font(None, 24)
        for i, row in enumerate(current_data):
            for j, value in enumerate(row):
                text = font.render(str(value), True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (table_x + (j + 0.5) * (table_width / columns_per_page),
                                    table_y + (i + 0.5) * (table_height / rows_per_page))
                screen.blit(text, text_rect)

        pygame.display.update()


def hasilScreen(screen):
    SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
    pygame.display.set_caption('PROJECT KECERDASAN BUATAN')
    # Load image
    bg = pygame.image.load('projectai/assets/bg.png')
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_width = bg.get_width()
    bg_rect = bg.get_rect()
    # Scrolling background
    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    run = True
    while run:
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll
            pygame.draw.rect(screen, (0, 0, 0), bg_rect, 1)
            scroll -= 1
            if abs(scroll) > bg_width:
                scroll = 0
        start = ButtonImage((400, 200), (400, 100), 'projectai/assets/start1.png', 'projectai/assets/start2.png')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.is_clicked(event):
                    inputNMesinScreen(screen)

        pos = pygame.mouse.get_pos()

        if pos[0] >= 50 and pos[0] <= 250 and pos[1] >= 150 and pos[1] <= 210:
            start.hover(screen)
        else:
            start.draw(screen)

        pygame.display.update()


startScreen(screen)
pygame.quit()
