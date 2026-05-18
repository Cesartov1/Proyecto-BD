from models import CrearUsuario, ModificarUsuario, ConsultarUsuarioPorId, Salida, CrearDocente, ModificarDocente, ConsultarDocente
from datetime import date
import bcrypt

#DOCENTE
class DocenteDAO:
    def __init__(self, conexion):
        self.conexion = conexion
    
    def crearDocente(self, docente:CrearDocente):
        salida = Salida(codigo=0, mensaje="")
        try:
            cursor = self.conexion.cursor()
            cursor.execute("select * from usuarios where idUsuario = %s", (docente.idUsuario,))
            usuarioExiste = cursor.fetchone()
            if not usuarioExiste:
                salida.codigo=404
                salida.mensaje="Usuario no encontrado"
            else:
                cursor.execute("select * from docentes where idUsuario = %s", (docente.idUsuario,))
                docenteExiste = cursor.fetchone()
                if docenteExiste:
                    salida.codigo = 400
                    salida.mensaje = "El usuario ya tiene un registro como docente" 
                elif docente.fechaIngreso > date.today():
                    salida.codigo=400
                    salida.mensaje="Fecha de ingreso no valida"
                else:
                    cursor.execute("""insert into docentes (idUsuario, gradoEstudio, fechaIngreso, estadoLaboral,
                    correoInstitucional, horasFrenteAlGrupo, horasDocencia, horasAdministrativas, tipoContrato)
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (docente.idUsuario, docente.gradoEstudio,
                    docente.fechaIngreso, docente.estadoLaboral, docente.correoInstitucional,
                    docente.horasFrenteAlGrupo, docente.horasDocencia, docente.horasAdministrativas,
                    docente.tipoContrato))
                    self.conexion.commit()
                    salida.codigo = 201
                    salida.mensaje = "Docente creado exitosamente"
        except Exception as e:
            self.conexion.rollback()
            salida.codigo = 500
            salida.mensaje = "Error al crear docente"
        return salida

    def modificarDocente(self, idDocente:int, docente:ModificarDocente):
        salida = Salida(codigo=0, mensaje="")
        try:
            cursor = self.conexion.cursor()
            cursor.execute("select * from docentes where idDocente = %s", (idDocente,))
            docenteExiste = cursor.fetchone()
            if not docenteExiste:
                salida.codigo = 404
                salida.mensaje = "Docente no encontrado"
            elif docenteExiste['estadoLaboral'] != 'Activo':
                salida.codigo = 400
                salida.mensaje = "El docente no tiene un estado laboral activo"
            else:
                cursor.execute("""update docentes set gradoEstudio = %s, estadoLaboral = %s, correoInstitucional = %s,
                horasFrenteAlGrupo = %s, horasDocencia = %s, horasAdministrativas = %s, tipoContrato = %s
                where idDocente = %s""", (docente.gradoEstudio, docente.estadoLaboral,
                docente.correoInstitucional, docente.horasFrenteAlGrupo, docente.horasDocencia,
                docente.horasAdministrativas, docente.tipoContrato, idDocente))
                self.conexion.commit()
                salida.codigo = 200
                salida.mensaje = "Docente modificado exitosamente"
        except Exception as e:
            self.conexion.rollback()
            salida.codigo = 500
            salida.mensaje = "Error al modificar docente"
        return salida
    
    def cancelarDocente(self, idDocente:int):
        salida = Salida(codigo=0, mensaje="")
        try:
            cursor = self.conexion.cursor()
            cursor.execute("select * from docentes where idDocente = %s", (idDocente,))
            docenteExiste = cursor.fetchone()
            if not docenteExiste:
                salida.codigo = 404
                salida.mensaje = "Docente no encontrado"|
            elif docenteExiste['estadoLaboral'] != 'Activo':
                salida.codigo = 400
                salida.mensaje = "El docente no tiene un estado laboral activo"
            else:
                cursor.execute("""update docentes set estadoLaboral = %s where idDocente = %s """, ('Inactivo', idDocente))
                self.conexion.commit()
                salida.codigo = 200
                salida.mensaje = "Docente cancelado exitosamente"
        except Exception as e:
            self.conexion.rollback()
            salida.codigo = 500
            salida.mensaje = "Error al cancelar docente"
        return salida
    
    def consultarDocentePorId(self, idDocente:int):
        salida = ConsultarDocentePorId(codigo=0, mensaje="", docente=None)
        try:
            cursor = self.conexion.cursor()
            cursor.execute("select * from docentes where idDocente = %s", (idDocente,))
            docenteExiste = cursor.fetchone()
            if not docenteExiste:
                salida.codigo = 404
                salida.mensaje = "Docente no encontrado"
            else:
                salida.codigo = 200
                salida.mensaje = "Docente encontrado"
                salida.docente = docenteExiste
        except Exception as e:
            salida.codigo = 500
            salida.mensaje = "Error al consultar docente"
        return salida 

#CARRERA
class CarreraDAO:
    def __init__(self, conexion):
        self.conexion = conexion
    
    def crearCarrera(self, carrera:CrearCarrera):
        salida = Salida(codigo=0, mensaje="")
        try:
            cursor = self.conexion.cursor()
            cursor.execute("select * from carreras where nombreCarrera = %s", (carrera.nombreCarrera,))
            carreraExiste = cursor.fetchone()
            if carreraExiste:
                salida.codigo = 400
                salida.mensaje = "La carrera ya existe"
            else:
                cursor.execute("""insert into carreras (nombreCarrera, descripcion) values (%s, %s)""", (carrera.nombreCarrera, carrera.descripcion))
                self.conexion.commit()
                salida.codigo = 201
                salida.mensaje = "Carrera creada exitosamente"
        except Exception as e:
            self.conexion.rollback()
            salida.codigo = 500
            salida.mensaje = "Error al crear carrera"
        return salida

    def modificarCarrera(self, idCarrera:int, carrera:ModificarCarrera):
        salida = Salida(codigo=0, mensaje="")
        try:
            cursor = self.conexion.cursor()
            cursor.execute("select * from carreras where idCarrera = %s", (idCarrera,))
            carreraExiste = cursor.fetchone()
            if not carreraExiste:
                salida.codigo = 404
                salida.mensaje = "Carrera no encontrada"
            else:
                cursor.execute("""update carreras set nombreCarrera = %s, descripcion = %s where idCarrera = %s""", (carrera.nombreCarrera, carrera.descripcion, idCarrera))
                self.conexion.commit()
                salida.codigo = 200
                salida.mensaje = "Carrera modificada exitosamente"
        except Exception as e:
            self.conexion.rollback()
            salida.codigo = 500
            salida.mensaje = "Error al modificar carrera"
        return salida

    def cancelarCarrera(self, idCarrera:int):
        salida = Salida(codigo=0, mensaje="")
        try:
            cursor = self.conexion.cursor()
            cursor.execute("select * from carreras where idCarrera = %s", (idCarrera,))
            carreraExiste = cursor.fetchone()
            if not carreraExiste:
                salida.codigo = 404
                salida.mensaje = "Carrera no encontrada"
            else:
                cursor.execute("SELECT COUNT(*) as total FROM docentes WHERE idCarrera = %s AND estadoLaboral = 'Activo'", (idCarrera,))
                docentesAsignados = cursor.fetchone()

                if docentesAsignados and docentesAsignados['total'] > 0:
                    salida.codigo = 400
                    salida.mensaje = "No se puede cancelar la carrera porque tiene docentes activos asignados"
                else:
                    cursor.execute("update carreras set activo = 0 where idCarrera = %s", (idCarrera,))
                    self.conexion.commit()
                    salida.codigo = 200
                    salida.mensaje = "Carrera cancelada exitosamente"
        except Exception as e:
            self.conexion.rollback()
            salida.codigo = 500
            salida.mensaje = "Error al cancelar carrera"
        return salida

    def consultarCarreraPorId(self, idCarrera:int):
        salida = ConsultarCarreraPorId(codigo=0, mensaje="", carrera=None)
        try:
            cursor = self.conexion.cursor()
            cursor.execute("select * from carreras where idCarrera = %s", (idCarrera,))
            carreraExiste = cursor.fetchone()
            if not carreraExiste:
                salida.codigo = 404
                salida.mensaje = "Carrera no encontrada"
            else:
                salida.codigo = 200
                salida.mensaje = "Carrera encontrada"
                salida.carrera = carreraExiste
        except Exception as e:
            salida.codigo = 500
            salida.mensaje = "Error al consultar carrera"
        return salida
