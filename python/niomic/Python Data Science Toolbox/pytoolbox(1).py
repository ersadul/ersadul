# # 1. User-defined Functions
# def kotak():
#     nilai_baru = 4 ** 2
#     print(nilai_baru)

# def kotak(nilai):
#     """Fungsi kuadrat"""
#     nilai_baru = nilai ** 2
#     print(nilai_baru)

# kotak(3)


# # Multiple Parameter and Return Values ( 2 )
# def kotak (nilai1, nilai2):
#     hasil = nilai1 ** nilai2
#     return hasil

# print(kotak(2, 1))
# print(kotak(2, 7))

# nomor = (2, 4, 6)
# print(type(nomor))
# print(nomor[1])


# # Scope and User-defined Functions ( 3 )
# def kotak(nilai):
#     """Fungsi kuadrat"""
#     nilai_baru = nilai ** 2
#     return nilai_baru

# print(kotak(2))
# print(nilai_baru) # error because nilai_baru is a variable scope

# test 
# nilai_baru = 10
# def kotak(nilai):
#     """Fungsi kuadrat"""
#     nilai_baru = nilai ** 2
#     return nilai_baru

# print(kotak(2))
# print(nilai_baru)

# test global scope variable
# nilai_baru = 100
# def kotak():
#     """Fungsi kuadrat"""
#     nilai_baru2 = nilai_baru ** 2
#     return nilai_baru2

# print(kotak())
# print(nilai_baru)


# # Nested Functions ( 4 )
# def mod2plus5(x1, x2, x3):
#     new_x1 = x1 % 2 + 5
#     new_x2 = x2 % 2 + 5
#     new_x3 = x3 % 2 + 5

#     return (new_x1, new_x2, new_x3)

# def mod2plus5(x1, x2, x3):
#     def inner(x):
#         return x % 2 + 5
#     return (inner(x1), inner(x2), inner(x3))

# print(mod2plus5(1, 2, 3))


# # Default and Flexible Arguments ( 5 )
# def power(nomor, pow = 1):
#     nilai_baru = nomor ** pow
#     return nilai_baru

# print(power(9))
# print(power(9, 2))

# def add_all(*args):
#     sum_all = 0

#     for num in args:
#         sum_all += num
    
#     return sum_all

# print(add_all(5, 10, 15, 20))


# # Lambda Functions ( 6 )
# nilai = lambda x, y: x ** y
# print(nilai(2, 2))

# nomor = [48, 6, 9, 21, 1]
# kotak = map(lambda nom : nom ** 2, nomor)
# print(list(kotak))


# # Introduction to Error-Handling ( 7 )
# def asd(x):
#     try:
#         return x ** 0.5
#     except:
#         print('x harus INT atau FLOAT')

# print(asd("2"))