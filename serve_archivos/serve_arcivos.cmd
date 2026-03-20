@echo off

c:
cd C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/

http-server -p 5198 -a 0.0.0.0  --cors ./

pause

@REM c:
@REM cd C:\Users\nicolas.valbuena\Documents\nueva_mapa\nueva_mapa\documentos\documentos

@REM http-server -p 5000 -a 0.0.0.0  --cors ./
@REM pause
@echo off
title Servidor HTTP - JEMOP
color 0A
cls
echo ---------------------------------------
echo     INICIANDO SERVIDORES HTTP - JEMOP
echo ---------------------------------------

REM Iniciar servidor en carpeta documentos_serve_jemop (puerto 5198)
start "Servidor 5198" cmd /k "cd /d C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop && http-server -p 5198 -a 0.0.0.0 --cors ./"

REM Iniciar servidor en carpeta nueva_mapa\documentos (puerto 5000)
start "Servidor 5000" cmd /k "cd /d C:\Users\nicolas.valbuena\Documents\nueva_mapa\nueva_mapa\documentos\documentos && http-server -p 5000 -a 0.0.0.0 --cors ./"

echo Servidores lanzados en puertos 5198 y 5000.
echo Puedes cerrar esta ventana o dejarla abierta como referencia.
pause
