import tkinter as tk
import customtkinter
from tkinter import filedialog
import time
import pygame
import random
from pypresence import Presence

btns = [
    {
        "label": "XRLM RPC",
        "url": "https://telegra.ph/XRLMS-RPC-Packet-05-16"
    }
]

# Создание окна приложения
app = customtkinter.CTk()
app.geometry("600x720")
app.title("XRLM RPC-Discord packets. Catalog=Main t.me/quesada_team")

# Установка фона главного меню
background_image = tk.PhotoImage(file="wex.png")
background_label = tk.Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Установка темы
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

def close_info_window(window):
    window.destroy()

def print_sent_packets(console, number):
    message = f"Sent Packet ({number})\n"
    console.insert(tk.END, message)

def print_sent_packetss(console, number):
    message = f"Sent Packet ({number})\n"
    console.insert(tk.END, message)

# Функция для воспроизведения звука
def play_sound():
    pygame.mixer.init()
    sound = pygame.mixer.Sound("gpu.mp3")
    sound.play()

# Функция для вывода пакетов
def print_sent_packets(console):
    for _ in range(90):
        random_number = random.randint(793, 1769)
        message = f"Sent Packet ({random_number})\n"
        console.insert(tk.END, message)
        time.sleep(0.03)

def show_info():
    info_window = customtkinter.CTk()
    info_window.title("XRLM RPC-Discord packets. Catalog=Info t.me/quesada_team")
    info_window.geometry("850x370")

    info_text = """
    Discord RPC (Rich Presence) - это интерфейс, который позволяет играм и приложениям взаимодействовать с Discord.
    Он позволяет отображать информацию о текущей активности пользователя, такую как играемая игра, состояние, 
    детали игрового процесса и многое другое.

    Реализация Discord RPC в приложении позволяет игрокам отображать свою активность в Discord, 
    что делает опыт общения более интересным и интерактивным. Discord RPC также может быть использован 
    для управления функциями приложения из Discord, такими как приглашение друзей в игру или просмотр 
    информации о текущей активности других пользователей.

    Использование Discord RPC требует регистрации приложения на платформе Discord и использования 
    специального токена для взаимодействия с API Discord. После регистрации приложения разработчику 
    предоставляется доступ к документации и инструментам для интеграции Discord RPC в свои проекты.

    Discord RPC может быть использован для различных целей, включая отображение информации о текущей игре, 
    предоставление возможности присоединения к игре через Discord, уведомления о достижениях или событиях в игре, 
    и многое другое.
    """
    info_label = customtkinter.CTkLabel(info_window, text=info_text, justify=tk.LEFT)
    info_label.pack(pady=10, padx=10)

    close_button = customtkinter.CTkButton(info_window, text="Закрыть", command=lambda: close_info_window(info_window))
    close_button.pack(pady=10)

    info_window.mainloop()

# Функция, вызываемая при нажатии кнопки "Connect"
def connect_button_clicked(console):
    print("Подключение...")
    client_id = '1195008935992774718'
    RPC = Presence(client_id)
    RPC.connect()

    try:
        with open("rpc.txt", "r") as f:
            settings = {}
            for line in f:
                key, value = line.strip().split(": ")
                settings[key] = value

        party_size_1 = int(settings.get("party_size_1", 63))
        party_size_2 = int(settings.get("party_size_2", 100))

        message = "Настройки конфига из файла:\n"
        for key, value in settings.items():
            message += f"{key}: {value}\n"
        console.insert(tk.END, message)

        RPC.update(
            state=settings["state"],
            details=settings["details"],
            start=15076,
            large_image=settings["large_image"],
            large_text=settings["large_text"],
            small_image=settings["small_image"],
            small_text=settings["small_text"],
            party_id="Много хочешь..",
            party_size=[party_size_1, party_size_2],
            join="https://google.com",
            instance=True
        )
    except FileNotFoundError:
        print("Файл rpc.txt не найден. Используются настройки по умолчанию.")
        RPC.update(
            state="Blutooth connected.",
            details="Компилируем логи в .bomjara",
            start=15076,
            large_image="bomjara",
            large_text="Компиляция? Да ладно зачем она нужна",
            small_image="tihon",
            small_text="Де-компиляция..",
            party_id="Много хочешь..",
            party_size=[63, 100],
            join="https://google.com",
            instance=True
        )

    play_sound()
    print_sent_packets(console)

    print('####### ### ### ##### #### ###', file=console)
    print('### ### ### ### ### ### ### ###', file=console)
    print('### ### ### ### ### ### ### ###', file=console)
    print('### ### ### ### ### ### ### ###', file=console)
    print('####### ### ### ##### #### ###', file=console)

    time.sleep(5)

    print('RPC Connected successful!', file=console)

