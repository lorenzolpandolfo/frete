import pandas as pd
import json
import matplotlib.pyplot as plt

# abre o arquivo das distâncias com a biblioteca pandas
arquivo = pd.read_csv('distancias.csv', encoding='UTF-8', sep=';')

# define a lista de cidades
listaCidades = []

# define as variáveis globais
distanciaTotal = 0
pesoTotal = 0
dinheiro = 0

# define o dicionário "dc"
dc = {
    'celular': 0.5,
    'geladeira': 60,
    'freezer': 100,
    'cadeira': 5,
    'luminaria': 0.8,
    'lavadoraderoupa': 120
}

# define os dicionários "salvar" e "dcCidadeDistancia"
salvar = {}
dcCidadeDistancia = {}


def menu():
    """
    Inicia o menu do programa e roda a função interagir(x), sendo x a opção selecionada no menu.

    Raises:
        ValueError: Se x não for um número inteiro, roda a função erro() informando o erro.
    """
    try:
        # cria o menu e pergunta qual opção o usuário quer escolher
        x = int(input('='*40 + '\n1. Consultar Trechos x Modalidade\n2. Cadastrar Transporte\n3. Dados Estatísticos\n4. Finalizar o Programa\n' + '='*40 + '\nO que você gostaria de fazer? '))

        # roda a função interagir com o parametro x
        interagir(x)

    # caso haja um erro de valor inserido
    except ValueError:
        # o erro é informado ao usuário
        erro('O valor inserido é inválido. Informe somente um valor numérico referente à opção desejada no menu.\n')


def trechosModalidade(c1, c2, m):
    """
    Calcula o preço por modalidade da viagem da cidade 1 para a cidade 2.
    Escreve na tela os seus resultados.

    Args:
        c1 (str): A primeira cidade.
        c2 (str): A segunda cidade.
        m (str): O tipo de modalidade.
    """
    # define a distancia
    distancia = arquivo[c1][arquivo.columns.get_loc(c2)]

    # define a lista de cidades com os valores das cidades
    cidades = [c1, c2]

    # salva informações no dicionário "salvar"
    salvar['quantidadeCidades'] = 2
    salvar['listaCidades'] = cidades
    salvar['distanciaTotal'] = int(distancia)
    salvar['veiculosDeslocados'] = 1

    # compara a variável m e a multiplica pelo valor correspondente
    if m == 'P':
        valor = int(distancia) * 4.87
        salvar['qtdPequeno'] = 1

    elif m == 'M':
        valor = int(distancia) * 11.92
        salvar['qtdMedio'] = 1

    else:
        valor = int(distancia) * 27.44
        salvar['qtdGrande'] = 1

    # formata o valor do dinheiro
    dinheiroCortado = '%.2f' % valor
    displayValor = str(dinheiroCortado).replace('.', ',')

    # define as modalidades em um dicionario, com seus valores
    modalidades = {
        'P': 4.87,
        'M': 11.92,
        'G': 27.44
    }

    # remove a variável 'm' do dicionário "modalidades"
    del modalidades[m]

    # escreve os resultados
    print('-' * 40 + f'\nDe {c1} para {c2}, utilizando a modalidade {m}, a distância é de {distancia} km e o custo será de R$ {displayValor}.\n'
          + '-' * 40 + '\nPara as outras modalidades, os valores são:')

    # para cada item no dicionário modalidades
    for item in modalidades:
        # define o dcvalor
        dcvalor = modalidades[item]

        # define o preco
        preco = dcvalor * distancia

        # formata o preço
        precoFormatado = ('%.2f' % preco).replace('.', ',')

        # escreve na tela as modalidades e preço
        print(f' > Na modalidade {item}, o preço é R$ {precoFormatado}')

    # salva o valor total
    salvar['valorTotal'] = valor

    # chama a função salvarInfos com o parâmetro "salvar"
    salvarInfos(salvar)

    # escreve uma separação final na tela
    print('=' * 40)

    # chama a função de reiniciar
    reiniciar()


