import pyautogui as pag
import time
pag.moveTo(1935,419)#slide sample
time.sleep(0.1)
pag.click()

pag.moveTo(1300,770)
time.sleep(0.1)
pag.scroll(-200)
time.sleep(0.1)
pag.moveTo(915,550,duration=0.1)
pag.dragRel(0,300,duration=0.5)
