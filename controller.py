'''### info:
     CONTROL 
'''
from flask import request, session,redirect,render_template
from datetime import datetime
from model import *
from werkzeug.utils import secure_filename
import os
from uuid import uuid4
from appConfig import config

LISTA_ADMINS = [1]

def obtenerSideBar(param):
    param["boton"] = {"id": "toglesidebar", "class": "toglesidebar"}
    param['id_usuario'] = session.get("id_usuario")
    if param['id_usuario'] in LISTA_ADMINS:
        param['menu'] ={
            "ADMIN": {"href": "admin", "content": "ADMIN", "class": " "},
            "PERFIL": {"href": "perfil", "content": "PERFIL", "class": " "},
            "SUBIR ARCHIVOS": {"href": "subirarchivos", "content": "SUBIR ARCHIVOS", "class": " "},
            "VER ARCHIVOS": {"href": "verarchivos", "content": "VER ARCHIVOS", "class": " "},
            "CERRAR SESION": {"href": "logout", "content": "CERRAR SESION", "class": " "},   
        }
    else:
        param['menu'] ={
            "PERFIL": {"href": "perfil", "content": "PERFIL", "class": " "},
            "SUBIR ARCHIVOS": {"href": "subirarchivos", "content": "SUBIR ARCHIVOS", "class": " "},
            "VER ARCHIVOS": {"href": "verarchivos", "content": "VER ARCHIVOS", "class": " "},
            "CERRAR SESION": {"href": "logout", "content": "CERRAR SESION", "class": " "},   
        }
    





##########################################################################
# + + I N I C I O + + MANEJO DE  REQUEST + + + + + + + + + + + + + + + + +
##########################################################################

def getRequet(diResult):
    if request.method=='POST':
        for name in request.form.to_dict().keys():
            li=request.form.getlist(name)
            if len(li)>1:
                diResult[name]=request.form.getlist(name)
            elif len(li)==1:
                diResult[name]=li[0]
            else:
                diResult[name]=""
    elif request.method=='GET':  
        for name in request.args.to_dict().keys():
            li=request.args.getlist(name)
            if len(li)>1:
                diResult[name]=request.args.getlist(name)
            elif len(li)==1:
                diResult[name]=li[0]
            else:
                diResult[name]=""     
 
"""
def getRequet(request):
    '''info:
        Lee un solicitud 'request' y hace tratamiento de lectura diferenciado
        dependiendo del metodo (post o get). Luego unifica  el contenido del
        request en un diccionario 'myrequest'.
        Retorna 'myrequest' un diccionario con los datos 
               recibidos en la solicitud 'request'
    '''
    try: 
        if request.method =="POST":                           # Solicitud x POST, creación de una session
            myrequest=request.form          
        elif request.method =="GET" and len(request.args)!=0: # Solicitud x GET, creación de una session
            myrequest=request.args
        else:
            myrequest={}
    except ValueError:                              
        myrequest={}
    return myrequest
"""
##########################################################################
# - - F I N - - MANEJO DE  REQUEST - - - - - - - - - - - - - - - - - - - -
##########################################################################

##########################################################################
# + + I N I C I O + + MANEJO DE  SUBIDA DE ARCHIVOS  + + + + + + + + + + +
##########################################################################

