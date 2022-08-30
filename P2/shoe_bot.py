import pyautogui
import time

# user_first_name = input('Firstname ')
# user_last_name = input('Lastname ')
# address = input('Adress ')
# email = input('email ')
# user_phone_number = input('phone number')


# time.sleep(3)
# print(pyautogui.position())


def run_bot():
    pyautogui.click(1219, 8)
    pyautogui.typewrite("safari")
    pyautogui.press("return")
    time.sleep(2)
    pyautogui.click(1375, 25)
    pyautogui.typewrite(
        "https://www.nike.com/t/mercurial-superfly-8-elite-fg-firm-ground-soccer-cleats-htj6pt/DJ2839-484"
    )
    time.sleep(1.5)
    pyautogui.press("return")
    time.sleep(3)
    pyautogui.click(1280, 883)
    time.sleep(1.5)
    pyautogui.scroll(-20)
    time.sleep(1.5)
    pyautogui.click(1165, 506)
    time.sleep(1)
    pyautogui.click(1272, 405)
    time.sleep(1)
    pyautogui.click(1272, 405)
    time.sleep(3)
    pyautogui.click(505, 570)
    pyautogui.typewrite("Ethan")
    pyautogui.press("tab")
    pyautogui.typewrite("Castano")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.typewrite("8265 sw 78th st")
    pyautogui.press("tab")
    pyautogui.typewrite("ethancastano1@gmail.com")
    pyautogui.press("tab")
    pyautogui.typewrite("786-348-8745")
    pyautogui.sleep(3)
    pyautogui.click(424, 795)
    pyautogui.scroll(-30)
    time.sleep(1)
    pyautogui.click(748, 548)
    pyautogui.scroll(-30)
    time.sleep(1)
    print(pyautogui.position())


def main():
    run_bot()


if __name__ == "__main__":
    main()
