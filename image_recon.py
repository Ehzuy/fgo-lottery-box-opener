import time

import pyautogui
import keyboard
import get_coordinate


def image_recon(region):
    """
    depreciated, not using anymore, use onUpdate() instead
    :param region:
    :return:
    """
    x, y, dx, dy = region
    pyautogui.leftClick(x + dx / 2, y + dy / 2)
    print("focusing..")
    while keyboard.is_pressed("q") is False:

        flag = "None"
        xy = pyautogui.locateCenterOnScreen("button-10.png", region=(x, y, dx, dy))
        if xy is not None:
            click_and_print(xy, 'at main,clicking button 10', 1)

        else:

            xy = pyautogui.locateCenterOnScreen("button-10-alternative.png", region=(x, y, dx, dy))

            if xy is not None:
                click_and_print(xy, 'opening boxes', 5)

            else:

                xy = pyautogui.locateCenterOnScreen("prize-reset.png", region=(x, y, dx, dy))
                if xy is not None:
                    click_and_print(xy, "initiating reset", 1)

                else:
                    print("looking...")
                    print("reset?", pyautogui.locateCenterOnScreen("reset-button.png", region=(x, y, dx, dy)))
                    print("close?", pyautogui.locateCenterOnScreen("close.png", region=(x, y, dx, dy)))
                    if pyautogui.locateCenterOnScreen("reset-button.png", region=(x, y, dx, dy)) is not None:
                        xy = pyautogui.locateCenterOnScreen("reset-button.png", region=(x, y, dx, dy))
                        click_and_print(xy, 'clicking reset button', 1)

                    if pyautogui.locateCenterOnScreen("close.png", region=(x, y, dx, dy)) is not None:
                        xy = pyautogui.locateCenterOnScreen("close.png", region=(x, y, dx, dy))
                        click_and_print(xy, 'closing reset comfirm', 1)


def click_and_print(xy, flag, clicks):
    pyautogui.click(xy, clicks=clicks, interval=0.2, button='left')
    print(flag, xy)


def onUpdate(region):
    x, y, dx, dy = region
    button_10 = pyautogui.locateCenterOnScreen("button-10.png", region=(x, y, dx, dy))
    button_10_alternative = pyautogui.locateCenterOnScreen("button-10-alternative.png", region=(x, y, dx, dy))

    if button_10 is not None:
        click_and_print(button_10, "start unboxing", 1)
        time.sleep(1.5)
        pyautogui.leftClick(x + dx / 4, y + dy / 2)

        return
    if button_10_alternative is not None:
        click_and_print(button_10_alternative, "opening...", 10)
        return

    reset_box = pyautogui.locateCenterOnScreen("prize-reset.png", region=(x, y, dx, dy))
    reset_button = pyautogui.locateCenterOnScreen("reset-button.png", region=(x, y, dx, dy))
    close_button = pyautogui.locateCenterOnScreen("close.png", region=(x, y, dx, dy))

    if button_10 is None and button_10_alternative is None and reset_button is None and reset_box is None and close_button is None:
        # pyautogui.leftClick(button_10_alternative)
        print("...")
        return
    if reset_box is not None and button_10 is None:
        click_and_print(reset_box, "start resetting", 1)
        return
    if reset_button is not None:
        click_and_print(reset_button, "resetting", 1)
        return
    if close_button is not None:
        click_and_print(close_button, "closing", 1)
        return


def main():
    region = get_coordinate.get_coordinate()
    # image_recon(region)

    while keyboard.is_pressed('q') is False:
        onUpdate(region)


if __name__ == "__main__":
    main()
