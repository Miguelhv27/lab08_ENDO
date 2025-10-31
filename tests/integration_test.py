#!/usr/bin/env python3
"""
Test de integración para el pipeline completo.
"""
import sys
import os

# Añadir el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.orchestrator import PipelineOrchestrator
from src.data_validation import DataValidator
from src.data_processing import DataProcessor
from src.data_enrichment import DataEnricher
from src.quality_checks import QualityChecker

def test_integration():
    """Test de integración de todos los componentes"""
    print(" Ejecutando test de integración...")
    
    try:
        # 1. Inicializar orquestador
        print("1. Inicializando orquestador...")
        orchestrator = PipelineOrchestrator('config/pipeline_config.yaml')
        assert orchestrator.config is not None
        print("    Orquestador inicializado")
        
        # 2. Probar validación
        print("2. Probando módulo de validación...")
        validator = DataValidator(orchestrator.config['validation'])
        validation_result = validator.validate()
        assert isinstance(validation_result, dict)
        print("    Módulo de validación funcionando")
        
        # 3. Probar procesamiento
        print("3. Probando módulo de procesamiento...")
        processor = DataProcessor(orchestrator.config['processing'])
        processing_result = processor.process()
        assert 'processed_data' in processing_result
        assert 'record_count' in processing_result
        print("    Módulo de procesamiento funcionando")
        
        # 4. Probar enriquecimiento
        print("4. Probando módulo de enriquecimiento...")
        enricher = DataEnricher(orchestrator.config['enrichment'])
        sample_data = [{'id': 1, 'producto': 'Test', 'venta': 100}]
        enrichment_result = enricher.enrich(sample_data)
        assert 'enriched_data' in enrichment_result
        print("    Módulo de enriquecimiento funcionando")
        
        # 5. Probar calidad
        print("5. Probando módulo de calidad...")
        quality_checker = QualityChecker(orchestrator.config['quality'])
        quality_result = quality_checker.check_quality(sample_data)
        assert 'passed' in quality_result
        print("    Módulo de calidad funcionando")
        
        # 6. Probar ejecución completa 
        print("6. Probando configuración de ejecución...")

        assert hasattr(orchestrator, 'execute_pipeline')
        assert callable(getattr(orchestrator, 'execute_pipeline'))
        print("    Configuración de ejecución correcta")
        
        print("\n ¡Todos los tests de integración pasaron!")
        
    except Exception as e:
        print(f"\n Error en test de integración: {e}")
        raise

if __name__ == "__main__":
    test_integration()