import pygame
import random


pygame.init()
window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Flappy Bird by GS")
clock = pygame.time.Clock()


class user:
    def __init__(self):
        self.xPos = 200
        self.yPos = 300
        self.birdPic = pygame.transform.scale(pygame.image.load("Data/bird.png"), (80, 60))

        self.points = [[self.xPos+40, self.yPos], [self.xPos+40, self.yPos+60], [self.xPos+80, self.yPos+30]]
        

    def move(self, moveBy):
        self.yPos -= moveBy

        for point in self.points:
            point[1] -= moveBy


    def draw(self):
        window.blit(self.birdPic, (self.xPos, self.yPos))

class object:
    def __init__(self, xPos, yPos, height, width):
        self.xPos = xPos
        self.yPos = yPos
        self.height = height
        self.width = width
        self.coords = [xPos, yPos, xPos+width, yPos+height]

        if self.yPos > 400:
            self.picture =  pygame.transform.scale(main.tunnelPic, (self.width, self.height))
        else:
            self.picture = pygame.transform.flip((pygame.transform.scale(main.tunnelPic, (self.width, self.height))), False, True)

        self.rect = self.picture.get_rect()

    def draw(self):
        window.blit(self.picture, (self.xPos, self.yPos))
        


class MainClass:
    def __init__(self):
        self.bigtext = pygame.font.SysFont("comic sans", 80)
        self.backgroundPic = pygame.transform.scale((pygame.image.load("Data/background.jpg"))
                                , (1200, 800))
        
        self.tunnelPic = pygame.image.load("Data/tunnelPic.jpg")
        self.tunnelPic.set_colorkey((255, 255, 255))
        
        self.allObjects = []


    def draw(self):
        global running 
        window.blit(self.backgroundPic, (0, 0, 1200, 800))

        bird.draw()

        for obj in self.allObjects:
            obj.draw()

        if running == False:
            pygame.draw.rect(window, "red", (300, 200, 600, 200))
            newText = self.bigtext.render("You Lost!", 20, "black")
            window.blit(newText, (400, 260, 100, 100))



        pygame.display.update()





window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Flappy Bird by GS")
clock = pygame.time.Clock()
main = MainClass()
bird = user()

count = 0
lastMade = 900
difficulty = 1
running = True
pace = 80
fallingMultiplier = 1
sinceLastMove = 0

while running == True:
    clock.tick(60)
    lastMade += pace
    sinceLastMove += 1
    count += pace
    bird.move(-fallingMultiplier)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keyPressed = pygame.key.get_pressed()


    if keyPressed[pygame.K_SPACE]:
        bird.move(13)
        fallingMultiplier = 1


    toPop = []
    for index in range(len(main.allObjects)):
        obj = main.allObjects[index]

   
        for coords in bird.points:
            newRect = pygame.Rect(obj.rect[0]+obj.xPos, obj.rect[1]+obj.yPos, obj.rect[2], obj.rect[3])
            if newRect.collidepoint (coords[0], coords[1]):
                running = False

        if obj.xPos < -400:
            toPop.append(index)

        else:
            obj.xPos -= 2
            obj.coords[1] -= 2
            obj.coords[3] -= 2







    for i in toPop:
        main.allObjects.pop(i)


    if lastMade > (pace * random.randint(130, 450)):
        lastMade = 0

        if difficulty == 1:
            ranHeight1 = random.randint(240, 350)
            ranHeight2 = random.randint(240, 350)

        elif difficulty == 2:
            ranHeight1 = random.randint(230, 340)
            ranHeight2 = random.randint(230, 340)

        newWidth = random.randint(80, 150)

            

        main.allObjects.append(object(1200, 0, ranHeight1, newWidth))
        main.allObjects.append(object(1200, 800-ranHeight2, ranHeight2, newWidth))

    if sinceLastMove > 25:
        fallingMultiplier += 1
        sinceLastMove = 0

    main.draw()



running2 = True
while running2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running2 = False



   
    main.draw()

