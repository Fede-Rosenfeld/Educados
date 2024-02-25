'''### info:
    ACCESO A LOS DATOS
'''
from _mysql_db import *


def crearUsuario(di):
    '''### Información:
        Agrega un nuevo usuario (un registro) en la tabla usuario de la DB
        Recibe 'di' un diccionario con los datos del usuario a agegar en la tabla.
        Retorna True si realiza con existo el insert, False caso contrario.
    '''
    sQuery=""" 
        INSERT INTO usuario
        (id, nombre, apellido, nomusuario, email, contrasena)
        VALUES
        (%s,%s, %s, %s, %s, %s);
    """
    val=(None,di.get('nombre'), di.get('apellido'),  di.get('nomusuario'),di.get('email'), di.get('password2'))
    resul_insert=insertDB(BASE,sQuery,val)
    return resul_insert==1

def obtenerInfo(param):
    sSql = """SELECT COUNT(*) AS cantidad_usuario
            FROM usuario
        """
    cant_usuarios = selectDB(BASE, sSql, title=False)
    param["cant_usuarios"] = cant_usuarios[0][0]

    sSql = """SELECT COUNT(*) AS cantidad_archivos_verificados
                FROM archivo WHERE revisado="Revisado"
            """
    cant_revisados = selectDB(BASE, sSql, title=False)
    param["cant_revisados"] = cant_revisados[0][0]

    sSql = """SELECT COUNT(*) AS cantidad_archivos_resumen
                FROM archivo WHERE id_tipo=5
            """
    cant_resumenes = selectDB(BASE, sSql, title=False)
    param["cant_resumenes"] = cant_resumenes[0][0]

    sSql = """SELECT COUNT(DISTINCT id_usuario) AS cantidad_contribuidores
                FROM archivo
            """
    cant_contribuidores = selectDB(BASE, sSql, title=False)
    param["cant_contribuidores"] = cant_contribuidores[0][0]






#######################################################
#################### ADMIN ############################
#######################################################
def crearMateria(di, materia):
    sQuery = """ 
        INSERT INTO materias
        (id, nombre)
        VALUES
        (%s, %s);
    """
    val = (None, materia)
    try:
        resul_insert = insertDB(BASE, sQuery, val)  # Asegúrate de que BASE esté definido
        return resul_insert == 1
    except :
        pass
    return False

def vermaterias(param):
    sSql = """SELECT * FROM materias"""
    val = None
    fila = selectDB(BASE, sSql, val)
    param["lista_materias"] = fila
    sSql = """SELECT COUNT(*) AS total_materias FROM materias;
            """
    val = None
    fila = selectDB(BASE, sSql, val)
    param["cantidad_materias"] = fila

def eliminarMateria(materia_id):
    try:
        sSql = "DELETE FROM materias WHERE id=%s;"
        val = (materia_id,)  # Asegurar que val sea una tupla
        result_delete = deleteDB(BASE, sSql, val)
        return result_delete == 1
    except Exception as e:
        # Manejar errores y registrar o devolver información útil
        print(f"Error al borrar en la base de datos: {e}")
        return False

def eliminarTipos(tipo_id):
    try:
        sSql = "DELETE FROM tipos WHERE id=%s;"
        val = (tipo_id,)  # Asegurar que val sea una tupla
        result_delete = deleteDB(BASE, sSql, val)
        return result_delete == 1
    except Exception as e:
        # Manejar errores y registrar o devolver información útil
        print(f"Error al borrar en la base de datos: {e}")
        return False

def crearTipo(tipo):
    sQuery = """ 
        INSERT INTO tipos
        (id, nombre)
        VALUES
        (%s, %s);
    """
    val = (None,tipo)
    try:
        resul_insert = insertDB(BASE, sQuery, val)
        return resul_insert == 1
    except Exception as e:
        print(f"Error inserting tipo: {e}")
        return False

def borrarArchivo(idarchivo):
    try:
        sSql = "DELETE FROM archivo WHERE id=%s;"
        val = (idarchivo,)  # Asegurar que val sea una tupla
        result_delete = deleteDB(BASE, sSql, val)
        return result_delete == 1
    except Exception as e:
        # Manejar errores y registrar o devolver información útil
        print(f"Error al borrar en la base de datos: {e}")
        return False

#######################################################
#################### END ADMIN ########################
#######################################################


#######################################################
#################### VERARCHIVOS ######################
#######################################################

