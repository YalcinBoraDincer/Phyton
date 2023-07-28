# Concession stand program

menu={"pizza":120.00,
      "nachos":45.50,
      "fries":15.55,
      "cikolata":5.65,
      "kola":3.99,
      "su":0.55}

cart=[]
total=0

print("=========== Menu =============")
print()
for key,value in menu.items():
    print(f"{key:10}: $ {value:.2f}")
print()
print("=============================")
print()
while True:
    secim=input("Istediginiz urunleri seciniz (Cikmak icin q) : ").lower()


    if secim == "q":
        break    
    elif menu.get(secim) is not None:
        cart.append(secim)

for food in cart:
    total+=menu.get(food)        


print(f"Your cart is {cart}")
print(f"Total $ {total} ")     