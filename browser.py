from os import close, path
import sys
import os
  
class browser:
    def __init__(self):
        self.__dado = []

    #MÉTODO PARA RETORNA NUMERO DE PAGINAS VISITADAS
    def size(self):
        return len(self.__dado)

    #MÉTODO PARA RETORNAR A PAGINA ATUAL
    def home(self):
        try:
            return self.__dado[-1]
        except:
            print('Não existe página.')
    
    #MÉTODO PARA EXIBIR HISTORICO DE VISITAS
    def imprimir(self):
        if len(self.__dado) == 0:
            print("Histórico Vazio!")
        else:
            print(self.__dado.__str__())

    #MÉTODO PARA PROCESSAR DADOS DO USUARIO 
    def menu(self,url):
        #VARIAVEIS PARA VALIDAÇÃO E EXIBIÇÃO DAS PAGINAS
        #caminho para a pasta principal
        root = 'World Wide Web'
        #caminho digitado pelo usuario guardado na variavel "sub"
        sub = url
        #caminho completo
        path = os.path.join(root,sub)

        #VARIAVEIS PARA ABERTURA DOS ARQUIVOS TXT
        #caminho completo ate a pasta do arquivo
        diretorio = path
        #nome do arquivo, com a extensão adicionada 
        arquivo = '/' + url + '.txt'
        # caminho até o arquivo + nome do arquivo com extensao
        caminho = diretorio + arquivo
        # abertura e print do arquivo
        
        #opções do menu
        help = [ "#add: Adicionar nova URL", "#sair: Fechar o Browser", "#showhist: Mostrar o histórico de navegação"]
        
        #EXIBIR TODAS AS FUNÇÕES DO NAVEGADOR
        if url == '#help':
            for i in help:
                print(f'    {i}')

        
        #RETORNAR PARA ULTIMA URL
        elif url == '#back':
            #apenas retorna se houver paginas disponiveis
            try:
                self.__dado.pop()
                print()
                print()
            except:
                print("Não existe Url para retornar.")
            


        #ADICIONAR NOVA URL       
        elif url == '#add':     
            f = 1
            while f == 1:
                nova_url = input(str("Digite a nova URL(#sair):"))
                if nova_url == "#sair":
                    f = 0 
                elif nova_url.startswith('www.') and ('.com' in nova_url or '.com.br' in nova_url) :
                    #definição do caminho, unindo a pasta root + a url digitada pelo usuario
                    path = os.path.join(root,nova_url)
                    os.makedirs(path) 
                    f = 0
                else:
                    print("Url inválida. Teente novamente.")
    
        
        #MOSTRAR HISTORICOS DE VISITAS 
        elif url == '#showhist':
            try:
                print(self.__dado.__str__())
            except:
                print("Histórico Vazio!")
        
        # ENCERRAR O PROGRAMA
        elif url == '#sair':
            sys.exit()
        
        #VALIDAR URLS
        elif os.path.isdir(path):
            self.__dado.append(url)
            # ABRIR O ARQUIVO TXT
            try:
                f = open(caminho, 'r')
                file_contents = f.read()
                print("Página Encontrada:")
                print (file_contents)
                f.close()
            except:
                print("Erro 404: Página Vazia.")
        
        # CONDIÇÃO PARA O COMPLEMENTO INICIADO POR ' / '
        elif str(sub).startswith('/'):
            #subdir é a ultima pagina visitada + o novo dado digitado pelo usario
            #iniciado com '/'
            subdir = self.__dado[-1] + sub
            #o fullpath é a pasta com todos os links(root) + o subdir
            fullpath = os.path.join(root,subdir)
            # testar se a URL resultante é valida
            if os.path.isdir(fullpath):
                self.__dado.append(subdir)
                #ABRIR O ARQUIVO TXT
                try:
                    f = open(caminho, 'r')
                    file_contents = f.read()
                    print("Página Encontrada.")
                    print (file_contents)
                    f.close()
                except:
                    print("Erro 404: Arquivo não encontrado.")
            else:
                print('Entrada inválida!')


        #ENTRADAS INVÁLIDAS 
        else:
            print('Entrada inválida!')

    # MÉTODO PARA EXIBIR OS LINKS ADICIONAIS CASO EXISTIREM 
    def Links(self):
        root = 'World Wide Web'
        sub = self.__dado[-1]
        path = os.path.join(root,sub)
        #condição para se url for valida
        if os.path.isdir(path) :
            #condição para testar se existem sublinks na pagina
            num = len([name for name in os.listdir(path)])
            if num != 0:
                print('Links disponiveis:')
                for i in os.listdir(path):
                    if str(i).endswith('.txt'):
                        None
                    else:
                        print(f'    /{i}')
                    
        else:
            return None


        
    def __str__(self):
        return self.__dado.__str__()


