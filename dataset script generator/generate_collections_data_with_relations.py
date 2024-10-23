import json
from faker import Faker
from datetime import date, datetime
import random

fake = Faker()

def get_dummy_value(field_type):
    if field_type == "payment_method":
        return generate_payment_method()
    if field_type == "order_status":
        return generate_order_status()
    if field_type == "continent":
        return generate_continent()
    if field_type == "random_int_20_to_85":
        return fake.random_int(min=20, max=85)  # Genera un entero aleatorio entre 20 y 85
    if field_type == "random_int_1000_to_10000":
        return fake.random_int(min=1000, max=10000)  # Genera un entero aleatorio entre 1000 y 10000                
    if field_type == "random_float_0.5_50":
        return round(fake.random.uniform(0.5, 50), 2)  # Genera un float entre 0.5 y 50
    
    fake_method = getattr(fake, field_type, None)
    
    if callable(fake_method):
        value = fake_method()
        if isinstance(value, (date, datetime)):
            return value.isoformat()  # Convierte a formato ISO
        return value
    else:
        return f"Field type '{field_type}' not found."

def generate_order_status():
    order_statuses = ["shipped", "pending", "delivered", "cancelled", "returned"]
    return fake.random_element(elements=order_statuses)

def generate_payment_method():
    payment_methods = ["Credit Card", "Debit Card", "PayPal", "Bank Transfer", "Cash"]
    return fake.random_element(elements=payment_methods)

def generate_continent():
    continents = ["Africa", "America", "Asia", "Europe", "Oceania"]
    return fake.random_element(elements=continents)


def save_collections_to_json(generated_data):
    for collection_name, data in generated_data.items():
        with open(f"{collection_name}.json", "w") as file:
            for record in data:
                file.write(json.dumps(record) + "\n")  # Guarda cada registro en una sola línea

def generate_customers(total_samples):
    return [
        {
            "customer_id": i,  # ID del cliente
            "name": get_dummy_value("name"),
            "email": get_dummy_value("email"),
            "phone": get_dummy_value("phone_number"),
            "address": get_dummy_value("address"),
            "age": get_dummy_value("random_int_20_to_85"),
            "nationality": get_dummy_value("country"),
            "current_continent": get_dummy_value("continent"),
            "salary": get_dummy_value("random_int_1000_to_10000")            
        }
        for i in range(total_samples)
    ]

def generate_orders(total_samples, customer_ids):
    selected_customers = random.sample(customer_ids, k=int(total_samples * 0.75))
    return [
        {
            "order_id": i,  # ID de la orden
            "customer_id": fake.random_element(elements=selected_customers),  # Usar un customer_id aleatorio
            "order_date": get_dummy_value("date_this_year"),
            "last_purchase_date": get_dummy_value("date"),
            "discount": f"{get_dummy_value('random_float_0.5_50')} %",
            "total_amount": get_dummy_value("random_int"),
            "status": generate_order_status()
        }
        for i in range(total_samples)
    ]

def generate_payments(total_samples, order_ids):
    selected_orders = random.sample(order_ids, k=int(total_samples * 0.85))
    return [
        {
            "payment_id": i,  # ID del pago
            "order_id": fake.random_element(elements=selected_orders),  # Usar un order_id aleatorio
            "payment_date": get_dummy_value("date_this_month"),
            "amount": get_dummy_value("random_int"),
            "payment_method": generate_payment_method(),
            "currency": get_dummy_value("currency"),
        }
        for i in range(total_samples)
    ]

def generate_collections_data(total_samples):
    customers = generate_customers(total_samples)
    customer_ids = [customer['customer_id'] for customer in customers]  # Obtener los customer_ids

    orders = generate_orders(total_samples, customer_ids)
    order_ids = [order['order_id'] for order in orders]  # Obtener los order_ids

    payments = generate_payments(total_samples, order_ids)

    return {
        "Customers": customers,
        "Orders": orders,
        "Payments": payments
    }

# Parámetros de entrada para las colecciones Customers, Orders y Payments
total_samples = 200

# Generar y guardar los datos
generated_data = generate_collections_data(total_samples)
save_collections_to_json(generated_data)

print("Datos guardados en archivos JSON separados.")