import pygame,time
pygame.init()
s=pygame.display.set_mode((640,480))

"""
pygame tends to loose focus on Mac OS X, 
to work around the issue, I
created a user-event to make some noise in the event queue
and regain the focus with event.wait() after each time.sleep() 
"""
def MySleep(seconds): # a sleep function won't get pygame screen loose focus 
        
    # the user-Event
    D = {'frameDrawDone': 1};
    userEvent =  pygame.event.Event(pygame.USEREVENT, D)

    pygame.event.post(userEvent) # pitch the event into the event queue
    time.sleep(seconds)
    event = pygame.event.wait() # help pygame to regain the focus
"""
# test 

for idx in range(10):

    p1=pygame.image.load(str(idx+1)+".png").convert()
    s.blit(p1,(0,0))
    pygame.display.update()
    MySleep(0.1)
"""

p1=pygame.image.load("1.png")
s.blit(p1,(0,0))
pygame.display.update()
MySleep(0.1)


p2=pygame.image.load("2.png")
s.blit(p2,(0,0))
pygame.display.update()
MySleep(0.1)

p3=pygame.image.load("3.png")
s.blit(p3,(0,0))
pygame.display.update()
MySleep(0.1)

p4=pygame.image.load("4.png")
s.blit(p4,(0,0))
pygame.display.update()
MySleep(0.1)

p5=pygame.image.load("5.png")
s.blit(p5,(0,0))
pygame.display.update()
MySleep(0.1)

p6=pygame.image.load("6.png")
s.blit(p6,(0,0))
pygame.display.update()
MySleep(0.1)

p7=pygame.image.load("7.png")
s.blit(p7,(0,0))
pygame.display.update()
MySleep(0.1)

p8=pygame.image.load("8.png")
s.blit(p8,(0,0))
pygame.display.update()
MySleep(0.1)


p9=pygame.image.load("9.png")
s.blit(p9,(0,0))
pygame.display.update()
MySleep(0.1)

p10=pygame.image.load("10.png")
s.blit(p10,(0,0))
pygame.display.update()
MySleep(0.1)

# quit elegantly
time.sleep(2)
pygame.quit()