def upload_file (diResult) :
    UPLOAD_EXTENSIONS = ['.pdf']
    MAX_CONTENT_LENGTH = 1024 * 1024     
    if request.method == 'POST' :         
        for key in request.files.keys():  
            diResult[key]={} 
            diResult[key]['file_error']=False            
            
            f = request.files[key] 
            if f.filename!="":     
                #filename_secure = secure_filename(f.filename)
                file_extension=str(os.path.splitext(f.filename)[1])
                filename_unique = uuid4().__str__() + file_extension
                path_filename=os.path.join( config['upload_folder'] , filename_unique)
                # Validaciones
                if file_extension not in UPLOAD_EXTENSIONS:
                    diResult[key]['file_error']=True
                    diResult[key]['file_msg']='Error: No se admite subir archivos con extension '+file_extension
                if os.path.exists(path_filename):
                    diResult[key]['file_error']=True
                    diResult[key]['file_msg']='Error: el archivo ya existe.'
                    diResult[key]['file_name']=f.filename
                try:
                    if not diResult[key]['file_error']:
                        diResult[key]['file_error']=True
                        diResult[key]['file_msg']='Se ha producido un error.'

                        f.save(path_filename)   
                        diResult[key]['file_error']=False
                        diResult[key]['file_name_new']=filename_unique
                        diResult[key]['file_name']=f.filename
                        diResult[key]['file_msg']='OK. Archivo cargado exitosamente'
                        diResult["fecha"] = datetime.now() 
                        diResult["id_usuario"] = session['id_usuario']
                        crearArchivo(diResult)
 
                except:
                        pass
            else:
                diResult[key]={} # viene vacio el input del file upload


    # si existe el archivo devuelve True
    # os.path.exists(os.path.join('G:\\directorio\\....\\uploads',"agua.png"))

    # borrar un archivo
    # os.remove(os.path.join('G:\\directorio\\.....\\uploads',"agua.png"))

##########################################################################
# - - F I N - - MANEJO DE  SUBIDA DE ARCHIVOS  - - - - - - - - - - - - - - 
##########################################################################


##########################################################################
# + + I N I C I O + + MANEJO DE  SESSION + + + + + + + + + + + + + + + + +
##########################################################################

def cargarSesion(dicUsuario):
    '''info:
        Realiza la carga de datos del usuario
        en la variable global dict 'session'.
        recibe 'dicUsuario' que es un diccionario con datos
               de un usuario 
    '''

    session['id_usuario'] = dicUsuario['id']
    session['nombre']     = dicUsuario['nombre']
    session['apellido']   = dicUsuario['apellido']
    session['nomusuario'] = dicUsuario['nomusuario'] 
    session['username']   = dicUsuario['email'] # es el mail

    session['imagen']     = ""
    session['rol']        = ""
    session["time"]       = datetime.now()  

def crearSesion(request):
    '''info:
        Crea una sesion. Consulta si los datos recibidos son validos.
        Si son validos cargar una sesion con los datos del usuario
        recibe 'request' una solicitud htpp con los datos 'email' y 'pass' de un usuario
        retorna True si se logra un session, False caso contrario
    '''
    sesionValida=False
    mirequest={}
    try:           
        getRequet(mirequest)
        # CONSULTA A LA BASE DE DATOS, Si usuario es valido => crea session
        dicUsuario={}
        if obtenerUsuarioXEmailPass(dicUsuario,mirequest.get("email"),mirequest.get("password")):
            # Carga sesion (Usuario validado)
            cargarSesion(dicUsuario)
            sesionValida = True
    except ValueError:                              
        pass
    return sesionValida

def haySesion():  
    '''info:
        Determina si hay una sesion activa observando si en el dict
        session se encuentra la clave 'username'
        retorna True si hay sesión y False si no la hay.
    '''
    return session.get("username")!=None

def cerrarSesion():
    '''info:
        Borra el contenido del dict 'session'
    '''
    try:    
        session.clear()
    except:
        pass

##########################################################################
# - - F I N - - MANEJO DE  SESSION - - - - - - - - - - - - - - - - - - - -
##########################################################################


##########################################################################
# + + I N I C I O + + PAGINA login,  home y/o principal    + + + + + + + + 
##########################################################################

def home_pagina(param): 
    ''' Info:
      Carga la pagina home.
      Recibe 'param' el diccionario de parametros
      Retorna la pagina 'home'
    '''
    obtenerInfo(param)
    return render_template('landingpage.html',param=param)

