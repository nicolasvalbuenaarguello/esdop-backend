
import sys
from anyio import Path
from fastapi import HTTPException
from models.conexion_mysql import *


# from models.conexion import conexion_bd
from models.models import seleciones, close
from models.modelsUser import ModelUser
from models.entities.user import User
import os
from dotenv import load_dotenv

from models.conexion_pos import Databa_bases_posgrest
load_dotenv()
from datetime import timedelta, datetime
from jose import JWTError, jwt


import ephem
from datetime import datetime

db = Databa_bases.conexion_directa()


TOKEN = os.getenv('TOKEN')
def create_token(data:dict, time_expire: datetime):

    SECRETE_KEY = os.getenv('SECRETE')
    ALGORITHM = os.getenv('ALGORITHM')

    data_copy = data.copy() 

    if time_expire is None:
            expires = datetime.utcnow() + timedelta(minutes=120)

    else:
            expires = datetime.utcnow() +time_expire

    data_copy.update({"exp": expires})
    token_jwt = jwt.encode(data_copy, key=SECRETE_KEY, algorithm = ALGORITHM)
    return token_jwt

class Ingreso():




    # Solicitar la fecha al usuario

    # Obtener y mostrar la fase lunar


    def logui(nombre, password):
        user = User(user_name = nombre, password =password)

        logged_user = ModelUser.loguin(user)
        conexion_pos = Databa_bases_posgrest()
        date = datetime.now()
        #print(logged_user)
        moon = ephem.Moon(date)
        phase = moon.phase
        luna=  str(round(phase))

        if logged_user != None:
            if logged_user.disabled:
                access_token_expire =  timedelta(minutes=120)
                
                query =  "SELECT * FROM usuarios_sejec where id  = {}".format(logged_user.id)
                datos = conexion_pos.comando_query(query)
                for dato in datos:
                    roll =  dato[5]
                    access_token_jwt = create_token({"sub": logged_user.user_name, "code":roll}, access_token_expire)
                
                if roll != "ROOT":
                    query_c =  "SELECT * FROM permisos where roll <> 'ROOT' "
                else:
                    query_c =  "SELECT * FROM permisos"

                if  roll == "ROOT"  or  roll != "AMD":
                    query_f =  """SELECT DISTINCT 
                                                    usuarios_sejec.id, 
                                                    usuarios_sejec.full_nombre, 
                                                    usuarios_sejec.usuario,
                                                    usuarios_sejec.foto,
                                                    usuarios_sejec.roll,
                                                    usuarios_sejec.correo,
                                                    usuarios_sejec.per_select,
                                                    usuarios_sejec.per_insert,
                                                    usuarios_sejec.per_update,
                                                    usuarios_sejec.per_delete,
                                                    usuarios_sejec.crear_orden,
                                                    usuarios_sejec.asignar_orden,
                                                    usuarios_sejec.cerrar_orden,
                                                    usuarios_sejec.modificar_estado,
                                                    usuarios_sejec.crear_user,
                                                    usuarios_sejec.listado_user,
                                                    usuarios_sejec.editar_user,
                                                    cargos_plataforma.cargo_sejec,
                                                    firmas_documentos.estado_firma,
                                                    firmas_documentos.firma_numero, 
                                                    firmas_documentos.di_nombre,
                                                    unidades_internas.ABREV_JEFATURA,
                                                    unidades_internas.DESCRIPCION_JEFATURA,
                                                    firmas_documentos.firma
                    FROM usuarios_sejec INNER  JOIN unidades_internas ON unidades_internas.ID_COMAND = usuarios_sejec.ID_COMAND INNER  JOIN  firmas_documentos on firmas_documentos.di_nombre = usuarios_sejec.id  INNER  JOIN  cargos_plataforma on cargos_plataforma.id_cargos_plataforma = firmas_documentos.id_cargo;"""
                    query_f = conexion_pos.comando_query( query_f)
                else:
                     query_f = ""

                query_c = conexion_pos.comando_query( query_c)

                query_a =  "SELECT * FROM unidades_externas  "
                query_a = conexion_pos.comando_query( query_a)

                query_b =  "SELECT * from unidades_internas"
                query_b = conexion_pos.comando_query( query_b)

                query_d =  "SELECT * from origen"
                query_d = conexion_pos.comando_query( query_d)

                query_e =  "SELECT * from cargos_plataforma "
                query_e = conexion_pos.comando_query( query_e)

                                
                query_g =  "SELECT id_entidad, razon_social , razon_social from directorio_ecp"
                query_g = conexion_pos.comando_query( query_g)

                conexion_pos.close()
                for dato in datos:
                    msm = {
                        "access_token": access_token_jwt,
                        "token_type":"bearer",
                        'full_nombre' : dato[1],
                        'usuario' : dato[2],
                        'foto' : dato[4],
                        'roll' : dato[5],
                        'correo' : dato[6],
                        'unidad_user' : dato[7],
                        'per_select' : dato[8],
                        'per_insert' : dato[9],
                        'per_update' : dato[10],
                        'per_delete' : dato[11],
                        'crear_orden' : dato[12],
                        'asignar_orden' : dato[13],
                        'cerrar_orden' : dato[14],
                        'modificar_estado' : dato[15],
                        'crear_user' : dato[16],
                        'listado_user' : dato[17],
                        'editar_user' : dato[18],

                        "porcentaje_luna" : "Luminosidad: "+luna+" %",
                        
                        "unidades_externas":query_a,
                        "unidades_internas":query_b,
                        "permisos":query_c,
                        "origen":query_d,
                        "cargos_sejec": query_e,
                        "usuarios_sejec":query_f,
                        "directorio_ecp":query_g
 
                    }
                conexion_pos.close()
                return msm
            else:
                raise HTTPException(status_code=402, detail="Contraseña Incorreta",headers={"WWW-Authenticate":"Bearer"})

        else:
            raise HTTPException(status_code=402, detail="Usuario Incorreto",headers={"WWW-Authenticate":"Bearer"})
