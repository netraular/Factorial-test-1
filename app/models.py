from pydantic import BaseModel, EmailStr

class NewLead(BaseModel):
    """Modelo para el JSON de entrada (simulando un webhook de HubSpot)."""
    contact_id: str
    email: EmailStr
    country: str

class EnrichedData(BaseModel):
    """Modelo para los datos que devolvería el servicio de enriquecimiento."""
    company_name: str
    company_size: int

class ProcessedLead(NewLead, EnrichedData):
    """
    Modelo final del lead procesado.
    Hereda los campos de NewLead y EnrichedData y añade el owner_id.
    """
    owner_id: str