# Функция для открытия окна настроек
def settings_window():
    settings = customtkinter.CTkToplevel(app)
    settings.title("XRLM RPC-Discord packets. Catalog=SETTINGS t.me/quesada_team")
    settings.geometry("300x640")

    small_text_label = customtkinter.CTkLabel(settings, text="small_text:")
    small_text_label.pack(pady=5, padx=10)
    small_text_entry = customtkinter.CTkEntry(settings)
    small_text_entry.pack(pady=5, padx=10)

    large_text_label = customtkinter.CTkLabel(settings, text="large_text:")
    large_text_label.pack(pady=5, padx=10)
    large_text_entry = customtkinter.CTkEntry(settings)
    large_text_entry.pack(pady=5, padx=10)

    details_label = customtkinter.CTkLabel(settings, text="details:")
    details_label.pack(pady=5, padx=10)
    details_entry = customtkinter.CTkEntry(settings)
    details_entry.pack(pady=5, padx=10)

    state_label = customtkinter.CTkLabel(settings, text="state:")
    state_label.pack(pady=5, padx=10)
    state_entry = customtkinter.CTkEntry(settings)
    state_entry.pack(pady=5, padx=10)

    large_image_label = customtkinter.CTkLabel(settings, text="large_image:")
    large_image_label.pack(pady=5, padx=10)
    large_image_options = ["bomjara", "bitcoin", "dollar", "wild1", "nursultan", "tihon", "popovich", "rat", "nursultan", "wild2"]
    large_image_var = tk.StringVar(settings)
    large_image_var.set(large_image_options[0])
    large_image_dropdown = customtkinter.CTkComboBox(settings, values=large_image_options, variable=large_image_var)
    large_image_dropdown.pack(pady=5, padx=10)

    small_image_label = customtkinter.CTkLabel(settings, text="small_image:")
    small_image_label.pack(pady=5, padx=10)
    small_image_options = ["tihon", "popovich", "rat", "wild2", "nursultan1", "bomjara", "bitcoin", "dollar", "wild1", "nursultan"]
    small_image_var = tk.StringVar(settings)
    small_image_var.set(small_image_options[0])
    small_image_dropdown = customtkinter.CTkComboBox(settings, values=small_image_options, variable=small_image_var)
    small_image_dropdown.pack(pady=5, padx=10)

    party_size_1_label = customtkinter.CTkLabel(settings, text="party_size_1:")
    party_size_1_label.pack(pady=5, padx=10)
    party_size_1_entry = customtkinter.CTkEntry(settings)
    party_size_1_entry.pack(pady=5, padx=10)

    party_size_2_label = customtkinter.CTkLabel(settings, text="party_size_2:")
    party_size_2_label.pack(pady=5, padx=10)
    party_size_2_entry = customtkinter.CTkEntry(settings)
    party_size_2_entry.pack(pady=5, padx=10)

    def save_settings():
        settings_dict = {
            "small_text": small_text_entry.get(),
            "large_text": large_text_entry.get(),
            "details": details_entry.get(),
            "state": state_entry.get(),
            "large_image": large_image_var.get(),
            "small_image": small_image_var.get(),
            "party_size_1": party_size_1_entry.get(),
            "party_size_2": party_size_2_entry.get(),
        }

        with open("rpc.txt", "w") as f:
            for key, value in settings_dict.items():
                f.write(f"{key}: {value}\n")

    save_button = customtkinter.CTkButton(settings, text="Сохранить", command=save_settings)
    save_button.pack(pady=10, padx=10)

# Функция для загрузки конфигурационного файла
def load_cfg():
    filepath = filedialog.askopenfilename(filetypes=[("Config files", "*.cfg")])
    if filepath:
        with open(filepath, "r") as f:
            settings = {}
            for line in f:
                key, value = line.strip().split(": ")
                settings[key] = value

        print("Настройки конфига из файла:")
        for key, value in settings.items():
            print(f"{key}: {value}")

