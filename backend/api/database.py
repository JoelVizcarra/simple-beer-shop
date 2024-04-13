from api.schemas import Order

stock = {
    'last_updated': '2024-09-10 12:00:00',
    'beers': [
        {
            'name': 'Corona',
            'price': 115,
            'quantity': 2
        },
        {
            'name': 'Quilmes',
            'price': 120,
            'quantity': 0
        },
        {
            'name': 'Club Colombia',
            'price': 110,
            'quantity': 3
        }
    ]
}

orders = {
    '2030ba80-eff4-416d-a1bf-9dcef0e40cc3':{
    'created': '2024-09-10 12:00:00',
    'paid': False,
    'subtotal': 0,
    'taxes': 0,
    'discounts': 0,
    'items': [],
    'rounds': [
        {
            'created':  '2024-09-10 12:00:30',
            'items': [
                {
                    'name': 'Corona',
                    'quantity': 2
                },
                {
                    'name': 'Club Colombia',
                    'quantity': 1
                }
            ]
        },
        {
            'created':  '2024-09-10 12:20:31',
            'items': [
                {
                    'name': 'Club Colombia',
                    'quantity': 1
                },
                {
                    'name': 'Quilmes',
                    'quantity': 2
                }
            ]
        },
        {
            'created':  '2024-09-10 12:43:21',
            'items': [
                {
                    'name': 'Quilmes',
                    'quantity': 3
                }
            ]
        }

    ]
}}


def get_order(order_id: str) -> Order:
    if order_id not in orders:
        raise ValueError(f'Order with ID {order_id} not found')
    
    calculate_order_totals(orders[order_id])
    return orders[order_id]


def calculate_order_totals(order: Order):
    # simple cache
    stock_map = {}
    subtotal = 0
    for order_round in order['rounds']:
        for item in order_round['items']:
            # compare last_updated and move to its own util func
            beer = stock_map.get(item['name'])
            if not beer:
                beer, last_updated = get_beer(item['name'])
                stock_map[item['name']] = {**beer, 'last_updated': last_updated}
                price = beer['price']
            subtotal += item['quantity'] * price

    order['subtotal'] = subtotal
    order['taxes'] = 0
    order['discounts'] = 0

    order['total'] = order['subtotal'] + order['taxes'] - order['discounts']

def get_beer(beer_name: str) -> float:
    for beer in stock['beers']:
        if beer['name'].lower() == beer_name.lower():
            return beer, stock['last_updated']

    raise ValueError(f"Cerveza '{beer_name}' no encontrada en el inventario")
