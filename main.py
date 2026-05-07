from clientes import Cliente

# Prueba con cliente válido
print("Creando cliente válido...")
cliente1 = Cliente("Rocio", "rocio@test.com", "3101234567")
print(cliente1.mostrar_info())

# Prueba con nombre vacío
print("\nCreando cliente inválido...")
cliente2 = Cliente("", "correo@test.com", "3101234567")

# Prueba con correo vacío
print("\nCreando cliente con correo inválido...")
cliente3 = Cliente("Laura", "", "3101234567")

print("\nCreando cliente con telefono invalido...")
cliente4 = Cliente("Carlos", "carlos@test.com", "123")

print("\nCreando cliente con espacios...")
cliente5 = Cliente("    Andrea    ", "andrea@test.com", "3209876543")
print(cliente5.mostrar_info())


