# for i in range(1,2,1):
#     text = 10%10
#     print(text)
#     # digits=(str(text))
#     # print(digits)
#     # digit = (list(digits))
#     # print(digit)
#     # print(digit[1])
#
#
# #list=op[1]
# #print(op)
# # print(type(op))
# # print(list)
from hamcrest import assert_that, equal_to
from selenium.common import NoSuchElementException

# num = '16'
# after=num.lstrip('0')
# print(after)

# firstelement = "Greater than 1 day and lesser than equals to 2 days"
# secondelement = "Greater than 1 day & lesser than = to 2"
# S=firstelement.split()
# s1=S[0]
# print(S)
# if secondelement .__contains__(s1):
#     print("yes")
#
# if secondelement in S:
#     print("yes")
# else:
#     print("No")

# expected = 'The file size should not exceed 5MB.'
# actual ='The file size should not exceed 5MB.'
#
# assert_that(expected,equal_to(actual))

# x = "hello"
#
# #if condition returns False, AssertionError is raised:
# assert x == "hello", "hello"

# a=10
# b=0
# #print(a/b)
#
# try:
#     c=a/b
# except NoSuchElementException:
#     print("Zero Division Error")

# a=70
#
# alphabet = chr(a)
# print(alphabet)

import openpyxl
from openpyxl import workbook,load_workbook
book=load_workbook('C:\\Users\\PraveenKumar187\\Documents\\S2P\\Automation\\Content Intelligence\\Pytest\\testData\\Login_Amway_NewUI.xlsx')
sheet=book.active
sheet['C2'].value = 'Hello Python'
book.save('C:\\Users\\PraveenKumar187\\Documents\\S2P\\Automation\\Content Intelligence\\Pytest\\testData\\Login_Amway_NewUI.xlsx')