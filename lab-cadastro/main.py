import modules as md
import json
import random
from time import sleep


pnome = str(input("Nome do Paciente: ")).upper

while True:
    
    print("="*30)
    print("[1] Cadastrar Exames")
    print("[2] Registrar Resultados")
    print("[3] Consultar Resultados")
    print("[4] Sair do Aplicatio")
    print("="*30)

    menu = int(input("Escolha uma opção: "))
    if menu == 0 and menu > 4:
        while menu not in 1234:
            menu = int(input("Escolha uma opção válida: "))
    
    elif menu == 1:
        print("="*30)
        print(f"{'CADASTRO DE EXAMES':^30}")
        print("="*30)

        listaExames = [] #Lista com todos os exames para registrar
        while True: 
            
            nExam = str(input("Exame: ")).upper() #nome do exame
            listaExames.append(nExam) #append do exame na lista de exames

            proxExam = str(input("Deseja adicionar mais exames? ")).upper()
            while proxExam != "S" and proxExam != "N":
                proxExam = str(input("Deseja adicionar mais exames? ")).upper()
            if proxExam == "S":
                sleep(1)
            else:
                print("Seguindo para cadastro de resultados...")
                sleep(2)

                resultExam = str(input("Deseja adicionar os resultados agora? ")).upper()
                while resultExam != "S" and resultExam != "N":
                    resultExam = str(input("Deseja adicionar os resultados agora? ")).upper()
                
                if resultExam == "S":

                    listaResultados = []

                    for exame in listaExames:
                        resultado = input(f"Digite o Resultado do exame {exame}: ")
                        listaResultados.append(resultado)

                    resultadoFinal = zip(listaExames, listaResultados) #Montando dicionario para registro
                    print("Resultados cadastrados com sucesso!")
                    print("="*30)
                    sleep(2)
                    print(f"{'Confirmando resultados: ':^30}")
                    print("="*30)
                    sleep(2)
                    for k, v in resultadoFinal:
                        sleep(2)
                        print(f"- {k}: {v}")
                        print("-"*30)
                        sleep(2)
                    break 