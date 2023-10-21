from paciente import *



def main():
    while True:
        try:
            print("Qual é a operação desejada? \n"
                  "1. Criar novo paciente. \n"
                  "2. Vizualizar paciente. \n"
                  "3. Atualizar descrição. \n"
                  "4. Remover um paciente. \n"
                  "5. Arquivar um paciente. \n"
                  "6. Desarquivar um paciente \n"
                  "C. Cancelar e parar o programa. \n")
            usrAnswer = str(input("Digite aqui: "))  # Perguntar ao usuário oque ele quer
            print("Pegando informações... \n ")

            match usrAnswer.lower():
                case "1":
                    createPatient()  # Criar paciente
                case "2":
                    visualisePatients()  # Vizualizar paciente
                case "3":
                    editPatients()  # Editar descrição/histórico do paciente
                case "4":
                    removePatients()  # Remover um paciente
                case "5":
                    archivePatient()  # Arquivar um paciente
                case "6":
                    deArchivePatient()  # Desarquivar um paciente
                case "c":
                    print("--->Parando o programa. como desejado")
                    break
                case _:
                    print(
                        "--->Por favor, selecione umad as opções.\n")  # Caso "Default", para qualquer coisa que não esteja na listagem

        except Exception as erro:  # Caso algo dessa bomba dê merda
            print("Algo deu errado. Por faor, tente novamente~!")
            print(f"O erro em questão, caso você seja meio nerd: {erro}")


if __name__ == '__main__':  # Main
    main()
