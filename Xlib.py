from Xlib import X, display
disp = display.Display()
screen = disp.screen()
root =  screen.root
root.warp_pointer(100, 200)
d.sync()