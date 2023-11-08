import random
import datetime as dt 

customer_ds = list(range(1,17))
source_type = ["Takeway", "Dine In", "Home Delivery"]
quantity = list(range(1, 101))
per_unit_price = 300.0

def generate_order() -> dict:
    random_customer_id = random.choice(customer_ids)
    random_source_type = random.choice(source_type)
    random_quanity = random.choice(quantity)

    return {
        'customer_id': random_customer_id,
        'source': random_source_type,
        'quantity': random_quanity,
        'total': random_quanity * per_unit_price,
        'created_at': dt.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    }