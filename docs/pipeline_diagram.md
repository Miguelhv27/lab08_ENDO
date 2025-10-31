# Diagrama del Pipeline de Datos - Lab 08

## Objetivo
Diagramar, orquestar y ejecutar pipelines de datos complejos aplicando prácticas de DataOps.

## Arquitectura del Pipeline Completo

```mermaid
flowchart TB
    %% ========== FUENTES DE DATOS ==========
    subgraph FUENTES [Fuentes de Datos]
        direction TB
        API[API de Ventas<br/>REST JSON]
        CSV[Archivos CSV<br/>Ventas históricas]
        DB[Base de Datos<br/>Productos/Clientes]
    end

    %% ========== PROCESAMIENTO PRINCIPAL ==========
    subgraph PROCESOS [Procesamiento de Datos]
        direction TB
        VAL[Validación<br/>Esquema & Calidad]
        TRANS[Transformación<br/>Limpieza & Cálculos]
        ENR[Enriquecimiento<br/>+ Catálogos]
        CAL[Validación Final<br/>Calidad de Datos]
    end

    %% ========== DESTINOS ==========
    subgraph DESTINOS [Destinos Finales]
        direction TB
        DW[Data Warehouse<br/>Tablas analíticas]
        ARCH[Archivos Procesados<br/>Parquet/CSV]
        REP[Reportes<br/>Dashboard & KPIs]
    end

    %% ========== CONTROLES ==========
    subgraph CONTROLES [Sistema de Control]
        direction LR
        MON[Monitoreo]
        LOG[Logging]
        ALT[Alertas]
    end

    %% ========== FLUJO PRINCIPAL ==========
    FUENTES --> PROCESOS
    VAL --> TRANS
    TRANS --> ENR
    ENR --> CAL
    PROCESOS --> DESTINOS

    %% ========== CONEXIONES DE CONTROL ==========
    MON -.-> VAL
    MON -.-> TRANS
    MON -.-> ENR
    MON -.-> CAL
    
    LOG -.-> VAL
    LOG -.-> TRANS
    LOG -.-> ENR
    LOG -.-> CAL
    
    ALT --> MON

    %% ========== ESTILOS ==========
    classDef sources fill:#e3f2fd,stroke:#2196f3,stroke-width:2px
    classDef processing fill:#fff3e0,stroke:#ff9800,stroke-width:2px
    classDef destinations fill:#e8f5e8,stroke:#4caf50,stroke-width:2px
    classDef controls fill:#fce4ec,stroke:#e91e63,stroke-width:2px

    class API,CSV,DB sources
    class VAL,TRANS,ENR,CAL processing
    class DW,ARCH,REP destinations
    class MON,LOG,ALT controls

    