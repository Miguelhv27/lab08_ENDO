class QualityChecker:
    def __init__(self, config):
        """
        Inicializa el validador de calidad.
        
        Args:
            config (dict): Configuración de calidad
        """
        self.config = config
        self.checks = config.get('checks', [])

    def check_quality(self, data):
        """
        Ejecuta las verificaciones de calidad configuradas.
        
        Args:
            data: Datos a validar
            
        Returns:
            dict: Resultado de las verificaciones de calidad
        """
        quality_results = {
            'passed': True,
            'issues': [],
            'metrics': {}
        }

        # Ejecutar cada verificación de calidad configurada
        for check in self.checks:
            check_result = self._run_quality_check(check, data)
            if not check_result['passed']:
                quality_results['passed'] = False
                quality_results['issues'].extend(check_result['issues'])
            
            quality_results['metrics'].update(check_result['metrics'])

        return quality_results

    def _run_quality_check(self, check_name, data):
        """
        Ejecuta una verificación de calidad específica.
        
        Args:
            check_name (str): Nombre de la verificación
            data: Datos a verificar
            
        Returns:
            dict: Resultado de la verificación
        """
        result = {'passed': True, 'issues': [], 'metrics': {}}
        
        if "completeness_threshold" in check_name:
            completeness_result = self._check_completeness(data)
            result['passed'] = completeness_result['passed']
            result['issues'].extend(completeness_result['issues'])
            result['metrics']['completeness'] = completeness_result['completeness_rate']
            
        elif "freshness_max_hours" in check_name:
            freshness_result = self._check_freshness(data)
            result['passed'] = freshness_result['passed']
            result['issues'].extend(freshness_result['issues'])
            
        return result

    def _check_completeness(self, data):
        """
        Verifica la completitud de los datos.
        
        Returns:
            dict: Resultado de la verificación de completitud
        """
        # Simulación de verificación de completitud
        return {
            'passed': True,
            'issues': [],
            'completeness_rate': 0.98
        }

    def _check_freshness(self, data):
        """
        Verifica la frescura de los datos.
        
        Returns:
            dict: Resultado de la verificación de frescura
        """
        # Simulación de verificación de frescura
        return {
            'passed': True,
            'issues': []
        }