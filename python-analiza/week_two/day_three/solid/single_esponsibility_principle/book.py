class Book:
    def __init__(self, title: str, author: str, content : str):
        self.title = title
        self.author = author
        self.content = content
        
    def save_to_file(self, filename: str):
        with open(filename, 'w') as file:
            file.write(self.content)   
                
    def load_from_file(self, filename: str):
        with open(filename, 'r') as file:
            self.content = file.read()
            
             
class Book:
    def __init__(self, title: str, author: str, content : str):
        self.title = title
        self.author = author
        self.content = content

class BookRepository:
    def save_to_file(self, book: Book, filename: str):
        with open(filename, 'w') as file:
            file.write(book.content)

    def load_from_file(self, book: Book, filename: str):
        with open(filename, 'r') as file:
            book.content = file.read()