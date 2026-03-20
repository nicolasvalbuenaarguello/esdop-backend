@echo off

c:
cd C:\Users\nicolas.valbuena\Documents\programacion 2023\server\env\Scripts\
call activate.bat
cd ../..
cd serve_archivos

python servidor_archivos.py
pause 