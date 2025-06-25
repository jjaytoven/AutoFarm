import time
import pyautogui

# ─── CONFIG ──────────────────────────────────────────────────────────
okay_button = 'okay_button.png'  # your exact crop of the "Okay" button
attack = 'attack.png'
check = 'check.png'
heavy = 'heavy.png'
agent = 'agent.png'
CONFIDENCE = 0.6                # try 0.5–0.7 if it still misses
DELAY_BEFORE = 10                  # seconds to alt-tab into your game
SCAN_INTERVAL = 0.5                # seconds between each search
# ─────────────────────────────────────────────────────────────────────

def get_scaling():
    screen_w, screen_h = pyautogui.size()
    shot = pyautogui.screenshot()
    shot_w, shot_h = shot.size
    return shot_w / screen_w, shot_h / screen_h

def main():
    # give you time to switch into the game window
    time.sleep(DELAY_BEFORE)
    scale_x, scale_y = get_scaling()

    #attack
    attack_pos = pyautogui.locateCenterOnScreen(attack, confidence=CONFIDENCE)
    attack_screen_x = attack_pos.x / scale_x
    attack_screen_y = attack_pos.y / scale_y

    pyautogui.moveTo(attack_screen_x, attack_screen_y, duration=0.2)
    pyautogui.click()

    #check
    check_pos = pyautogui.locateCenterOnScreen(check, confidence=CONFIDENCE)
    check_screen_x = check_pos.x / scale_x
    check_screen_y = check_pos.y / scale_y
    pyautogui.moveTo(check_screen_x, check_screen_y, duration=0.2)
    pyautogui.click()


    #heavy place
    heavy_pos = pyautogui.locateCenterOnScreen(heavy, confidence=CONFIDENCE)
    heavy_screen_x = heavy_pos.x / scale_x
    heavy_screen_y = heavy_pos.y / scale_y
    pyautogui.moveTo(heavy_screen_x, heavy_screen_y, duration=0.2)
    pyautogui.doubleClick()
    pyautogui.doubleClick()

    #agent
    agent_pos = pyautogui.locateCenterOnScreen(agent, confidence=CONFIDENCE)
    agent_screen_x = agent_pos.x / scale_x
    agent_screen_y = agent_pos.y / scale_y
    pyautogui.moveTo(agent_screen_x, agent_screen_y, duration=0.2)
    pyautogui.tripleClick()









if __name__ == '__main__':
    main()