import sys
from typing import Iterable, Any
# generators sao uma sintaxe que facilita a implementacao de um iterator protocol
# sao memory eficient porque nao armazenam todos os dados na memoria
# os dados sao utilizados e GERADOS conforme demanda

# Aqui abaixo um exemplo disto

# map eh um metodo que atribui uma funcao a um objeto iterable passado
# ele processa os valores conforme demanda, ele eh um generator
#y = map(lambda i: i **2, x)
# se printarmos o valor de map veremos que ocupa menos memoria que a lista padrao
# print(sys.getsizeof(list(y)))
# print(sys.getsizeof(y))

# nao eh necessario armazenar a sequencia completa na memoria
# podemos pegar os dados conforme iteramos a sequencia

# o comportamento do for loop executa mais ou menos assim

#y = map(lambda i: i **2, x)
#while True:
#    try:
#        print(next(y))
#    except StopIteration:
#        break
#print(y)

# sem o try teriamos o erro de StopIteration
# agora vamos implementar um iterator

class GenericIterator:
    def __init__(self, sequence:  Iterable[Any]): 
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            value = self._sequence[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

x = (1,2,3,4,5)
x_iterator = GenericIterator(x)
for i in x_iterator:
     print(i)
# print("---")

# for i in x_iterator:
#     print(i)

# Agora iremos criar um generator
# def gen(n):
#     for i in range(n):
#         yield i

# gen_object = gen(5)

# print(gen_object.__next__())

# Aqui o comportamento eh igual a um iterator
# ao chamar o __next__ obtemos um valor do iterator
# com isso o estado atual fica salvo na memoria, ele refere-se ao proximo valor
# como ja chamamos o primeiro valor, ele nao esta mais disponivel
# ao chamar o dunder method __next__ iremos obter o proximo valor
# e assim sucessivamente

# print(gen_object.__next__())
# print(gen_object.__next__())
# print(gen_object.__next__())
# podemos utilizar normamente o next() tambem
# print(next(gen_object))

# outra forma de chamar o yield 
# def gen2():
#     yield 1 
#     yield 2
#     yield 3 
#     yield 4 

# gen_object2 = gen2()

# chamamos o primeiro yield, pausamos a execucao da funcao e assim sucessivamente
# print(next(gen_object2))
# print(next(gen_object2))
# print(next(gen_object2))

# ---------------------------------
# CASO DE USO DE UM ITERATOR
# SISTEMA DE GERENCIAMENTO DE LOGS GIGANTES UTILIZANDO GENERATORS 
# Nosso problema aqui eh o processamento de um arquivo de logs muito grande
# Imagine que temos um arquivo com linhas e linhas e logs
# e estamos buscando um informacao especifica neste arquivo
# 1: Podemos ler o arquivo inteiro de uma ver e colocar na memoria
# ocuparia muito espaco e nao seria eficiente
# 2: Utilizamos generators e percorremos linha a linha
#  para checar a informacao que buscamos

# def read_line(file_name):
#     with open(file_name) as line:
#         yield line.readline()

# for line in read_line("fake_logs.txt"):
#     if line.find("user_id=4006"):
#         print(line)
#         break
#     else:
#         continue

# Generator expressions

# para declarar um generator expression eh necesario defini-lo como tuples
# exp_generator = (i for i in range(0, 10))
# print(exp_generator)
# print(next(exp_generator))
# print(next(exp_generator))
# print(next(exp_generator))
# assim ele nao cria a lista inteira na memoria, ele apenas cria o generator
# conforme for necessario ser chamado ele ira gerando os valores

# Os casos de usos mais claros de generators eh quando nao queremos armazenar
# todos os dados de alguma estrutura de dados na memoria
# seja um arquivo, uma lista de numeros ou outro tipo de dado que seja muito massivo
# Ou caso seria quando nao sabemos exatamente quantos valores vamos receber
# isto pode estourar a memoria no momento das verificacoes ou alguma operacao

# send() e throw() 
