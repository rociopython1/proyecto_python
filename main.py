from clientes import Cliente

# Prueba con cliente válido
print("Creando cliente válido...")
cliente1 = Cliente("Rocio", "rocio@test.com")
print(cliente1.mostrar_info())

# Prueba con nombre vacío
print("\nCreando cliente inválido...")
cliente2 = Cliente("", "correo@test.com")

# Prueba con correo vacío
print("\nCreando cliente con correo inválido...")
cliente3 = Cliente("Laura", "")


