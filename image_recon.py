import pyautogui
import keyboard
import get_coordinate


def image_recon(region):
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
    pyautogui.click(xy, clicks=clicks, interval=1, button='left')
    print(flag, xy)


def main():
    region = get_coordinate.get_coordinate()
    image_recon(region)


if __name__ == "__main__":
    main()
