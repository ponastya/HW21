from courier import Courier
from exceptions import BaseError
from request import Request
from shop import Shop
from store import Store

shop = Shop(
    items={
        'клюква': 3,
        'арбуз': 5
    }
)

store = Store(
    items={
        'клюква': 13,
        'арбуз': 51
    }
)

storages = {
    'магазин': shop,
    'склад': store
}

while True:
    for storage_name in storages:
        print(f'В {storage_name} хранится: {storages[storage_name].get_items()}')

    user_input = input(
        'Введите строку в формате "Доставить 3 клюква из склад в магазин"\n'
        'Введите стоп или stop, чтобы продолжить... '
    )
    if user_input in ('стоп', 'stop'):
        break
    try:
        request = Request(request=user_input, storages=storages)
        courier = Courier(request=request, storages=storages)
        courier.move()
    except BaseError as error:
        print(error.message)

