from datetime import datetime

class Library:
    def __init__(self, max_books_per_user=3):
        self.books = []
        self.users = []
        self.max_books_per_user = max_books_per_user
    
    def add_book(self, book):
        #TODO tambahkan buku ke array self.books
        self.books.append(book)
        print(f"Buku {book.title} berhasil ditambahkan.")
    
    def remove_book(self, book):
        #TODO hapus buku dari array self.books
    
    def register_user(self, user):
        self.users.append(user)
        print(f"User {user.name} berhasil diregistrasi.")
    
    def lend_book(self, user, book):
        if book in self.books and book.is_available:
            book.is_available = False
            return True
        return False
    
    def return_book(self, book):
        book.is_available = True
    
    def check_availability(self, book):
        if book in self.books:
            print(f"Buku {book.title} {'tersedia' if book.is_available else 'tidak tersedia'}.")
        else:
            print(f"{book.title} tidak ada di perpustakaan")
    
    def user_loan_history(self, user):
        print(f"Riwayat peminjaman {user.name}:")
        for loan in user.loans:
            status = "Dikembalikan" if loan.returned else "Belum dikembalikan"
            print(f"  - {loan.book.title} ({status}) - Dipinjamkan pada {loan.loan_date.strftime('%Y-%m-%d')}")
