from fastapi import FastAPI
from fastapi.responses import JSONResponse
from . import services, storage

app = FastAPI()

@app.get("/run-flow")
async def run_processing_flow():
    # Datos de prueba fijos
    test_lead_data = {
        "contact_id": "test-contact-001",
        "email": "name@bigcorp.com",
        "country": "USA"
    }

    # Enriquecer datos del lead
    enriched_data = await services.enrich_lead_data(email=test_lead_data["email"])
    
    # Asignar propietario
    owner_id = services.get_lead_owner(
        country=test_lead_data["country"],
        company_size=enriched_data["company_size"]
    )

    # Combinar resultados
    processed_lead = {**test_lead_data, **enriched_data, "owner_id": owner_id}

    # Guardar localmente
    storage.save_to_local_json(processed_lead)

    return JSONResponse(content=processed_lead)