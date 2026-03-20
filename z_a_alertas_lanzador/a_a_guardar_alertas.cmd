@echo off

c:
cd C:\Users\nicolas.valbuena\Documents\programacion 2023\server\env\Scripts\
call activate.bat
cd ../..
cd tipo_docker_alertas/a_a_guardar_evento


python a_a_guardar_alerta.py
pause 