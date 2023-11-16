# TODO 1 Buatlah Fungsi add_expense disini
# TODO 2 Buatlah fungsi calculate_total_expenses disini
# TODO 3 Buatlah fungsi get_expenses_by_date disini
# TODO 4 Buatlah fungsi generate_expenses_report disini

# menyimpan data pengeluaran
expenses = [
    {"tanggal": "2023-07-25", "deskripsi": "Makan Siang", "jumlah": "50000"},
    {"tanggal": "2023-07-25", "deskripsi": "Transportasi", "jumlah": "25000"},
    {"tanggal": "2023-07-26", "deskripsi": "Belanja", "jumlah": "100000"},
]


def add_expense(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))

    expenses.append(
        {"tanggal": date, "deskripsi": description, "jumlah": amount},
    )
    print("Pengeluaran berhasil ditambahkan.")
    return expenses


def calculate_total_expenses(expenses):
    target_date = input("Masukkan tanggal (YYYY-MM-DD) : ")
    total = sum(
        map(
            lambda expense: int(expense["jumlah"])
            if expense["tanggal"] == target_date and expense["jumlah"].isdigit()
            else 0,
            expenses,
        )
    )
    return total


def get_expenses_by_date(expenses):
    tanggal = input("Masukkan tanggal (YYYY-MM-DD) : ")
    matching_expenses = [
        expense for expense in expenses if expense["tanggal"] == tanggal
    ]
    return print(matching_expenses)


def generate_expenses_report(expenses):
    report = ""
    for expense in expenses:
        report += f"Tanggal: {expense['tanggal']}, Deskripsi : {expense['deskripsi']}, Jumlah : {expense['jumlah']}\n"

    return print(report)


def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar\n")


# code 6 lambda

def get_user_get_user_input(command):
    return int(input(command))


def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_get_user_input("Pilih Menu : ")

        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            get_expenses_by_date(expenses)
        elif choice == 4:
            generate_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")


if __name__ == "__main__":
    main()
