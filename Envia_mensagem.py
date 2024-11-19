import boto3

queue_url = 'https://sqs.us-east-1.amazonaws.com/311351879181/Ada-Fila'

sqs = boto3.client('sqs', region_name='us-east-1')

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Aluna Michelle entregou o projeto'
)

print("Mensagem enviada com sucesso. ID da mensagem:", response['MessageId'])