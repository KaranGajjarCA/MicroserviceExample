import pika
import json

params = pika.URLParameters('amqps://kjbfuxzj:G4sLpXK6yDglHUPlJXfmpEtbWhd_ubRm@owl.rmq.cloudamqp.com/kjbfuxzj')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
