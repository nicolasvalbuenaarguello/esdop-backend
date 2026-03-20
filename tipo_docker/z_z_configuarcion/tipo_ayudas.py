def tipo_ayudas_template(prs):
    for i, master in enumerate(prs.slide_masters):
        print(f"🧩 Patrón {i}:")

        for j, layout in enumerate(master.slide_layouts):
            nombre = layout.name if layout.name else "Sin nombre"
            print(f"   ├─ Diseño {j}: {nombre}")

        print("-" * 40)