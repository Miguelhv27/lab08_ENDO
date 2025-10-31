# Reflexión Final - Laboratorio de Orquestación de Pipelines

## 1. Diseño de Pipelines: ¿Cómo decidió dividir un pipeline en componentes? ¿Qué criterios uso para definir las dependencias?

**División en componentes:**
Dividí el pipeline en componentes basándome en el principio de responsabilidad única y el flujo natural de procesamiento de datos. Los componentes principales son: Fuentes de Datos (API, CSV, Base de Datos), Validación, Transformación, Enriquecimiento, Validación de Calidad y Destinos Finales. Cada componente tiene una función específica y bien definida, lo que permite mantenimiento independiente, pruebas aisladas y escalabilidad selectiva.

**Criterios para dependencias:**
- **Dependencias funcionales**: Un proceso requiere la salida del proceso anterior (Transformación depende de Validación exitosa)
- **Dependencias de recursos**: Componentes requieren recursos externos (Validación necesita esquemas versionados, Enriquecimiento necesita catálogos actualizados)
- **Dependencias de calidad**: Procesos posteriores dependen de que los datos cumplan estándares (Destinos requieren Validación de Calidad aprobada)
- **Dependencias temporales**: Secuencia natural de procesamiento que no puede alterarse

## 2. Orquestación vs Ejecución: ¿Cuál es la diferencia entre orquestar un pipeline y ejecutar sus componentes individualmente?

**Ejecución Individual:**
- Componentes se ejecutan de forma aislada sin coordinación
- Manejo manual de dependencias y secuencia
- No hay visibilidad del estado global del pipeline
- Manejo fragmentado de errores y recuperación
- Monitoreo por componente sin contexto global

**Orquestación:**
- Coordinación automática de todos los componentes
- Manejo automático de dependencias (no ejecuta Transformación si Validación falla)
- Seguimiento del estado global en tiempo real
- Manejo centralizado de errores y estrategias de recuperación consistentes
- Monitoreo unificado con métricas consolidadas
- Escalabilidad coordinada de todos los componentes
- Garantías de consistencia en el flujo de datos

La orquestación transforma componentes individuales en un sistema cohesivo que funciona como una unidad inteligente.

## 3. Manejo de Fallos: ¿Qué estrategias implementaría para:

### Reintentos automáticos:
- **Dependencias externas**: 3 reintentos con backoff exponencial (1s, 5s, 15s) para APIs y conexiones a BD
- **Procesamiento**: 2 reintentos inmediatos para fallos temporales de memoria o timeout
- **Configuración**: 1 reintento después de verificar rutas y permisos de archivos
- **Circuit breaker**: Detener reintentos después de fallos repetitivos para evitar saturación

### Continuación desde el punto de fallo:
- **Checkpoints por etapa**: Cada componente guarda estado al completarse exitosamente
- **Persistencia de datos intermedios**: Almacenamiento temporal con versionado entre etapas
- **Identificación precisa**: El orquestador detecta exactamente qué etapa falló y por qué
- **Recuperación selectiva**: Reinicio desde última etapa exitosa, no desde el inicio
- **Manejo de datos parciales**: Capacidad de procesar solo datos no procesados

### Notificaciones escalonadas:
- **Nivel 1 (Monitoreo)**: Fallos no críticos → Solo logging detallado
- **Nivel 2 (Técnico)**: Fallos en componentes principales → Email equipo técnico + Slack
- **Nivel 3 (Crítico)**: Fallos que detienen pipeline → SMS/Push notifications + Llamadas automáticas
- **Nivel 4 (Negocio)**: Impacto a SLA o pérdida financiera → Notificación ejecutiva + Plan de contingencia

## 4. Monitoreo: ¿Qué métricas monitorearía para evaluar la salud del pipeline?

**Métricas de Rendimiento:**
- Tiempo de ejecución por etapa (para identificar cuellos de botella)
- Throughput (registros procesados por segundo/minuto)
- Latencia end-to-end (desde ingesta hasta disponibilidad en destinos)

**Métricas de Calidad de Datos:**
- Completitud (porcentaje de datos completos vs esperados)
- Freshness (tiempo desde generación hasta disponibilidad)
- Exactitud (porcentaje que pasa validaciones de negocio)
- Consistencia (variación en volúmenes entre ejecuciones)

**Métricas de Confiabilidad:**
- Tasa de éxito (porcentaje de ejecuciones exitosas)
- MTTR (Mean Time To Recovery - tiempo promedio de recuperación)
- Disponibilidad (porcentaje de tiempo operativo)
- Tasa de error por componente

**Métricas de Recursos:**
- Utilización de CPU/memoria por componente
- Uso de almacenamiento temporal y resultados
- Costos por ejecución y costo por registro procesado

## 5. Costos: ¿Cómo optimizaría los costos de ejecución en la nube?

**Optimización Computacional:**
- **Serverless computing**: Azure Functions (pago solo por ejecución)
- **Auto-scaling inteligente**: Escalar solo durante horas pico, reducir en baja demanda
- **Instancias eficientes**: Spot instances para ahorrar hasta 90%, Reserved instances para compromiso a largo plazo
- **Right-sizing**: Seleccionar tamaños de VM apropiados para la carga real

**Optimización de Almacenamiento:**
- **Tiered storage**: Hot para datos frecuentes, Cool/Archive para históricos con ahorros de 30-80%
- **Lifecycle policies**: Movimiento automático entre tiers basado en antigüedad y acceso
- **Compresión eficiente**: Formatos columnares (Parquet) y deduplicación de datos redundantes

**Optimización de Procesamiento:**
- **Procesamiento incremental**: Solo procesar datos nuevos/cambiantes, no datasets completos
- **Filtrado temprano**: Eliminar datos innecesarios lo antes posible en el pipeline
- **Particionamiento optimizado**: Por fecha, región o claves de negocio para consultas eficientes

**Estrategias de Governance:**
- **Monitoreo de costos**: Alertas cuando se exceden umbrales, dashboards en tiempo real
- **Chargeback/Showback**: Asignación precisa de costos a departamentos/proyectos
- **Reservas y compromisos**: Reserved Instances y Savings Plans para descuentos sustanciales
- **Modelo híbrido**: Combinar cloud con procesamiento local para cargas predecibles