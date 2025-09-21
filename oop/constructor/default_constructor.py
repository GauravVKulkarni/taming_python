class Book:
    def __init__(self, title = None, author = None):
        self.title = title if title else "Unknown"
        self.author = author if author else "Unknown"

    def describe(self):
        return {"Title": self.title, "Author": self.author}

book1 = Book()
book2 = Book("Once upon a time in Kurduwadi")
book3 = Book(None, "Jensen Huang")
book4 = Book("The path that leads to peace", "Donald J. Trump")

print([x for x in [book1.describe(),book2.describe(),book3.describe(),book4.describe()]])