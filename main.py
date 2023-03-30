
# Zadanie nr1

shopping_list = {"piekarnia": ["chleb", "bułki", "pączek"],
                 "warzywniak": ["marchew", "seler", "rukola"]}
for shop, product in shopping_list.items():
    print(f"Idę do {shop.title()} i kupuję tam: {str(product).title()}")

products = 0
for values in shopping_list.values():
    products += len(values)
print(f"W sumie kupuję {products} produktów.")


# Zadanie nr2

numbers = [a for a in range(0, 101) if a % 5 == 0 if a != 0]
print(f"Liczby podzielne przez 5:{numbers}")
numbers2 = [a**3 for a in numbers]
print(f"Liczby podzielne przez 5, podniesione do potęgi 3: {numbers2}")
