from executavelGUI import *
import pyautogui as pg
import time


def buscarTela():
    print("INICIOU A BUSCA")
    img = pg.locateCenterOnScreen('teste.png', confidence=0.7)

    if img is not None:
        pg.click(img.x, img.y)
        pg.write("teste")
    else:
        print("Não encontrou")
    


def run_app():  
    window = main_page()

    #events
    while True:
        event, values = window.read()
        
        #variáveis do usuário 
        login = None
        password = None

        match(event):
            case '-AJUDA-':
                window.close()
                window = help_page()
            case '-VOLTAR-':
                window.close()
                window = main_page()
            case '-INICIAR-':
                buscarTela()
                        
        if event == WIN_CLOSED or event == 'SAIR':
            break

        
    window.close()

if __name__ == '__main__':
    run_app()