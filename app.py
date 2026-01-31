import pygame
import requests
import random

# --- INSTELLINGEN ---
# VERVANG DEZE LINK door jouw eigen link van Render!
URL = "https://online-server-tama-2.onrender.com/update"
MIJN_NAAM = "Putsie" 
MIJN_KLEUR = (0, 255, 0) # Felgroen zodat je jezelf goed ziet

pygame.init()
scherm = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tamagotchi World")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

x, y = 400, 300
andere_spelers = {}

running = True
while running:
    # 1. Achtergrond tekenen (donkergrijs)
    scherm.fill((50, 50, 50)) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Bewegen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= 5
    if keys[pygame.K_RIGHT]: x += 5
    if keys[pygame.K_UP]: y -= 5
    if keys[pygame.K_DOWN]: y += 5

    # 3. Teken de Locaties (Zodat het scherm niet leeg is!)
    pygame.draw.rect(scherm, (255, 215, 0), (50, 50, 100, 100))   # BANK
    scherm.blit(font.render("BANK", True, (0,0,0)), (70, 90))
    
    pygame.draw.rect(scherm, (100, 100, 255), (650, 450, 100, 100)) # ARCADE
    scherm.blit(font.render("ARCADE", True, (255,255,255)), (660, 490))

    # 4. Sync met Server (met een korte 'timeout' zodat de game niet bevriest)
    try:
        # We sturen onze info en krijgen de hele wereld terug
        r = requests.post(URL, json={"naam": MIJN_NAAM, "x": x, "y": y, "actie": "update"}, timeout=0.2)
        if r.status_code == 200:
            andere_spelers = r.json().get("spelers", {})
    except:
        # Als de server traag is, tekenen we gewoon even geen andere spelers
        pass

    # 5. Teken andere spelers
    for naam, info in andere_spelers.items():
        if naam != MIJN_NAAM:
            pygame.draw.rect(scherm, (200, 200, 200), (info['x'], info['y'], 40, 40))
            scherm.blit(font.render(naam, True, (255, 255, 255)), (info['x'], info['y'] - 20))

    # 6. Teken jezelf
    pygame.draw.rect(scherm, MIJN_KLEUR, (x, y, 40, 40))
    scherm.blit(font.render("JIJ (" + MIJN_NAAM + ")", True, (255, 255, 255)), (x, y - 25))

    pygame.display.flip()
    clock.tick(60) # 60 frames per seconde voor soepel wandelen

pygame.quit()
