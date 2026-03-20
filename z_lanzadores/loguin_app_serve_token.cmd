@echo off

c:
cd C:\Users\nicolas.valbuena\Documents\programacion 2023\server\env\Scripts\
call activate.bat
cd ../..
cd loguin_app_serve_token
python loguin_app_serve_token.py
pause

loguin_app_serve_token