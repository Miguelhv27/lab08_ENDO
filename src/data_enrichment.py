class DataEnricher:
    def __init__(self, config):
        """
        Inicializa el enriquecedor de datos.
        
        Args:
            config (dict): Configuración de enriquecimiento
        """
        self.config = config
        self.catalog_path = config.get('catalog_path')
        self.lookup_tables = config.get('lookup_tables', [])

    def enrich(self, data):
        """
        Enriquece los datos con información adicional.
        
        Args:
            data: Datos a enriquecer
            
        Returns:
            dict: Datos enriquecidos
        """
        # Simulación de enriquecimiento de datos
        enriched_data = []
        
        for record in data:
            # Añadir información de enriquecimiento
            enriched_record = record.copy()
            enriched_record['categoria'] = self._get_product_category(record.get('producto', ''))
            enriched_record['impuesto'] = record.get('venta', 0) * 0.19  # 19% de impuesto
            enriched_record['enriched'] = True
            enriched_data.append(enriched_record)

        return {
            'enriched_data': enriched_data,
            'enrichment_applied': True,
            'catalog_used': self.catalog_path is not None,
            'lookup_tables_used': self.lookup_tables
        }

    def _get_product_category(self, product_name):
        """
        Obtiene la categoría de un producto (simulado).
        
        Args:
            product_name (str): Nombre del producto
            
        Returns:
            str: Categoría del producto
        """
        # Simulación de búsqueda en catálogo
        categories = {
            "Laptop": "Tecnología",
            "Mouse": "Tecnología", 
            "Teclado": "Tecnología"
        }
        return categories.get(product_name, "Otra")