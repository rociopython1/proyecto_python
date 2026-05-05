# Importar la clase Cliente para realizar pruebas
from clientes import Cliente

# Prueba con cliente válido
print("Creando cliente válido...")
cliente1 = Cliente("Rocio", "rocio@test.com")

# Prueba con nombre vacío
print("\nCreando cliente inválido...")
cliente2 = Cliente("", "correo@test.com")

# Prueba con correo vacío
print("\nCreando cliente con correo vacío...")
cliente3 = Cliente("Laura", "")

