import boto3

# Crear cliente de Amazon Inspector2
client = boto3.client('inspector2')

# Listar los hallazgos
response = client.list_findings()

# Verificar si hay hallazgos disponibles
if not response['findings']:
    print("No hay hallazgos disponibles.")
else:
    # Mostrar los hallazgos
    for finding in response['findings']:
        print(f"ID: {finding['findingArn']}")
        print(f"Severity: {finding['severity']}")
        print(f"Title: {finding['title']}\n")