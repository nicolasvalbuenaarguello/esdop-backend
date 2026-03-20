@echo off

c:
cd C:\Users\nicolas.valbuena\Documents\programacion 2023\server\env\Scripts\
call activate.bat
cd ../..
cd tipo_docker_personal/usuarios

python personal.py
pause 