def login_pagina(param):
    ''' Info:
      Carga la pagina login.
      Recibe 'param' el diccionario de parametros
      Retorna la pagina 'login'
    '''
    return render_template('login.html',param=param)

##########################################################################
# - - F I N - - PAGINA home, main y login  - - - - - - - - - - - - - - - -
##########################################################################


##########################################################################
# + + I N I C I O + + USUARIO: registro, edicion, actualizacion  + + + + + 
##########################################################################



def ingresoUsuarioValido(param,request):
    '''info:
        Valida el usuario y el pass contra la BD.
        recibe 'param' dict de parámetros
        recibe 'request' una solicitud http con los datos usuario y pass
        retorna: 
            Si es valido el usuario y pass => crea una session y retorna 
            la pagina home.
            Si NO es valido el usuario y pass => retorna la pagina login
            y agrega en el diccionario de parámetros una clave con un mensaje 
            de error para ser mostrada en la pagina login.
    '''
    if crearSesion(request):
        res=verarchivos(param)
    else:
        param['error_msg_login']="Error: Usuario y/o password inválidos"
        res= login_pagina(param)        
    return res  

def registro_pagina(param):
    '''info:
        Carga la pagina 'register'
    '''      
    return render_template('register.html',param=param)

def registrarUsuario(param,request):
    '''info:
      Realiza el registro de un usuario en el sistema, es decir crea un nuevo usuario
      y lo registra en la base de datos.
      recibe 'param' el diccionario de parámetros.
      recibe request es la solicitud (post o get) proveniente del cliente
      retorna la pagina del login, para forzar a que el usuario realice el login con
      el usuario creado.
    '''
    mirequest={}
    getRequet(mirequest)
    
    # CONSULTA A LA BASE DE DATOS: Realiza el insert en la tabla usuario
    if crearUsuario(mirequest):
        param['succes_msg_login']="Se ha creado el usuario con exito"
        cerrarSesion()           # Cierra sesion existente(si la hubiere)
        res=login_pagina(param)  # Envia al login para que vuelva a loguearse el usuario
    else:
        param['error_msg_register']="Error: No se ha podido crear el usuario"
        res=registro_pagina(param)

    return res 

def editarUsuario_pagina(param):
    '''info:
        Carga la pagina edit_user
        Retorna la pagina edit_user, si hay sesion; sino retorna la home.
    '''
    res= redirect('/') # redirigir al home o a la pagina del login

    if haySesion():    # hay session?
        # Confecciona la pagina en cuestion

        obtenerUsuarioXEmail(param,session.get('username'), 'edit_user')
        res= render_template('edit_user.html',param=param)
           
    return res  


def actualizarDatosDeUsuarios(param,request):
    '''info:
            Recepciona la solicitud request que es enviada
            desde el formulario de edit_user 
          Retorna 
            si hay sesion: retorna la edit_user con los datos actualizados
               y un mensaje de exito o fracaso sobre el mismo form ; 
            si no hay sesion: retorna la home.
    '''
    res=False
    msj=""
    mirequest={}
    try:     
        getRequet(mirequest)      
        # *** ACTUALIZAR USUARIO ***
        
        if actualizarUsuario(mirequest,session.get("username")):
            print("hola")
            res=True
            param['succes_msg_updateuser']="Se ha ACTUALIZADO el usuario con exito"
        else:
            #error
            print("chau")
            res=False
            param['error_msg_updateuser']="Error: No se ha podido ACTUALIZAR el usuario"

        res= perfil(param)
    except ValueError as e :                   
        pass
    return res 



##########################################################################
# - - F I N - - USUARIO: registro, edicion, actualizacion  - - - - - - - -
##########################################################################
 

##########################################################################
# + + I N I C I O + +  OTRAS PAGINAS     + + + + + + + + + + + + + + + + +
##########################################################################

def subirarchivos(param):  
    if haySesion():       # hay session?       
        # Confecciona la pagina en cuestion
        obtenerSideBar(param)
        vermaterias(param)
        vertipo(param)
        res= render_template('subirarch.html',param=param)
    else:
        res= redirect('/')   # redirigir al home o a la pagina del login
    return res  
    

