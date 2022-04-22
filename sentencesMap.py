import click as clk
from numpy import char

dicionarioDeFrases = dict(
    {1: "Oi mundo",   2: "Esse é um typeGame feito em python"})


class GeradorDeFrases(object):
    index = 0

    def __init__(self, index:int) -> None:
        index = self.index
        pass
        
    def gerarFrase(self, index: int) -> str:
        self.index = index
        return dicionarioDeFrases[index]

    def pegarFrase(self) -> str:
        return dicionarioDeFrases[self.index]

    def retornarCharDoIndex(self, index:int) -> char:
        return dicionarioDeFrases[self.index][index]

        


gerador = GeradorDeFrases(1)
minhaResposta = print("Escreva a seguinte frase: {} ".format(gerador.gerarFrase(1)))

indexDeChar = 0

while(indexDeChar < len(gerador.pegarFrase())):
    c = clk.getchar()   # Gets a single character

    if c == gerador.retornarCharDoIndex(indexDeChar):
        indexDeChar+=1
        print(c)
    else: #errou
        break


