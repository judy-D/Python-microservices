import pika, json

params = pika.URLParameters('amqps://zghxmhiw:6Rkpz1XvK9Apaoo_Syczobn_UXmPN0xf@hornet.rmq.cloudamqp.com/zghxmhiw')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)