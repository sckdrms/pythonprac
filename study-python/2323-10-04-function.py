# def abc():
#   print('a')
#   print('b')
#   print('c')
# abc()
# print(1)

# abc()
# print(2)

# abc()
# print(3)
def cost():
  price = float(input('price: '))
  vat_rate = 0.1
  print(price*vat_rate)
# cost()

def cost1(price):
  vat_rate = 0.1
  print(price*vat_rate)
# cost1(100000)

def cost2(price, vat_rate):
  print(price*vat_rate)
# cost2(100000,0.2)

def cost3():
  print()

def cost4(price, vat_rate = 0.1):
  return price*vat_rate
print(cost4(100000))
# send_price(123-123-123-123, cost4(200000, 0.5))

