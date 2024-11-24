import subprocess
import os
import psutil
import tkinter as tk
from tkinter import messagebox

#'''
class Jar:
    def __init__(self):
        self.executar_jar()
        
    def is_jar_running(self, jar_name):
        #Verifica se o JAR está em execução
        for process in psutil.process_iter(['name', 'cmdline']):
            try:
                cmdline = process.info['cmdline']
                if cmdline and jar_name in cmdline:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return False

    def executar_jar(self):
        jar_file = 'SkyGreen-0.0.1-SNAPSHOT.jar'
        
        if os.path.isfile(jar_file):
            if not self.is_jar_running(jar_file):
                try:
                    # Abre o JAR em uma nova janela do CMD
                    comando = ['java', '-jar', jar_file]
                    subprocess.Popen(comando, creationflags=subprocess.CREATE_NEW_CONSOLE)
                    
                except subprocess.CalledProcessError as e:
                    print(f"Ocorreu um erro ao executar o JAR: {e}")
            else:
                print(f"O JAR {jar_file} já está em execução.")
        else:
            print(f"O arquivo {jar_file} não foi encontrado no diretório.")

if __name__ == "__main__":
    Jar()
#'''

#manutenção==

'''

class Jar:
    def __init__(self):
        self.jar_file = 'SkyGreen-0.0.1-SNAPSHOT.jar'
        self.criar_interface()

    def is_jar_running(self):
        # Verifica se o JAR está em execução
        for process in psutil.process_iter(['name', 'cmdline']):
            try:
                cmdline = process.info['cmdline']
                if cmdline and self.jar_file in cmdline:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return False

    def executar_jar(self, modo):
        if os.path.isfile(self.jar_file):
            if not self.is_jar_running():
                try:
                    if modo == "Homologação":
                        comando = ['java', '-jar', self.jar_file, '--spring.profiles.active=dsv']
                        self.root.destroy()
                    elif modo == "Produção":
                        comando = ['java', '-jar', self.jar_file]
                        self.root.destroy()
                    else:
                        messagebox.showerror("Erro", "Modo inválido!")
                        return
                    
                    subprocess.Popen(comando, creationflags=subprocess.CREATE_NEW_CONSOLE)

                except subprocess.CalledProcessError as e:
                    messagebox.showerror("Erro", f"Ocorreu um erro ao executar o JAR: {e}")
                    self.root.destroy()
            else:
                messagebox.showinfo("Aviso", f"O JAR {self.jar_file} já está em execução.")
                self.root.destroy()
        else:
            messagebox.showerror("Erro", f"O arquivo {self.jar_file} não foi encontrado no diretório.")
            self.root.destroy()

    def criar_interface(self):

        self.root = tk.Tk()
        self.root.title("Gerenciador de JAR")

        btn_producao = tk.Button(self.root, text="Produção", command=lambda: self.executar_jar("Produção"), width=20)
        btn_producao.pack(pady=10)

        btn_homologacao = tk.Button(self.root, text="Homologação", command=lambda: self.executar_jar("Homologação"), width=20)
        btn_homologacao.pack(pady=10)

        self.root.mainloop()

if __name__ == "__main__":
    Jar()

'''
