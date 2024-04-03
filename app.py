from interface import *




def run_app():  
    window = main_page()

    #events
    while True:
        event, values = window.read()
        
        #variáveis do usuário 
        login = 'bm'
        password = None

        match(event):
            case '-AJUDA-':
                window.close()
                window = help_page()
            case '-VOLTAR-':
                window.close()
                window = main_page()
            case '-GERAR-':
                if popup_yes_no("Login:" , values['-LOGIN-']) == 'Yes':
                    if popup_yes_no("Senha:", values['-SENHA-']) == 'Yes':
                        login = values['-LOGIN-']
                        password = values['-SENHA-']
                        
        if event == WIN_CLOSED or event == 'SAIR':
            break

        
    window.close()

if __name__ == '__main__':
    run_app()