def compararPrecos(peso, distancia):
    """
    Calcula, de acordo com o peso, a opção mais barata de caminhões.

    Args:
        peso (float): o peso da carga.
        distancia (float): a distância total da viagem.
    """
    # usa a variavel global pesoTotal
    global pesoTotal

    # define as variaveis pequeno, medio e grande
    pequeno = 0
    medio = 0
    grande = 0

    # compara o peso para ver se é decimal. Se for, arredonda-o para cima
    if peso != int(peso):
        peso = round(peso + 0.5)

    # define o algarismo da unidade do peso
    unidade = peso % 10

    # enquanto o peso for maior do que 2, realiza as relações lógicas
    while peso > 2:
        unidade = peso % 10

        if 1 <= unidade <= 2:
            pequeno += unidade
            peso -= unidade

        elif unidade == 3:
            medio += 1
            peso -= 4

        elif 4 <= unidade <= 6:
            medio += 1
            pequeno += unidade - 4
            peso -= 4 + (unidade - 4)

        elif 7 <= unidade <= 8:
            medio += 2
            peso -= 8

        elif unidade == 9 or unidade == 0:
            grande += 1
            peso -= 10

    # se for menor ou igual a 2 e maior do que 0, adiciona o valor na variável pequeno
    else:
        if peso > 0:
            pequeno += unidade

    # chama a função precoViagem
    precoViagem(pequeno, medio, grande, distancia)

    # arruma o plural das frases
    if pequeno == 0:
        frasep = ''
    elif pequeno == 1:
        frasep = 'caminhão pequeno'
    else:
        frasep = 'caminhões pequenos'

    if medio == 0:
        frasem = ''
    elif medio == 1:
        frasem = 'caminhão médio'
    else:
        frasem = 'caminhões médios'

    if grande == 0:
        fraseg = ''
    elif grande == 1:
        fraseg = 'caminhão grande'
    else:
        fraseg = 'caminhões grandes'

    # escreve uma separação
    print('-'*40)

    # escreve o título dos tipos de transporte
    print(f'De forma a resultar no menor custo de transporte por km rodado, deve-se utilizar:')

    # loop que roda 3 vezes, cada uma para cada modalidade
    for i in range(0, 3):
        if i == 0:
            # confere se é diferente de 0
            if pequeno != 0:
                # escreve na tela a modalidade
                print(f'• {int(pequeno)} {frasep}')

        elif i == 1:
            if medio != 0:
                print(f'• {int(medio)} {frasem}')

        elif i == 2:
            if grande != 0:
                print(f'• {int(grande)} {fraseg}')

    # escreve uma separação
    print('='*40)

    # reseta a variável pesoTotal
    pesoTotal = 0


def precoViagem(p, m, g, distancia):
    """
    Calcula o preço da viagem, de acordo com o número de caminhões de cada modalidade e com a distância.

    Args:
        p (int) = número de caminhões pequenos
        m (int) = número de caminhões médios
        g (int) = número de caminhões grandes
        distancia (int) = distância total do trajeto
    """
    # utiliza a variável global dinheiro
    global dinheiro

    # define a variavel veiculosDeslocados como a parte inteira da soma dos parâmetros p, m, g
    veiculosDeslocados = int(p + m + g)

    # salva as informações no dicionário "salvar"
    salvar['veiculosDeslocados'] = veiculosDeslocados
    salvar['qtdPequeno'] = p
    salvar['qtdMedio'] = m
    salvar['qtdGrande'] = g

    # multiplica as variáveis pelos valores de cada modalidade e pela distância
    p = p * 4.87 * distancia
    m = m * 11.92 * distancia
    g = g * 27.44 * distancia

    # define o valor total como a soma das modalidades agora multiplicadas pela distância e pela modalidade
    valorTotal = p + m + g

    # formata o dinheiro, deixando apenas 2 caracteres após a vírgula
    dinheiro = '%.2f' % valorTotal

    # salva o valor total no dicionário "salvar"
    salvar['valorTotal'] = valorTotal

    # escreve uma separação
    print('-'*40)

    # escreve o valor total da viagem
    print(f'O valor total da viagem será R${dinheiro.replace(".", ",")}.')


def erro(e):
    """
    Retorna uma mensagem erro no console.

    Args:
        e (str): a mensagem de erro.
    """
    # escreve o parâmetro "e"
    print(e)

    # roda a função reiniciar
    reiniciar()