def verarchivos(param):  
    ''' Info:
        Carga la pagina 02
        Retorna la pagina 02, si hay sesion; sino retorna la home.
    '''
    if haySesion():   # hay session?
        param = {}
        obtenerSideBar(param)
        sSql = "SELECT * FROM archivo;"
        idusuario = session["id_usuario"]
        obtenerArchivos(param,sSql,idusuario)
        # Confecciona la pagina en cuestion
        res= render_template('sistema.html',param=param)
    else:
        res= redirect('/login') # redirigir al home o a la pagina del login
    return res 



def sis_modificarlike(param,request):
    mirequest = {}
    getRequet(mirequest)
    try:
        archivoid = mirequest.get("archivo_id")
        usuario = session['id_usuario']
        if verificarLike(archivoid, usuario):
            borrarLike(archivoid, usuario)
            param["MENSAJE_like"] = "Le has sacado like"
            print("hola")
        else:
            crearLike(archivoid, usuario)
            param["MENSAJE_like"] = "Le has dado like"
            print("chau")
    except Exception as e:
        print(f"Error al modificar like: {e}")

def sis_modificarfavoritos(param, request):
    mirequest = {}
    getRequet(mirequest)
    try:
        archivoid = mirequest.get("archivo_id")
        usuario = session['id_usuario']
        if verificarFavorito(archivoid, usuario):
            borrarFavorito(archivoid, usuario)
            param["estilo estrella"] = "starBtn"
            print("hola")
        else:
            crearFavorito(archivoid, usuario)
            param["estilo estrella"] = "star_click"
            print("chau")
    except Exception as e:
        print(f"Error al modificar like: {e}")

def sis_enviarcomentario(param, request):
    mirequest = {}
    getRequet(mirequest)
    try:
        comentario = mirequest.get("com")
        usuario = session['id_usuario']
        archivoid =  mirequest.get("archivo_id")
        crearComentario(comentario, usuario,archivoid)
    except Exception as e:
        print(f"Error al modificar like: {e}")

def perfil_sacarfavorito(param, request):
    mirequest = {}
    getRequet(mirequest)
    try:
        archivoid = mirequest.get("archivo_id")
        usuario = session['id_usuario']
        borrarFavorito(archivoid, usuario)
        param["estilo estrella"] = "starBtn"
        print("hola")
    except Exception as e:
        print(f"Error al modificar like: {e}")

def perfil(param):  
    ''' Info:
        Carga la pagina 02
        Retorna la pagina 02, si hay sesion; sino retorna la home.
    '''
    if haySesion():   # hay session?
        obtenerSideBar(param)
        iduser=session['id_usuario']
        obtenerUsuarioXid(param,iduser,clave='usuario')
        # Confecciona la pagina en cuestion
        res= render_template('perfil.html',param=param)
    else:
        res= redirect('/') # redirigir al home o a la pagina del login
    return res 

def perfil_favoritos(param):  
    ''' Info:
        Carga la pagina 02
        Retorna la pagina 02, si hay sesion; sino retorna la home.
    '''
    if haySesion():   # hay session?
        param = {}
        obtenerSideBar(param)
        idusuario = session["id_usuario"]
        #esta fun es para obtener los id de los archivos los cuales guarde
        #es parecida a obtener archivos solo q accede a dos tablas
        obtenerFavoritos(param,idusuario) 
        # Confecciona la pagina en cuestion
        res= render_template('favoritos.html',param=param)
    else:
        res= redirect('/') # redirigir al home o a la pagina del login
    return res  

