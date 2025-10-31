#!/usr/bin/env python3
"""
Script para generar reportes de ejecución del pipeline.
"""
import json
import glob
import os
from datetime import datetime

def generate_execution_report():
    """
    Genera un reporte consolidado de las ejecuciones del pipeline.
    """
    print("Generando reporte de ejecución...")
    
    # Buscar todos los reportes de ejecución
    report_files = glob.glob('data/outputs/report_*.json')
    
    if not report_files:
        print(" No se encontraron reportes de ejecución")
        return
    
    # Consolidar reportes
    execution_reports = []
    for report_file in report_files:
        with open(report_file, 'r') as f:
            report_data = json.load(f)
            execution_reports.append(report_data)
    
    # Generar reporte consolidado
    consolidated_report = {
        'generated_at': datetime.now().isoformat(),
        'total_executions': len(execution_reports),
        'successful_executions': len([r for r in execution_reports if r.get('status') == 'completed_successfully']),
        'failed_executions': len([r for r in execution_reports if r.get('status') != 'completed_successfully']),
        'total_records_processed': sum(r.get('records_processed', 0) for r in execution_reports),
        'executions': execution_reports
    }
    
    # Guardar reporte consolidado
    report_filename = f"data/outputs/consolidated_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_filename, 'w') as f:
        json.dump(consolidated_report, f, indent=2)
    
    print(" Reporte de ejecución generado:")
    print(f"   - Archivo: {report_filename}")
    print(f"   - Total de ejecuciones: {consolidated_report['total_executions']}")
    print(f"   - Ejecuciones exitosas: {consolidated_report['successful_executions']}")
    print(f"   - Registros procesados: {consolidated_report['total_records_processed']}")

if __name__ == "__main__":
    generate_execution_report()