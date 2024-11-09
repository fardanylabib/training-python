class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # Status ketersediaan buku
    
    def __str__(self):
        return f"{self.title} oleh {self.author} (ISBN: {self.isbn}) - {'Tersedia' if self.is_available else 'Tidak Tersedia'}"