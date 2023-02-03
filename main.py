# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyautogui
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def nextItem():
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')

    pyautogui.press('left')
    pyautogui.press('left')

    pyautogui.press('enter')

def changePrices(price_a,price_bottom,price_b,price_c):
    # tab to cost tab
    pyautogui.press('f6')

    # 4 tabs to get to the List price
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')

    pyautogui.write(price_a)
    pyautogui.press('tab')
    pyautogui.write(price_bottom)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(price_a)
    pyautogui.press('tab')
    pyautogui.write(price_b)
    pyautogui.press('tab')
    pyautogui.write(price_c)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(.5)
    pyautogui.press('enter')

    # 9 tabs to get to the bottom botton rows
    nextItem()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pyautogui.getWindowsWithTitle("I/M")[0].maximize()
    # SUPER IMPORTANT. NO ACTIVE WINDOW MODULE. NEED TO CLICK ON THE I/M WINDOW ITSELF
    time.sleep(5)

#    # FB changes. 66 items total
#    for i in range(66):
#        changePrices('4.75','4.5','6','6.75')

#    # JB changes. 15 items total
#    for i in range(15):
#        changePrices('4.75','4.5','6','6.75')

    # TB Changes. 65 items but belt in the middle.
    for i in range(54):
        changePrices('4.75', '4.5', '6', '6.75')

    nextItem()
    nextItem()

    for i in range(9):
        changePrices('4.75', '4.5', '6', '6.75')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
