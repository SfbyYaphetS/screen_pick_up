import eel
import time
import pyautogui as pg
import tesseract_lib as tes


@eel.expose
def position(self):
    time.sleep(2)
    start_pos = pg.position()
    print(start_pos)
    time.sleep(2)
    end_pos = pg.position()
    print(end_pos)
    pos_text = tes.read_text(start_pos + end_pos).tes_read()
    return pos_text


eel.init("web")
eel.start("main.html", size=(400, 400))
