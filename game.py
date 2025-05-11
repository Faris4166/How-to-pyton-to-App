import pygame

# เริ่มต้น pygame
pygame.init()

# ตั้งค่าหน้าต่างเกม
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game")

# สีที่ใช้ในเกม
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# ตัวแปรสำหรับควบคุมการเคลื่อนที่
x, y = screen_width // 2, screen_height // 2
speed = 5

# เกมหลัก
running = True
while running:
    screen.fill(WHITE)  # เติมพื้นหลังด้วยสีขาว
    
    # ตรวจสอบเหตุการณ์ต่างๆ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # ควบคุมการเคลื่อนที่ของตัวละคร
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    # วาดตัวละคร (สี่เหลี่ยม)
    pygame.draw.rect(screen, BLUE, (x, y, 50, 50))
    
    # อัปเดตหน้าจอ
    pygame.display.update()
    
    # ตั้งค่าเฟรมเรต
    pygame.time.Clock().tick(60)

# ออกจากเกม
pygame.quit()
