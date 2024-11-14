orders = [
   {"order_id": 1, "status": "оплачен", "amount": 250.75, "buyer": "Алексей"},
   {"order_id": 2, "status": "отменен", "amount": 0, "buyer": "Мария"},
   {"order_id": -1, "status": "оплачен", "amount": 100.50, "buyer": "Иван"},
   {"order_id": 3, "status": "в обработке", "amount": 50.25, "buyer": ""},
   {"order_id": 4, "status": "ошибка", "amount": 300.00, "buyer": "Николай"},
   
]


def validate_orders(orders):

    valid_order = []
   
    for order in orders:

        if order['order_id'] > 0:
            valid_order.append[order]        
        else:
            print(f'Некорректный ID {order['order_id']}')
            
        if order['status'] in ["оплачен", "отменен", "в обработке"]:
            valid_order.append[order]
        else:
            print(f'Статус заказа {order['order_id']} не соответствует')

        if order['amount'] > 0:
            valid_order.append[order]
        else:
            print(f'Сумма заказа {order['order_id']} 0')

        if order['buyer'] != '':
            valid_order.append[order]
        else:
            print(f'Имя покупателя заказа {order['order_id']} пустое')
    
    return valid_order


validate_orders(orders)













