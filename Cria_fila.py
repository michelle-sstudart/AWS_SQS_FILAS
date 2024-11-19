import boto3 # type: ignore

sqs = boto3.client ('sqs', region_name='us-east-1') 

# Cria a fila SQS
response = sqs.create_queue(
    QueueName='Ada-Fila',
    Attributes={
        'DelaySeconds': '5'  # Atraso opcional para as mensagens 

    }
)

# Obtém a URL da fila criada

queue_url = response['QueueUrl']
print("Fila criada com sucesso. URL da Fila:", queue_url) # type: ignore