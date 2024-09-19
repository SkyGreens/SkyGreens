from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter


from tela_home import telaHome
from tela_monitoramento import telaMonitoramento
from tela_producao import telaProducao
from tela_pedidos import telaPedidos
from tela_usuario import telaUsuarios
from tela_fornecedor import telaFornecedor


fg = "#3ab355" # menu
hover = "#316133" # hover/principal
bg = "#dfeedf" #background


class main:
    
    def __init__(self, root):
        self.root = root
        self.telas = {}

        self.telas["telaHome"] = telaHome(root, self)
        self.telas["telaMonitoramento"] = telaMonitoramento(root, self)
        self.telas["telaFornecedor"] = telaFornecedor(root,self)
        self.telas["telaProducao"] = telaProducao(root, self)
        self.telas["telaPedidos"] = telaPedidos(root,self)
        self.telas["telaUsuarios"] = telaUsuarios(root,self)
        
        
        self.mostrar_tela("telaHome") 

    def mostrar_tela(self, tela_nome):

        for tela in self.telas.values():
            tela.esconder()

        self.telas[tela_nome].mostrar()
    
if __name__ == "__main__":
    
    root = Tk()
    root.title("SkyGreens")
    root.geometry("1300x500")
    root.configure(background=bg)
    app = main(root)
    
    #img_icon_perfil = PhotoImage(file="img\\icon_perfil.png")
    #img_icon_perfil = img_icon_perfil.subsample(3, 3) #diminuir o tamanho
    
    def menu(self):
        
        frame = Frame(root)
        frame.pack(side=TOP,anchor=CENTER)
        frame.configure(background=bg)
        
        button_home = ctk.CTkButton(frame, text="Home",font=('Arial',15,'bold'),corner_radius=3,width=200,height=40,fg_color=fg,hover_color=hover
                                             ,command=lambda: verificar(1))

        button_home.pack(pady=10,padx=1,side=LEFT)

        button_monitoramento = ctk.CTkButton(frame, text="Monitoramento",font=('Arial',15,'bold'),corner_radius=3,width=200,height=40,fg_color=fg,hover_color=hover
                                             ,command=lambda: verificar(2))
        
        button_monitoramento.pack(pady=10,padx=1,side=LEFT)

        button_fornecedor = ctk.CTkButton(frame, text="Fornecedores",font=('Arial',15,'bold'),corner_radius=3,width=200,height=40,fg_color=fg,hover_color=hover
                                             , command=lambda: verificar(3))
        button_fornecedor.pack(pady=10,padx=1,side=LEFT)
        
        button_producao = ctk.CTkButton(frame, text="Produção",font=('Arial',15,'bold'),corner_radius=3,width=200,height=40,fg_color=fg,hover_color=hover
                                             , command=lambda: verificar(4))
        button_producao.pack(pady=10,padx=1,side=LEFT)

        button_pedidos = ctk.CTkButton(frame,text="Pedidos",font=('Arial',15,'bold'),corner_radius=3,width=200,height=40,fg_color=fg,hover_color=hover
                                             ,command=lambda: verificar(5))
        button_pedidos.pack(pady=10,padx=1 ,side=LEFT)
        
        button_usuarios = ctk.CTkButton(frame,text="Usuarios",font=('Arial',15,'bold'),corner_radius=3,width=200,height=40,fg_color=fg,hover_color=hover
                                             ,command=lambda: verificar(6))
        button_usuarios.pack(pady=10,padx=1,side=LEFT)

        def verificar(n):
            buttons = [button_home,button_monitoramento,button_fornecedor,button_producao,button_pedidos,button_usuarios]
            
            # cor padrão
            for button in buttons:
                button.configure(fg_color=fg)
            
            # cor de hover e exibe a tela correspondente
            buttons[n-1].configure(fg_color=hover)
            telas = ["telaHome","telaMonitoramento","telaFornecedor","telaProducao","telaPedidos","telaUsuarios"]
            self.mostrar_tela(telas[n-1])

        if app:
            verificar(1)
    
    def top():
        
        
        frame_top = Frame(root)
        frame_top.pack(side=TOP,fill="x")
        
        label = ctk.CTkLabel(frame_top, text="SkyGreens",font=('Arial',20,'bold'),width=200,height=40,text_color="#353847")
        label.pack(pady=10,side=LEFT)

        #button_perfil = ctk.CTkButton(frame_top,text="",image=img_icon_perfil,width=0,hover_color=hover,fg_color="#172200")
        button_perfil = ctk.CTkButton(frame_top,text="",width=60,hover_color=hover,fg_color="#172200")
        button_perfil.pack(pady=10,padx=20,side=RIGHT)
        menu(app)
        
    top()
    root.mainloop()