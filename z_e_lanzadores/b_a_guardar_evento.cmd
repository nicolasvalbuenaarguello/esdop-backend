@echo off

c:
cd C:\Users\nicolas.valbuena\Documents\programacion 2023\server\env\Scripts\
call activate.bat
cd ../..
cd tipo_docker_eventos/b_a_copiar_arch_evento


python b_a_guardar_evento.py
pause 