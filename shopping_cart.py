

# shopping cart 클래스 생성
class ShoppingCart:
# 상품 목록 저장 기능
    def __init__(self):
        self.bucket = []

#매서드
# - 장바구니 담기
    def add_item(self, item):
        self.bucket.append(item)
# - 장바구니 빼기
    def remove_item(self,item):
        self.bucket.remove(item)
# - 상품 목록 조회
    def show_items(self):
        return self.bucket

# 상품클래스
# 속성
# - 제품명
# - 가격

class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 쇼핑카트생성
cart =ShoppingCart()
    
# 상품3개 생성
item_a = item("apple", 1000)
item_b = item("kiwi", 2000)
item_c = item("banana", 3000)
        
# 상품 1개 장바구니 담기
cart.add_item(item_a)
# 상품 1개 장바구니 담기
cart.add_item(item_b)
# 상품 1개 장바구니 담기
cart.add_item(item_c)
# 상품 1개 장바구니에서 빼기
cart.remove_item(item_b)
# 장바구니에 담긴 상품 목록 조회
for item in cart.show_items():
    print(item.name, item.price)






        