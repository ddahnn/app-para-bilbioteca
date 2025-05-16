from modelos.itens.ItemBiblioteca import ItemBiblioteca

class Revista( ItemBiblioteca ):
    def __init__(self, titulo, autor, preco, edicao):
        super().__init__(titulo, autor, preco)
        self.edicao = edicao
