# data produk
jenis_produk = {
    1: "kebutuhan kamar",
    2: "pakaian",
    3: "sekincare",
    4: "alat elektronik",
    5: "alat tulis",
    6: "make up"
}

list_produk = {
    1: {
        "lemari           ": 2000000,
        "kasur            ": 1800000,
        "bantal           ": 35000,
        "guling           ": 40000,
        "kaca             ": 350000,
        "AC               ": 3000000
    },
    2: {
        "baju             ": 200000,
        "celana           ": 180000,
        "hijab            ": 80000,
        "jaket            ": 250000,
        "rok              ": 150000
    },
    3: {
        "cream pagi & malam": 400000,
        "handbody          ": 90000,
        "moisturizer       ": 80000,
        "sunscreen         ": 60000,
        "serum             ": 60000
    },
    4: {
        "handphone         ": 4000000,
        "laptop            ": 8000000,
        "mouse             ": 250000,
        "keyboard          ": 350000,
        "ipad              ": 6000000,
        "kipas angin       ": 1300000
    },
    5: {
        "pensil            ": 2500,
        "bulpoin           ": 3000,
        "penghapus         ": 2000,
        "tip-x             ": 4000,
        "stabilo           ": 5000
    },
    6: {
        "eyeshadow         ": 100000,
        "eyeliner          ": 40000,
        "foundation        ": 150000,
        "lipstik           ": 90000,
        "mascara           ": 45000
    }
}

# Fungsi untuk menampilkan produk
def tampilkan_produk():
    print("\nPilih Kategori Produk:")
    for key, value in jenis_produk.items():
        print(f"{key}. {value}")
    pilihan_kategori = int(input("Pilih kategori produk (1-6): "))
    if pilihan_kategori not in jenis_produk:
        print("Kategori tidak valid.")
        return 
    print(f"\nDaftar produk {jenis_produk[pilihan_kategori]}:")
    produk_kategori = list_produk[pilihan_kategori]
    i = 1
    for produk, harga in produk_kategori.items():
        print(f"{i}. {produk}      - Harga: Rp {harga}")
        i += 1
    pilih_produk = int(input("Pilih produk yang ingin dibeli (1-5): "))
    if pilih_produk < 1  or pilih_produk > len(produk_kategori):  # len untuk menghitung yg ada dalam list/dictionary
        print("Produk tidak valid.")
        return
        
    produk_terpilih = list(produk_kategori.items())[pilih_produk - 1]
    produk_nama, harga = produk_terpilih
    print(f"Produk yang Anda pilih: {produk_nama} - Harga: Rp {harga}")
    return (produk_nama, harga)

