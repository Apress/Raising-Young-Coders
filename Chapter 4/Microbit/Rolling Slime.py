from microbit import *
import music
image = Image('00500:'
              '05050:'
              '59095:'
              '50005:'
              '05550')
display.show(image)
while True:
    if accelerometer.was_gesture('up'):
        display.show(image.shift_down(1))
        audio.play(Sound.YAWN)
    if accelerometer.was_gesture('down'):
        display.show(image.shift_up(1))
        audio.play(Sound.HAPPY)
    if accelerometer.was_gesture('left') or button_a.was_pressed():
        display.show(image.shift_left(1))
        audio.play(Sound.SLIDE)
    if accelerometer.was_gesture('right') or button_b.was_pressed():
        display.show(image.shift_right(1))
        audio.play(Sound.SLIDE)
    if pin_logo.is_touched():
        music.play(music.NYAN, wait=False)
        for i in range(5):
            display.show(image.shift_up(i))
            sleep(500)
        for i in range(5, -1, -1):
            display.show(image.shift_up(i))
            sleep(500)
