import subprocess
import os
import psutil

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
                    comando = ['java', '-jar', jar_file, '--spring.profiles.active=dsv']
                    subprocess.Popen(comando, creationflags=subprocess.CREATE_NEW_CONSOLE)
                    
                except subprocess.CalledProcessError as e:
                    print(f"Ocorreu um erro ao executar o JAR: {e}")
            else:
                print(f"O JAR {jar_file} já está em execução.")
        else:
            print(f"O arquivo {jar_file} não foi encontrado no diretório.")

if __name__ == "__main__":
    Jar()