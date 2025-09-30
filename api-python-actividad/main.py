from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define los orígenes que pueden hacer peticiones a tu API
origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Repositorio de datos: lista de diccionarios en memoria
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1200},
    {"id": 2, "nombre": "Mouse", "precio": 25},
    {"id": 3, "nombre": "Teclado", "precio": 75}
]

# --- Endpoints de la API ---

# GET: Obtiene todos los productos
@app.get("/productos")
def get_productos():
    return productos

# POST: Crea un nuevo producto
@app.post("/productos")
def create_producto(producto: dict):
    productos.append(producto)
    return {"message": "Producto creado con éxito", "data": producto}

# PUT: Actualiza un producto por ID
@app.put("/productos/{id}")
def update_producto(id: int, producto_actualizado: dict):
    for index, producto in enumerate(productos):
        if producto["id"] == id:
            productos[index].update(producto_actualizado)
            return {"message": "Producto actualizado con éxito", "data": productos[index]}
    raise HTTPException(status_code=404, detail="Producto no encontrado")

# DELETE: Elimina un producto por ID
@app.delete("/productos/{id}")
def delete_producto(id: int):
    for index, producto in enumerate(productos):
        if producto["id"] == id:
            eliminado = productos.pop(index)
            return {"message": "Producto eliminado con éxito", "data": eliminado}
    raise HTTPException(status_code=404, detail="Producto no encontrado")
