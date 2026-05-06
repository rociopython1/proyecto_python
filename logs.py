from datetime import datetime

def registrar_log(nivel, mensaje, modulo):
    """
    Registro avanzado de eventos para Software FJ.
    Niveles: 'INFO', 'WARNING', 'ERROR'
    """
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{ahora}] [{nivel}] [Modulo: {modulo}] - {mensaje}\n"
    
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea)
        
