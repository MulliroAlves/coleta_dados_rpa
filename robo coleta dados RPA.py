import pyautogui
import subprocess
import time
import webbrowser

# Caminho para o arquivo de bloco de notas
bloco_caminho = r"C:\Users\MDT Store\Desktop\Dados CNPJs.txt"

# Tempo para esperar carregamento de página ou janela
DELAY = 3


def abrir_site():
    webbrowser.open("https://cnpja.com/")
    time.sleep(5)  # Tempo maior para abrir o navegador e carregar o site


def clicar(x, y):
    pyautogui.click(x, y)
    time.sleep(DELAY)


def digitar(texto):
    pyautogui.write(texto, interval=0.1)
    time.sleep(2)

def digitar_numeros(numeros):
    pyautogui.write(str(numeros), interval=0.1)
    time.sleep(1)


def colar_dados():
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.write (';') 
    time.sleep(1)


def abrir_bloco_notas():
    subprocess.Popen(['notepad.exe', bloco_caminho])
    time.sleep(3)


def voltar_para_navegador():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(2)


def abrir_e_colar():
    abrir_bloco_notas()
    colar_dados()
    voltar_para_navegador()

def copiar_dados():
    clicar(387, 272)      # Clica no resultado
    abrir_bloco_notas()  # Abre o bloco de notas
    pyautogui.press('enter')  # Pressiona Enter para criar uma nova linha
    abrir_e_colar()       # Copia e cola no bloco de notas

    clicar(723, 294)
    abrir_e_colar()

    clicar(863, 344)
    abrir_e_colar()

    clicar(869, 395)
    abrir_e_colar()

    clicar(734, 425)
    abrir_e_colar()
    abrir_bloco_notas()  # Abre o bloco de notas
    pyautogui.press('enter')  # Pressiona Enter para criar uma nova linha



# ===== EXECUÇÃO PRINCIPAL =====

abrir_site()

clicar(635, 411)      # Clique na barra de pesquisa
digitar("Finan")      # Digita "Finan"
clicar(577, 318)      # Clica na sugestão
clicar(387, 272)      # Clica no resultado
abrir_bloco_notas()  # Abre o bloco de notas
pyautogui.press('enter')  # Pressiona Enter para criar uma nova linha
abrir_e_colar()       # Copia e cola no bloco de notas

clicar(723, 294)
abrir_e_colar()

clicar(863, 344)
abrir_e_colar()

clicar(869, 395)
abrir_e_colar()

clicar(734, 425)
abrir_e_colar()
abrir_bloco_notas()  # Abre o bloco de notas
pyautogui.press('enter')  # Pressiona Enter para criar uma nova linha

clicar (904, 111)
digitar_numeros ("00000000000353")

clicar(488, 195) # Clique para copiar o nome
abrir_bloco_notas()  # Abre o bloco de notas
pyautogui.press('enter')  # Pressiona Enter para criar uma nova linha
colar_dados()       # Copia e cola no bloco de notas

voltar_para_navegador()  # Volta para o navegador
clicar(484, 260)      # Clica no resultado
abrir_bloco_notas()  # Abre o bloco de notas
colar_dados()       # Copia e cola no bloco de notas

voltar_para_navegador()  # Volta para o navegador
clicar(698, 292)      # Clica no resultado
abrir_bloco_notas()  # Abre o bloco de notas
colar_dados()       # Copia e cola no bloco de notas

voltar_para_navegador()  # Volta para o navegador
clicar(716, 345)      # Clica no resultado
abrir_bloco_notas()  # Abre o bloco de notas
colar_dados()       # Copia e cola no bloco de notas

voltar_para_navegador()  # Volta para o navegador
clicar(417, 516)
abrir_bloco_notas()  # Abre o bloco de notas
colar_dados()       # Copia e cola no bloco de notas    

voltar_para_navegador()  # Volta para o navegador
clicar(384, 264)
abrir_bloco_notas()  # Abre o bloco de notas
colar_dados()       # Copia e cola no bloco de notas

voltar_para_navegador()  # Volta para o navegador
clicar(308, 185)
abrir_bloco_notas()  # Abre o bloco de notas
colar_dados()       # Copia e cola no bloco de notas
pyautogui.press('enter')  # Pressiona Enter para criar uma nova linha

