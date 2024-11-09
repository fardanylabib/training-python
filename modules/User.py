from modules.Loan import Loan
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.loans = []  # Riwayat peminjaman
    
    def borrow_book(self, book, library):
        if len(self.loans) >= library.max_books_per_user:
            print(f"{self.name} telah mencapai batas peminjaman maksimum.")
            return
        if library.lend_book(self, book):
            loan = Loan(self, book)
            self.loans.append(loan)
            print(f"{self.name} meminjam {book.title}.")
        else:
            print(f"{book.title} sedang tidak dapat dipinjam")
    
    def return_book(self, book, library):
        for loan in self.loans:
            if loan.book == book and not loan.returned:
                loan.mark_returned()
                library.return_book(book)
                print(f"{self.name} mengembalikan {book.title}.")
                return
        print(f"{self.name} tidak meminjam {book.title}.")
    
    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id})"
