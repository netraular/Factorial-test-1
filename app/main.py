# app/main.py

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field
from . import services, storage

# 1. Definimos el modelo de entrada con Pydantic
class LeadInput(BaseModel):
    contact_id: str
    email: EmailStr
    country: str

    # 2. Añadimos un ejemplo para la documentación de la API
    class Config:
        json_schema_extra = {
            "example": {
                "contact_id": "123",
                "email": "test@bigcorp.com",
                "country": "USA"
            }
        }


app = FastAPI()

# 3. Actualizamos la firma del endpoint para usar nuestro modelo
@app.post("/process-lead", status_code=200)
async def process_new_lead(lead_input: LeadInput):

    # Enriquecer datos
    try:
        enriched_data = await services.enrich_lead_data(email=lead_input.email)
    except Exception as e:
        raise HTTPException(status_code=503, detail="Enrichment service failed.")

    # Asignar owner
    owner_id = services.get_lead_owner(
        country=lead_input.country,
        company_size=enriched_data["company_size"]
    )

    # Combinar datos y guardar
    processed_lead = {**lead_input.model_dump(), **enriched_data, "owner_id": owner_id}
    storage.save_to_local_json(processed_lead)

    return JSONResponse(content=processed_lead)