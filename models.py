from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date


#DOCENTE
class CrearDocente(BaseModel):
    idUsuario:int
    gradoEstudio:str
    fechaIngreso:date
    estadoLaboral:str
    correoInstitucional:EmailStr
    horasFrenteAlGrupo:int
    horasDocencia:int
    horasAdministrativas:int
    tipoContrato:str

class ModificarDocente(BaseModel):
    gradoEstudio:Optional[str]=None
    estadoLaboral:Optional[str]=None
    correoInstitucional:Optional[EmailStr]=None
    horasFrenteAlGrupo:Optional[int]=None
    horasDocencia:Optional[int]=None
    horasAdministrativas:Optional[int]=None
    tipoContrato:Optional[str]=None

class Docente(BaseModel):
    idDocente:int
    idUsuario:int
    gradoEstudio:str
    fechaIngreso:date
    estadoLaboral:str
    correoInstitucional:EmailStr
    horasFrenteAlGrupo:int
    horasDocencia:int
    horasAdministrativas:int
    tipoContrato:str

class ConsultarDocentePorId(BaseModel):
    codigo:int
    mensaje:str
    docente:Optional[Docente]=None

#ASIGNATURA
class CrearAsignatura(BaseModel):
    nombre:str
    clave:str
    creditos:int

class ModificarAsignatura(BaseModel):
    nombre:Optional[str]=None
    clave:Optional[str]=None
    creditos:Optional[int]=None

class Asignatura(BaseModel):
    idAsignatura:int
    nombre:str
    clave:str
    creditos:int

class ConsultarAsignaturaPorId(BaseModel):
    codigo:int
    mensaje:str
    asignatura:Optional[Asignatura]=None

#CARRERA
class CrearCarrera(BaseModel):
    nombreCarrera:str
    descripcion:str

class ModificarCarrera(BaseModel):
    nombreCarrera:Optional[str]=None
    descripcion:Optional[str]=None

class Carrera(BaseModel):
    idCarrera:int
    nombreCarrera:str
    descripcion:str

class ConsultarCarreraPorId(BaseModel):
    codigo:int
    mensaje:str
    carrera:Optional[Carrera]=None
    