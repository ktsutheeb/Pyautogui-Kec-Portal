import pyautogui as pag
import pyperclip
import time

print("Press Ctrl-C to stop.")
try:
    pag.moveTo(2454,20)
    time.sleep(0.1)
    pag.click()

    pag.moveTo(283,53,duration=0)#website
    x,y=pag.position()
    if(x,y==(283,53)):
        time.sleep(0.1)
        pag.doubleClick()
        time.sleep(7)
        pag.moveTo(1700,758,duration=0)#mail fill
        x,y=pag.position()
        if(x,y==(1700,758)):
            time.sleep(0.1)
            pag.click()
            i=1
            while (i==1):
                pyperclip.copy("sutheebkt.22aim@kongu.edu")
                time.sleep(0.1)
                pag.hotkey('ctrl','v')
                i=i+1
            pag.moveTo(1500,850)#next
            if(pag.position()==(1500,850)):
                time.sleep(0.1)
                pag.click()
                time.sleep(6)
                pag.moveTo(1500,880)#password
                if(pag.position()==(1500,880)):
                    time.sleep(0.1)
                    pag.click()
                    pyperclip.copy("sutheeb2005")
                    time.sleep(0.1)
                    pag.hotkey('ctrl','v')
                    pag.moveTo(1500,1000)#login
                    if(pag.position()==(1500,1000)):
                        time.sleep(0.1)
                        pag.click()
                        time.sleep(8)
                        pag.moveTo(1500,545)#close google
                        time.sleep(0.1)
                        pag.click()
                        time.sleep(0.1)
                        pag.moveTo(46,362)#course
                        time.sleep(0.1)
                        pag.click()
                        time.sleep(3.5)
                        pag.moveTo(300,555)#pst
                        time.sleep(0.1)
                        pag.click()
                        time.sleep(6)

                        pag.moveTo(1300,770)
                        time.sleep(0.1)
                        pag.scroll(-200)
                        time.sleep(0.1)
                        pag.moveTo(915,550,duration=0.1)
                        pag.dragRel(0,300,duration=0.5)

                        pag.moveTo(400,1250)
                        time.sleep(0.1)
                        pag.click()
                        time.sleep(0.1)
                        pag.moveTo(400,1250)
                        time.sleep(0.1)
                        pag.moveTo(915,870,duration=0.1)
                        pag.dragRel(0,300,duration=0.5)

                        pag.moveTo(300,1250)
                        time.sleep(0.1)
                        pag.click()
                        time.sleep(0.1)

                        pag.moveTo(2400,415,duration=0.2)
                        time.sleep(0.1)
                        pag.click()
                        time.sleep(2)

                        pag.moveTo(1701,1243)
                        time.sleep(3)
                        pag.click()
                        
                        


                        # pag.moveTo(915,614)
                        # time.sleep(0.1)
                        # pag.dragRel(0,400)
                        # time.sleep(0.1)
                        # pag.moveTo(500,1350)
                        # time.sleep(0.1)
                        # pag.click()
                        # pag.moveTo(915,950)
                        # time.sleep(0.1)
                        # pag.dragRel(0,400)

                        



            
except:
    print("\nProgram stopped")