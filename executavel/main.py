from executavelGUI import *
import pyautogui as pg
import time


def buscarTela():
    procurar = "sim"
    print("INICIOU A BUSCA")

    while procurar == "sim":

        try:
            img = pg.locateCenterOnScreen('impressora.png', confidence=0.7)
            #img_login = pg.locateCenterOnScreen('credenciais.png', confidence=0.7)

            pg.click(img.x, img.y)
            time.sleep(1)
            pg.click(img.x, img.y)
            print('encontrou!')
            procurar = "não"

        except:
            time.sleep(1)
            print("Não encontrou ainda")


            '''if img is not None:
                pg.click(img.x, img.y)
                time.sleep(1)
                print('encontrou!')
                break
            
            else:
                print("Não encontrou")
                time.sleep(1)
            
            '''


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