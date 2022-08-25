from time import sleep
from funcionalidades import interface, utilidades
arq = 'clientes.txt'

if not utilidades.arquivoExiste(arq):
    utilidades.criarArquivo(arq)

interface.topo('MENU DE PRINCIPAL')
def principal():
    while True:
        interface.linha()
        interface.lista()
        opcao = utilidades.opcao()
        if opcao == 1:
            interface.topo('PESSOAS CADASTRADAS')
            utilidades.lercadastros(arq)
            sleep(1)
            continue

        elif opcao == 2:
            interface.topo('NOVO CADASTRO')
            utilidades.cadastrar(arq)
            sleep(1)
            continue

        elif opcao == 3:
            encerrar = utilidades.finalizar()
            if encerrar:
                utilidades.fecharPrograma()
            else:
                sleep(1)
                continue


principal()

