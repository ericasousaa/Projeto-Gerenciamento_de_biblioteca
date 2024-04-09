class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_book_by_author(self, author):
        author_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                author_books.append(book)
        return author_books

    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        return available_books

    def lend_book(self, book):
        if book.available:
            book.available = False
            print(f"O livro '{book.title}' foi emprestado com sucesso.")
        else:
            print(f"O livro '{book.title}' não está disponível no momento.")

    def return_book(self, book):
        if not book.available:
            book.available = True
            print(f"O livro '{book.title}' foi devolvido com sucesso.")
        else:
            print("Este livro já está disponível na biblioteca.")

    def display_books(self):
        if self.books:
            print("Livros disponíveis na biblioteca:")
            for book in self.books:
                availability = "Disponível" if book.available else "Indisponível"
                print(f"{book} - {availability}")
        else:
            print("Não há livros na biblioteca no momento.")


def main():
    library = Library()

    while True:
        print("\nBem-vindo ao Gerenciamento de Biblioteca! Escolha sua Opção")
        print("1. Adicionar Livro")
        print("2. Buscar Livro por Título")
        print("3. Buscar Livros por Autor")
        print("4. Listar Livros Disponíveis")
        print("5. Emprestar Livro")
        print("6. Devolver Livro")
        print("7. Mostrar Todos os Livros")
        print("8. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            title = input("Digite o título do livro: ")
            author = input("Digite o autor do livro: ")
            isbn = input("Digite o ISBN do livro: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)
            print("O Livro foi adicionado com sucesso!")
        elif choice == "2":
            title = input("Digite o título do livro a ser buscado: ")
            found_book = library.find_book_by_title(title)
            if found_book:
                print(found_book)
            else:
                print("Livro não foi encontrado.")
        elif choice == "3":
            author = input("Digite o autor dos livros a serem buscados: ")
            found_books = library.find_book_by_author(author)
            if found_books:
                print("Livros encontrados:")
                for book in found_books:
                    print(book)
            else:
                print("Nenhum livro encontrado para este autor.")
        elif choice == "4":
            available_books = library.list_available_books()
            if available_books:
                print("Livros disponíveis na biblioteca:")
                for book in available_books:
                    print(book)
            else:
                print("Não há livros disponíveis no momento.")
        elif choice == "5":
            title = input("Digite o título do livro a ser emprestado: ")
            book_to_lend = library.find_book_by_title(title)
            if book_to_lend:
                library.lend_book(book_to_lend)
            else:
                print("Livro não foi encontrado.")
        elif choice == "6":
            title = input("Digite o título do livro a ser devolvido: ")
            book_to_return = library.find_book_by_title(title)
            if book_to_return:
                library.return_book(book_to_return)
            else:
                print("Livro não foi encontrado.")
        elif choice == "7":
            library.display_books()
        elif choice == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente!")


if __name__ == "__main__":
    main()
