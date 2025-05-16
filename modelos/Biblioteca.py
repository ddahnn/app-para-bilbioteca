from modelos.Avaliacao import Avaliacao
from modelos.itens.ItemBiblioteca import ItemBiblioteca


class Biblioteca:
    bibliotecas = []
    def __init__(self, nome):
        self.nome = nome 
        self._ativo = False
        self._avaliacao = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)


    def __str__(self) -> str:
    #    retorna o dado do nome quando efetuado um print no objeto
        return self.nome
    

    # função para a classe
    @classmethod
    def listar_Bibliotecas( cls ):
    #   Lista o nome e a sitação das biliotecas estanciadas
        print(f"{'Nome da bilioteca'.ljust(25)}  |  {'Nota média'.ljust(25)}  |  {'Status'}")#  ljust  adiciona um espaçamento
        for biblioteca in Biblioteca.bibliotecas:
           print(f"{biblioteca.nome.ljust(25)}  |  {str({biblioteca.mediaAvaliacoes}).ljust(25)}  |  {biblioteca.ativo}")

    
    @property
    def ativo(self):
        return "Ativado" if self._ativo else "Desativada"



    def alternaEstado(self):
        # alterna o estado do serviço da biblioteca
        self._ativo = not self._ativo

    def receber_Avaliacao(self, cliente, nota):
        # Recebe avaliaçãoes 
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def mediaAvaliacoes(self):
        #caucula media de avaliação
        if not self._avaliacao:
            return'-'* 10
        soma=sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao), 1)
        return media

    def adicionar_itens(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)
    
    def exibir_Itens(self):
        print(f"Itens da Biblioteca {self.nome}\n")
        for indice, item in enumerate(self._itens, start =1):
            if hasattr(item, "isbn"):
                msg_livro = f'{indice}. Titulo: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | ISBN: {item.isbn}'
                print(msg_livro)
            else:
                msg_revisa= f'{indice}. Titulo: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | Edição: {item.edicao}'
                print(msg_revisa)





















""" 

bibliotecaPublica = Biblioeca()
bibliotecaPublica.nome = "Biblioteca Publica Porto Alegre."
bibliotecaPublica.ativo = True



 VARS = da acesso ao atributo como se fosse um dicionario 
print(vars(bibliotecaPublica))


bibliotecaShopping = Biblioteca()
# Caso o objeto esteja vazio ele retorna um objeto vazio 
print(vars(bibliotecaShopping))

bibliotecas = [bibliotecaPublica, bibliotecaShopping]

for biblioteca in bibliotecas:
    print(vars(biblioteca)) """