**Lead Routing & Enrichment Flow - Versión Simplificada**

Este proyecto implementa un flujo automatizado para procesar leads usando FastAPI.

**Cómo funciona:**
- Endpoint POST /process-lead recibe un lead como JSON
- Valida automáticamente los campos requeridos (contact_id, email, country) usando modelos Pydantic
- Enriquece los datos del lead simulando una llamada a API externa (como Clearbit)
- Asigna un propietario (owner_id) basado en país y tamaño de empresa e intención (ej. si pidió una demo) usando reglas configurables
- Guarda el resultado en /data como archivo JSON
- Devuelve el lead procesado con todos los datos combinados

**Estructura:**
- main.py: Endpoint principal y orquestación del flujo
- models.py: Define los formatos de datos para entrada, enriquecimiento y salida
- services.py: Lógica de enriquecimiento y ruteo
- storage.py: Almacenamiento en archivos JSON

**Cómo probarlo:**
1. Instalar dependencias: pip install -r requirements.txt
2. Ejecutar servidor: uvicorn app.main:app --reload
3. Acceder a http://127.0.0.1:8000/docs
4. Probar el endpoint POST /process-lead con un JSON como:
```
  {
    "contact_id": "123",
    "email": "test@bigcorp.com",
    "country": "USA",
    "intent_signal": "demo_request"
  }
```
5. Tambiuén se puede obtener un lead estándar sin intención específica:
```
  {
    "contact_id": "456",
    "email": "contact@startup.es",
    "country": "Spain"
  }
```
   
**Requisitos técnicos:**
- Python
- FastAPI para la API web
- Pydantic para modelos de datos
- Uvicorn como servidor
