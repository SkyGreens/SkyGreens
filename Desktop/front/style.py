import customtkinter as ctk
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #pip install matplotlib
import matplotlib.pyplot as plt
from tkinter import Toplevel  # pip install tkinter
import pandas as pd #pip install pandas
from openpyxl.workbook import Workbook #pip install openpyxl
from tkinter import messagebox

class Style:
        
    def color (color_nome):
        colors = {
            'fg' : "#316133",  # Cor para botões - Verde Escuro
            'hover' : "#5d732f",  # Cor ao passar o mouse - Verde Claro
            'bg' : "#D9D9D9",  # Cor de fundo - Cinza
            'bg_frame' : "#E7E7E7",  # Cor de fundo do frame - Quase Branco
            'fg_2' : "#cdcdcd", # Cor para botões - Cinza escuro
            'hover_2' : "#a0a0a0", # Cor ao passar o mouse - Cinza Claro
            'fg_red' : "#c30000", #Cor do botao - Vermelho
            'hover_red':"#6f0000" #Cor ao passar o mouse - Vermelho claro
        }
        return colors.get(color_nome)
    
    def font_style():
        fontStyle = ("Lucida Grande",16)
        return fontStyle
    
    def img(img_nome):
        
        def abrir_img(caminho,size):

            img = ctk.CTkImage(Image.open(caminho), size=size)  
            return img  
      
        imgs={
            'img_icon_pedidoVenda':abrir_img("img\\icon_pedidoVenda.png",(80, 80)),
            'img_icon_pedidoCompra':abrir_img("img\\icon_pedidoCompra.png",(80, 80)),
            'img_icon_insumos':abrir_img("img\\icon_insumos.png",(40, 40)),
            'img_icon_relatorio':abrir_img("img\\icon_relatorio.png",(40, 40)),
            'img_icon_estoque':abrir_img("img\\icon_estoque.png",(40, 40)),
            'img_icon_producao':abrir_img("img\\icon_producao.png",(40, 40)),
            'img_icon_perfil':abrir_img("img\\icon_perfil.png",(26, 26)),
            'img_icon_saida':abrir_img("img\\icon_saida.png",(26, 26)),
            'img_icon_delete':abrir_img("img\\icon_delete.png",(26, 26)),
            'img_icon_edit':abrir_img("img\\icon_edit.png",(26, 26)),
            'img_icon_voltar':abrir_img("img\\icon_voltar.png",(26, 26))
        }
        return imgs.get(img_nome)
        
    def criar_grafico_circular(tela,valor, desc, titulo):
        fig, ax = plt.subplots()
        fig.patch.set_alpha(0.0)
        ax.pie(valor, labels=desc, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Para manter o formato do gráfico como círculo
        plt.title(titulo, fontsize=12, color="black")  # Ajuste de título e tamanho da fonte
        canvas = FigureCanvasTkAgg(fig, tela)
        plt.close()
        return canvas

    def centralizar_janela(root, largura, altura):
        
        tela_largura = root.winfo_screenwidth()
        tela_altura = root.winfo_screenheight()

        x = (tela_largura // 2) - (largura // 2)
        y = (tela_altura // 2) - (altura // 2)

        root.geometry(f"{largura}x{altura}+{x}+{y}")
        
    def criar_janela_flutuante(titulo, largura, altura):
        root = Toplevel()
        root.title(titulo)
        root.overrideredirect(True)
        root.configure(background="#c8c8c8", borderwidth=2, relief="ridge")
        Style.centralizar_janela(root, largura, altura)
        
        root.maxsize(largura, altura)
        root.minsize(largura, altura)
        root.focus_force()
        root.grab_set()
        
        return root
    
    def gerar_relatorio(dados,nomearq):

        df = pd.DataFrame.from_dict(dados)
        df.to_excel(f"Relatorio {nomearq}.xlsx", index=False)

class MessageBox:

    def showinfo(self, title, message):
        return messagebox.showinfo(title, message)

    def showwarning(self, title, message):
        return messagebox.showwarning(title, message)

    def showerror(self, title, message):
        return messagebox.showerror(title, message)

    def askquestion(self, title, message):
        return messagebox.askquestion(title, message)

    def askretrycancel(self, title, message):
        return messagebox.askretrycancel(title, message)
    