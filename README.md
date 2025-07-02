**Lead Routing & Enrichment Flow - Versión Simplificada**

Este proyecto implementa un flujo automatizado para procesar leads usando FastAPI. Es una versión que funciona con diccionarios.

**Cómo funciona:**
- Endpoint POST /process-lead recibe un lead como JSON
- Valida manualmente los campos requeridos (contact_id, email, country)
- Enriquece los datos del lead usando el email
- Asigna un propietario basado en país y tamaño de empresa
- Guarda el resultado en /data como archivo JSON
- Devuelve el lead procesado

**Estructura:**
- main.py: Endpoint principal y validación manual
- services.py: Lógica de enriquecimiento y ruteo
- storage.py: Almacenamiento en archivos JSON


**Cómo probarlo:**
1. Instalar dependencias: pip install -r requirements.txt
2. Ejecutar servidor: uvicorn app.main:app --reload
3. Acceder a http://127.0.0.1:8000/docs
4. Probar el endpoint POST /process-lead con un JSON válido:
   {
     "contact_id": "123",
     "email": "test@bigcorp.com",
     "country": "USA"
   }