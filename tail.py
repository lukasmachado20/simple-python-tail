# Nome projeto: Tail Python
# Uso de Iterators, Generators e Coroutines
# Author: Lukas Silva Machado

# O objetivo inicial do tail eh ler um arquivo linha a linha e ficar aguardando
# mais linha ate ser cancelado com CRTL+C

from time import sleep
from os import SEEK_END

def tail(file_name: str):
    # abrimos o arquivo e vamos diretamente para o seu final
    file = open(file_name) 
    file.seek(0, SEEK_END)
    while True:
        line = file.readline()
        if line == "":
            # dorme por um tempo
            # depois le novamente a linha
            sleep(0.4)
        else:
            yield line

def main() -> None:
    # criamos o generator tail
    gen_tail = tail("../countries.txt")
    while True:
        # adicionamos em um loop, assim ele ira rodar
        # indefinidamente esta rotina
        # comportamento padrao de um 'tail -f'
        log_line = next(gen_tail)
        print(log_line, end="")


if __name__ == "__main__":
    main()
