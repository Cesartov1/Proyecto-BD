# pyrefly: ignore [missing-import]
from fastapi import FastAPI, Request
from models import CrearUsuario, ModificarUsuario, ConsultarUsuarioPorId, Salida, Usuario
from dao import UsuarioDAO
# pyrefly: ignore [missing-import]
import uvicorn
app=FastAPI()

#DOCENTE

@app.post("/docentes", response_model=Salida)
async def crearDocente(request:Request, docente:CrearDocente):
    conexion = request.app.state.conexion
    docente_dao = DocenteDAO(conexion)
    salida = docente_dao.crearDocente(docente)
    return salida

@app.put("/docentes/{idDocente}",response_model=Salida)
async def modificarDocente(request:Request, idDocente:int, docente:ModificarDocente):
    conexion = request.app.state.conexion
    docente_dao = DocenteDAO(conexion)
    salida = docente_dao.modificarDocente(idDocente, docente)
    return salida

@app.delete("/docentes/{idDocente}",response_model=Salida)
async def cancelarDocente(request:Request, idDocente:int):
    conexion = request.app.state.conexion
    docente_dao = DocenteDAO(conexion)
    salida = docente_dao.cancelarDocente(idDocente)
    return salida

@app.get("/docentes/{idDocente}",response_model=ConsultarDocentePorId)
async def consultarDocentePorId(request:Request, idDocente:int):
    conexion = request.app.state.conexion
    docente_dao = DocenteDAO(conexion)
    salida = docente_dao.consultarDocentePorId(idDocente)
    return salida

#CARRERA
@app.post("/carreras", response_model=Salida)
async def crearCarrera(request:Request, carrera:CrearCarrera):
    conexion = request.app.state.conexion
    carrera_dao = CarreraDAO(conexion)
    salida = carrera_dao.crearCarrera(carrera)
    return salida

@app.put("/carreras/{idCarrera}",response_model=Salida)
async def modificarCarrera(request:Request, idCarrera:int, carrera:ModificarCarrera):
    conexion = request.app.state.conexion
    carrera_dao = CarreraDAO(conexion)
    salida = carrera_dao.modificarCarrera(idCarrera, carrera)
    return salida

@app.delete("/carreras/{idCarrera}",response_model=Salida)
async def cancelarCarrera(request:Request, idCarrera:int):
    conexion = request.app.state.conexion
    carrera_dao = CarreraDAO(conexion)
    salida = carrera_dao.cancelarCarrera(idCarrera)
    return salida

@app.get("/carreras/{idCarrera}",response_model=ConsultarCarreraPorId)
async def consultarCarreraPorId(request:Request, idCarrera:int):
    conexion = request.app.state.conexion
    carrera_dao = CarreraDAO(conexion)
    salida = carrera_dao.consultarCarreraPorId(idCarrera)
    return salida