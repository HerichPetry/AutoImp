from interface import *
from py_execute import generate_executable



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
                        popup_ok('Selecione o local para salvar o programa')
                        save_path = popup_get_folder('Selecione o local para salvar o programa', no_window=True)

                        if save_path:
                            generate_executable(login, password, save_path)
                            popup_ok("Programa criado!")
                            break
                        
                        else:
                            popup_ok('Falha na operação')
                            break

        if event == WIN_CLOSED or event == 'SAIR':
            break

        
    window.close()

if __name__ == '__main__':
    run_app()