# Dependencias del Pipeline - Lab 08

## Justificación del Diagrama y Dependencias

Basado en el diagrama de arquitectura del pipeline, se han establecido las siguientes dependencias que garantizan el flujo correcto de datos y el cumplimiento de las prácticas de DataOps.

## Dependencias Funcionales del Pipeline

### **Fuentes de Datos → Validación**
- **API de Ventas**: Requiere conexión activa y autenticación válida
- **Archivos CSV**: Requiere archivos en ruta especificada con formato correcto
- **Base de Datos**: Requiere conexión estable y credenciales válidas

### **Validación → Transformación**
- **Dependencia**: Validación exitosa de todos los datos de entrada
- **Requisitos**:
  - Esquema versionado en `data/schemas/sales_schema_v1.json`
  - 100% de los registros pasan las validaciones de esquema
  - Datos cumplen con los tipos y formatos esperados
- **Justificación**: No se deben procesar datos inválidos que puedan corromper el pipeline

### **Transformación → Enriquecimiento**
- **Dependencia**: Transformación completada exitosamente
- **Requisitos**:
  - Datos limpios de duplicados y valores nulos manejados
  - Cálculos de totales y métricas realizados correctamente
  - Estructura de datos estandarizada y normalizada
- **Justificación**: El enriquecimiento requiere datos estructurados consistentes

### **Enriquecimiento → Validación Final de Calidad**
- **Dependencia**: Enriquecimiento aplicado completamente
- **Requisitos**:
  - Catálogo de productos actualizado en `data/reference/product_catalog.csv`
  - Tablas de lookup de regiones y categorías disponibles
  - Todos los joins y enriquecimientos aplicados correctamente
- **Justificación**: La validación de calidad debe evaluar los datos ya enriquecidos

### **Validación Final → Destinos**
- **Dependencia**: Validación de calidad aprobada
- **Requisitos**:
  - Completitud ≥ 95% (umbral configurable)
  - Frescura ≤ 24 horas (umbral configurable) 
  - Variación en conteo de registros ≤ 10% (umbral configurable)
  - Cero errores críticos de calidad
- **Justificación**: Solo datos de alta calidad deben cargarse a los destinos finales

## Dependencias Técnicas y de Infraestructura

### **Infraestructura**
- **Python 3.8+**: Versiones compatibles con las librerías utilizadas
- **Memoria RAM**: Suficiente para procesar los volúmenes de datos esperados
- **Almacenamiento**: Espacio en disco para datos temporales y resultados
- **Conectividad**: Acceso a todas las fuentes y destinos de datos

### **Dependencias de Software**
```yaml
dependencies:
  core:
    - pandas>=1.5.0
    - pyyaml>=6.0
    - requests>=2.28.0
  testing:
    - pytest>=7.0.0
    - pytest-mock>=3.10.0
  database:
    - sqlalchemy>=1.4.0
  utilities:
    - python-dotenv>=0.19.0