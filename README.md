Lead Routing & Enrichment Flow

Cómo Funciona:  
- La aplicación tiene un endpoint: GET /run-flow  
- Usa datos de prueba fijos para simular un lead  
- Simula llamar a una API externa para enriquecer los datos (obtener tamaño de empresa)  
- Asigna un propietario al lead basado en reglas simples (país y tamaño de empresa)  
- Guarda el resultado en un archivo JSON en la carpeta /data  
- Devuelve el resultado como respuesta  

Estructura:  
- main.py: Servidor web y endpoint  
- services.py: Lógica de negocio (enriquecimiento y ruteo)  
- storage.py: Guardado de datos  

Cómo probarlo:  
1. Instalar dependencias: pip install -r requirements.txt  
2. Ejecutar servidor: uvicorn app.main:app --reload  
3. Acceder a http://127.0.0.1:8000/docs  
4. Probar el endpoint GET /run-flow desde la interfaz  
5. Verás la respuesta JSON y se creará un archivo en /data  