# Функция для создания нового конфигурационного файла
def create_cfg():
    new_cfg_window = customtkinter.CTkToplevel(app)
    new_cfg_window.title("Create New Config")
    new_cfg_window.geometry("300x640")

    small_text_label = customtkinter.CTkLabel(new_cfg_window, text="small_text:")
    small_text_label.pack(pady=5, padx=10)
    small_text_entry = customtkinter.CTkEntry(new_cfg_window)
    small_text_entry.pack(pady=5, padx=10)

    large_text_label = customtkinter.CTkLabel(new_cfg_window, text="large_text:")
    large_text_label.pack(pady=5, padx=10)
    large_text_entry = customtkinter.CTkEntry(new_cfg_window)
    large_text_entry.pack(pady=5, padx=10)

    details_label = customtkinter.CTkLabel(new_cfg_window, text="details:")
    details_label.pack(pady=5, padx=10)
    details_entry = customtkinter.CTkEntry(new_cfg_window)
    details_entry.pack(pady=5, padx=10)

    state_label = customtkinter.CTkLabel(new_cfg_window, text="state:")
    state_label.pack(pady=5, padx=10)
    state_entry = customtkinter.CTkEntry(new_cfg_window)
    state_entry.pack(pady=5, padx=10)

    large_image_label = customtkinter.CTkLabel(new_cfg_window, text="large_image:")
    large_image_label.pack(pady=5, padx=10)
    large_image_options = ["bomjara", "bitcoin", "dollar", "wild1", "nursultan", "tihon", "popovich", "rat", "nursultan", "wild2"]
    large_image_var = tk.StringVar(new_cfg_window)
    large_image_var.set(large_image_options[0])
    large_image_dropdown = customtkinter.CTkComboBox(new_cfg_window, values=large_image_options, variable=large_image_var)
    large_image_dropdown.pack(pady=5, padx=10)

    small_image_label = customtkinter.CTkLabel(new_cfg_window, text="small_image:")
    small_image_label.pack(pady=5, padx=10)
    small_image_options = ["tihon", "popovich", "rat", "wild2", "nursultan1", "bomjara", "bitcoin", "dollar", "wild1", "nursultan"]
    small_image_var = tk.StringVar(new_cfg_window)
    small_image_var.set(small_image_options[0])
    small_image_dropdown = customtkinter.CTkComboBox(new_cfg_window, values=small_image_options, variable=small_image_var)
    small_image_dropdown.pack(pady=5, padx=10)

    party_size_1_label = customtkinter.CTkLabel(new_cfg_window, text="party_size_1:")
    party_size_1_label.pack(pady=5, padx=10)
    party_size_1_entry = customtkinter.CTkEntry(new_cfg_window)
    party_size_1_entry.pack(pady=5, padx=10)

    party_size_2_label = customtkinter.CTkLabel(new_cfg_window, text="party_size_2:")
    party_size_2_label.pack(pady=5, padx=10)
    party_size_2_entry = customtkinter.CTkEntry(new_cfg_window)
    party_size_2_entry.pack(pady=5, padx=10)

    def save_new_cfg():
        settings_dict = {
            "small_text": small_text_entry.get(),
            "large_text": large_text_entry.get(),
            "details": details_entry.get(),
            "state": state_entry.get(),
            "large_image": large_image_var.get(),
            "small_image": small_image_var.get(),
            "party_size_1": party_size_1_entry.get(),
            "party_size_2": party_size_2_entry.get(),
        }

        with open("new_config.cfg", "w") as f:
            for key, value in settings_dict.items():
                f.write(f"{key}: {value}\n")

    save_button = customtkinter.CTkButton(new_cfg_window, text="Сохранить", command=save_new_cfg)
    save_button.pack(pady=10, padx=10)

# Создание фрейма для элементов интерфейса
frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Создание заголовка
label = customtkinter.CTkLabel(master=frame, text="Maden by: XLRM & КРЫСОЛОВ", font=("Arial", 18))
label.pack(pady=12, padx=10)

# Создание кнопки "Connect"
console = tk.Text(frame, height=20, width=60, bg="gray20", fg="green")
console.pack(pady=10, padx=10)
connect_button = customtkinter.CTkButton(master=frame, text="Connect", command=lambda: connect_button_clicked(console))
connect_button.pack(pady=12, padx=10)

# Создание кнопки "Настроить"
settings_button = customtkinter.CTkButton(master=frame, text="Настроить", command=settings_window)
settings_button.pack(pady=12, padx=10)

info_button = customtkinter.CTkButton(app, text="Info", command=show_info)
info_button.pack(pady=20)

send_frame = customtkinter.CTkFrame(master=frame)
send_frame.pack(pady=10, padx=10)
send_entry = customtkinter.CTkEntry(master=send_frame)
send_entry.pack(side=tk.LEFT, padx=5)
send_button = customtkinter.CTkButton(master=send_frame, text="Отправить", command=lambda: print_sent_packetss(console, send_entry.get()))
send_button.pack(side=tk.LEFT, padx=5)

# Кнопка загрузки .cfg
load_cfg_button = customtkinter.CTkButton(master=frame, text="Загрузить .cfg", command=load_cfg)
load_cfg_button.pack(pady=12, padx=10)

# Кнопка создания нового .cfg
create_cfg_button = customtkinter.CTkButton(master=frame, text="Создать .cfg", command=create_cfg)
create_cfg_button.pack(pady=12, padx=10)

# Запуск приложения
app.mainloop()