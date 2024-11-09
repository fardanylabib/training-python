from modules.Library import Library
from modules.Book import Book
from modules.User import User

def display_menu():
    print("\nSistem Manajemen Perpustakaan")
    print("1. Tambah Buku")
    print("2. Buang Buku")
    print("3. Registrasi User")
    print("4. Pinjam Buku")
    print("5. Kembalikan Buku")
    print("6. Cek Ketersediaan Buku")
    print("7. Tampilkan Riwayat Peminjaman")
    print("8. Keluar")

def main():
    library = Library() #objek library
    
    while True:
        display_menu()
        choice = input("Pilih opsi: ")
        
        if choice == '1':
            title = input("Masukkan judul buku: ")
            author = input("Masukkan nama penulis: ")
            isbn = input("Masukkan ISBN buku: ")
            #TODO Implementasikan proses penambahan buku "add_book" ke dalam objek library

        elif choice == '2':
            isbn = input("Masukkan ISBN buku yang akan dibuang: ")
            book = next((b for b in library.books if b.isbn == isbn), None)
            if book:
                #TODO Implementasikan proses pembuangan buku "remove_book" dari objek library
            else:
                print("Buku tidak ditemukan")
        elif choice == '3':
            name = input("Masukkan nama user: ")
            user_id = input("Masukkan ID user: ")
            #TODO implementasikan registrasi user ke dalam library
        
        elif choice == '4':
            user_id = input("Masukkan ID user: ")
            isbn = input("Masukkan ISBN buku untuk dipinjam: ")
            user = next((u for u in library.users if u.user_id == user_id), None)
            book = next((b for b in library.books if b.isbn == isbn), None)

            #TODO implementasikan peminjaman buku yang dilakukan uleh user dengan ID yang dimasukkan
            
        elif choice == '5':
            user_id = input("Masukkan ID user: ")
            isbn = input("Masukkan ISBN buku untuk dikembalikan: ")
            user = next((u for u in library.users if u.user_id == user_id), None)
            book = next((b for b in library.books if b.isbn == isbn), None)
            
            #TODO implementasikan pengembalian buku yang dilakukan uleh user dengan ID yang dimasukkan
        
        elif choice == '6':
            isbn = input("Masukkan ISBN buku to dicek: ")
            book = next((b for b in library.books if b.isbn == isbn), None)
            #TODO implementasikan pengecekan ketersediaan buku
        
        elif choice == '7':
            user_id = input("Masukkan ID user untuk melihat riwayat peminjaman: ")
            user = next((u for u in library.users if u.user_id == user_id), None)
            #TODO implementasikan kode untuk melihat riwayat peminjaman oleh user yang diinput
        
        elif choice == '8':
            print("Keluar dari sistem")
            break
        
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()