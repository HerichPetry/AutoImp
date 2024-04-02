from PySimpleGUI import *

#Configuração da Página Principal
def main_page():
    layout_left= [
        [Image(filename='imp.png', subsample=2)]
    ]

    layout_right = [
        [Push(), Text('AUTOIMP', font=('Arial', 30), text_color='black'), Push()],
        [Text("LOGIN")],
        [Input("bm", key=('-LOGIN-'))],
        [Text("SENHA")],
        [Input(key=('-SENHA-'))],
        [Push(), Button("GERAR", key=('-GERAR-')), Push(), Button("AJUDA", key=('-AJUDA-')),Push(), Button("SAIR"), Push()]
    ]

    layout = [
        [Column(layout_left), VSeparator(), Column(layout_right)]
    ]

    return Window('AutoImp', layout=layout, font=('Arial', 15), size=(600, 300)) 


#Configuração da Página de Ajuda
def help_page():
    layout_left= [
        [Image(filename='exemplo.png')]
    ]

    helpText = 'Este programa permite automatizar o processo de inserção de Login e Senha durante a instalação de uma impressora de rede. Após inserir suas credenciais de Administrador de Rede, clique em "GERAR" para que um executável possa ser enviado ao distinatário.'

    layout_right = [
        [Push(), Text('AUTOIMP', font=('Arial', 30), text_color='black'), Push()],
        [Text(helpText, size=(50,0), justification='left')],
        [Push(), Button("VOLTAR", key=('-VOLTAR-')), Push()]
    ]

    layout = [
        [Column(layout_left), VSeparator(), Column(layout_right)]
    ]

    return Window('AutoImp', layout=layout, font=('Arial', 15), size=(930, 300)) 


window = main_page()

#events
while True:
    event, values = window.read()

    match(event):
        case '-AJUDA-':
            window.close()
            window = help_page()
        case '-VOLTAR-':
            window.close()
            window = main_page()

    if event == WIN_CLOSED or event == 'SAIR':
        break

       
window.close()