import pyautogui


def get_coordinate():
    prompt_list = ["move mouse to top left of emulator and press enter",
                   "move mouse to top right of emulator and press enter"]
    coordinate_list = []

    for i in range(len(prompt_list)):
        input(prompt_list[i])
        x, y = pyautogui.position()
        coordinate_list.append(pyautogui.position())
        print("x is ", x)
        print("y is ", y)

    starting_point_x, starting_point_y = coordinate_list[0]
    bottom_x, bottom_y = coordinate_list[1]
    dimension_x = bottom_x - starting_point_x
    dimension_y = bottom_y - starting_point_y

    print(starting_point_x, starting_point_y, dimension_x, dimension_y)

    return starting_point_x, starting_point_y, dimension_x, dimension_y


if __name__ == "__main__":
    get_coordinate()
