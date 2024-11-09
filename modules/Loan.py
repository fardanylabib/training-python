from datetime import datetime
class Loan:
    def __init__(self, user, book):
        self.user = user
        self.book = book
        self.loan_date = datetime.now()
        self.returned = False
    
    def mark_returned(self):
        self.returned = True
        self.return_date = datetime.now()
    
    def __str__(self):
        return f"{self.book.title} Dipinjam oleh {self.user.name} pada {self.loan_date.strftime('%Y-%m-%d')}"
