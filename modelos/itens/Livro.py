from modelos.itens.ItemBiblioteca import ItemBiblioteca

class Livro( ItemBiblioteca ):
    #herança de sobre escrita, adicona algo que não existia na classe pai
    def __init__(self, titulo, autor, preco, isbn):
        super().__init__(titulo, autor, preco)
        self.isbn = isbn

    def aplicar_Descontos(self):
        self._preco -= (self._preco* 0.10) # 10% de  desconto