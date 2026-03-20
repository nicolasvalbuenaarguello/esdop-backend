from werkzeug.security import generate_password_hash
print(generate_password_hash("Hernan.rojasr**"))


#from werkzeug.security import generate_password_hash, check_password_hash

#hashed = generate_password_hash("NICval10**")
#print("Hashed:", hashed)

#print("Valid?", check_password_hash(hashed, "NICval10**"))  # Debe dar True
#print("Invalid?", check_password_hash(hashed, "NICval10**"))     # Debe dar False


        # if  filtro[4] == "lugar":
        #     if filtro[6]!="" and filtro[6]!="---" :#filtro por municipio
        #         nueva=filtro[6].split(",")
        #         dato = ""
        #         dato_res=""
        #         if len(nueva) > 1:
        #                 ids = tuple(nueva)
        #                 dato = "and dpto = '{}' and mpio in {}".format(filtro[5], ids)
        #                 dato_res= "and hop_depto = '{}' and hop_mpio in {}".format(filtro[5], ids)

        #         else:
        #             mpio = nueva[0]  
        #             dato = "and {} = '{}' and {} = '{}'".format("dpto",filtro[5], "mpio",mpio)
        #             dato_res = "and {} = '{}' and {} = '{}'".format("hop_depto", filtro[5], "hop_mpio",mpio)
        #         filtros =[dato_res, dato, ""]
        #     else:
        #         if dato == "":
        #             filtros = selecion_filtro(filtro)
        #         else:
        #             filtros = dato
        # else:
        #     if dato == "":
        #         filtros = selecion_filtro(filtro)
        #     else:
        #         filtros = dato


        #!/usr/bin/env python
