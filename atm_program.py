import random
import datetime
from customer import Customer

atm = Customer(id)

# LOOPING PEMERIKSAAN
while True:
    id = int(input("Masukan Pin ATM Anda: "))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin anda salah. Silahkan Masukan Pin lagi: "))
        trial += 1
        if trial == 3:
            print("Error, Terlalu Banyak Kesalahan Dalam Memasukkan Pin.")
            exit()
    while True:
        print("Selamat Datang Di ATM Barengan!")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar")

        selectmenu = int(input("\nSilahkan Pilih Menu: "))

        if selectmenu == 1:
            print("\nSaldo Yang Anda Miliki Sekarang Adalah: Rp. " + str(atm.checkBalance()) + "\n")
        elif selectmenu == 2:
            nominal = float(input("Masukan Nominal Saldo: "))
            verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal " + str(nominal) + "? y/n " + " ")
            if verify_withdraw == "y":
                print("Saldo awal anda adalah: Rp. " + str(atm.checkBalance()) + "")
            else:
                break
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil!")
                print("Saldo anda sekarang tersisa: Rp. " + str(atm.checkBalance()) + "")
            else:
                print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
                print("Silahkan lakukan penambahan saldo")
        elif selectmenu == 3:
            nominal = float(input("Masukan nominal saldo: "))
            verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal " + str(nominal) + "? y/n " + " ")
            if verify_deposit == "y":
                atm.depositBalance(nominal)
                print("Saldo anda sekarang adalah: Rp. " + str(atm.checkBalance()) + "\n")
            else:
                break
        elif selectmenu == 4:
            verify_pin = int(input("Masukan pin anda:"))
            while verify_pin != int(atm.checkPin()):
                print("Pin anda salah, silahkan masukan pin:")

            updated_pin = int(input("Silahkan masukan Pin baru: "))
            print("Pin anda berhasil diganti!")

            verify_newpin = int(input("Coba masukan pin baru!: "))

            if verify_newpin == updated_pin:
                print("pin anda berhasil di perbaharui!")
            else:
                print("Maaf, pin anda salah!")
        elif selectmenu == 5:
            print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
            print("No. Rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", atm.checkBalance())
            print("Terima kasih telah menggunakan ATM Barengan.")
            exit()
        else:
            print("Error. Harap Masukan Nomor Menu yang benar!")