import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import httpx


load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Allowed origins
    allow_credentials=True,          # Support cookies/auth headers
    allow_methods=["*"],             # Allow all standard HTTP methods
    allow_headers=["*"],             # Allow all HTTP headers
)

@app.get("/clima")
async def clima(ciudad: str):
    data = {
        "q": ciudad,
        "appid": api_key,
        "units": "metric",
        "lang": "es"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.openweathermap.org/data/2.5/weather", params=data)
        datos_clima = response.json()
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Ciudad no encontrada")
        else:
            datos_filtrados = {
                "ciudad": datos_clima["name"],
                "temperatura": datos_clima["main"]["temp"],
                "descripcion": datos_clima["weather"][0]["description"],
                "icono": datos_clima["weather"][0]["icon"]
            }
            return datos_filtrados