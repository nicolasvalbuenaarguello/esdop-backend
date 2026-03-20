@echo off

c:
cd C:\Users\nicolas.valbuena\Documents\nueva_mapa\nueva_mapa\documentos\documentos

http-server -p 5000 -a 0.0.0.0  --cors ./
pause