### **1. El Problema a Resolver: El Caos de Empresas Clonadas**

El problema central es la existencia de múltiples registros para una misma entidad de empresa en nuestro CRM. Estos "clones" o duplicados se manifiestan de formas perjudiciales para el negocio, impidiendo una gestión eficiente y una visión clara de nuestros clientes.

**Manifestaciones del Problema:**

*   **Nombres y Dominios Similares:** Registros como "Acme Inc.", "Acme", "acme.com" y "acme.io" coexisten para la misma compañía.
*   **Registros Asociados Fragmentados:** Un clon tiene los contactos clave, mientras que otro contiene los negocios (deals) importantes.
*   **Propiedades Inconsistentes:** Un registro indica que la industria es "Software" y otro "Tecnología"; el ciclo de vida o la región pueden ser diferentes.
*   **Historial de Actividad Disperso:** Las actividades (llamadas, emails, reuniones) y el scoring de leads están repartidos, impidiendo una visión real del engagement del cliente.

**Consecuencias Directas:**

*   **Visión Incompleta:** Es imposible entender la relación completa y el valor real de un cliente.
*   **Ineficiencia Operativa:** Los equipos de Ventas y Marketing contactan al mismo cliente sin contexto, duplicando esfuerzos y creando una mala experiencia.
*   **Analítica y Reporting Deficiente:** Métricas clave incorrectas y poco fiables.
*   **Pérdida de Oportunidades:** Un comercial puede descartar un lead sin saber que otro registro de la misma empresa tiene un negocio de alto valor a punto de cerrarse.

---

### **2. Técnicas Fundamentales de Implementación**

#### **A. Sanitización y Normalización de Entradas (Inputs)**
La comparación de datos solo es fiable si los datos están limpios y en un formato estándar. 

*   **Lógica:** Crear una función o proceso que transforme los datos crudos en un formato consistente.
*   **Ejemplos de Implementación:**
    *   **Nombres de Empresa:** Convertir a minúsculas, eliminar caracteres especiales (`.`, `,`, `-`) y remover términos genéricos como `Inc.`, `Ltd.`, `LLC`, `S.L.`.
    *   **Dominios Web:** Extraer el dominio raíz sin el TLD (Top-Level Domain) y sin subdominios.

#### **B. Lógica de Coincidencia y Puntuación (Matching & Scoring)**
Los duplicados pueden no ser idénticos. Por ello, se necesita un sistema que mida la "probabilidad" de que dos registros sean la misma entidad.
*   **Lógica:** Asignar una puntuación de similitud basada en la coincidencia de diferentes campos, dando más peso a los identificadores más fiables.
*   **Ejemplos de Implementación:**
    *   **Coincidencia Fuerte:** Si el **dominio raíz normalizado** es idéntico, se asigna una puntuación muy alta (ej. 95 puntos).
    *   **Coincidencia Débil:** Para los nombres, se utilizan algoritmos de similitud de cadenas de texto.

#### **C. Reglas de Fusión y Selección de los Datos Finales**
Una vez identificado un grupo de duplicados, se necesita una lógica clara para unificarlos en un único registro maestro.
*   **Lógica:** Definir un conjunto de reglas jerárquicas para decidir qué registro sobrevive y qué datos se conservan.
*   **Ejemplos de Implementación:**
    *   **Selección del Maestro:** 1) El registro con el negocio ganado de mayor valor, 2) El registro con la actividad más reciente, 3) El registro creado más antiguo.
    *   **Fusión de Propiedades:** `El Más Reciente Gana`, `Rellenar Vacíos`, `Concatenar`.

---

### **3. Soluciones Implementables**

A continuación se presentan las soluciones completas, que combinan las técnicas anteriores.

#### **Solución 1: Limpieza Masiva Inicial por Lotes**
Ideal para realizar una limpieza profunda inicial de toda la base de datos existente.