def interagir(acao):
    """
    Adquire as informações para posteriormente rodar as funções de cada opção escolhida no menu.

    Args:
        acao (int): opção selecionada na função menu().
    """
    # informa quais variáveis globais serão utilizadas
    global distanciaTotal
    global pesoTotal

    # define a lista tiposDeModalidade
    tiposDeModalidade = ['P', 'M', 'G']

    # se a ação escolhida for 1
    if acao == 1:
        # cria o menu do Consultar Trechos x Modalidade
        cidade1 = input('\n' + '='*40 + '\nConsultar Trechos x Modalidade\n' + '='*40 + '\nInsira a Cidade 1: ').upper().strip()

        # se a cidade1 escolhida estiver no arquivo
        if cidade1 in arquivo.columns:

            # pede para o usuário inserir a cidade2
            cidade2 = input('Insira a Cidade 2: ').upper()

            # se a cidade2 escolhida estiver no arquivo
            if cidade2 in arquivo.columns:

                # se as cidades forem diferentes
                if cidade2 != cidade1:

                    # pede para o usuário inserir a modalidade
                    modalidade = input('Insira a Modalidade (P, M, G): ').upper()

                    # se a modalidade for considerada
                    if modalidade in tiposDeModalidade:
                        # chama a função trechosModalidade
                        trechosModalidade(cidade1, cidade2, modalidade)

                    # caso a modalidade não exista
                    else:
                        erro(f'a modalidade {modalidade} não existe.\n')

                # caso as cidades sejam iguais
                else:
                    erro(f'As cidades {cidade1} e {cidade2} são iguais.\n')

            # caso a cidade2 não seja encontrada
            else:
                erro(f'A cidade {cidade2} não foi encontrada no sistema.\n')

        # caso a cidade1 não seja encontrada
        else:
            erro(f'A cidade {cidade1} não foi encontrada no sistema.\n')

    # se a ação escolhida for 2
    elif acao == 2:
        try:
            # cria o menu do Cadastrar Transporte e pergunta quantas cidades serão consideradas
            quantidadeCidades = int(input('\n' + '='*40 + '\nCadastrar Transporte\n' + '='*40 + '\nQuantas cidades serão consideradas? '))

            # salva o número de cidades consideradas no dicionário "salvar"
            salvar['quantidadeCidades'] = quantidadeCidades

            # se a quantidade de cidades for menor ou igual a 1
            if quantidadeCidades <= 1:
                erro('Você deve especificar ao menos duas cidades.\n')

            # para cada cidade considerada
            for i in range(0, quantidadeCidades):
                # pede para o usuário digitar o nome da cidade
                cidade = input(f'Digite o nome da Cidade {i + 1} ').upper()

                # se a cidade estiver no arquivo
                if cidade in arquivo.columns:

                    # adiciona à lista "listaCidades" a cidade
                    listaCidades.append(cidade)

                    # se o index do loop for maior do que 0
                    if i > 0:

                        # salva o nome da cidade anterior
                        cidadeAnterior = str(listaCidades[i-1 : i]).replace("'", "").replace(']','').replace('[', '')

                        # salva a distância anterior em relação à atual
                        distanciaAnteriorAtual = float(arquivo[cidadeAnterior][arquivo.columns.get_loc(cidade)])

                        # adiciona à distância total a distância anterior em relação à atual
                        distanciaTotal += distanciaAnteriorAtual

                        # adiciona no dicionário a distância entre a cidade anterior e a cidade atual
                        dcCidadeDistancia[f'{cidadeAnterior} para {cidade}'] = int(distanciaAnteriorAtual)

                # se a cidade nao for encontrada no arquivo
                else:
                    erro(f'A cidade {cidade} não foi encontrada no sistema.\n')

            # salva a lista de cidades e trechos por cidades
            salvar['listaCidades'] = listaCidades
            salvar['trechosPorCidades'] = dcCidadeDistancia

            # cria uma separação
            print('-'*40)

            # pergunta ao usuário quantos itens diferentes serão levados
            item = int(input('Quantos tipos de itens diferentes serão levados na viagem? (celular, geladeira, cadeira, etc) '))

            # se o item for menor ou igual a 0
            if item <= 0:
                # informa sobre o erro
                erro('Você deve especificar uma quantidade válida de itens.\n')

            # se o item for maior do que 0
            else:
                # salva o item
                salvar['quantidadeItens'] = item

            # define o dicionário listaItens
            listaItens = {}

            # loop para cada item
            for x in range(0, item):
                # pede ao usuário o nome do item
                tipo = input(f'Insira o nome do item {x + 1} ')

                # confere se o tipo de item está no dicionário
                if tipo.lower().replace(' ', '') in dc.keys():

                    # retoma o peso em kg do item
                    pesoPorItem = float(dc.get(tipo.lower().replace(' ', '')))

                # se o item não está no dicionário
                else:
                    # pede para o usuário inserir o peso da unidade em kg
                    pesoPorItem = float(input(f'Por favor, insira o peso em kg da unidade de {tipo}. '))

                    # confere se o peso é válido
                    if pesoPorItem <= 0:
                        erro('O peso não pode ser menor ou igual a 0 kg.\n')

                # pergunta a quantidade de itens do tipo inserido
                quantidadeItens = int(input(f'Qual a quantidade de itens do tipo {tipo}? '))

                # confere se a quantidade de itens é valida
                if quantidadeItens <= 0:
                    # informa ao usuário sobre o erro
                    erro('A quantidade não pode ser menor ou igual a 0 unidades.\n')

                # escreve uma separação no console
                print('-' * 40)

                # adiciona ao peso total o produto da quantidade de itens pelo peso
                pesoTotal += (quantidadeItens * pesoPorItem)

                # arruma o plural da variável texto
                if quantidadeItens > 1:
                    texto = 'unidades'
                else:
                    texto = 'unidade'

                # formata os pesos por item, deixando-o com apenas 1 casa decimal
                pesoPorItemFormatado = '%.1f' % pesoPorItem
                totalFormatado = '%.1f' % (quantidadeItens * pesoPorItem)

                # exibe na tela as informações
                listaItens[tipo] = f'{int(quantidadeItens)} {texto} ({pesoPorItemFormatado.replace(".", ",")} kg por unidade, {totalFormatado.replace(".", ",")} kg ao total).'

            # formata o peso total, deixando-o com apenas 1 casa decimal
            pesoTotalFormatado = '%.1f' % pesoTotal

            # exibe na tela o peso total
            print(f'O peso total é de {pesoTotalFormatado.replace(".", ",")} kg\nA viagem tem ao total {int(distanciaTotal)} km')

            # exibe na tela cada trecho no dicionário, com suas distâncias
            for cidade in dcCidadeDistancia:
                localValor = dcCidadeDistancia[cidade]
                print(f'  > {cidade}: {localValor} km')

            # salva os itens
            salvar['tiposItens'] = listaItens
            salvar['distanciaTotal'] = distanciaTotal
            salvar['pesoTotal'] = pesoTotal

            # chama a função compararPrecos
            compararPrecos(pesoTotal/1000, distanciaTotal)

            # salva o dicionario "salvar"
            salvarInfos(salvar)

            # chama a função reiniciar
            reiniciar()

        # se acontecer um erro de valor inserido, informa ao usuario chamando a função de erro
        except ValueError:
            erro('O valor inserido é inválido. Informe somente valores numéricos inteiros.\n')

    # roda se a ação escolhida for 3
    elif acao == 3:
        # cria o menu dos Dados Estatísticos
        print('\n' + '=' * 40 + '\nDados Estatísticos\n' + '=' * 40)

        # chama a função lerInfos
        lerInfos()

    # fecha o programa caso nenhuma ação considerada tenha sido escolhida
    else:
        exit()


