# frete
Programa de fretes desenvolvido integralmente por mim com um prazo de uma semana.
Abaixo, segue uma explicação detalhada do seu funcionamento.

<details>
<summary>Clique aqui para ler a explicação completa do código</summary>
  Ao iniciar, o programa exibe uma tela de menu com 4 opções de escolha, sendo elas 
as funcionalidades: “Consultar Trecho x Modalidade”, “Registrar Transporte”, 
“Dados Estatísticos” e “Finalizar Programa”. Para o programa funcionar, existe uma
função chamada “interagir”, que recebe o valor escolhido no menu. De acordo com a 
opção escolhida, ela contém diferentes operações, mas, basicamente, ela coleta, organiza 
e salva os dados que serão utilizados para cada operação.

  Na primeira funcionalidade, Consultar Trecho x Modalidade, o usuário insere duas 
cidades e uma modalidade, e assim o programa retorna a distância das duas cidades, o 
preço para realizar essa viagem na modalidade escolhida e informa também o preço nas 
outras modalidades. A lógica por trás dessa funcionalidade baseia-se em uma função, 
chamada “trechosModalidade”, que recebe 3 valores: a cidade 1, a cidade 2 e a 
modalidade. Assim, a função coleta a distância das duas cidades, inserida no documento 
csv, agora aberto em uma variável chamada “arquivo”, graças à biblioteca “pandas”. Logo 
após adquirir a informação da distância, são salvas as informações referentes ao número 
de cidades, ao nome das cidades, à distância total e aos veículos deslocados no dicionário 
“salvar”, que posteriormente será salvo completamente em um arquivo chamado 
“data.txt”, que coleta as informações de cada viagem. Logo após, é calculado o valor total 
da viagem pela relação “valor = distância * custo por km”. Depois, com um loop for, são 
feitos os cálculos para as modalidades restantes. Após isso, é perguntado se o usuário 
gostaria de retornar ao menu principal.

  Na segunda funcionalidade, “Registrar Transporte”, o usuário insere quantas cidades 
serão consideradas, os nomes das cidades, quantos tipos de itens diferentes serão levados 
na viagem, o nome do item, (caso não sejam itens que estão na tabela disponibilizada, o 
usuário insere o peso do item em kg) e a quantidade do item. Assim, é retornado para o 
usuário: o peso total a ser levado em quilos, a distância total da viagem, juntamente com 
a distância de cada trecho (ambos em quilômetros), o valor total da viagem em reais, e 
informa também a maneira mais econômica de escolher as opções de tamanho de 
caminhão. Por fim, pergunta ao usuário se quer voltar ao menu principal.

  A lógica por trás da segunda funcionalidade utiliza as informações inseridas, ainda na 
função “interagir” e as funções “compararPrecos” e “salvarInfos”. Na função interagir, é 
obtida a quantidade de cidades a serem consideradas na viagem. Se o valor for maior ou 
igual a 1, é rodado um loop for que pergunta o nome da cidade. Se ela estiver na tabela 
csv, agora aberta na variável “arquivo”, o programa guarda o nome da cidade em uma 
lista chamada “listaCidades” e roda o loop novamente, até o número de cidades 
selecionado pelo usuário. Caso o index do loop não seja 0, o programa salva no dicionário
chamado “dcCidadeDistancia” o nome da cidade anterior, o nome da cidade atual no 
index do loop e a distância entre as duas cidades. No fim do loop, é salvo a “listaCidades” 
no dicionário “salvar”, assim como o “dcCidadeDistancia”, com as keys “listaCidades” e 
“trechosPorCidades”, respectivamente.

  Após isso, é perguntado ao usuário quantos tipos diferentes de itens serão levados na 
