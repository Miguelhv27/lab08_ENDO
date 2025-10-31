#!/usr/bin/env python3
"""
Script para descargar datos de muestra para el pipeline.
"""
import os
import pandas as pd

def download_sample_data():
    """
    Crea datos de muestra para pruebas del pipeline.
    """
    print("Generando datos de muestra...")
    
    # Crear directorios necesarios
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/reference', exist_ok=True)
    
    # Datos de ventas de muestra
    sales_data = [
        {'id': 1, 'producto': 'Laptop', 'venta': 1500, 'region': 'Norte', 'fecha': '2025-01-30'},
        {'id': 2, 'producto': 'Mouse', 'venta': 50, 'region': 'Sur', 'fecha': '2025-01-30'},
        {'id': 3, 'producto': 'Teclado', 'venta': 80, 'region': 'Este', 'fecha': '2025-01-30'},
        {'id': 4, 'producto': 'Monitor', 'venta': 300, 'region': 'Oeste', 'fecha': '2025-01-30'},
        {'id': 5, 'producto': 'Impresora', 'venta': 200, 'region': 'Norte', 'fecha': '2025-01-30'}
    ]
    
    # Catálogo de productos de muestra
    product_catalog = [
        {'producto': 'Laptop', 'categoria': 'Tecnología', 'precio_base': 1200},
        {'producto': 'Mouse', 'categoria': 'Tecnología', 'precio_base': 40},
        {'producto': 'Teclado', 'categoria': 'Tecnología', 'precio_base': 70},
        {'producto': 'Monitor', 'categoria': 'Tecnología', 'precio_base': 250},
        {'producto': 'Impresora', 'categoria': 'Oficina', 'precio_base': 180}
    ]
    
    # Guardar datos como CSV
    sales_df = pd.DataFrame(sales_data)
    catalog_df = pd.DataFrame(product_catalog)
    
    sales_df.to_csv('data/raw/sales_data.csv', index=False)
    catalog_df.to_csv('data/reference/product_catalog.csv', index=False)
    
    print(" Datos de muestra generados:")
    print(f"   - Ventas: {len(sales_data)} registros en data/raw/sales_data.csv")
    print(f"   - Catálogo: {len(product_catalog)} productos en data/reference/product_catalog.csv")

if __name__ == "__main__":
    download_sample_data()