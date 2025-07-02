from fastapi import FastAPI, HTTPException
from . import services, storage
from .models import NewLead, ProcessedLead

app = FastAPI()

@app.post("/process-lead", response_model=ProcessedLead, status_code=200)
async def process_new_lead(lead_input: NewLead):
    try:
        enriched_data = await services.enrich_lead_data(lead_input.email)
    except Exception as e:
        raise HTTPException(status_code=503, detail="Enrichment service failed")

    owner_id = services.get_lead_owner(
        country=lead_input.country,
        company_size=enriched_data.company_size
    )

    processed_lead = ProcessedLead(
        **lead_input.model_dump(),
        **enriched_data.model_dump(),
        owner_id=owner_id
    )

    storage.save_to_local_json(processed_lead)
    return processed_lead

@app.get("/")
def read_root():
    return {"status": "ok"}