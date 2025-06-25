import time
import pyautogui
# ─── CONFIG ──────────────────────────────────────────────────────────
WINDOW_TITLE   = "Battle Nations"
loading_screen = 'loading.png'
attack         = 'attack.png'
check          = 'check.png'

agent          = 'agent.png'
fight          = 'fight.png'
agent_back     = 'agent_back.png'
loading2       = 'loading2.png'
gas            = 'gas.png'
raptor         = 'raptorwarrior.png'
okay_button = 'okay_button.png'
orange_okay = 'orange_okay.png'
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
    #pyautogui.moveTo(x, y, **move_kwargs)
    print(x, y)
    for _ in range(clicks):
        pyautogui.click(x,y)

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

        # 5) Agent
        agent_pos = pyautogui.locateCenterOnScreen(agent, confidence=CONFIDENCE)
        agent_screen_x = agent_pos.x / scale[0]
        agent_screen_y = agent_pos.y / scale[1]
        pyautogui.mouseDown(agent_screen_x, agent_screen_y)
        pyautogui.mouseUp(agent_screen_x, agent_screen_y)
        pyautogui.mouseDown(agent_screen_x, agent_screen_y)
        pyautogui.mouseUp(agent_screen_x, agent_screen_y)
        pyautogui.mouseDown(agent_screen_x, agent_screen_y)
        pyautogui.mouseUp(agent_screen_x, agent_screen_y)
        pyautogui.mouseDown(agent_screen_x, agent_screen_y)
        pyautogui.mouseUp(agent_screen_x, agent_screen_y)
        pyautogui.mouseDown(agent_screen_x, agent_screen_y)
        pyautogui.mouseUp(agent_screen_x, agent_screen_y)

        click_image(fight, clicks=1, scale=scale, duration=0.2)

        # 7) Wait for second loading screen
        wait_until_gone(loading2)

        click_image(gas, clicks=1, scale=scale, duration=0.2)

        # 10) Raptor warrior
        #pyautogui.moveTo(561.0, 203.5, duration=0.2)
        pyautogui.mouseDown(561.0, 203.5)
        pyautogui.mouseUp(561.0, 203.5)

        time.sleep(14)
        #pyautogui.moveTo(514.5, 359.5, duration=0.2)
        pyautogui.mouseDown(514.5, 359.5)
        pyautogui.mouseUp(514.5, 359.5)

        click_image(gas, clicks=1, scale=scale, duration=0.2)


        #pyautogui.moveTo(561.0, 203.5, duration=0.2)
        pyautogui.mouseDown(561.0, 203.5)
        pyautogui.mouseUp(561.0, 203.5)

        time.sleep(12)
        #pyautogui.moveTo(636.5, 410.5, duration=0.2)
        pyautogui.mouseDown(636.5, 410.5)
        pyautogui.mouseUp(636.5, 410.5)

        click_image(gas, clicks=1, scale=scale, duration=0.2)

        #pyautogui.moveTo(561.0, 203.5, duration=0.2)
        pyautogui.mouseDown(561.0, 203.5)
        pyautogui.mouseUp(561.0, 203.5)

        time.sleep(12)
        #pyautogui.moveTo(756.5, 476.5, duration=0.2)
        pyautogui.mouseDown(756.5, 476.5)
        pyautogui.mouseUp(756.5, 476.5)

        click_image(gas, clicks=1, scale=scale, duration=0.2)

        #pyautogui.moveTo(561.0, 203.5, duration=0.2)
        pyautogui.mouseDown(561.0, 203.5)
        pyautogui.mouseUp(561.0, 203.5)
        time.sleep(10)
        try:
            pos = pyautogui.locateCenterOnScreen(raptor, confidence=CONFIDENCE)
        except pyautogui.ImageNotFoundException:
            pos = None

        if pos:
            #pyautogui.moveTo(876.0, 528.0, duration=0.2)
            pyautogui.mouseDown(876.0, 528.0)
            pyautogui.mouseUp(876.0, 528.0)

            click_image(gas, clicks=1, scale=scale, duration=0.2)

            #pyautogui.moveTo(561.0, 203.5, duration=0.2)
            pyautogui.mouseDown(561.0, 203.5)
            pyautogui.mouseUp(561.0, 203.5)

            time.sleep(7)
            click_image(orange_okay, clicks=1, scale=scale, duration=0.2)
            click_image(okay_button, clicks=1, scale=scale, duration=0.2)
            wait_until_gone(loading_screen)
            time.sleep(0.1)
        else:
            time.sleep(7)
            click_image(orange_okay, clicks=1, scale=scale, duration=0.2)
            click_image(okay_button, clicks=1, scale=scale, duration=0.2)
            wait_until_gone(loading_screen)
            time.sleep(0.1)

if __name__ == '__main__':
    main()