import cv2
import pyautogui

# ─── CONFIG ──────────────────────────────────────────────────────────
IMG_PATH = 'layout6.png'   # your 2800×1800 full-screen PNG
# ─────────────────────────────────────────────────────────────────────

# 1) get your real display size (points)
screen_w, screen_h = pyautogui.size()

# 2) load the image and read its pixel dims
img = cv2.imread(IMG_PATH)
img_h, img_w = img.shape[:2]

# 3) compute scaling factors
scale_x = img_w / screen_w
scale_y = img_h / screen_h

# 4) show the image
cv2.namedWindow('Screenshot', cv2.WINDOW_NORMAL)
cv2.imshow('Screenshot', img)

# 5) on click, compute & print both coords
def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        screen_x = x / scale_x
        screen_y = y / scale_y
        print(f"> Image pixel:    ({x}, {y})")
        print(f"> Screen (real):  ({screen_x:.1f}, {screen_y:.1f})\n")

cv2.setMouseCallback('Screenshot', on_click)

cv2.waitKey(0)
cv2.destroyAllWindows()
