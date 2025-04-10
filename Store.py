class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}
    
    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в {self.name} по цене {price}")
    
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из {self.name}")
        else:
            print(f"Товар '{item_name}' не найден в {self.name}")
    
    def get_price(self, item_name):
        return self.items.get(item_name, None)
    
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price} в {self.name}")
        else:
            print(f"Товар '{item_name}' не найден в {self.name}")

# Создаем несколько магазинов
store1 = Store("Продуктовый рай", "ул. Центральная, 5")
store2 = Store("ТехноМир", "пр. Космонавтов, 12")
store3 = Store("Дом книги", "ул. Пушкина, 42")

# Добавляем товары в магазины
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store1.add_item("молоко", 1.2)

store2.add_item("ноутбук", 999.99)
store2.add_item("смартфон", 499.99)
store2.add_item("наушники", 79.99)

store3.add_item("Война и мир", 25.5)
store3.add_item("1984", 18.75)
store3.add_item("Гарри Поттер", 30.0)

# Тестируем методы на одном из магазинов (store1)
print("\nТестирование методов для магазина:", store1.name)
# Получаем цену товара
print("Цена яблок:", store1.get_price("яблоки"))
print("Цена несуществующего товара:", store1.get_price("апельсины"))

# Обновляем цену
store1.update_price("яблоки", 0.55)
store1.update_price("апельсины", 0.7)  # Товара нет

# Удаляем товар
store1.remove_item("бананы")
store1.remove_item("апельсины")  # Товара нет

# Добавляем новый товар
store1.add_item("хлеб", 1.0)

# Проверяем текущий ассортимент
print("\nТекущий ассортимент в", store1.name)
for item, price in store1.items.items():
    print(f"{item}: {price}")