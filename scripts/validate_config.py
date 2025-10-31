#!/usr/bin/env python3
"""
Script para validar la configuración del pipeline.
"""
import yaml
import os
import sys

def validate_config():
    """
    Valida la configuración del pipeline.
    
    Returns:
        bool: True si la configuración es válida, False en caso contrario
    """
    config_path = 'config/pipeline_config.yaml'
    
    print(" Validando configuración del pipeline...")
    
    # Verificar que el archivo existe
    if not os.path.exists(config_path):
        print(f" Archivo de configuración no encontrado: {config_path}")
        return False
    
    try:
        # Cargar y validar YAML
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        # Validaciones básicas
        required_sections = ['version', 'pipeline', 'validation', 'processing', 'enrichment', 'quality']
        
        for section in required_sections:
            if section not in config:
                print(f" Sección requerida faltante: {section}")
                return False
        
        # Validaciones específicas
        if 'name' not in config['pipeline']:
            print(" Nombre del pipeline no definido")
            return False
            
        if 'schema_path' not in config['validation']:
            print(" Ruta de esquema no definida en validación")
            return False
            
        if 'output_path' not in config['processing']:
            print(" Ruta de salida no definida en procesamiento")
            return False
            
        if 'catalog_path' not in config['enrichment']:
            print(" Ruta de catálogo no definida en enriquecimiento")
            return False
            
        if 'checks' not in config['quality']:
            print(" Chequeos de calidad no definidos")
            return False
        
        print(" Configuración válida:")
        print(f"   - Versión: {config['version']}")
        print(f"   - Pipeline: {config['pipeline']['name']}")
        print(f"   - Validación: {len(config['validation'].get('required_files', []))} archivos requeridos")
        print(f"   - Procesamiento: {len(config['processing'].get('steps', []))} pasos definidos")
        print(f"   - Calidad: {len(config['quality'].get('checks', []))} chequeos configurados")
        
        return True
        
    except yaml.YAMLError as e:
        print(f" Error en formato YAML: {e}")
        return False
    except Exception as e:
        print(f" Error inesperado: {e}")
        return False

if __name__ == "__main__":
    success = validate_config()
    sys.exit(0 if success else 1)