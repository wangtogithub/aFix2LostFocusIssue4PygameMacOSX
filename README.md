# aFix2LostFocusIssue4PygameMacOSX
A METHOD TO WORK AROUND THE ISSUE THAT PYGAME LOOSES FOCUS AFTER PYGAME.TIME.WAIT() ON MAC OSX MOJAVE.


regain pygame's focus using event handling

make some noise in the event queue with user defined event

then call the pygame.time.wait(xx), pygame window might well loose its focus

after that, regain the focus back with pygame.event.wait()

since there is at least one event, our user event posted earlier, this wait() shall return immediately.
