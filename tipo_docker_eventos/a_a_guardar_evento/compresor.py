from os import getcwd
import os
import shutil
from dotenv import load_dotenv
load_dotenv()
import zipfile


raiz= "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker_eventos/a_a_guardar_evento/documentos"


def zip_dir(directory, zipname):
    """
    Compress a directory (ZIP file).
    """
    if os.path.exists(directory):
        outZipFile = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)

        # The root directory within the ZIP file.
        rootdir = os.path.basename(directory)

        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:

                # Write the file named filename to the archive,
                # giving it the archive name 'arcname'.
                filepath   = os.path.join(dirpath, filename)
                parentpath = os.path.relpath(filepath, directory)
                arcname    = os.path.join(rootdir, parentpath)

                outZipFile.write(filepath, arcname)

    outZipFile.close()




if __name__ == '__main__':
    zip_dir(raiz, "documentos_com/ZIPFILE_NAME.zip")