def obtenerArchivos(param,sSql,idusuario):
    datos = selectDB(BASE, sSql, title=False)
    param["cantdatos"] = [f"archivo_id={archivo[0]}" for archivo in datos]
    for archivo in datos:
        momento = f"archivo_id={archivo[0]}"
        param[momento] = {
            "archivo_id": archivo[0],
            "nombre_archivo": archivo[1],
            "nombre_pdf": archivo[2],
        }

        usuario = selectDB(BASE, f"SELECT * FROM usuario WHERE id={archivo[3]}", title=False)
        param[momento]["nombre_usuario"] = usuario[0][3] if usuario else "Usuario no encontrado"

        materia = selectDB(BASE, f"SELECT * FROM materias WHERE id={archivo[4]}", title=False)
        param[momento]["nombre_materia"] = materia[0][1] if materia else "Materia no encontrada"

        tipo = selectDB(BASE, f"SELECT * FROM tipos WHERE id={archivo[5]}", title=False)
        param[momento]["nombre_tipo"] = tipo[0][1] if tipo else "Tipo no encontrado"

        sSql = f"SELECT COUNT(*) AS total_likes FROM control_like WHERE id_archivo={archivo[0]}"
        likes = selectDB(BASE, sSql, title=False)
        param[momento]["cant_likes"] = likes[0][0]

        if verificarLike(param[momento]["archivo_id"], idusuario): #le paso id arch y id usuario
            param[momento]["estilo_like"] = "like_click"
        else:
            param[momento]["estilo_like"] = "likeBtn"

        if verificarFavorito(param[momento]["archivo_id"], idusuario):
             param[momento]["estilo_fav"] = "star_click"
        else:
            param[momento]["estilo_fav"] = "starBtn"


        #ESTO ES PARA VER LOS COMENTARIOS
        sSql = f"""
            SELECT comentarios.textocomentario, usuario.nomusuario
            FROM comentarios
            INNER JOIN usuario ON comentarios.id_usuario = usuario.id
            WHERE comentarios.id_archivo={archivo[0]}
        """
        comentarios = selectDB(BASE, sSql, title=False)
        param[momento]["comentarios"] = []  # Inicializa la lista de comentarios

        for coments in comentarios:
            comentario_actual = {
                "text": coments[0],
                "nombre": coments[1]
            }
            param[momento]["comentarios"].append(comentario_actual)
        





def verificarLike(archivoid, usuario):
    sQuery = """ 
        SELECT *
        FROM  control_like 
        WHERE id_usuario=%s AND id_archivo=%s;
    """
    val = (usuario, archivoid)
    try:
        resul_select = selectDB(BASE, sQuery, val)
        if len(resul_select) >= 1:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error inserting tipo: {e}")
        return False


def crearLike(archivoid, usuario):
    sQuery = "INSERT INTO control_like (id,id_usuario, id_archivo) VALUES (%s,%s, %s);"
    val = (None, usuario, archivoid)
    try:
        resul_insert = insertDB(BASE, sQuery, val)
        return resul_insert == 1
    except Exception as e:
        print(f"Error al crear like: {e}")
        return False

def borrarLike(archivoid, usuario):
    sQuery = "DELETE FROM control_like WHERE id_usuario=%s AND id_archivo=%s;"
    val = (usuario, archivoid)
    try:
        resul_delete = deleteDB(BASE, sQuery, val)
        return resul_delete == 1
    except Exception as e:
        print(f"Error al borrar like: {e}")
        return False


def verificarFavorito(archivoid, usuario):
    sQuery = """ 
        SELECT *
        FROM  favoritos 
        WHERE id_usuario=%s AND id_archivo=%s;
    """
    val = (usuario, archivoid)
    try:
        resul_select = selectDB(BASE, sQuery, val)
        if len(resul_select) >= 1:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error inserting tipo: {e}")
        return False
    

def crearFavorito(archivoid, usuario):
    sQuery = "INSERT INTO favoritos (id,id_usuario, id_archivo) VALUES (%s,%s, %s);"
    val = (None, usuario, archivoid)
    try:
        resul_insert = insertDB(BASE, sQuery, val)
        return resul_insert == 1
    except Exception as e:
        print(f"Error al crear like: {e}")
        return False

def borrarFavorito(archivoid, usuario):
    sQuery = "DELETE FROM favoritos WHERE id_usuario=%s AND id_archivo=%s;"
    val = (usuario, archivoid)
    try:
        resul_delete = deleteDB(BASE, sQuery, val)
        return resul_delete == 1
    except Exception as e:
        print(f"Error al borrar like: {e}")
        return False

