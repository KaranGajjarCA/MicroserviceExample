import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adminApp.settings")
django.setup()
from products.models import Product

params = pika.URLParameters('your_amqps_url')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print("Product Likes increased!")


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("Stated Consuming")

channel.start_consuming()
channel.close()
