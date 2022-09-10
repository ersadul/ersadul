# # 1. Hello World 
# print("Hello World")
# print("Saya sedang belajar Python")
# print("Saya menggunakan Sistem operasi Windows")
# print("Saya menggunakan teks editor VisualStudioCode")
# print("Selamat Datang di Python")


# # 2. Variables & Type 
# panjang = 1.52
# lebar = 52.5
# hasil = lebar / panjang ** 2
# # print(hasil)

# print(type(hasil)) # <class 'float'>

# bulan = 30
# print(type(bulan)) # <class 'int'>

# x = 'strings'
# print(type(x)) # <class 'str'>

# y = True
# print(type(y)) # <class 'bool'>


# # 3. Definition Lists
# panjang1 = 5
# panjang2 = 4
# panjang3 = 6

# warna = [6.3, 7.3, 8.3, 9.1]
# print(warna)

# warna = ['merah', 6.3, 'kuning', 7.6, 'hijau', 8.2, 'biru', 9.1]
# print(warna)

# kel_warna = [['merah', 6.3], ['kuning', 7.6], ['hijau', 8.2], ['biru', 9.1]]
# print(kel_warna)
# print(type(kel_warna)) # <class 'list'>
# print(type(warna)) # <class 'list'>


# # 4. Subsetting Lists
# keluarga = ['irin', 4.23, 'agus', 4.69, 'sena', 4.36, 'dian', 4.81]
# print(keluarga[3], keluarga[6])
# print(keluarga[-1], keluarga[-2])
# print(keluarga[3:5])
# print(keluarga[1:4])
# print(keluarga[:4])
# print(keluarga[1:])


# # 5. Lists Manipulation
# keluarga = ['irin', 4.23, 'agus', 4.69, 'sena', 4.36, 'dian', 4.81]
# keluarga[5] = 4.42
# print(keluarga)
# keluarga[:2] = ['kharin', 1.0]
# print(keluarga)
# print(keluarga + ['gery', 4.23])
# print(keluarga)
# tam_kel = keluarga + ['gery', 4.23]
# print(keluarga)
# del(keluarga[2])
# print(keluarga)


# # 6. Functions
# angka = [5.32, 5.52, 5.82, 5.91, 5.71]
# print(angka)
# print(max(angka))
# print(round(1.48))
# print(round(1.59))
# print(round(1.48, 1))


# # 7. Methods
# keluarga  = ['irin', 4.23, 'agus', 4.69, 'sena', 4.36, 'dian', 4.81]
# print(keluarga.index("sena"))
# print(keluarga.count(4.36))

# adik = 'dian'
# print(adik.capitalize())
# print(adik.replace('d', 'andr'))

# keluarga.append('abi')
# print(keluarga)
# keluarga.append('4.69')
# print(keluarga)

# print(type(keluarga))



# # 8. Packages
# import numpy as np
# np.array([1, 2, 3])
# print(np.array([1, 2, 3d]))

# from numpy import array
# print(array([1, 2, 3]))
# print(type(array([1, 2, 3])))

# import numpy
# keluarga  = ['irin', 4.23, 'agus', 4.69, 'sena', 4.36, 'dian', 4.81]
# tam_kel = keluarga + ['abi', 4.69]
# print(str(len(tam_kel)) + ' element di dalam list tam_kel')

# np_kel = numpy.array(tam_kel)


# # 9. Definition NumPy
# import numpy as np
# tinggi = [1.73, 1.68, 1.71, 1.89, 1.79]
# lebar = [65.4, 59.2, 63.6, 88.4, 68.7]
# np_tinggi = np.array(tinggi)
# np_lebar = np.array(lebar)
# hasil = np_lebar / np_tinggi ** 2
# print(hasil)

# py_list = [1, 2, 3]
# np_array = np.array([1, 2, 3])
# print(py_list + py_list)
# print(np_array + np_array)
# print(hasil[1])
# print(hasil > 23)
# print(hasil[hasil > 23])


# # 10. 2D NumPy Arrays
# import numpy as np
# np_tinggi = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
# np_lebar = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

# np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 59.2, 63.6, 88.4, 68.7]])
# print(np_2d)
# print(np_2d.shape)
# print(np_2d[0])
# print(np_2d[0][2])
# print(np_2d[0,2])
# print(np_2d[:,1:3])
# print(np_2d[0,:])
# print(np_2d[1,:])
# print(np_2d[:,0])
# print(np_2d[:,1])


# # 11. NumPy: Basic Statistics
# import numpy as np
# np_kota = np.array([[1.64, 71.78], [1.37, 63.35], [1.6, 55.09], [2.04, 74.85], [2.01, 73.57]])
# print(np_kota)
# print(np.mean(np_kota[:,0]))
# print(np.median(np_kota[:,0]))
# print(np.std(np_kota[:,0]))
# print(np.corrcoef(np_kota[:,0], np_kota[:,0]))
