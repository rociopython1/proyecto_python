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

print("\n===== PRUEBAS ADICIONALES =====")

# Cliente válido
cliente6 = Cliente("Miguel", "miguel@test.com", "3004567890")
print(cliente6.mostrar_info())

# Nombre inválido
cliente7 = Cliente("", "ana@test.com", "3101234567")

# Correo inválido
cliente8 = Cliente("Carlos", "carlosemail.com", "3101234567")

# Teléfono con letras
cliente9 = Cliente("Laura", "laura@test.com", "310ABC4567")

# Nombre con espacios
cliente10 = Cliente("   Andrea   ", "andrea@test.com", "3209876543")
print(cliente10.mostrar_info())
