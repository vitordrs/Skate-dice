import customtkinter as ctk
import random


#Dicionario de manobras, juntamente a funçao que as chama(para adicionar mais basta aumentar o "randint" e acrescentar a trick ao final com o numero correspondente)
def tricksolo():
    manobra = random.randint(1, 40)
    if manobra == 1:
        return "Ollie"
    elif manobra == 2:
        return "Fs Ollie 180"
    elif manobra == 3:
        return "Bs Ollie 180"
    elif manobra == 4:
        return "Varial"
    elif manobra == 5:
        return "Shove-it"
    elif manobra == 6:
        return "Flip"
    elif manobra == 7:
        return "Heelflip"
    elif manobra == 8:
        return "Fs Ollie 360"
    elif manobra == 9:
        return "Bs Ollie 360"
    elif manobra == 10:
        return "Fs Flip"
    elif manobra == 11:
        return "Bs Flip"
    elif manobra == 12:
        return "Fs Heelflip"
    elif manobra == 13:
        return "Bs Heelflip"
    elif manobra == 14:
        return "Varial 360"
    elif manobra == 15:
        return "Shove-it 360"
    elif manobra == 16:
        return "Bs BigSpin"
    elif manobra == 17:
        return "Fs BigSpin"
    elif manobra == 18:
        return "Varial Flip"
    elif manobra == 19:
        return "Shove-it Heel"
    elif manobra == 20:
        return "KickiFlip"
    elif manobra == 21:
        return "Lazer Heel"
    elif manobra == 22:
        return "Inward Heel"
    elif manobra == 23:
        return "HardFlip"
    elif manobra == 24:
        return "Fs Flip 360"
    elif manobra == 25:
        return "Bs Flip 360"
    elif manobra == 26:
        return "Fs HeelFlip 360"
    elif manobra == 27:
        return "Bs HeelFlip 360"
    elif manobra == 28:
        return "Flip BigSpin"
    elif manobra == 29:
        return "HeelFlip BigSpin"
    elif manobra == 30:
        return "DolphinFlip"
    elif manobra == 31:
        return "540Flip"
    elif manobra == 32:
        return "360 DoubleFlip"
    elif manobra == 33:
        return "DoubleFlip"
    elif manobra == 34:
        return "FootFlip"
    elif manobra == 35:
        return "DoubleHeel"
    elif manobra == 36:
        return "Foot HeelFlip"
    elif manobra == 37:
        return "Late Varial"
    elif manobra == 38:
        return "Late Shove-it"
    elif manobra == 39:
        return "Inward Heel Reverse"
    elif manobra == 40:
        return "HardFlip Reverse"

def mostar_manobra():
    manobra = tricksolo()
    stance = random.choice(base)
    resultado_label2.configure(text=f"{stance}\n{manobra}\n{random.randint(1,4)} Chances!")   

def trickcaixote1():
    trickcaixotenv1 = f"{random.choice(base)}\n{random.choice(direcao)}\n{random.choice(caixa)}\nSaindo: {random.choice(saida2)}\n{random.randint(1,6)} Chances!"
    trickcaixotenv1_label.configure(text=trickcaixotenv1)

def trickcaixote2():
    resultado = f"{random.choice(base)}\n{random.choice(direcao)}\n{random.choice(caixa)}\nEntrando: {random.choice(entrada)}\nSaindo: {random.choice(saida2)}\n{random.randint(1, 6)} Chances!"
    resultado_label.configure(text=resultado)

def trickcaixote3():
    trickcaixotenv3 = f"{random.choice(base)}\n{random.choice(direcao)}\n{random.choice(caixa)}\nEntrando: {random.choice(entrada)}\n Saindo: {random.choice(saida)}\n {random.randint(1,10)} Chances!"
    trickcaixotenv3_label.configure(text=trickcaixotenv3)

#listas
base = ['Base', 'Nollie', 'Fakie', 'Switch']
caixa = ['5050', 'Grind', 'Nosegrind', 'NoseSlide', 'TailSlide', 'Feeble', 'Smith', 'Crooked', 'OverCrooked', 'BluntSlide', 'NoseBluntSlide', 'Salad']
direcao = ['FS', 'BS']
entrada = ['Normal','Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Com Giro', 'Flip', 'Heel', 'Varial', 'Shove-it', 'BS180', 'FS180']
saida = ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Reverse', 'Reverse', 'Reverse', 'Reverse', 'Reverse', '270', 'Com Giro', 'Flip', 'Heel', 'Varial', 'Shove-it']
saida2 = ['Normal', 'Reverse']

#nome do app
window = ctk.CTk()
window.title("Skate Dice")
window.configure(fg_color="#3F3F3F")
window.geometry("350x750")

#fonte
fonte_app = ctk.CTkFont(family="", size=43, weight="bold")
fonte_botao = ctk.CTkFont(family="", size=13, weight="bold", slant="italic")
fonte_resultados = ctk.CTkFont(family="", size=15, weight="normal", slant="roman")

#mensagem indicativa
label = ctk.CTkLabel(window, text="SKATE DICE", fg_color="#3F3F3F", font=fonte_app)
label.pack()

#botão solo
button1 = ctk.CTkButton(window, text="Solo", command=mostar_manobra, fg_color="#C0C0C0", text_color="#000000", font=fonte_botao)
button1.pack()
resultado_label2 = ctk.CTkLabel(window, text="", wraplength=200, fg_color="#3F3F3F", text_color="#FFFFF0", font=fonte_resultados)
resultado_label2.pack()

#Botão caixote 1
button2 = ctk.CTkButton(window, text="Caixote Nv1", command=trickcaixote1, fg_color="#C0C0C0", text_color="#000000", font=fonte_botao)
button2.pack()
trickcaixotenv1_label = ctk.CTkLabel(window, text="", wraplength=200, fg_color="#3F3F3F", text_color="#FFFFF0", font=fonte_resultados)
trickcaixotenv1_label.pack()

#botão caixote 2 
button3 = ctk.CTkButton(window, text="Caixote Nv2", command=trickcaixote2, fg_color="#C0C0C0", text_color="#000000", font=fonte_botao)
button3.pack()
resultado_label = ctk.CTkLabel(window, text="", wraplength=200, fg_color="#3F3F3F", text_color="#FFFFF0", font=fonte_resultados)
resultado_label.pack()

#Botao caixote 3
button4 = ctk.CTkButton(window, text="Caixote Nv3", command=trickcaixote3, fg_color="#C0C0C0", text_color="#000000", font=fonte_botao)
button4.pack()
trickcaixotenv3_label = ctk.CTkLabel(window, text="", wraplength=200, fg_color="#3F3F3F", text_color="#FFFFF0", font=fonte_resultados)
trickcaixotenv3_label.pack()

window.mainloop()
