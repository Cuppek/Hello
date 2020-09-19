import pyautogui as py
py.click()
distance = 200
while distance > 0:
    print(distance, 0)
    py.dragRel(distance, 0, duration=1)
    distance = distance - 25
    print(0, distance)
    py.dragRel(0, -distance, duration=1)
    print(distance, 0)
    py.dragRel(-distance, 0, duration=1)
    distance = distance - 25
    print(0, distance)
    py.dragRel(0, distance, duration=1)