def perfil_creados(param):  
    ''' Info:
        Carga la pagina 02
        Retorna la pagina 02, si hay sesion; sino retorna la home.
    '''
    if haySesion():   # hay session?
        param = {}
        obtenerSideBar(param)
        sSql = "SELECT * FROM  archivo WHERE id_usuario={};".format(session["id_usuario"])
        idusuario = session["id_usuario"]
        obtenerArchivos(param,sSql,idusuario)
        # Confecciona la pagina en cuestion
        res= render_template('creados.html',param=param)
    else:
        res= redirect('/') # redirigir al home o a la pagina del login
    return res 





def admin(param):
    ''' Info:
        Carga la pagina admin
        Retorna la pagina, si hay sesion Y ES ADMIN; sino retorna la home.
    '''
    if haySesion():   # hay session?
        # EL ID 1 SOY YO, SOY EL UNICO ADMIN
        # TENDRIA QUE MODIFICAR ACA SI QUIERO MAS ADMINS
        if session.get("id_usuario") in LISTA_ADMINS:
            vermaterias(param)
            vertipo(param)
            admin_creartabla(param)
            # Confecciona la pagina en cuestion
            res= render_template('admin.html',param=param)
        else:
            res= redirect('/verarchivos') # redirigir al home o a la pagina del login
    return res 


def admin_subirmateria(param, request):
    mirequest = {}
    getRequet(mirequest)
    if session.get("id_usuario") in LISTA_ADMINS:
        try:
            dicUsuario = {}
            materia = mirequest.get("addMateria")
            
            if crearMateria(dicUsuario, materia):
                param["MENSAJE"] = "SE HA CREADO EL NOMBRE DE LA MATERIA EXITOSAMENTE"
            else:
                param["MENSAJE"] = "ERROR NO SE PUDO CREAR EL NOMBRE DE LA MATERIA"
        except:
            pass
        return admin(param)

def admin_subirtipo(param, request):
    mirequest = {}
    getRequet(mirequest)
    if session.get("id_usuario") in LISTA_ADMINS:
        try:
            dicUsuario = {}
            tipo = mirequest.get("addFileType")
            
            if crearTipo(tipo):
                param["MENSAJE"] = "SE HA CREADO EL NOMBRE DEL TIPO DE ARCH EXITOSAMENTE"
            else:
                param["MENSAJE"] = "ERROR NO SE PUDO CREAR EL NOMBRE DEL TIPO DE MATERIA"
        except:
            pass
        return admin(param)

def admin_eliminarmateria(param, request):
    mirequest = {}
    getRequet(mirequest)
    if session.get("id_usuario") in LISTA_ADMINS:
        try:
            materia_id = mirequest.get("materia_id")
            if eliminarMateria(materia_id):
                param["MENSAJE DE BORRADO"] = "SE HA ELIMINADO CORRECTAMENTE"
            else:
                param["MENSAJE DE BORRADO"] = "ERROR: NO SE PUDO ELIMINAR CORRECTAMENTE"
        except Exception as e:
            # Manejar errores y registrar o devolver información útil
            print(f"Error al eliminar materia: {e}")
            param["MENSAJE DE BORRADO"] = "ERROR: OCURRIÓ UN PROBLEMA AL ELIMINAR LA MATERIA"
        
        return admin(param)

def admin_eliminartipos(param, request):
    mirequest = {}
    getRequet(mirequest)
    if session.get("id_usuario") in LISTA_ADMINS:
        try:
            tipo_id = mirequest.get("tipos_id")
            if eliminarTipos(tipo_id):
                param["MENSAJE DE BORRADO"] = "SE HA ELIMINADO CORRECTAMENTE"
            else:
                param["MENSAJE DE BORRADO"] = "ERROR: NO SE PUDO ELIMINAR CORRECTAMENTE"
        except Exception as e:
            # Manejar errores y registrar o devolver información útil
            print(f"Error al eliminar materia: {e}")
            param["MENSAJE DE BORRADO"] = "ERROR: OCURRIÓ UN PROBLEMA AL ELIMINAR LA MATERIA"
        
        return admin(param)


