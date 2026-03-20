import os
import subprocess
from datetime import datetime

# 🔹 CONFIGURACIÓN
DB_NAME = "dirop"
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_PASSWORD = "NICval10**"  # ⚠️ opcional
BACKUP_DIR = r"C:\Users\nicolas.valbuena\Documents\bakoup_dirop"

# 🔹 Crear carpeta si no existe
os.makedirs(BACKUP_DIR, exist_ok=True)

# 🔹 Nombre del archivo con fecha
fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = os.path.join(BACKUP_DIR, f"{DB_NAME}_{fecha}.backup")

# 🔹 Ruta de pg_dump (ajusta si es necesario)
PG_DUMP_PATH = r"C:\Program Files\PostgreSQL\15\bin\pg_dump.exe"

# 🔹 Variables de entorno (para evitar pedir password)
env = os.environ.copy()
env["PGPASSWORD"] = DB_PASSWORD

# 🔹 Comando
cmd = [
    PG_DUMP_PATH,
    "-h", DB_HOST,
    "-p", DB_PORT,
    "-U", DB_USER,
    "-F", "c",     # formato custom
    "-Z", "6",     # compresión
    "-f", backup_file,
    DB_NAME
]

print("🚀 Iniciando backup...")

try:
    subprocess.run(cmd, env=env, check=True)
    print(f"✅ Backup creado exitosamente:\n{backup_file}")

except subprocess.CalledProcessError as e:
    print("❌ Error al generar backup")
    print(e)