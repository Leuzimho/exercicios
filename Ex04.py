# Dicionário global para armazenar os usuários
banco_usuarios = []

# Lista global para armazenar os campos obrigatórios definidos pelo usuário
campos_obrigatorios = []

# Função para cadastrar um usuário com campos definidos
def cadastrar_usuario(campos_obrigatorios):
    usuario = {}
    
    # Preencha os campos obrigatórios
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para o campo '{campo}': ")
        usuario[campo] = valor
    
    # Permita ao usuário adicionar campos adicionais
    while True:
        campo_adicional = input("Deseja adicionar um campo adicional (Digite 'sair' para encerrar): ")
        if campo_adicional.lower() == "sair":
            break
        valor_adicional = input(f"Digite o valor para o campo adicional '{campo_adicional}': ")
        usuario[campo_adicional] = valor_adicional
    
    # Adicione o usuário ao banco de dados
    banco_usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# Função para imprimir os usuários com várias opções
def imprimir_usuarios(*args, **kwargs):
    if not banco_usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    while True:
        print("\nMenu de Impressão:")
        print("1 - Imprimir todos os usuários com todas as informações")
        print("2 - Imprimir dados de usuários com nomes especificados")
        print("3 - Imprimir dados de usuários com campos e valores especificados")
        print("4 - Imprimir dados de usuários com nomes e campos especificados")
        print("0 - Voltar ao menu principal")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "0":
            print("Retornando ao menu principal.")
            break
        
        try:
            opcao = int(opcao)
            if opcao == 1:
                imprimir_todos_usuarios()
            elif opcao == 2:
                nomes = input("Digite os nomes separados por vírgula: ").split(",")
                imprimir_usuarios_por_nomes(nomes)
            elif opcao == 3:
                campo = input("Digite o campo para filtrar: ")
                valor = input(f"Digite o valor para o campo '{campo}': ")
                imprimir_usuarios_por_campos(campo, valor)
            elif opcao == 4:
                nomes = input("Digite os nomes separados por vírgula: ").split(",")
                campo = input("Digite o campo para filtrar: ")
                valor = input(f"Digite o valor para o campo '{campo}': ")
                imprimir_usuarios_por_nomes_e_campos(nomes, campo, valor)
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Opção inválida. Tente novamente.")

# Função para imprimir todos os usuários com todas as informações
def imprimir_todos_usuarios():
    print("Lista de Usuários:")
    for usuario in banco_usuarios:
        print(usuario)

# Função para imprimir usuários com nomes especificados
def imprimir_usuarios_por_nomes(nomes):
    if not banco_usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    if not nomes:
        print("Nenhum nome especificado.")
        return
    
    print("Usuários com nomes especificados:")
    for nome in nomes:
        nome = nome.strip()
        for usuario in banco_usuarios:
            if "nome" in usuario and usuario["nome"] == nome:
                print(usuario)

# Função para imprimir usuários com campos e valores especificados
def imprimir_usuarios_por_campos(campo, valor):
    if not banco_usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    if not campo or not valor:
        print("Nenhuma condição especificada.")
        return
    
    print("Usuários que satisfazem às condições:")
    for usuario in banco_usuarios:
        if campo in usuario and usuario[campo] == valor:
            print(usuario)

# Função para imprimir usuários com nomes e campos especificados
def imprimir_usuarios_por_nomes_e_campos(nomes, campo, valor):
    if not banco_usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    if not nomes:
        print("Nenhum nome especificado.")
        return
    
    if not campo or not valor:
        print("Nenhuma condição especificada.")
        return
    
    print("Usuários com nomes e campos especificados:")
    for nome in nomes:
        nome = nome.strip()
        for usuario in banco_usuarios:
            if "nome" in usuario and usuario["nome"] == nome and campo in usuario and usuario[campo] == valor:
                print(usuario)

# Função principal do programa
def main():
    print("Bem-vindo ao Sistema de Gerenciamento de Usuários")
    
    while True:
        print("\nMenu Principal:")
        print("1 - Cadastrar Usuário")
        print("2 - Imprimir Usuários")
        print("0 - Encerrar")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "0":
            print("Encerrando o programa.")
            break
        
        try:
            opcao = int(opcao)
            if opcao == 1:
                cadastrar_usuario(campos_obrigatorios)
            elif opcao == 2:
                imprimir_usuarios()
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
