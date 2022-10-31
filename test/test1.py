# # def get_loss(w1, w2, w3, w4):
# #     try:a
# #         rel = w1//w2
# #     except ArithmeticError:
# #         print("Divide by zero")
# #     else:
# #         return 10*rel - 5*w2*w3 + w4
# #
# #
# # class LimitException(Exception):
# #     """Перевищення ліміту"""
# #
# #
# # error = LimitException('перевищення ліміту навантаження')
# # raise error
#
# a, b = input().split()
# try:
#     s = int(a) + int(b)
# except:
#     s = a + b
# finally:
#     print(s)
#
try:
    print(sqrt(2))
except:
    print("Cannot calculate sqrt")
finally:
    import math as m
    print(sqrt(2))