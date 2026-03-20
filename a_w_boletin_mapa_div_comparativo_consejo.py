from multiprocessing import Process
import os
import subprocess
import time
import signal

def lanzar_uvicorn(puerto, env):
    subprocess.run([
        "uvicorn", "a_w_boletin_mapa_div_comparativo_consejos_replicas:app",
        "--host", "0.0.0.0",
        "--port", str(puerto),
        "--log-level", "error"
    ], env=env)

def start_replicas(num_replicas=20, puerto_base=8010):
    procesos = []
    for i in range(num_replicas):
        puerto = puerto_base + i
        env = os.environ.copy()
        env["PUERTO"] = str(puerto)
        p = Process(target=lanzar_uvicorn, args=(puerto, env))
        p.start()
        print(f"✅ Réplica {i+1} corriendo en puerto {puerto}")
        procesos.append(p)
        time.sleep(0.3)
    return procesos

if __name__ == "__main__":
    try:
        replicas = start_replicas()
        input("\n⏸ Presiona Enter para detener las réplicas...\n")
    finally:
        print("\n⛔ Terminando réplicas...")
        for p in replicas:
            p.terminate()
            p.join()
        print("✅ Todas las réplicas han sido cerradas.")