def reiniciar(g='', a=0.0, b=0):
    """
    Pergunta ao usuário se gostaria de retornar ao menu principal.
    É utilizada após erros ou a conclusão de operações.
    """
    # define as variaveis globais a serem utilizadas
    global distanciaTotal
    global pesoTotal
    global listaCidades
    global dcCidadeDistancia

    # se o parâmetro g for igual a 'grafico'
    if g == 'grafico':
        # pergunta se o usuário quer checar o gráfico
        escolha = input('Se quiser checar o gráfico de Custo por Distância, digite g.\nSenão, deseja retornar ao Menu Principal? (S/N) ').upper()

        # se o usuário digitar 'S'
        if escolha == 'S':
            # pula uma linha e reseta as variaveis globais
            print('')
            distanciaTotal = 0
            pesoTotal = 0
            listaCidades.clear()
            dcCidadeDistancia.clear()
            menu()

        # se o usuario digitar 'G'
        elif escolha == 'G':
            # define a função do gráfico
            x = [0, b]
            y = [i * a for i in x]

            # cria o gráfico
            plt.plot(x, y, color='r', linestyle='solid')

            # define o eixo X
            plt.xlabel('Distância')

            # define o eixo Y
            plt.ylabel('Custo')

            # define o título
            plt.title('Gráfico custo por distância')

            # exibe o grafico
            plt.show()

            # ao fechar o grafico, pergunta se o usuário quer voltar ao menu
            reiniciar()

        # se o usuário não escolheu nem 'S' nem 'G'
        else:
            # fecha o programa
            exit()
    # se o parâmetro G não for igual a 'grafico'
    else:
        # pergunta se o usuario quer voltar ao menu principal
        escolha = input('Retornar ao Menu Principal? (S/N) ').upper()

        # se ele escolher S
        if escolha == 'S':

            # pula uma linha
            print('')

            # reseta as variáveis globais
            distanciaTotal = 0
            pesoTotal = 0
            listaCidades.clear()
            dcCidadeDistancia.clear()

            # volta ao menu
            menu()

        # se ele não escolher S
        else:
            # fecha o programa
            exit()