# Fungsi untuk fitur diskon belanja dan pelanggan lama
def pelanggan(total_belanja, pelanggan_lama):
    if pelanggan_lama == 'y':
        print("Selamat anda mendapatkan diskon 15%")
        diskon = 15
    else:
        print("Ayo daftarkan diri anda dan dapatkan diskon anda")
        diskon = 0  

    if total_belanja > 2000000:
        print("Selamat anda mendapatkan diskon 50%")
        diskon += 50
    elif total_belanja > 1000000:
        print ("selamat anda mendapatkan diskon 30%")
        diskon += 30

    total_diskon = total_belanja * (diskon // 100)
    total_setelah_diskon = total_belanja - total_diskon
    print ("diskon yang didapat :",diskon,"%")
    
    return total_diskon, total_setelah_diskon
# fungsi fitur penawaran di ulang tahun pelanggan
def ulang_tahun():
    penawaran = ("apakah anda sekarang berulang tahun : (y/n)")
    if penawaran == "y":
        print ("selamat ulang tahun!!!!")
        print ("anda mendapat gift spesial dar toko kami")

# Fungsi untuk fitur ongkir
def cek_ongkir(total_ongkir):
    ongkir = 15000
    print(f"Ongkos kirim: Rp {ongkir}")
    return total_ongkir

# Fungsi untuk fitur pendapatan koin karena pengiriman terlambat
def koin_terlambat():
    koin = 0
    terlambat = input("Apakah pengiriman terlambat? (y/n): ")
    if terlambat == "y":
        print("Anda mendapatkan 10k koin untuk pengiriman terlambat!")
        koin += 10000
    return koin

# Fungsi untuk menambah, mengubah, dan menghapus produk dari keranjang belanja
def crud_belanja(keranjang):
    while True:
        print("\n--- CRUD Belanja ---")
        print("1. Tambah Produk")
        print("2. Hapus Produk")
        print("3. Tampilkan Keranjang")
        print("4. Perbarui Produk")
        print("5. Selesai")

        pilihan = int(input("Pilih opsi (1-5): "))

        if pilihan == 1:  # Tambah Produk
            produk = tampilkan_produk()
            if produk:
                nama, harga = produk
                jumlah = int(input("Masukkan jumlah produk: "))
                if jumlah > 3:
                    print("Anda mendapat bonus 1 produk")
                if nama in keranjang:
                    keranjang[nama]['jumlah'] += jumlah
                    keranjang[nama]['total'] += harga * jumlah
                else:
                    keranjang[nama] = {'harga': harga, 'jumlah': jumlah, 'total': harga * jumlah}
                print(f"{jumlah} {nama} berhasil ditambahkan ke keranjang.")

        elif pilihan == 2:  # Hapus Produk
            if not keranjang:
                print("Keranjang belanja kosong.")
            else:
                print("Produk dalam keranjang:")
                for i, (produk, info) in enumerate(keranjang.items(), 1):
                    print(f"{i}. {produk} - {info['jumlah']} pcs - Harga Total: Rp {info['total']}")
                
                hapus = int(input("Pilih produk yang ingin dihapus (misal 1): "))
                if hapus < 1 or hapus > len(keranjang):
                    print("Produk tidak valid.")
                else:
                    produk_dihapus = list(keranjang.items())[hapus - 1]
                    del keranjang[produk_dihapus[0]]
                    print(f"Produk {produk_dihapus[0]} berhasil dihapus.")

        elif pilihan == 3:  # Tampilkan Keranjang
            if not keranjang:
                print("Keranjang belanja kosong.")
            else:
                total_belanja = 0
                print("\n--- Keranjang Belanja ---")
                for produk, info in keranjang.items():
                    print(f"{produk} - {info['jumlah']} pcs - Harga Total: Rp {info['total']}")
                    total_belanja += info['total']
                print(f"Total Belanja: Rp {total_belanja}")

        elif pilihan == 4:  # Perbarui Produk
            if not keranjang:
                print("Keranjang belanja kosong.")
            else:
                print("Produk dalam keranjang:")
                for i, (produk, info) in enumerate(keranjang.items(), 1):
                    print(f"{i}. {produk} - {info['jumlah']} pcs - Harga Total: Rp {info['total']}")
                
                pilih_produk = int(input("Pilih produk yang ingin diperbarui (misal 1): "))
                if pilih_produk < 1 or pilih_produk > len(keranjang):
                    print("Produk tidak valid.")
                else:
                    produk_terpilih = list(keranjang.items())[pilih_produk - 1]
                    nama_produk = produk_terpilih[0]
                    harga_produk = produk_terpilih[1]['harga']
                    print(f"Produk yang dipilih: {nama_produk} - Jumlah: {produk_terpilih[1]['jumlah']} pcs")
                    
                    # Hanya memperbarui jumlah produk
                    jumlah_tambah = int(input("Masukkan jumlah produk yang ingin ditambah: "))
                    keranjang[nama_produk]['jumlah'] += jumlah_tambah
                    keranjang[nama_produk]['total'] += harga_produk * jumlah_tambah
                    print(f"{jumlah_tambah} {nama_produk} berhasil ditambahkan ke keranjang.")

        elif pilihan == 5:  # Selesai
            break
        else:
            print("Pilihan tidak valid.")
    
    return keranjang

# fungsi utama
def proses_belanja():
    print("==========SELAMAT DATANG DI TOKO HAPPY OFFICIAL STORE==========")
    print("=======================SELAMAT BERBELANJA======================")
    print("              Silahkan membuat akun terlebih dahulu")
    login_nama    = input("Nama Lengkap     :")
    login_alamat  = input("Alamat Lengkap   :")
    login_umur    = input("Umur             :")
    jenis_kelamin = input("Jenis Kelamin    :")
    print("             Identitas akun anda berhasil di simpan")

    keranjang = {}  
    while True:
        print("\n--- Belanja ---")
        print("1. Belanja Produk")
        print("2. Proses Pembayaran")
        print("3. Keluar")
        
        pilihan = int(input("Pilih opsi (1-3): "))
        
        if pilihan == 1:  # Belanja Produk
            keranjang = crud_belanja(keranjang)
        
        elif pilihan == 2:  # Proses Pembayaran

                total_belanja = 0
                for item in keranjang.values():
                    total_belanja += item['total']  
                print(f"Total Belanja Sebelum Diskon: Rp {total_belanja}")
                
                vip = input("Apakah anda termasuk pelanggan VIP ? (y/n): ").lower()
                diskon, total_setelah_diskon = pelanggan(total_belanja, vip)
                print(f"Total Setelah Diskon: Rp {total_setelah_diskon}")
                 
                total_ongkir = 15000 
                total_pengiriman = cek_ongkir(total_ongkir) 
                total_harus_dibayar = total_setelah_diskon + total_pengiriman
                print("\n       Riwayat chekout")
                print("Nama Lengkap   :",login_nama)
                print("Alamat Lengkap :",login_alamat)
                print("Umur           :",login_umur)
                print("Jenis Kelamin  :",jenis_kelamin)
                kurir = (input("Jasa Kurir     : "))
                print("Ongkir         :",total_ongkir)
                print("Total yang harus dibayar: Rp",total_harus_dibayar)
                
                print("\n=====Pilih Metode Pembayaran=====")
                print("1. Kartu Kredit/cicilan")
                print("2. Transfer Bank")
                print("3. Shopee pay")
                print("4. Pembayaran di Tempat (COD)")
                pilihan = int(input("Pilih metode pembayaran (1-3): "))

                if pilihan == 1:
                    while True :
                        kredit = int(input("pembayaran dalam 3 bulan / 6 bulan (3/6):"))
                        if kredit == 3:
                            print("setiap bulan anda harus membayar Rp",total_harus_dibayar//3)
                            print("pembayaran dimulai dari bulan depan")
                            break
                        elif kredit == 6:
                            print("setiap bulan anda harus membayar Rp",total_harus_dibayar//6)
                            print("pembayaran dimulai dari bulan depan")
                            break
                        else:
                            print("input tidak valid")
                        
                elif pilihan == 2:
                    namabank = input("Nama bank    :")
                    rekening = input("No. rekening :")
                    print("Pembayaran berhasil")
                elif pilihan == 3:
                    print("Anda memilih metode pembyaran shopee pay")
                elif pilihan == 4:
                    print("siapkan uang tunai sebesar Rp",total_harus_dibayar)
                else:
                    print("Metode pembayaran tidak valid.")

                print(ulang_tahun())
                koin = koin_terlambat() 
                print(f"Anda mendapatkan {koin} koin.")

        elif pilihan == 3:  # Keluar
            print("Terima kasih telah berbelanja!")
            break
        else:
            print("Pilihan tidak valid.") 

# Menjalankan program utama
proses_belanja()
