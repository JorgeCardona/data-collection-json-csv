import json
from faker import Faker
from datetime import date, datetime  # Importa las clases date y datetime
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
    
def save_collections_to_json(generated_data):
    for collection_name, data in generated_data.items():
        with open(f"{collection_name}.json", "w") as file:
            for record in data:
                file.write(json.dumps(record) + "\n")  # Guarda cada registro en una sola línea

def generate_collections_data(total_samples, collections_info):
    dict_list = {
        collection_name: [
            {**{f'Id_reference_{collection_name}': sample_number}, 
              **{field_name: get_dummy_value(field_type) for field in fields for field_name, field_type in field.items()}}
            for sample_number in range(total_samples)
        ]
        for collection_name, fields in collections_info.items()
    }
    return dict_list

# Parámetros de entrada para las colecciones Customers, Orders y Payments
total_samples = 100
collections_info = {
    "Customers": [
        {"customer_id": "random_int"},        # ID del cliente
        {"name": "name"},                     # Nombre del cliente
        {"email": "email"},                   # Correo electrónico
        {"phone": "phone_number"},            # Número de teléfono
        {"address": "address"},               # Dirección
        {"age": "random_int_20_to_85"},      # Edad (entre 20 y 85)
        {"nationality": "country"},           # Nacionalidad
        {"current_continent": "continent"},  # continente donde vive en este momento
        {"salary": "random_int_1000_to_10000"}, # Salario
    ],
    "Orders": [
        {"order_id": "random_int"},           # ID de la orden
        {"customer_id": "random_int"},        # ID del cliente (referencia)
        {"order_date": "date_this_year"},    # Fecha de la orden
        {"last_purchase_date": "date"},       # Última fecha de compra
        {"discount": f"{get_dummy_value('random_float_0.5_50')} %"}, # Descuento aplicado (tipo float)
        {"total_amount": "random_int"},       # Monto total
        {"status": "order_status"},            # Estado de la orden (e.g., "shipped", "pending")
    ],
    "Payments": [
        {"payment_id": "random_int"},         # ID del pago
        {"order_id": "random_int"},           # ID de la orden (referencia)
        {"payment_date": "date_this_month"},  # Fecha del pago
        {"amount": "random_int"},             # Monto del pago
        {"payment_method": "payment_method"}, # Método de pago (e.g., "credit_card", "paypal")
        {"currency": "currency"}               # Tipo de moneda
    ],
}

# Generar y guardar los datos
generated_data = generate_collections_data(total_samples, collections_info)
save_collections_to_json(generated_data)

print("Datos guardados en archivos JSON separados.")