def lerInfos():
    # abre o arquivo para contar o numero de linhas
    with open('data.txt', 'r', encoding='utf8') as notas:
        # recebe as linhas na variável linhas
        linhas = notas.readlines()

        # salva o número de linhas na variável numLinhas
        numLinhas = len(linhas)

        # fecha o arquivo
        notas.close()

    try:
        # informa quantas linhas tem no arquivo e pergunta o que o usuário quer fazer
        escolha = int(input(f'> O arquivo contém {numLinhas} registros.\nCaso queira checar algum registro,'
                            f' digite o número.\nSenão, aperte Enter para retornar ao menu. '))

        # abre o arquivo para ler a linha correta
        with open('data.txt', 'r', encoding='utf8') as blocodetexto:

            # ignora as linhas que não estão sendo procuradas
            for i in range(escolha - 1):
                blocodetexto.readline()

            # le a linha correta e salva na variavel linha
            linha = blocodetexto.readline()

        # se a escolha for maior do que 0
        if escolha > 0:
            # escreve o título de Informações Estatistícas da Viagem
            print('\n' + '=' * 40 + f'\nInformações Estatistícas da Viagem {escolha}:\n' + '=' * 40)

            # carrega o dicionário na linha na variável "dicionario"
            dicionario = json.loads(linha)

            # define duas variáveis
            localDistanciaTotal = 0
            localCustoMedio = 0

            # para cada chave no dicionário
            for chave in dicionario:

                # define o valor da chave
                valor = dicionario[chave]

                # define o sufixo
                sufixo = ''

                # para cada tipo de chave, realiza operações específicas
                if chave == 'pesoTotal':
                    chave = 'Peso Total'
                    valor = '%.1f' % valor
                    valor = valor.replace(".", ",").replace(",0", "")
                    sufixo = 'kg.'

                elif chave == 'quantidadeCidades':
                    chave = 'Quantidade de Cidades'
                    sufixo = 'cidades.'

                elif chave == 'quantidadeItens':
                    chave = 'Quantidade de Itens'
                    if valor > 1:
                        sufixo = 'itens.'
                    else:
                        sufixo = 'item.'

                elif chave == 'veiculosDeslocados':
                    chave = 'Veículos Deslocados'
                    if valor > 1:
                        sufixo = 'caminhões.'
                    else:
                        sufixo = 'caminhão.'
                    print('-' * 40)

                elif chave == 'distanciaTotal':
                    chave = 'Distância Total'
                    valor = int(valor)
                    localDistanciaTotal = valor
                    sufixo = 'km.'
                    print('-' * 40)

                elif chave == 'valorTotal':
                    chave = 'Valor Total'
                    print('-' * 40)

                elif chave == 'listaCidades':
                    chave = 'Cidades'
                    valor = str(valor).replace('[','').replace("'", "").replace(']','')

                # se tiver "qtd" na chave, ou seja, quantidade de caminhões
                if 'qtd' in chave:
                    if valor == 1:
                        sufixo = 'caminhão.'
                        chave = chave.replace('qtd', 'Quantidade de Caminhão ').replace('Medio', 'Médio')
                        print(f'• {chave}: {1} {sufixo}')

                    elif valor > 1:
                        sufixo = 'caminhões.'
                        chave = chave.replace('qtd', 'Quantidade de Caminhões ').replace('Pequeno', 'Pequenos')\
                            .replace('Medio','Médios').replace('Grande', 'Grandes')
                        print(f'• {chave}: {int(valor)} {sufixo}')

                # se for algo relacionado a dinheiro
                elif 'custo' in chave or 'Valor' in chave:
                    sufixo = 'Reais.'
                    formatadoParaDinheiro = '%.2f' % valor
                    formatadoParaDinheiro = formatadoParaDinheiro.replace(".", ",").replace(",0", "")

                    if chave == 'custoPorTrecho':
                        chave = 'Custo sobre Trecho'

                    elif chave == 'custoMedioPorKm':
                        chave = 'Custo Médio por Km'
                        localCustoMedio = valor

                    print(f'• {chave}: {formatadoParaDinheiro} {sufixo}')

                elif chave == 'trechosPorCidades':
                    qtdTrechos = len(valor.keys())
                    if qtdTrechos > 1:
                        sufixo = 'trechos'
                    else:
                        sufixo = 'trecho'

                    print(f'• Quantidade de Trechos: {qtdTrechos} {sufixo}.')

                    print('• Trechos por Cidades:')
                    for i in valor:
                        distancia = valor[i]
                        dinheiroFormatado = ("%.2f" % (distancia * dicionario["custoMedioPorKm"])).replace('.', ',')
                        print(f'  > {i}: {distancia} km (O trecho custa R$ {dinheiroFormatado} para ser rodado).')
                    print('-'*40)

                elif chave == 'tiposItens':
                    for c in valor:
                        info = valor[c]
                        print(f'  > {c}: {info.replace(",0", "")}')

                else:
                    print(f'• {chave}: {valor} {sufixo}')

            # escreve uma separação
            print('-' * 40)

            # fecha o arquivo
            blocodetexto.close()

            # chama a função reiniciar, com os parâmetros: gráfico, localCustoMedio, localDistanciaTotal
            reiniciar('grafico', localCustoMedio, localDistanciaTotal)

        # se a escolha não for maior do que 0
        else:
            # escreve uma separação
            print('')
            # volta para o menu
            menu()

    # caso haja um erro de valor inserido
    except ValueError:
        # cria uma separação
        print('')
        # volta para o menu
        menu()


def salvarInfos(dicionario):
    """
    salva as informações no arquivo de texto "data.txt"
    define também as informações de custo por trecho e custo médio por km
    """
    # define o valor de localValorTotal como o valor total da viagem
    localValorTotal = salvar.get('valorTotal')

    # define as variaveis custo por trecho e custo medio por km
    custoPorTrecho = localValorTotal / (salvar.get('quantidadeCidades') - 1)
    custoMedioPorKm = localValorTotal / salvar.get('distanciaTotal')

    # salva as variaveis custo por trecho e custo medio por km no dicionario "salvar"
    salvar['custoPorTrecho'] = custoPorTrecho
    salvar['custoMedioPorKm'] = custoMedioPorKm

    # abre o arquivo e escreve na linha mais recente o dicionário, parâmetro da função, e pula uma linha
    with open('data.txt', 'a', encoding='utf8') as notas:
        json.dump(dicionario, notas)
        notas.write('\n')

    # limpa o dicionário salvar
    salvar.clear()

    # fecha o arquivo
    notas.close()


# inicia o menu
menu()
