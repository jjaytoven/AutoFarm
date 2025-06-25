#!/usr/bin/env python3
# pip install pyautogui pyobjc-framework-Quartz

import time
import pyautogui



# ─── CONFIG ──────────────────────────────────────────────────────────
WINDOW_TITLE   = "Battle Nations"
loading_screen = 'loading.png'
attack         = 'attack.png'
check          = 'check.png'
heavy          = 'heavy.png'

fight          = 'fight.png'
wimp = 'wimp.png'
loading2       = 'loading2.png'
raptor         = 'raptorwarrior.png'
heavy_back1 = 'heavy_back1.png'
heavy_back2 = 'heavy_back2.png'
heavy_back3 = 'heavy_back3.png'
spray = 'spray.png'
okay_button = 'okay_button.png'
orange_okay = 'orange_okay.png'
cannoneer = 'cannoneer.png'


CONFIDENCE     = 0.6
DELAY_BEFORE   = 6
SCAN_INTERVAL  = 0.5
APPEAR_TIMEOUT = 10    # seconds to wait for each image to appear
# ─────────────────────────────────────────────────────────────────────

def get_scaling():
    screen_w, screen_h = pyautogui.size()
    shot = pyautogui.screenshot()
    shot_w, shot_h = shot.size
    return shot_w / screen_w, shot_h / screen_h

def wait_until_gone(image, confidence=CONFIDENCE, interval=SCAN_INTERVAL):
    """Block until `image` no longer appears on screen."""
    while True:
        try:
            found = pyautogui.locateOnScreen(image, confidence=confidence)
        except pyautogui.ImageNotFoundException:
            # If it never sees the image at all, that's "gone" too
            break

        # If locateOnScreen used to find it but now returns None → also gone
        if found is None:
            break

        # Otherwise it’s still visible, wait a bit and try again
        time.sleep(interval)

def click_image(img, clicks=1, confidence=CONFIDENCE, scale=(1,1), **move_kwargs):
    """Find center of `img`, scale coordinates, move & click."""
    pos = pyautogui.locateCenterOnScreen(img, confidence=confidence)
    if not pos:
        raise RuntimeError(f"Could not find {img} on screen")
    x = pos.x / scale[0]
    y = pos.y / scale[1]
    pyautogui.moveTo(x, y, **move_kwargs)
    print(x, y)
    for _ in range(clicks):
        pyautogui.click()




