from tkinter import Label, font, Frame
import os

actions_lights = []  # lista na kontrolki sygnalizujące użycie danej akcji

# kolory kontrolek
TURN_OFF_COLOR = "#696969"
TURN_ON_COLOR = "#0063c7"


def init_gui(frame):
    """Tworzy interfejs graficzny do zadania"""

    # tytuł sekcji
    title = Label(frame, text="Actions on host", font=font.Font(size=20))
    title.grid(column=0, row=0)

    # kontener na ledy
    actions_frame = Frame(frame)
    actions_frame.grid(column=0, row=1)

    # tworzenie i ustawianie ledów
    for col in range(8):
        light = Label(actions_frame, text='S'+str(col+1), width=2, height=1, bg=TURN_OFF_COLOR)
        light.grid(column=col, row=1)
        actions_lights.append(light)
        actions_frame.grid_columnconfigure(col, minsize=40)

    take_action(60)  # wywołanie
    # TODO: usunąć potem


def take_action(action_number: int):
    """Podejmuje odpowiednią akcję na hoście w zależności od otrzymanej wartości i sygnalizują ją w GUI poprzez
    zapalenie kontrolki odpowiadającej danej akcji."""

    for i in range(8):  # gasi wszystkie kontrolki
        actions_lights[i].configure(background=TURN_OFF_COLOR)

    if action_number == 3:  # przeglądarka WWW
        actions_lights[0].configure(background=TURN_ON_COLOR)
        os.system("firefox")  # lub inna zainstalowana na danej maszynie

    elif action_number == 12:  # edytor tekstu Vi
        actions_lights[1].configure(background=TURN_ON_COLOR)
        os.system("vi")

    elif action_number == 48:  # program mc
        actions_lights[2].configure(background=TURN_ON_COLOR)
        os.system("mc")  # na Fedorze konieczne instalowanie odpowiedniego pakietu

    elif action_number == 192:  # nowy terminal
        actions_lights[3].configure(background=TURN_ON_COLOR)
        os.system("gnome-terminal")

    elif action_number == 15:  # kalendarz
        actions_lights[4].configure(background=TURN_ON_COLOR)
        os.system("cal")

    elif action_number == 60:  # wybrane polecenie/skrypt w terminalu
        actions_lights[5].configure(background=TURN_ON_COLOR)
        os.system("bash script1.sh")  # lub "sh script1.sh"

    elif action_number == 240:  # wybrane polecenie/skrypt w terminalu
        actions_lights[6].configure(background=TURN_ON_COLOR)
        os.system("bash script2.sh")

    elif action_number == 195:  # wybrane polecenie/skrypt w terminalu
        actions_lights[7].configure(background=TURN_ON_COLOR)
        os.system("bash script3.sh")

    else:
        print("Nieznana wartość!")