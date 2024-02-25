'''### info:
     CONTROL 
'''
import os
from flask import Flask, render_template, request, redirect, session, flash, url_for  
from controller import *
from werkzeug.utils import secure_filename

def route(app): 
    """CARGA LA LANDING"""   
    @app.route("/")
    @app.route("/landingpage")
    def landingpage():
        ''' Info:
          Carga la pagina del home
        '''
        param={} 
        return home_pagina(param)   
        
    
    @app.route("/login")
    def login():
        """CARGA EL LOGIN"""   
        param={}
        return login_pagina(param)     
        
    
    @app.route("/register")
    def register():
      """CARGA EL REGISTER"""
      param={}
      return registro_pagina(param)  

    
    @app.route("/signup", methods =["GET", "POST"])
    def signup():
        ''' Info:
          Recepciona la solicitud request que es enviada
          desde el formulario de registro 
          registroDeUsuario: Lueog de realizar el porceso de 
             registro del ussuario, retorna la pagina del login 
        '''
        param={}
        return registrarUsuario(param,request)


    @app.route('/signin', methods =["GET", "POST"])
    def signin(): 
        ''' Info: 
          Recepciona la solicitud request que es enviada
          desde el formulario de login 
          retorna la pagina home en caso de exito 
                  o la pagina login en caso de fracaso
        '''
        param={}
        return ingresoUsuarioValido(param,request)

 
    @app.route("/logout")
    def logout():  
        ''' Info: 
          Cierra la sesión.
          retorna la redirección a la pagina home   
        ''' 
        cerrarSesion()     
        return redirect('/')
    

    @app.route("/subirarchivos")
    def subirarch():
        ''' Info:
          Carga la pagina PARA SUBIR ARCHVOS
          Retorna la pagina PARA SUBIR ARCHVOS, si hay sesion; sino retorna la home.
        '''
        param={}
        return subirarchivos(param)


    @app.route("/verarchivos")
    def verarch():
        ''' Info:
          Carga la paginaPARA VER ARCHVOS
          Retorna la pagina PARA VER ARCHVOS, si hay sesion; sino retorna la home.
        '''
        param={}
        return verarchivos(param)   
    
    @app.route("/modificarlike", methods=["GET", "POST"])
    def modificarlike():
      ''' Info:
          RECEPCIONA EL FORMULARIO PARA AGREGAR O SACAR LIKE
        '''
      param = {}
      sis_modificarlike(param,request)
      return verarch()
    
    @app.route("/agregarfavoritos", methods=["GET", "POST"])
    def modificarfavoritos():
      ''' Info:
          RECEPCIONA EL FORMULARIO PARA AGREGAR O SACAR FAVORITO
        '''
      param = {}
      sis_modificarfavoritos(param, request)
      return verarch()



    @app.route("/enviarcomentario", methods=["GET", "POST"])
    def enviarcomentario():
      ''' Info:
          RECEPCIONA EL FORMULARIO PARA ENVIAR EL COMENTARIO
        '''
      param = {}
      sis_enviarcomentario(param, request)
      return verarch()
    


    @app.route("/admin")
    def cargaradmin():
        ''' Info:
          Carga LA PAGINA DE ADMIN
          Retorna LA PAGINA DE ADMIN, si hay sesion Y SOS ADMIN
        '''
        param={}
        return admin(param)

    @app.route("/subirmateria", methods =["GET", "POST"])
    def admin_subirmat():
        ''' Info:
          RECEPCIONA EL FORMULARIO PARA SUBIR MATERIA
        '''
        param={}
        return admin_subirmateria(param,request)

    @app.route("/eliminarmateria", methods=["GET", "POST"])
    def admin_elimmateria():
      ''' Info:
          RECEPCIONA EL FORMULARIO PARA ELIMINAR MATERIA
        '''
      param = {}
      return admin_eliminarmateria(param, request)
    
    @app.route("/eliminartipos", methods=["GET", "POST"])
    def admin_elimtipos():
      ''' Info:
          RECEPCIONA EL FORMULARIO PARA ELIMINAR TIPO
        '''
      param = {}
      return admin_eliminartipos(param, request)
        
  
    @app.route("/subirtipo", methods =["GET", "POST"])
    def admin_subirtipomateria():
        ''' Info:
          RECEPCIONA EL FORMULARIO PARA SUBIR TIPO
        '''
        param={}
        return admin_subirtipo(param,request)
    
    @app.route("/actualizarestado", methods =["GET", "POST"])
    def actualizarestado():
        ''' Info:
          RECEPCIONA EL FORMULARIO PARA PONER REVISADO O NO LOS ARCHIVOS DE LA GENTE
        '''
        param={}
        return admin_actualizarestado(param,request)
    
    @app.route("/admin-subidos")
    def cargar_admin_subidos():
        ''' Info:
          CARGA LA PAGINA DE SUBIDOSS
        '''
        param={}
        return admin_subidos(param)

    @app.route("/borrararchivo", methods =["GET", "POST"])
    def routeborrararchivo():
        ''' Info:
          RECEPCIONA EL FORMULARIO PARA BORRAR ARCHIVO
          LO USAN PERFIL-CREADOS  Y ADMIN-SUBIDOS
        '''
        param={}
        borrararchivo(param,request)
        return admin_subidos(param)

    @app.route("/perfil")
    def cargar_perfil():
        ''' Info:
          CARGA LA PAGINA DE PERFIL
        '''
        param={}
        return perfil(param) 

    @app.route("/perfil-favoritos")
    def cargar_perfil_favoritos():
      ''' Info:
          CARGA LA PAGINA DE PERFIL FAV
        '''
      param={}
      return perfil_favoritos(param) 

    @app.route("/modificarfavoritoperfil", methods=["GET", "POST"])
    def sacarfavoritos():
      ''' Info:
          RECEPCIONA EL MODIFICAR FAV PERFIL PERO TE REDIRIGE NUEVAMENTE A FAV PERFIL
        '''
      param = {}
      perfil_sacarfavorito(param, request)
      return cargar_perfil_favoritos()

    @app.route("/modificarlikeperfil", methods=["GET", "POST"])
    def modificarlikeperfil():
      ''' Info:
          RECEPCIONA EL MODIFICAR LIKE PERFIL PERO TE REDIRIGE NUEVAMENTE A FAV PERFIL
        '''
      param = {}
      sis_modificarlike(param, request)
      return cargar_perfil_favoritos()


    """
    @app.route("/enviarcomentarioperfil", methods=["GET", "POST"])
    def enviarcomentarioperfil():
      ''' Info:
          RECEPCIONA EL FORMULARIO PARA ENVIAR EL COMENT PERO TE REDIRIGE A FAV PERFIL
        '''
      param = {}
      sis_enviarcomentario(param, request)
      return cargar_perfil_favoritos()
    """

    @app.route("/perfil-creados")
    def cargar_perfil_creados():
      ''' Info:
          CARGA PERFIL CREADO
        '''
      param={}
      return perfil_creados(param) 
    
    @app.route("/borrararchivoperfil", methods=["GET", "POST"])
    def borrararchivoperfil():
      ''' Info:
          RECEPCIONA EL FORMULARIO PARA BORRAR EL ARCHIVO CREADO
      '''
      param = {}
      borrararchivo(param,request)
      return cargar_perfil_creados()
        

    @app.route("/actualizarusuario", methods =["GET", "POST"])
    def update_user():
        ''' Info:
          Recepciona la solicitud request que es enviada
              desde el formulario de edit_user 
          Retorna 
            si hay sesion: retorna la edit_user con los datos actualizados
               y un mensaje de exito o fracaso sobre el mismo form ; 
            si no hay sesion: retorna la home.
        '''
        param={}
        return actualizarDatosDeUsuarios(param,request)
        


    @app.route('/<name>')
    def noEncontrada(name):
        ''' Info:
          Entra en esta ruta todo direccionamiento recibido que 
          no machea con ningun otro route. Es decir no es un pagina (dirección)
            válida en el sistema.
          Retorna una pagina indicando el error. 
        '''  
        
        return paginaNoEncontrada(name)
        

    
    def allowed_file(filename):
        ALLOWED_EXTENSIONS = {'pdf'}
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
    @app.route('/uploader', methods = ['GET', 'POST']) 
    def uploader() : 
      diResult={}
      getRequet(diResult)
      upload_file(diResult)
      return subirarch()
        

            
    # si existe el archivo devuelve True
    # os.path.exists(os.path.join('G:\\Mi unidad\\NUBE\\Docencia\\UCA\\_Materias\\03-UCA.PW\\_Python\\_PythonFlask\\07_login_register_bd\\uploadfile',"agua.png"))
    
    # borrar un archivo
    # os.remove(os.path.join('G:\\Mi unidad\\NUBE\\Docencia\\UCA\\_Materias\\03-UCA.PW\\_Python\\_PythonFlask\\07_login_register_bd\\uploadfile',"agua.png"))
    
    