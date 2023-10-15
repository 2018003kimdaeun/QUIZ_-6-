class Bungeoppang:
    def __init__(self, contents, price, stock):
        self.contents = contents
        self.price = price
        self.stock = stock
        self.sold = 0

    def sell(self, quantity):
        revenue = self.price * quantity
        self.stock -= quantity
        self.sold += revenue
        print(f"{self.contents}붕어빵 {quantity}개를 판매하였습니다. 수익: {revenue}")

    def eat(self, quantity):
        self.stock -= quantity
        print(f"{self.contents}붕어빵 {quantity}개를 먹었습니다.")

슈크림 = Bungeoppang("슈크림", 1500, 10)
팥 = Bungeoppang("팥", 1200, 15)

print("1.슈크림 붕어빵")
print("2.팥 붕어빵")

choice = input("원하는 작업을 선택하세요: ")

if choice == "1":
    quantity = int(input("몇 개를 판매하시겠습니까? "))
    quantity = int(input("몇 개를 먹겠습니까? "))
    슈크림.sell(quantity)
    슈크림.eat(quantity)

elif choice == "2":
    quantity = int(input("몇 개를 판매하시겠습니까? "))
    quantity = int(input("몇 개를 먹겠습니까? "))
    팥.sell(quantity)
    팥.eat(quantity)

print(f"총 슈크림 붕어빵 수익: {슈크림.sold}원")
print(f"총 팥 붕어빵 수익: {팥.sold}원")
