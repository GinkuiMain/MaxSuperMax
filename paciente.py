import os.path
import shutil


def validar():  # Validar o diretório
    CWD = os.getcwd()
    os.chdir(fr'{CWD}')
    dst_path = 'pacientes'
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)


validar()

cwd = os.getcwd()
os.chdir(f'{cwd}/pacientes')  # Qual o diretório que estamos usando. CWD = Current Working Directory


def createPatient():
    name = str(input("Digite o nome do paciente: "))

    if os.path.exists(f"{name}.txt"):
        return print("\nUsuário já existente\n")  # Se o usuário existe ou não

    desc = str(input("Digite a condição/descrição do paciente: "))
    with open(f"{name}.txt", "w") as file:  # Criar um novo txt, fazendo o uso do "w" (write)
        file.write(f"Nome do Paciente: {name} \n")
        file.write(f"Descrição do paciente: {desc} \n")
        print("\n---> Usuário adicionado com sucesso! \n")


def visualisePatients():
    name = str(input("Digite o nome do paciente que será vizualizado: "))
    print("")

    if os.path.exists(f"{name}.txt"):
        with open(f"{name}.txt", "r") as file:  # Ler o txt, fazendo uso do "r" (read)
            print(file.read())
            print("")
    else:
        print("---> Paciente não encontrado. \n")


def editPatients():
    name = str(input("Digite o nome do paciente que será editado: "))
    descAlter = str(input("Nova descrição: "))

    if os.path.exists(f'{name}.txt'):
        with open(f'{name}.txt', 'r') as f:  # editar a descrição do sujeito, na mesma lógica do adicionar um novo
            lines = f.readlines()
        lines[1] = f"Descrição do paciente: {descAlter} \n"

        with open(f'{name}.txt', 'w') as f:
            f.writelines(lines)
            print("---> Descrição mudada com sucesso!!")
    else:
        print('Paciente não encontrado.')


def removePatients():
    name = str(input("Digite o nome do paciente que será deletado: "))

    if os.path.exists(f"{name}.txt"):  # Validar se usuário existe para deletar
        os.remove(f'{name}.txt')
        print("\n---> Paciente removido com sucesso! \n")
    else:
        print("Usuário não encontrado.")


def archivePatient():
    dst_path = 'pacientesArquivados'
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    name = str(input("Digite o nome do paciente que será arquivado: "))
    if os.path.exists(f"{name}.txt"):
        shutil.move(fr"{cwd}/pacientes/{name}.txt",
                    fr"{cwd}/pacientes/pacientesArquivados/{name}.txt")  # Mover o .txt do paciente com uso do shutil (só está aqui para isso mesmo)
        print("\n---> Paciente arquivado com sucesso! \n")
    else:
        print('Paciente não encontrado.')


def deArchivePatient():
    os.chdir(fr'{cwd}/pacientes/pacientesArquivados')
    name = str(input("Digite o nome do paciente que será arquivado: "))

    if os.path.exists(f"{name}.txt"):
        shutil.move(fr"{cwd}/pacientes/pacientesArquivados/{name}.txt",
                    fr"{cwd}/pacientes/{name}.txt")  # Mover o .txt do paciente com uso do shutil (só está aqui para isso mesmo)
        print("\n---> Paciente desarquivado com sucesso! \n")
    else:
        print('Paciente não encontrado.')
