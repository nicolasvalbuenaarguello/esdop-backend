import os
from datetime import datetime
def copia_seguridad_mysql():
    fecha = datetime.today().strftime('%Y_%m_%d_%H_%M')

    respaldo = "C:/Users/nicolas.valbuena/Documents/New folder/mysql/dirop_"+str(fecha)+".sql"

    path_base = "C:\\Program Files\\MariaDB 10.10\\bin\\mysqldump.exe"

    archivo_zip = "C:/Users/nicolas.valbuena/Documents/New folder/mysql/dirop_"+str(fecha)+".zip"
    try:
        # os.popen(path_base+" -u 'root' dirop > "+respaldo)
        respaldo = "{} -h 'localhost' -u 'root' -p dirop > {}".format(path_base, respaldo)
        os.popen(respaldo)
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