*   **Diagrama de Flujo:**
    ```mermaid
    graph TD
        subgraph "Fase 1 - Detección Automática"
            A["Inicio: Tarea Programada<br>(Ej. cada noche)"] --> B{"Extraer todas las empresas vía API"};
            B --> C["Sanitizar y Normalizar Datos<br>(Nombres y Dominios)"];
            C --> D{"Agrupar por Dominio Raíz Normalizado"};
            D --> E{"Para cada grupo con >1 empresa...<br>Aplicar Lógica de Puntuación (Scoring)<br>"};
            E --> F{"¿Puntuación > Umbral de Confianza?<br>(Ej. 90%)"};
        end
    
        subgraph "Fase 2 - Fusión Automática"
            F -- Sí --> G["Seleccionar Variables Finales<br>(Basado en reglas: más actividad, etc.)"];
            G --> H["Fusionar Propiedades Conflictivas<br>(Reglas: más reciente gana, rellenar vacíos)"];
            H --> I["Migrar todos los Objetos Asociados<br>(Contactos, Negocios, Tickets)"];
            I --> J["Archivar/Eliminar Registros Clonados"];
            J --> K["Registrar Fusión en Log de Auditoría"];
            K --> L["Fin del Proceso"];
        end
    
        F -- No --> L;
    ```

#### **Solución 2: Interfaz de Revisión Humana Asistida (El Modelo Híbrido)**
La solución más segura, ya que permite validación humana.

*   **Diagrama de Flujo:**
    ```mermaid
    graph TD
        subgraph "Detección y Clasificación (Automático)"
            A["Inicio: Tarea Programada"] --> B{"Extraer y Sanitizar Datos de Empresas"};
            B --> C{"Agrupar y Calcular Puntuación de Similitud"};
            C --> D{"Clasificar según Umbral"};
        end
    
        subgraph "Triage y Acción"
            D -- "Puntuación > 95% (Confianza Muy Alta)" --> E_AUTO["Fusión Automática<br>(Mismo proceso que Solución 1)"];
            
            D -- "75% < Puntuación <= 95% (Confianza Media)" --> F_MANUAL{"Añadir a la 'Cola de Revisión Humana'"};
            F_MANUAL --> G["Guardián de Datos Revisa el Grupo en la UI"];
            G --> H{"¿Aprobar Fusión?"};
            H -- Sí --> I["Ejecutar Fusión Asistida<br>(El sistema realiza la fusión)"];
            H -- No --> J["Marcar como 'No es un Duplicado'<br>(Excluir de futuras revisiones)"];
            
            D -- "Puntuación <= 75% (Confianza Baja)" --> K_IGNORE["Ignorar"];
        end
    
        E_AUTO --> L["Fin"];
        I --> L;
        J --> L;
        K_IGNORE --> L;
    ```

#### **Solución 3: Prevención Proactiva en el Formulario de Creación**
La solución más estratégica, ya que ataca el problema en su origen.

*   **Diagrama de Flujo:**
    ```mermaid
    graph TD
        subgraph "Interfaz de Usuario (Frontend)"
            A["Usuario empieza a escribir en el<br>formulario 'Crear Empresa'"] --> B{"Input de Nombre/Dominio se modifica"};
            B --> C["El script sanitiza la entrada<br>del usuario (en tiempo real)"];
            C --> D_API_CALL["Llamada asíncrona a la API del CRM<br>con el dato sanitizado"];
            D_API_CALL --> E{"Esperando respuesta..."};
            F_BACKEND_RESPONSE --> G{"¿Se encontraron duplicados probables?"};
            G -- Sí --> H["Mostrar Alerta en la UI<br>'Posible duplicado encontrado...'"];
            H --> I{"¿Usuario selecciona un registro existente?"};
            I -- Sí --> J["Redirigir a la página<br>de la empresa existente"];
            I -- No (Usuario hace clic en 'Crear de todos modos') --> K["Permitir guardar el nuevo registro"];
            G -- No --> K;
            J --> L["Fin del Proceso"];
            K --> L;
        end
        
        subgraph "CRM (Backend)"
            D_API_CALL --> E_BACKEND_SEARCH["Recibe la llamada y busca coincidencias<br>"];
            E_BACKEND_SEARCH --> F_BACKEND_RESPONSE["Devuelve una lista de posibles duplicados<br>(o lista vacía)"];
        end
    ```

---

### **4. Estrategias Complementarias de Soporte**

#### **A. Estandarización de Datos**
*   **Implementación:** Definir y aplicar reglas estrictas sobre la entrada de datos: usar listas desplegables para "Industria" o "País", hacer obligatorio el campo de dominio web y formar a los usuarios en las guías de estilo para nombrar empresas.

#### **B. Enriquecimiento de Datos con Fuentes Externas**
*   **Implementación:** Integrar el CRM con APIs de enriquecimiento. Cuando se crea una empresa, la API puede rellenar automáticamente datos estandarizados y verificados, previniendo conflictos y mejorando la calidad general.