import boto3
import time

# Crear cliente de CloudWatch
cloudwatch = boto3.client('cloudwatch')

# Función que simula una prueba de rendimiento
def simulated_performance_test():
    # Simula el tiempo que tarda en completarse una operación
    start_time = time.time()
    time.sleep(2)  # Simular un retraso
    end_time = time.time()
    
    # Calcular el tiempo total
    total_time = end_time - start_time
    print(f"Tiempo de operación: {total_time} segundos")

    # Enviar métricas personalizadas a CloudWatch
    cloudwatch.put_metric_data(
        MetricData=[
            {
                'MetricName': 'ResponseTime',
                'Dimensions': [
                    {
                        'Name': 'TestType',
                        'Value': 'Performance'
                    },
                ],
                'Unit': 'Seconds',
                'Value': total_time
            },
        ],
        Namespace='MyApplication'
    )

# Ejecutar la prueba
simulated_performance_test()