def admin_subidos(param):
    ''' Info:
        Carga la pagina admin
        Retorna la pagina, si hay sesion Y ES ADMIN; sino retorna la home.
    '''
    if haySesion():   # hay session?
        if session.get("id_usuario") in LISTA_ADMINS:
            obtenerSideBar(param)
            sSql = "SELECT * FROM  archivo"
            idusuario = session["id_usuario"]
            obtenerArchivos(param,sSql,idusuario)
            # Confecciona la pagina en cuestion
            res= render_template('subidos.html',param=param)
            return res
    
        res = redirect('/') # redirigir al home o a la pagina del login
        return res 

def admin_creartabla(param):
    #Es muy parecidad a la funcion de verarchivos en html sistema
    datos=[]
    sql = """SELECT *
            FROM archivo
            ORDER BY fecha DESC
            LIMIT 10;"""
    datos=selectDB(BASE,sql,title=False)
    param["cantdatos"] = [f"archivo_id={archivo[0]}" for archivo in datos] #El valor es una lista de tu tuplas, es para ver cuantas veces se repite el ciclo
    for archivo in datos:
        momento = f"archivo_id={archivo[0]}"
        param[momento] = {
            "archivo_id": archivo[0],
            "nombre_archivo": archivo[1],
            "nombre_pdf": archivo[2],
        }
        param[momento]["estado"] = archivo[7]
        param[momento]["fecha"] = archivo[6][:-7] # le hago slicing xq sino es mucho decimal
        usuario = selectDB(BASE, f"select * from usuario WHERE id={archivo[3]}", title=False)
        param[momento]["nombre_persona"] = usuario[0][1]+" "+usuario[0][2] if usuario else "Usuario no encontrado"
        param[momento]["email"] = usuario[0][4]
        materia = selectDB(BASE, f"select * from materias WHERE id={archivo[4]}", title=False)
        param[momento]["nombre_materia"] = materia[0][1] if materia else "Materia no encontrada"
        tipo = selectDB(BASE, f"select * from tipos WHERE id={archivo[5]}", title=False)
        param[momento]["nombre_tipo"] = tipo[0][1] if tipo else "Tipo no encontrado"

    return param


def admin_actualizarestado(param,request):
    res=False
    msj=""
    mirequest={}
    try:     
        getRequet(mirequest)      
        # *** ACTUALIZAR USUARIO ***
        idarchivo = mirequest.get("archivo_id")
        estado = mirequest.get("estado")
        if actualizarEstado(mirequest,idarchivo,estado):
            print("hola")
            res=True
            param['succes_msg_updateuser']="Se ha ACTUALIZADO el usuario con exito"
        else:
            #error
            print("chau")
            res=False
            param['error_msg_updateuser']="Error: No se ha podido ACTUALIZAR el usuario"

        res= admin(param)
    except ValueError as e :                   
        pass
    return res 

def borrararchivo(param,request):
    res=False
    msj=""
    mirequest={}
    try:     
        getRequet(mirequest)      
        # *** ACTUALIZAR USUARIO ***
        idarchivo = mirequest.get("archivo_id")
        if borrarArchivo(idarchivo):
            res=True
            param['succes_msg_updateuser']="Se ha ACTUALIZADO el usuario con exito"
        else:
            #error
            print("chau")
            res=False
            param['error_msg_updateuser']="Error: No se ha podido ACTUALIZAR el usuario"

        res= True
    except ValueError as e :                   
        pass
    return res 

def paginaNoEncontrada(name):
    ''' Info:
      Retorna una pagina generica indicando que la ruta 'name' no existe
    '''
    res='<h3>Pagina "{}" no encontrada<br></h3>'.format(name)
    res+='Click aquí para volver a la <a href="{}">{}</a>'.format("/","landingpage")
    
    return res


##########################################################################
# - - F I N - -   OTRAS PAGINAS    - - - - - - - - - - - - - - - - - - - -
##########################################################################


