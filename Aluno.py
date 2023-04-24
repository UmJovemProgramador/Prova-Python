# Aluno: César Queiroz Pontes
# Aluno: Antônio Lucas Costa Araújo 

opcao = 0
curso = 0
  
while opcao != 6:

    print("MENU\n Digite 1 para selecionar a turma de ENGENHARIA DE COMPUTAÇÃO\n Digite 2 para selecionar a turma de SISTEMAS DE INFORMAÇÃO\n")
    curso = int(input("Selecione o curso:\n"))

    if curso == 1:

        print("1 - Cadastrar \n")
        print("2 - Consultar \n")
        print("3 - Alterar \n")
        print("4 - Remover \n")
        print("5 - Retornar \n")

        opcao = int(input("Digite a opção \n"))
    #-----------------------------------------------------------------------------------------------------------------------
        if opcao == 1:
            arquivo = open('ENG.txt','a')
            arquivo.write(input("Digite a matrícula do aluno:\n"))
            arquivo.write("\n")
            arquivo.write(input("Digite o nome do aluno:\n"))
            arquivo.write("\n")
            print("Cadastrado com sucesso \n")
            input("Aperte ENTER para continuar")

    #-----------------------------------------------------------------------------------------------------------------------    

        elif opcao == 2:
            arquivo = open('ENG.txt','r')
            cadastro = []
            cadastro = arquivo.readlines()
            num = len(cadastro)
            cont = 0
            while cont < num:
                print("Matrícula do Aluno: ",cadastro[cont]," Nome do Aluno: ",cadastro[(cont+1)])
                cont = cont + 2
            input("Aperte ENTER para continuar\n")

    #-----------------------------------------------------------------------------------------------------------------------

        elif opcao == 5:
             input("Digite ENTER para retornar ao MENU de cursos.\n")
            
    #-----------------------------------------------------------------------------------------------------------------------

        elif opcao == 3:
            arquivo = open("ENG.txt", 'r')
            cadastro = []
            cadastro = arquivo.readlines()
            print(cadastro)
            cad = [s.strip() for s in cadastro]
            cont = 0
            num = len(cad)
            busca = False
            mat = input("Digite a matrícula do aluno:\n")
            while cont < num:
                if mat == cad[cont]:
                    cad[cont] =input("Digite a nova matrícula do aluno:\n")
                    cad[cont+1]=input("Digite a o novo nome do aluno:\n")
                    busca = True
                    break
                cont = cont + 2
            if busca == False:
                print("Matrícula não encontrada \n")
            else:
                arquivo = open("ENG.txt", 'w')
                cont = 0
                num = len(cad)
                while cont < num:
                    arquivo.write(cad[cont])
                    arquivo.write("\n")
                    cont = cont + 1
                print("Aluno cadastrado com sucesso.\n")
                input("Digite ENTER para continuar.\n")
    #-----------------------------------------------------------------------------------------------------------------------

        elif opcao == 4:
            arquivo = open("ENG.txt", 'r')
            cadastro = []
            cadastro = arquivo.readlines()
            cad = [s.strip() for s in cadastro]
            busca = False
            cont = 0
            num = len(cad)
            mat = input("Digite a matrícula do aluno: \n")
            while cont < num:
                if mat == cad[cont]:
                    cad.pop(cont)
                    cad.pop(cont)
                    busca = True
                    break
                cont = cont + 2
            if busca == False:
                print("Matrícula não encontrada.\n")
            else:
                arquivo = open("ENG.txt", 'w')
                cont = 0
                num = len(cad)
                while cont < num:
                    arquivo.write(cad[cont])
                    arquivo.write("\n")
                    cont = cont + 1
                    print("Aluno removido com sucesso")
                    input("Digite ENTER para continuar")
        else:
            print("Opçao Inválida \n")
            input("Aperte ENTER para continuar\n")

    #-----------------------------------------------------------------------------------------------------------------------


    if curso == 2:
        print("1 - Cadastrar \n")
        print("2 - Consultar \n")
        print("3 - Alterar \n")
        print("4 - Remover \n")
        print("5 - Retornar \n")

        opcao = int(input("Digite a opção \n"))
    #-----------------------------------------------------------------------------------------------------------------------
        if opcao == 1:
            arquivo = open('SI.txt','a')
            arquivo.write(input("Digite a matrícula do aluno:\n"))
            arquivo.write("\n")
            arquivo.write(input("Digite o nome do aluno:\n"))
            arquivo.write("\n")
            print("Cadastrado com sucesso \n")
            input("Aperte ENTER para continuar.\n")

    #-----------------------------------------------------------------------------------------------------------------------    

        elif opcao == 2:
            arquivo = open('SI.txt','r')
            cadastro = []
            cadastro = arquivo.readlines()
            num = len(cadastro)
            cont = 0
            while cont < num:
                print("Matrícula do Aluno: ",cadastro[cont]," Nome do Aluno: ",cadastro[(cont+1)])
                cont = cont + 2
            input("Aperte ENTER para continuar\n")

    #-----------------------------------------------------------------------------------------------------------------------

        elif opcao == 5:
            input("Aperte ENTER para retornar ao MENU de cursos.\n")

    #-----------------------------------------------------------------------------------------------------------------------

        elif opcao == 3:
            arquivo = open("SI.txt", 'r')
            cadastro = []
            cadastro = arquivo.readlines()
            print(cadastro)
            cad = [s.strip() for s in cadastro]
            cont = 0
            num = len(cad)
            busca = False
            mat = input("Digite a matrícula do aluno:\n")
            while cont < num:
                if mat == cad[cont]:
                    cad[cont] =input("Digite a nova matrícula do aluno:\n")
                    cad[cont+1]=input("Digite o novo nome do aluno:\n")
                    busca = True
                    break
                cont = cont + 2
            if busca == False:
                print("Matrícula não encontrada \n")
            else:
                arquivo = open("SI.txt", 'w')
                cont = 0
                num = len(cad)
                while cont < num:
                    arquivo.write(cad[cont])
                    arquivo.write("\n")
                    cont = cont + 1
                print("Aluno cadastrado com sucesso.\n")
                input("Digite ENTER para continuar\n")
    #-----------------------------------------------------------------------------------------------------------------------

        elif opcao == 4:
            arquivo = open("SI.txt", 'r')
            cadastro = []
            cadastro = arquivo.readlines()
            cad = [s.strip() for s in cadastro]
            busca = False
            cont = 0
            num = len(cad)
            mat = input("Digite a matrícula do aluno: \n")
            while cont < num:
                if mat == cad[cont]:
                    cad.pop(cont)
                    cad.pop(cont)
                    busca = True
                    break
                cont = cont + 2
            if busca == False:
                print("Matrícula não encontrada")
            else:
                arquivo = open("SI.txt", 'w')
                cont = 0
                num = len(cad)
                while cont < num:
                    arquivo.write(cad[cont])
                    arquivo.write("\n")
                    cont = cont + 1
                    print("Aluno removido com sucesso.\n")
                    input("Digite ENTER para continuar.\n")
        else:
            print("Opçao Inválida \n")
            input("Aperte ENTER para continuar\n")

    #-----------------------------------------------------------------------------------------------------------------------
    else:
        print("Opção de curso inválida.\n") 
        input("Digite ENTER para continuar.\n")