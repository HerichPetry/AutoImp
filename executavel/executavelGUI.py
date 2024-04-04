from PySimpleGUI import *

#Configuração da Página Principal
def main_page():
    layout_left= [
        [Image(filename='assets/imp.png', subsample=2)]
    ]

    layout_right = [
        [Push(), Text('AUTOIMP', font=('Arial', 30), text_color='black'), Push()],
        [Push(), Button("INICIAR", key=('-INICIAR-'), size=(10, 2), button_color=('white', 'blue')), Push()],
        [Text('')],
        [Push(), Button("AJUDA", key=('-AJUDA-'), button_color=('white', 'black')),Push(), Button("SAIR", button_color=('white', 'red')), Push()]
    ]

    layout = [
        [Column(layout_left), VSeparator(), Column(layout_right)]
    ]

    return Window('AutoImp', layout=layout, font=('Arial', 15), size=(525, 300)) 


#Configuração da Página de Ajuda
def help_page():
    layout_left= [
        [Image(filename='assets/exemplo.png')]
    ]

    helpText = 'Este programa permite automatizar o processo de instalação de uma impressora de rede. Clique em "INICIAR", após tente instalar a impressora desejada. O programa iniciará a instalação da impressora.'

    layout_right = [
        [Push(), Text('AUTOIMP', font=('Arial', 30), text_color='black'), Push()],
        [Text(helpText, size=(50,0), justification='left')],
        [Push(), Button("VOLTAR", key=('-VOLTAR-')), Push()]
    ]

    layout = [
        [Column(layout_left), VSeparator(), Column(layout_right)]
    ]

    return Window('AutoImp', layout=layout, font=('Arial', 15), size=(930, 300)) 