def main():
    while True:
        time.sleep(DELAY_BEFORE)
        scale = get_scaling()

        # 1) Attack
        click_image(attack, clicks=1, scale=scale, duration=0.2)

        # 2) Check
        click_image(check, clicks=1, scale=scale, duration=0.2)

        # 3) Wait for loading screen to vanish
        wait_until_gone(loading_screen)

        # 4) Heavy place

        heavy_pos = pyautogui.locateCenterOnScreen(heavy, confidence=CONFIDENCE)
        heavy_screen_x = heavy_pos.x / scale[0]
        heavy_screen_y = heavy_pos.y / scale[1]
        pyautogui.mouseDown(heavy_screen_x, heavy_screen_y)
        pyautogui.mouseUp(heavy_screen_x, heavy_screen_y)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.mouseDown()
        pyautogui.mouseUp()


        # 5) Agent
        click_image(wimp, clicks=3, scale=scale, duration=0.2)

        # 6) Fight
        click_image(fight, clicks=1, scale=scale, duration=0.2)

        # 7) Wait for second loading screen
        wait_until_gone(loading2)

        # Battle begins

        # 10) Raptor warrior
        click_image(raptor, clicks=1, scale=scale, duration=0.2)
        time.sleep(SCAN_INTERVAL)
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        # 11 position 1
        time.sleep(12)
        pyautogui.moveTo(514.5, 359.5, duration=0.2)
        pyautogui.mouseDown(514.5, 359.5)
        pyautogui.mouseUp(514.5, 359.5)

        pyautogui.moveTo(561.0, 203.5, duration=0.2)
        pyautogui.mouseDown(561.0, 203.5)
        pyautogui.mouseUp(561.0, 203.5)

        #12 position 2
        time.sleep(12)
        pyautogui.moveTo(636.5, 410.5, duration=0.2)
        pyautogui.mouseDown(636.5, 410.5)
        pyautogui.mouseUp(636.5, 410.5)

        pyautogui.moveTo(561.0, 203.5, duration=0.2)
        pyautogui.mouseDown(561.0, 203.5)
        pyautogui.mouseUp(561.0, 203.5)

        time.sleep(10)
        try:
            pos = pyautogui.locateCenterOnScreen(raptor, confidence=CONFIDENCE)
        except pyautogui.ImageNotFoundException:
            pos = None
        # if raptor not killed on 2 third attack
        if pos:

            pyautogui.moveTo(876.0, 528.0, duration=0.2)
            pyautogui.mouseDown(876.0, 528.0)
            pyautogui.mouseUp(876.0, 528.0)

            pyautogui.moveTo(561.0, 203.5, duration=0.2)
            pyautogui.mouseDown(561.0, 203.5)
            pyautogui.mouseUp(561.0, 203.5)

            time.sleep(12)
            pyautogui.moveTo(756.5, 476.5, duration=0.2)
            pyautogui.mouseDown(756.5, 476.5)
            pyautogui.mouseUp(756.5, 476.5)

            pyautogui.moveTo(561.0, 203.5, duration=0.2)
            pyautogui.mouseDown(561.0, 203.5)
            pyautogui.mouseUp(561.0, 203.5)

            time.sleep(10)
            try:
                pos = pyautogui.locateCenterOnScreen(orange_okay, confidence=CONFIDENCE)
            except pyautogui.ImageNotFoundException:
                pos = None


            if pos:
                click_image(orange_okay, clicks=1, scale=scale, duration=0.2)

                click_image(okay_button, clicks=1, scale=scale, duration=0.2)

                wait_until_gone(loading_screen)

                time.sleep(0.1)

            else:
                time.sleep(12)
                pyautogui.moveTo(514.5, 359.5, duration=0.2)
                pyautogui.mouseDown(514.5, 359.5)
                pyautogui.mouseUp(514.5, 359.5)
                cannoneer_pos = pyautogui.locateCenterOnScreen(cannoneer, confidence=CONFIDENCE)
                cannoneer_screen_x = cannoneer_pos.x / scale[0]
                cannoneer_screen_y = cannoneer_pos.y / scale[1]
                pyautogui.mouseDown(cannoneer_screen_x, cannoneer_screen_y)
                pyautogui.mouseUp(cannoneer_screen_x, cannoneer_screen_y)
                time.sleep(10)
                click_image(orange_okay, clicks=1, scale=scale, duration=0.2)
                click_image(okay_button, clicks=1, scale=scale, duration=0.2)
                wait_until_gone(loading_screen)
                time.sleep(0.1)


        else:
            time.sleep(7)
            pyautogui.moveTo(756.5, 476.5, duration=0.2)
            pyautogui.mouseDown(756.5, 476.5)
            pyautogui.mouseUp(756.5, 476.5)

            pyautogui.moveTo(561.0, 203.5, duration=0.2)
            pyautogui.mouseDown(561.0, 203.5)
            pyautogui.mouseUp(561.0, 203.5)

            time.sleep(10)

            try:
                pos = pyautogui.locateCenterOnScreen(orange_okay, confidence=CONFIDENCE)
            except pyautogui.ImageNotFoundException:
                pos = None

            if pos:
                click_image(orange_okay, clicks=1, scale=scale, duration=0.2)

                click_image(okay_button, clicks=1, scale=scale, duration=0.2)

                wait_until_gone(loading_screen)

                time.sleep(0.1)

            else:
                time.sleep(12)
                pyautogui.moveTo(514.5, 359.5, duration=0.2)
                pyautogui.mouseDown(514.5, 359.5)
                pyautogui.mouseUp(514.5, 359.5)
                cannoneer_pos = pyautogui.locateCenterOnScreen(cannoneer, confidence=CONFIDENCE)
                cannoneer_screen_x = cannoneer_pos.x / scale[0]
                cannoneer_screen_y = cannoneer_pos.y / scale[1]
                pyautogui.mouseDown(cannoneer_screen_x, cannoneer_screen_y)
                pyautogui.mouseUp(cannoneer_screen_x, cannoneer_screen_y)
                time.sleep(10)
                click_image(orange_okay, clicks=1, scale=scale, duration=0.2)
                click_image(okay_button, clicks=1, scale=scale, duration=0.2)
                wait_until_gone(loading_screen)
                time.sleep(0.1)





if __name__ == '__main__':
    main()
