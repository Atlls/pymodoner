import keyboard

while True:
    if keyboard.read_key() == "p":
        print("You pressed p")
        break

while True:
    if keyboard.is_pressed("q"):
        print("You pressed q")
        break

pressed = False
while not pressed:
    print('culo')
    pressed = keyboard.on_press_key("r", lambda _:print("You pressed r"))
