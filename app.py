from modelos.Biblioteca import Biblioteca
from modelos.itens.Livro import Livro
from modelos.itens.Revista import Revista


#estancia dos objetos
bibliotecaPublica = Biblioteca("Biblioteca Publica")
bibliotecaShopping = Biblioteca("Biblioteca Shopping")


livro1 = Livro ("1984", "George orwell", 30.00, "000-0000")
revista1 =Revista( "Nationa Geografic", 'john Doe', 15.00, "Quinta")
livro2 = Livro ( "Para Alem do Bem e do Mal", 'Frederic Nietchze',  45.00, '0000-0000' )

#altera o estado Ativo, Desativada
bibliotecaShopping.alternaEstado()

bibliotecaPublica.receber_Avaliacao("canabico", 9.9)
bibliotecaPublica.receber_Avaliacao("lsdetico" , 8.0)


livro1.aplicar_Descontos()
revista1.aplicar_Descontos()
livro2.aplicar_Descontos()




bibliotecaPublica.adicionar_itens(livro1)
bibliotecaPublica.adicionar_itens(revista1)
bibliotecaPublica.adicionar_itens(livro2)


#lista as biliotecas
def main():
    Biblioteca.listar_Bibliotecas()
    print(vars(livro1))
    print(vars(revista1))
    bibliotecaPublica.exibir_Itens()




if __name__ == "__main__":
    main()


