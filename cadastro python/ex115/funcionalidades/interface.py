def linha():
    print('-' * 50)


def topo(titulo):
    linha()
    print(f'{titulo:^50}')
    linha()


def lista():
    print('\033[1;36m1 - Ver pessoas cadastradas\033[m')
    print('\033[1;36m2 - Cadastrar nova pessoa\033[m')
    print('\033[1;36m3 - Sair do sistema\033[m')
    linha()

