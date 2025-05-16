from modelos.Biblioteca import Biblioteca
from modelos.itens.Livro import Livro
from modelos.itens.Revista import Revista
#estancia dos objetos
bibliotecaPublica = Biblioteca("Biblioteca Publica")
bibliotecaShopping = Biblioteca("Biblioteca Shopping")


livro1 = Livro ("1984", "George orwell", 30.0, "000-0000")
revista1 =Revista( "Nationa Geografic", 'john Doe', 15.0, "Quinta")


#altera o estado Ativo, Desativada
bibliotecaShopping.alternaEstado()

bibliotecaPublica.receber_Avaliacao("canabico", 9.9)
bibliotecaPublica.receber_Avaliacao("lsdetico" , 8.0)






#lista as biliotecas
def main():
    Biblioteca.listar_Bibliotecas()
    print(vars(livro1))
    print(vars(revista1))




if __name__ == "__main__":
    main()


