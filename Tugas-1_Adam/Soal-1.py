#1.	Buatlah sebuah program yang menerima 3 input dari user. 
    #Input tersebut berupa:
    #1. Nama bertipe data string
    #2. Umur bertipe data integer
    #3. Tinggi bertipe data float 

nama = input('Masukkan nama:')
umur = int(input('Masukkan umur:'))
tinggi = float(input('Masukkan tinggi:'))
text = 'Nama saya {}, umur saya {} tahun dan tinggi saya {}cm'.format(nama,umur,tinggi)

print(text)