from browser import *
import time

#   Variaveis

navegador = browser()
flag = 0
url = None

#main
while flag == 0:
    # URL DIGITADA PELO USUARIO
    url = input("Digite a url ou #back para retornar à última página visitada(#help para outras infos):")
    for i in range(3):
        print(".", end="",flush=False)
        time.sleep(0.4)

    print()
    print("*"*30)
    # CHAMADA DO METODO
    navegador.menu(url)

    #APENAS MOSTRAR AS INFORMÇÕES SE HOUVER AO MENOS UM SITE VISITADO
    if navegador.size() > 0:
        print()
        #MOSTRAR HISTORICO
        print(f"Histórico de Visitas:{navegador}")
        #MOSTRAR PAGINA ATUAL
        print(f"Home: {navegador.home()}")
        #CHAMADA DO METODO EM CASOS DE PAGINAS COM SUBLINKS
        navegador.Links() 
            
        print()
    print("*"*30)
    print()
    
    
