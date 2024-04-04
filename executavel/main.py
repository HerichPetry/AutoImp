from executavelGUI import *
import pyautogui as pg
import time


def buscarTela(window):
    procurar = 0
    print("INICIOU A BUSCA")
    popup_ok('Abra a tela de solicitação de credenciais de Administrador de Rede')
    

    while procurar < 10:

        try:
            img = pg.locateCenterOnScreen('impressora.png', confidence=0.7)
            #img_login = pg.locateCenterOnScreen('credenciais.png', confidence=0.7)

            pg.click(img.x, img.y)
            time.sleep(1)
            pg.click(img.x, img.y)
            print('encontrou!')
            break
            

        except:
            window['-INICIAR-'].update(disabled=True)
            window.refresh()
            time.sleep(1)
            print("Não encontrou ainda")
            print(procurar)
            procurar += 1

            if procurar == 9:
                popup_ok('Reinicie a busca!')
                



# Código principal

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
                buscarTela(window)
                window['-INICIAR-'].update(disabled=False)
                window.refresh()
                        
        if event == WIN_CLOSED or event == 'SAIR':
            break

        
    window.close()

if __name__ == '__main__':
    run_app()