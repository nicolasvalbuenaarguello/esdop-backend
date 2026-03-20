import os
from datetime import datetime
def copia_seguridad_posgret():
    fecha = datetime.today().strftime('%Y_%m_%d_%H_%M')

    respaldo = "Z:/COE/06. ESTADISTICA COE/bakup/posgrest/dirop_posgrest_"+str(fecha)+".sql"

    path_base = "E:\\automatizacion_py\\backup_mysql_posgrest\\bin\\"

    archivo_zip = "Z:/COE/06. ESTADISTICA COE/bakup/dirop_posgrest_"+str(fecha)+".zip"
    cmd_1 = 'SET PGPASSWORD=NICval10**'
    try:
        os.system(cmd_1 + '&&'+ path_base + 'pg_dump -U postgres -h localhost dirop > '+respaldo )
            # os.system(path_base+'pg_dumpall postgresql//postgres:NICval10**@127.0.0.1:5432/dirop >'+respaldo)
        
        print("ok")
        print("<br>")
    except:
        print("no se pudo")
        exit

    from threading import Timer

    def comprimir():
        import zipfile
        archivo_zip_1 = zipfile.ZipFile(archivo_zip, 'w')
        archivo_zip_1.write(respaldo, compress_type=zipfile.ZIP_DEFLATED)

        archivo_zip_1.close()
        print("<h1>archivo comprimido en " + archivo_zip +"</h1>")

        
    t = Timer(60, comprimir)
    t.start()
