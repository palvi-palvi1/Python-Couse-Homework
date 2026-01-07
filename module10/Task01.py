class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author, page_count ):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"book: {self.name}, author: {self.author}, page_count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        print(f"chief_editor: {self.chief_editor}, Magazine: {self.name}")


book = Book("Compartment No. 6", "Rosa Liksom", 192)
magazine = Magazine("Donald Duck", "Aki Hyyppä")
magazine.print_information()
book.print_information()