viagem. Se o valor informado for menor ou igual a 0, é exibido um aviso de erro, e 
pergunta ao usuário se ele quer retornar ao menu. Se o valor for maior ou igual a 1, é 
salvo no dicionário “salvar” a quantidade de itens diferentes que serão transportados, 
com a key “quantidadeItens”. Agora, é rodado um loop for que pergunta o nome do item, 
confere se ele está na tabela informada. Se o item não estiver na tabela, é pedido para o 
usuário inserir o peso de uma unidade do item em quilogramas. Se o peso for inválido, é 
exibida uma mensagem de erro ao usuário. Porém, se o peso for válido, o programa 
pergunta ao usuário a quantidade do item que será transportado.

  Na variável “pesoTotal”, ainda dentro do loop for, é somado ao seu atual valor o 
produto da quantidade pelo peso. Depois, é feita uma série de formatações, para que o 
programa informe no console a palavra “unidades” para quantidades maiores do que 1 e 
“unidade” para quantidades iguais a 1. Ainda, é removido o “.” e trocado por “,” ao 
informar o peso dos itens, em quilogramas. Feito isso, é rodado um outro loop for que 
informa ao usuário sobre todas as cidades da viagem, juntamente com as distâncias dos 
trechos. Por fim, é salvo no dicionário “salvar” a lista de itens, a distância total e o peso 
total, com as keys “tiposItens”, “distanciaTotal” e “pesoTotal”, respectivamente.

  Ainda dentro da funcionalidade 2, agora vamos utilizar a função “compararPrecos”, que 
recebe os valores de peso total, em toneladas, e a distância total, em quilômetros; para 
que o programa retorne ao usuário a melhor escolha de tamanhos de caminhões, a fim 
de obter o menor preço por quilômetro rodado.

  Ao iniciar a função, ela define 3 variáveis locais: pequeno, médio e grande, todas 
recebendo o valor 0. Elas referem-se à quantidade de caminhões de suas respectivas 
modalidades a serem utilizados na viagem. Depois, é feito um arredondamento no peso. 
Ou seja, se o peso (em toneladas) for um número decimal, será considerado o número 
inteiro maior e mais próximo. Assim, caso a carga tenha 0,5 tonelada ou 1 tonelada, nas 
duas situações, será necessário um caminhão pequeno, pois o mesmo comporta até 1 
tonelada.

  Em seguida, é definida na variável “unidade” a o algarismo da unidade do valor total 
do peso (em toneladas). Com ela, o programa realiza a lógica para escolher qual a melhor 
opção de transporte para esta situação. Em um loop while, com a condição de peso total 
sendo maior do que 2, a unidade é comparada diversas vezes, seguindo a lógica:

• Se for 1 ou 2, é adicionada à variável “pequeno” (quantidade de caminhões 
pequenos) o valor da unidade (algarismo da unidade do peso total). Depois, é 
subtraído do peso total o valor da unidade. Isso pois o peso equivalente da 
unidade agora está sendo levado por caminhões pequenos.

• Caso a unidade seja igual a 3, é adicionado 1 à variável “médio”, porque será 
utilizado 1 caminhão médio, e é subtraído 4 da variável “peso”, porque o 
caminhão médio leva até 4 toneladas.

• Caso a unidade esteja entre 4 e 6, será utilizado 1 caminhão médio para o 
transporte. Então, será adicionado à variável “médio” o valor 1, e subtraído o 
valor 4 da variável “peso”. Depois o valor “unidade - 4” (que é o peso que restou 
para levar em caminhões pequenos) será adicionado à variável “pequeno” e 
subtraído da variável “peso” (porque será transportado por caminhões 
pequenos);

• Caso a unidade seja 7 ou 8, adicione 2 à variável “médio” e subtraia 8 da variável
“peso”;
• E, por fim, se a unidade for 9 ou 0, adicione 1 à variável “grande” e subtraia da 
variável “peso” o valor 10. Caso o loop while não seja mais verdade, o valor 
restante de peso é adicionado à variável “pequeno”.

  Agora, é chamada a função “precoViagem”, que recebe os valores “pequeno, médio, 
