from tkinter import *
import customtkinter as ctk


from access import Access


fg = "#3ab355" # menu
hover = "#316133" # hover/principal
bg = "#dfeedf" #background


if __name__ == "__main__":

    #==Função para centralizar a tela
    def centralizar_tela():
        
        ww = 600 
        wh = 450
        sw = jn_login.winfo_screenwidth()
        sh = jn_login.winfo_screenheight()

        pt = int(sh / 2 - wh / 2)
        pr = int(sw / 2 - ww / 2)

        jn_login.geometry(f"{ww}x{wh}+{pr}+{pt}")

    #==função para pegar o conteudo dos entry e passar como parametro para a função login da classe access
    def chamar(enome,esenha):
        user = enome.get()
        senha = esenha.get()
        Access.login(user,senha)
    
    #==configurar janela
    ctk.set_appearance_mode("light")
    jn_login = Tk()
    jn_login.title("SkyGreens")
    jn_login.geometry("600x450")
    centralizar_tela()
    
    #==Definir o container(frame) para a tela de login
    frame = ctk.CTkFrame(master=jn_login, width=200, height=250, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    #==Componentes
    lb_titulo = ctk.CTkLabel(master=frame, text="Acesse sua conta", font=("Arial", 35, "bold"))
    lb_titulo.pack(pady=30)

    lb_subtitulo = ctk.CTkLabel(master=frame, text="Sua contribuição é essencial! Entre para colaborar conosco!", font=("Arial", 16))
    lb_subtitulo.pack(pady=0)

    en_nome = ctk.CTkEntry(frame,placeholder_text="Usuário",width=400,height=35)
    en_nome.pack(pady=10)
    
    en_senha = ctk.CTkEntry(frame,placeholder_text="Senha",show = "*",width=400,height=35)
    en_senha.pack(pady=10)

    lb_subtitulo = ctk.CTkLabel(master=frame, text=37*"-"+"ou"+37*"-", font=("Arial", 16))
    lb_subtitulo.pack()

    bt_esqsenha = ctk.CTkButton(master=frame, text="Esqueceu a senha?", width=50,height=10, fg_color=fg, hover_color=hover)
    bt_esqsenha.pack()
    
    bt_ok = ctk.CTkButton(frame,text="Ok",font=('Arial',15,'bold'),corner_radius=3,fg_color=fg,hover_color=hover
                              , command=lambda: chamar(en_nome,en_senha),width=400,height=35)
    bt_ok.pack(pady=10)

    jn_login.mainloop()