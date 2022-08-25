import re
from time import sleep

#Retorna opção no menu
def opcao():
    while True:
        op = 0
        try:
            op = int(input('\033[1;33mDigite sua opção: \033[m'))
            if op > 3 or op < 1:
                sleep(0.5)
                print('\033[1;31mERRO! Digite uma opção válida.\033[m')
                continue

        except (TypeError, ValueError):
            sleep(0.5)
            print('\033[1;31mERRO! Digite um valor válido.\033[m')
            continue

        except UnboundLocalError:
            print('\033[1;31mERRO! Tentando novamente...\033[m')
            sleep(1)
            break

        except KeyboardInterrupt:
            sleep(0.5)
            print('\033[1;31mUsuário cancelou a ação.\033[m')
            break
        else:
            break

    return op


#Retorna nome
def lerNome():
    while True:
            try:
                n = str(input('NOME: ')).strip().capitalize()
            except KeyboardInterrupt:
                print('\033[1;31mUsuário cancelou a ação.\033[m')
                break
            errado = bool(re.search(r'\d', n))

            if errado:
                print('\033[1;31mERRO! Digite um nome válido. (apenas caracteres de A-Z)\033[m')
                continue
            if n =='':
                print('\033[1;31mERRO! Digite um nome válido.\033[m')

            else:
                break


    return n


#Retorna idade
def lerIdade():
    while True:
        try:
            idade = int(input('IDADE: '))
            if idade > 130 or idade < 0:
                sleep(0.5)
                print('\033[1;31mERRO! Digite uma idade válida.\033[m')
                continue

        except (TypeError, ValueError):
            sleep(0.5)
            print('\033[1;31mERRO! Digite uma idade válida.\033[m')
            continue

        except KeyboardInterrupt:
            print('\033[1;31mUsuário cancelou a ação.\033[m')
            break

        else:
            break

    return idade


def cadastrar(arq):
    nome = lerNome()
    idade = lerIdade()
    try:
        a = open(arq, 'at')
    except:
        print('\033[1;31mERRO! Não Foi possível abrir o arquivo.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[1;31mERRO! Não foi possível escrever os dados')
        else:
            a.close()



    print('\033[1;32mPessoa cadastrada com Sucesso!\033[m')


def lercadastros(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('ERRO! Arquivo não encontrado.')
    except:
        print('ERRO! Não foi possível ler o arquivo.')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]:>3} anos')
    finally:
        a.close()


def finalizar():
    while True:
        parar = False
        loop = ''
        print('\033[1;33mDeseja encerrar o programa?\033[m')
        try:
            loop = str(input('\033[1;33m[S][N]: \033[m')).strip().upper()
        except KeyboardInterrupt:
            print('\033[1;31mUsuário cancelou a ação.\033[m')
            break

        errado = bool(re.search(r'\d', loop))

        if errado:
            print('\033[1;31mERRO! Digite uma resposta válida. (S ou N).\033[m')
            continue

        if loop not in 'SN' or loop == '':
            print('\033[1;31mERRO! Digite uma resposta válida. (S ou N).\033[m')
            continue

        if loop == 'S':
            parar = True
        if loop == 'N':
            break

        return parar


def fecharPrograma():
    print('\033[1;33mObrigado por usar o programa!!\033[m')
    print('\033[1;91mEncerrando\033[m', end='')
    sleep(1)
    print('\033[1;91m.\033[m', end='')
    sleep(1)
    print('\033[1;91m.\033[m', end='')
    sleep(1)
    print('\033[1;91m.\033[m', end='')
    sleep(1)

    exit(0)


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve erro na criação')
    else:
        print(f'Arquivo {nome} criado! ')
