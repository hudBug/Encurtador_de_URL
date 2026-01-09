import customtkinter as ctk
import pyshorteners
import pyperclip
from tkinter import messagebox

def encurtar_url():
    url_original = url_entrada.get()
    
    if not url_original:
        messagebox.showwarning("Atenção", "Digite uma URL!")
        return

    try:
        # Inicializa o encurtador
        encurtar = pyshorteners.Shortener()
        url_curta = encurtar.tinyurl.short(url_original)
        
        # Limpa o campo de resultado e insere a nova URL
        url_resultado.delete(0, 'end')
        url_resultado.insert(0, url_curta)
    except Exception as erro:
        messagebox.showerror("error", f"Não foi possível encurtar: {erro}")

def copiar_link():
    link = url_resultado.get()
    if link and "http" in link:
        pyperclip.copy(link)
        # Feedback visual para o usuário
        copiar.configure(text="Copiado")
    else:
        messagebox.showwarning("warning", "Não há link válido para copiar. ")

# Criação da janela principal
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
janela = ctk.CTk()
janela.title("Encurtador de URL em Python")
janela.geometry("450x350")

# Elementos da janela
titulo = ctk.CTkLabel(janela, text="Encurtador de URL em Python", font=("Arial", 20, "bold"))
titulo.pack(pady=20)
subtitulo= ctk.CTkLabel(janela, text="Encurta URLs usando o tinyURL\nDisponível em https://tinyurl.com/", font=("Arial", 12, "bold"))
subtitulo.pack(pady=10)

url_entrada = ctk.CTkEntry(janela, placeholder_text="Cole o link aqui", width=350)
url_entrada.pack(pady=10)

botao = ctk.CTkButton(janela, text="Encurtar URL ", command=encurtar_url)
botao.pack(pady=10)

url_resultado = ctk.CTkEntry(janela, placeholder_text="URL encurtada", width=350, fg_color="transparent")
url_resultado.pack(pady=10)

copiar = ctk.CTkButton(janela, text="Copiar URL encurtada", command=copiar_link)
copiar.pack(pady=10)

# Iniciar o loop da interface
janela.mainloop()