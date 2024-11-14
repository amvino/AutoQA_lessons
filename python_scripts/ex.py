orders = [
   {"order_id": 1, "status": "оплачен", "amount": 250.75, "buyer": "Алексей"},
   {"order_id": 2, "status": "отменен", "amount": 0, "buyer": "Мария"},
   {"order_id": -1, "status": "оплачен", "amount": 100.50, "buyer": "Иван"},
   {"order_id": 3, "status": "в обработке", "amount": 50.25, "buyer": ""},
   {"order_id": 4, "status": "ошибка", "amount": 300.00, "buyer": "Николай"},
   {"order_id": 4, "status": "ошибка", "amount": 300.00, "buyer": "Николай"}

]

uniq_id = set()
invalid_order = []
valid_order = []

for order in orders:
    uniq_id.add(order['order_id'])
    uniq_id_lst = list(uniq_id)

    if order['order_id'] in uniq_id_lst:
        invalid_order.append(order)
    
print(uniq_id)
print(invalid_order)
print(valid_order)