def crearComentario(comentario, usuario,archivoid):
    sQuery = """INSERT INTO comentarios
            (id,id_usuario, id_archivo,textocomentario) 
            VALUES (%s,%s, %s,%s);"""
    val = (None, usuario, archivoid,comentario)
    try:
        resul_insert = insertDB(BASE, sQuery, val)
        return resul_insert == 1
    except Exception as e:
        print(f"Error al crear like: {e}")
        return False

#######################################################
#################### END VERARCHIVOS ##################
#######################################################



#######################################################
#################### SUBIR ARCHIVOS ###################
#######################################################
def vertipo(param):
    sSql = """SELECT * FROM tipos"""
    val = None
    fila = selectDB(BASE, sSql, val)
    param["lista_tipos"] = fila
    sSql = """SELECT COUNT(*) AS total_tipos FROM tipos;
            """
    val = None
    fila = selectDB(BASE, sSql, val)
    param["cantidad_tipos"] = fila
    ######### ESTES CODIGO ES PARA CANTIDAD DE ARCHIVOS SUBIDOS ########
    sSql = """SELECT COUNT(*) AS total_archivos FROM archivo;
            """
    val = None
    fila = selectDB(BASE, sSql, val)
    param["cantidad_archivos"] = fila
    ######### ###################

def crearArchivo(di):
    '''{
    "fecha": "Thu, 23 Nov 2023 16:37:05 GMT",
    "id_usuario": 1,
    "materias": "29",
    "nombrearch": "fede",
    "pdf": {
        "file_error": false,
        "file_msg": "OK. Archivo cargado exitosamente",
        "file_name": "Programaci\u00f3n Web(Programa sintetico).pdf",
        "file_name_new": "add733e7-b197-415c-94a0-2e3617819f39.pdf"
    },
    "tipo": "3"
    }
    '''
    sQuery = """
        INSERT INTO archivo
        (id, nombre, pdf, id_usuario, id_materia, id_tipo, fecha, revisado)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    
    val = (None, di['nombrearch'], di['pdf']['file_name_new'], di.get('id_usuario'), di.get('materias'), di.get('tipo'), di.get("fecha"), "No Revisado")

    try:
        resul_insert = insertDB(BASE, sQuery, val)
        return resul_insert == 1
    except Exception as e:
        # Manejar errores y registrar o devolver información útil
        print(f"Error al insertar en la base de datos: {e}")
        return False

#######################################################
#################### END SUBIR ARCHIVOS ###############
#######################################################

#######################################################
#################### PERFIL ###############
#######################################################

def obtenerUsuarioXid(param,id,clave):

    sSql="""SELECT *
    FROM  usuario WHERE  id=%s;""" 
    val=(id,)

    fila=selectDB(BASE,sSql,val)
    param[clave]={}
    param[clave]['id']=fila[0][0]
    param[clave]['nombre']=fila[0][1]
    param[clave]['apellido']=fila[0][2]
    param[clave]['nomusuario']=fila[0][3]
    param[clave]['email']=fila[0][4]
    param[clave]['password']=fila[0][5]




def obtenerFavoritos(param,idusuario):
    #Me pega las dos tablas
    sSql = """SELECT archivo.id, archivo.nombre, archivo.pdf, 
            archivo.id_usuario, archivo.id_materia, archivo.id_tipo,
            archivo.fecha, archivo.revisado
            FROM favoritos
            INNER JOIN archivo ON favoritos.id_archivo = archivo.id
            WHERE favoritos.id_usuario = %s;"""
    val = (idusuario,)
    datos = selectDB(BASE, sSql, val)
    param["cantdatos"] = [f"archivo_id={archivo[0]}" for archivo in datos]

    for archivo in datos:
        momento = f"archivo_id={archivo[0]}"
        param[momento] = {
            "archivo_id": archivo[0],
            "nombre_archivo": archivo[1],
            "nombre_pdf": archivo[2],
        }

        usuario = selectDB(BASE, f"SELECT * FROM usuario WHERE id={archivo[3]}", title=False)
        param[momento]["nombre_usuario"] = usuario[0][3] if usuario else "Usuario no encontrado"

        materia = selectDB(BASE, f"SELECT * FROM materias WHERE id={archivo[4]}", title=False)
        param[momento]["nombre_materia"] = materia[0][1] if materia else "Materia no encontrada"

        tipo = selectDB(BASE, f"SELECT * FROM tipos WHERE id={archivo[5]}", title=False)
        param[momento]["nombre_tipo"] = tipo[0][1] if tipo else "Tipo no encontrado"

        sSql = f"SELECT COUNT(*) AS total_likes FROM control_like WHERE id_archivo={archivo[0]}"
        likes = selectDB(BASE, sSql, title=False)
        param[momento]["cant_likes"] = likes[0][0]

        if verificarLike(param[momento]["archivo_id"], idusuario): #le paso id arch y id usuario
            param[momento]["estilo_like"] = "like_click"
        else:
            param[momento]["estilo_like"] = "likeBtn"

        if verificarFavorito(param[momento]["archivo_id"], idusuario):
             param[momento]["estilo_fav"] = "star_click"
        else:
            param[momento]["estilo_fav"] = "starBtn"
        


#######################################################
#################### END PERFIL ###############
#######################################################


def obtenerUsuarioXEmail(param,email,clave='usuario'):
    '''### Información:
       Obtiene todos los campos de la tabla usuario a partir de la clave 'email'.
       Carga la información obtenida de la BD en el dict 'param'
       Recibe 'param' in diccionario
       Recibe 'email' que es el mail si se utiliza como clave en la búsqueda
       Recibe 'clave' que es a clave que se le colocará al dict 'param'
       
    '''
    sSql="""SELECT id, nombre,apellido,nomusuario,email,pass 
    FROM  usuario WHERE  email=%s;""" 
    val=(email,)

    fila=selectDB(BASE,sSql,val)
    param[clave]={}
    param[clave]['id']=fila[0][0]
    param[clave]['nombre']=fila[0][1]
    param[clave]['apellido']=fila[0][2]
    param[clave]['nomusuario']=fila[0][3]
    param[clave]['email']=fila[0][4]
    param[clave]['password']=fila[0][5]

def obtenerUsuarioXEmailPass(result,email,password):
    '''### Información:
       Obtiene todos los campos de la tabla usuario a partir de la clave 'email'
         y del 'password'.
       Carga la información obtenida de la BD en el dict 'result'
       Recibe 'result' in diccionario donde se almacena la respuesta de la consulta
       Recibe 'email' que es el mail si se utiliza como clave en la búsqueda
       Recibe 'password' que se utiliza en la consulta. (Para validadar al usuario)
       Retorna:
        True cuando se obtiene un registro de u usuario a partir del 'email' y el 'pass.
        False caso contrario.
    '''
    res=False
    sSql="""SELECT * 
    FROM  usuario WHERE  email=%s and contrasena=%s;"""
    val=(email,password)
    fila=selectDB(BASE,sSql,val)
    if fila!=[]:
        res=True
        result['id']=fila[0][0]
        result['nombre']=fila[0][1]
        result['apellido']=fila[0][2]
        result['nomusuario']=fila[0][3] # es el mail
        result['email']=fila[0][4]
        result['contrasena']=fila[0][5]
    return res    
        


def actualizarUsuario(di,email):
    '''### Información:
        Actualiza el registro de la tabla usuario para la clave 'email'
        Recibe 'di' un dict con los campos que se requiere modificar.
        Recibe 'email' que es la clave para identificar el regsitro a actualizar.
        Retorna True si realiza la actualización correctamente.
                False caso contrario.

    '''
    sQuery="""update usuario 
        SET nombre=%s, 
        apellido=%s,
        nomusuario=%s,
        email=%s,
        contrasena=%s
        WHERE email=%s;
        """
    val=(di.get('nombre'), 
         di.get('apellido'), 
         di.get('nomusuario'),
         di.get('email'), 
         di.get('password2'), 
         email )
    
    resul_update=updateDB(BASE,sQuery,val=val)
    return resul_update==1

def actualizarEstado(mirequest,idarchivo,estado):
    if estado == "No Revisado":
        sQuery="""update archivo 
            SET revisado=%s
            WHERE id=%s;
            """
        val=("Revisado", idarchivo )
        
        resul_update=updateDB(BASE,sQuery,val=val)
        return resul_update==1
    else:
        sQuery="""update archivo 
            SET revisado=%s
            WHERE id=%s;
            """
        val=("No Revisado", idarchivo)
        resul_update=updateDB(BASE,sQuery,val=val)
        return resul_update==1

# def validarUsuario(email,password):
#     '''### Información:
#           Se consulta a la BD un usuario 'email' y un 'password'
#           retorna True si 'email' y  'password' son válido
#           retorna False caso contrario
#     '''
#     sSql='''
#         SELECT * FROM  usuario
#             WHERE 
#             email=%s
#             AND 
#             pass=%s;
#     '''
#     val=(email,password)
#     fila=selectDB(BASE,sSql,val=val)
#     return fila!=[]
