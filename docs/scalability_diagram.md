# Diagrama de Estrategias de Escalabilidad - Pipeline de Datos

## Arquitectura de Escalabilidad Multi-Nivel

```mermaid
flowchart TD
    subgraph NIVEL1 [Nivel 1: Procesamiento Local]
        direction TB
        A1[GitHub Actions<br/>Runner Estándar]
        A2[Pandas & Python<br/>Procesamiento en Memoria]
        A3[Almacenamiento Local<br/>Archivos CSV/JSON]
    end

    subgraph NIVEL2 [Nivel 2: Nube Azure]
        direction TB
        B1[Azure Functions<br/>Serverless]
        B2[Azure Batch<br/>Procesamiento por Lotes]
        B3[Azure Blob Storage<br/>Almacenamiento Escalable]
        B4[Azure Monitor<br/>Seguimiento y Métricas]
    end

    subgraph NIVEL3 [Nivel 3: Procesamiento Distribuido]
        direction TB
        C1[Azure Databricks<br/>Spark Cluster]
        C2[Azure Synapse<br/>Analytics]
        C3[Azure Data Lake<br/>Storage Gen2]
        C4[Azure Kubernetes<br/>Service AKS]
    end

    %% Conexiones entre niveles
    NIVEL1 -->|Escala Horizontal| NIVEL2
    NIVEL2 -->|Escala Masiva| NIVEL3

    %% Especificaciones de volumen
    A1 -.-> V1[< 1 GB]
    B1 -.-> V2[1 GB - 10 GB]  
    C1 -.-> V3[> 10 GB]

    classDef level1 fill:#e8f5e8,stroke:#4caf50,stroke-width:2px
    classDef level2 fill:#e3f2fd,stroke:#2196f3,stroke-width:2px
    classDef level3 fill:#fff3e0,stroke:#ff9800,stroke-width:2px
    classDef volume fill:#fce4ec,stroke:#e91e63,stroke-width:1px

    class A1,A2,A3 level1
    class B1,B2,B3,B4 level2
    class C1,C2,C3,C4 level3
    class V1,V2,V3 volume