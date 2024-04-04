import tempfile
import subprocess
import os

def generate_executable(login, senha, save_path):

    print('Programa criado, suas credenciais e local salvo', login, senha, save_path)



    # AQUI VAI O SCRIPT PARA GERAR O PROGRAMA 'EXECUTAVEL' COM AS CREDENCIAIS FORNECIDAS
    # QUAIS SÃO OS REQUISITOS PARA RODAS ESSES EXECUTÁVEIS NO COMPUTADOR DO USUÁRIO FINAL???
    
    '''
    # Caminho para o script original do segundo programa
    script_path = 'caminho_para_o_segundo_programa.py'
    
    # Cria um diretório temporário para armazenar a cópia modificada
    with tempfile.TemporaryDirectory() as tmpdir:
        modified_script_path = os.path.join(tmpdir, 'script_modificado.py')
        
        # Lê o script original e substitui os placeholders
        with open(script_path, 'r') as original, open(modified_script_path, 'w') as modified:
            for line in original:
                modified_line = line.replace('LOGIN_PLACEHOLDER', login).replace('SENHA_PLACEHOLDER', senha)
                modified.write(modified_line)
        
        # Usa o PyInstaller para compilar o script modificado em um executável
        subprocess.run(['pyinstaller', '--onefile', '--distpath', save_path, modified_script_path], check=True)
        # O diretório temporário e o script modificado são automaticamente removidos após o bloco with
    '''