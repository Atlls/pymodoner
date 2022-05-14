import keyboard # Requiere sudo

def pulsa(tecla):
    print('Se ha pulsado la tecla ' + str(tecla))

def get_event_keyboard():
    if keyboard.read_key() == "p":
        print("You pressed p")