grande, distância”. Na função, é definida a variável “veiculosDeslocados”, que é a soma 
das variáveis pequeno, médio e grande. Logo após, é salvo as informações de: veículos 
deslocados, número de caminhões pequenos, médios e grandes, cada um em uma chave 
específica no dicionário “salvar”. Em seguida, as variáveis pequeno, médio e grande são 
multiplicadas pelos seus respectivos valores de custo por quilômetro, informados na 
tabela do exercício. Depois, é salvo em uma variável “valorTotal” a soma das três 
variáveis, que é salva no dicionário “salvar”. Depois, é informado no console o preço total 
da viagem.

  Continuando na função “compararPrecos”, depois de chamar a função “precoViagem”,
é feita uma série de comparações: são definidas três novas variáveis: “frasep”, “frasem” 
e “fraseg”, que recebem o valor “caminhão pequeno” quando suas respectivas variáveis
“pequeno”, “médio” ou “grande” sejam iguais a 1. Caso sejam maiores do que 1, a frase 
fica no plural: “caminhões pequenos”. E, caso sejam igual a 0, a frase é apagada, 
recebendo o valor “” (vazio). Depois, com um loop for, que roda 3 vezes, é escrito no 
console, com o plural correto, a quantidade de caminhões necessária para obter o melhor 
custo monetário. E, por fim, define o valor da variável “pesoTotal” para 0, para que uma 
futura operação não considere o peso da operação atual. Ainda, na função “interagir”, é 
chamada a função “salvarInfos”, que recebe o valor do dicionário “salvar”.

  Dentro da função “salvarInfos”, é definido o valor da variável “localValorTotal”, sendo 
o valor correspondente à key chamada “valorTotal”, dentro do dicionário “salvar”. Após 
isso, são definidas duas variáveis locais: “custoPorTrecho” e “custoMedioPorKm”, 
recebendo os valores, respectivamente, do valor “localValorTotal” dividido pela
(quantidade de cidades – 1) e a distância total (valores adquiridos pelo dicionário 
“salvar”, com suas respectivas keys). Depois, é salvo no dicionário “salvar” essas relações, 
recebendo as keys “custoPorTrecho” e “custoMedioPorKm”.

  Agora, o arquivo “data.txt” é aberto e é salvo o dicionário em uma nova linha do 
arquivo. Após isso, o dicionário é limpo, apagando as informações que agora estão salvas 
no arquivo de texto. Ainda dentro da função “interagir”, agora é chamada a função 
“reiniciar”, que pergunta ao usuário se ele gostaria de voltar ao menu principal.

  Na funcionalidade 3, “Dados Estatísticos”, a função “lerInfos” é chamada. Dentro da 
função, o arquivo “data.txt” é aberto para que as suas linhas sejam contadas e salvas na 
variável “numLinhas”, depois disso é fechado. Logo após, é informado ao usuário o 
número de linhas que o arquivo contém (cada linha é um registro de viagem), e que caso 
ele queira checar algum registro, o mesmo deve inserir o valor do registro.

  Depois, é aberto o arquivo novamente e a linha especificada pelo usuário é lida e salva 
na variável “linha”. Então, para cada chave, há um tratamento específico: caso seja 
relacionada ao peso, a variável sufixo é definida como “kg”, se for relacionada à distância, 
o sufixo é definido como “km”. Caso a chave seja um dicionário ou lista, seus elementos 
serão lidos e formatados corretamente com um loop for, de modo que seja criado um 
resumo legível e claro do que ocorreu na viagem.

  Depois de mostrar as informações da viagem, o programa pergunta se o usuário gostaria 
de checar o gráfico gerado pelo Custo por Distância, utilizando a biblioteca matplotlib. 
Caso o usuário digite “g”, a interface do gráfico abrirá, senão, se tiver digitado “s”, volta 
para o menu, senão o programa encerra. O gráfico é mostrado caso a função “reiniciar” 
receba o valor “grafico”, juntamente com os valores para cada eixo.

  Por fim, na funcionalidade 4, “Encerrar Programa”, o programa se encerra, utilizando a 
função nativa do Python, “exit”, que fecha o programa. Ainda, criei uma função chamada 
“erro”, que é chamada quando o usuário comete algum descuido na hora de utilizar o
programa, informando a ele o que aconteceu de errado, e perguntando se o mesmo 
gostaria de retornar ao Menu Principal.
</details>
