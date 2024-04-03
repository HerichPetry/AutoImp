from PySimpleGUI import *

#Configuração da Página Principal
def main_page():
    layout_left= [
        [Image(filename='assets/imp.png', subsample=2)]
    ]

    layout_right = [
        [Push(), Text('AUTOIMP', font=('Arial', 30), text_color='black'), Push()],
        [Text("LOGIN")],
        [Input("bm", key=('-LOGIN-'))],
        [Text("SENHA")],
        [Input(key=('-SENHA-'))],
        [Push(), Button("GERAR", key=('-GERAR-'), button_color=('white', 'blue'), size=(0, 2)), Push(), Button("AJUDA", key=('-AJUDA-'), button_color=('white', 'black')),Push(), Button("SAIR", button_color=('white', 'red')), Push()]
    ]

    layout = [
        [Column(layout_left), VSeparator(), Column(layout_right)]
    ]

    return Window('AutoImp', layout=layout, font=('Arial', 15), size=(600, 300)) 


#Configuração da Página de Ajuda
def help_page():
    layout_left= [
        [Image(filename='assets/exemplo.png')]
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
