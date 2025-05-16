from modelos.itens.ItemBiblioteca import ItemBiblioteca

class Livro( ItemBiblioteca ):
    #herança de sobre escrita, adicona algo que não existia na classe pai
    def __init__(self, titulo, autor, preco, isbn):
        super().__init__(titulo, autor, preco)
        self.isbn = isbn

