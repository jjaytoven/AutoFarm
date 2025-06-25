import time
import pyautogui


WINDOW_TITLE   = "Battle Nations"
loading_screen = 'loading.png'
attack         = 'attack.png'
check          = 'check.png'
tk = 'tk.png'
fight          = 'fight.png'
warmam = 'warmam.png'
mam = 'mam.png'
dust = 'dust.png'

loading2       = 'loading2.png'

okay_button = 'okay_button.png'
orange_okay = 'orange_okay.png'

cannoneer = 'cannoneer.png'

CONFIDENCE     = 0.7
DELAY_BEFORE   = 6
SCAN_INTERVAL  = 0.5
APPEAR_TIMEOUT = 10


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

        click_image(attack, clicks=1, scale=scale, duration=0.2)

        # 2) Check
        click_image(check, clicks=1, scale=scale, duration=0.2)

        # 3) Wait for loading screen to vanish
        wait_until_gone(loading_screen)

        click_image(tk, clicks=7, scale=scale, duration=0.2)

        click_image(fight, clicks=1, scale=scale, duration=0.2)

        # 7) Wait for second loading screen
        wait_until_gone(loading2)

        dust_pos = pyautogui.locateCenterOnScreen(dust, confidence=CONFIDENCE)
        dust_screen_x = dust_pos.x / scale[0]
        dust_screen_y = dust_pos.y / scale[1]
        pyautogui.mouseDown(dust_screen_x, dust_screen_y)
        pyautogui.mouseUp(dust_screen_x, dust_screen_y)

        time.sleep(12)
        pyautogui.moveTo(514.5, 359.5, duration=0.2)
        pyautogui.mouseDown(514.5, 359.5)
        pyautogui.mouseUp(514.5, 359.5)

        warmam_pos = pyautogui.locateCenterOnScreen(warmam, confidence=CONFIDENCE)
        warmam_screen_x = warmam_pos.x / scale[0]
        warmam_screen_y = warmam_pos.y / scale[1]
        pyautogui.mouseDown(warmam_screen_x, warmam_screen_y)
        pyautogui.mouseUp(warmam_screen_x, warmam_screen_y)


        time.sleep(12)
        pyautogui.moveTo(636.5, 410.5, duration=0.2)
        pyautogui.mouseDown(636.5, 410.5)
        pyautogui.mouseUp(636.5, 410.5)

        mam_pos = pyautogui.locateCenterOnScreen(mam, confidence=CONFIDENCE)
        mam_screen_x = mam_pos.x / scale[0]
        mam_screen_y = mam_pos.y / scale[1]
        pyautogui.mouseDown(mam_screen_x, mam_screen_y)
        pyautogui.mouseUp(mam_screen_x, mam_screen_y)

        time.sleep(12)
        pyautogui.moveTo(756.5, 476.5, duration=0.2)
        pyautogui.mouseDown(756.5, 476.5)
        pyautogui.mouseUp(756.5, 476.5)

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