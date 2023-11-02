#print pertama dan input
print ("Selamat Datang di Pizza Hut")
print ("Daftar Topping Yang Tersedia : \n1. Frankfurter BBQ \n2. Meat Monsta \n3. Super Supreme \n4. Super Supreme Chicken \n5. Meat Lovers \n6. Chicken Lovers \n7. Cheese Lovers \n8. American Favourite ")
topping = int(input("Silahkan Pilih Topping Anda (1-8): "))
print ("Daftar Crust Yang Tersedia : \n1. Pan \n2. StuffedCrust Cheese \n3. StuffedCrust Sausage \n4. Cheesy Bites \n5. Crown Crust")
crust = int(input("Silahkan Pilih Crust Anda (1-5): "))
print ("Daftar Ukuran Pizza Yang Tersedia : \n1. Personal \n2. Regular \n3. Large")
ukuran = int(input("Silahkan Pilih Ukuran Pizza Anda (1-3): "))
xtracz = input("Apakah Anda ingin Menambahkan Extra Cheese (Y/N)? ")

#daftar topping
daftar_topping = {
    1: "Frankfurter BBQ",
    2: "Meat Monsta",
    3: "Super Supreme",
    4: "Super Supreme Chicken",
    5: "Meat Lovers",
    6: "Chicken Lovers",
    7: "Cheese Lovers",
    8: "American Lovers",
}

#daftar crust
daftar_crust = {
    1: "Pan",
    2: "StuffedCrust Cheese",
    3: "StuffedCrust Sausage",
    4: "Cheesy Bites",
    5: "Crown Crust",
}

#daftar ukuran
daftar_ukuran = {
    1: "Personal",
    2: "Regular",
    3: "Large",
}

#mengambil nama berdasarkan nomor yang diinput
nama_topping = daftar_topping[topping]
nama_crust = daftar_crust[crust]
nama_ukuran = daftar_ukuran[ukuran]

#deklarasi harga awal = 0 rupiah
harga = 0

#fungsi if untuk harga crust Pan beserta dengan harga per ukuran pizza
if crust == 1:
    harga +=43637 #harga crust Pan
    if ukuran == 1:
        harga += 0 #harga jika ukuran personal
    elif ukuran == 2:
        harga += 57273 #harga jika ukuran legular
    else:
        harga += 89091 #harga jika ukuran large

#fungsi if untuk harga crust StuffedCrust Cheese beserta dengan harga per ukuran pizza
elif crust == 2:
    harga += 55455 #harga crust StuffedCrust Cheese
    if ukuran == !:
        harga += 0 #harga jika ukuran personal
    elif ukuran == 2:
        harga += 65455 #harga jika ukuran legular
    else:
        harga += 104545 #harga jika ukuran large

#fungsi if untuk harga crust StuffedCrust Sausage beserta dengan harga per ukuran pizza
elif crust == 3:
    harga += 52728 #harga crust StuffedCrust Sausage
    if ukuran == 1:
        harga += 0 #harga jika ukuran personal
    elif ukuran == 2:
        harga += 64545 #harga jika ukuran legular
    else:
        harga += 102727 #harga jika ukuran large
