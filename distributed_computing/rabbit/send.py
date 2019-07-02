"""
Rabbit MQ server - tutorial
first part of this using RabbitMQ and send a single message to queue
To do these, we need to establish a connection with Rabbit MQ sever

*Description
RabbitMQ server : Broker between producer(sender) and customer(reciever)
pika : protocol
"""

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

"""
if we wanted to connect to a broker on a different machine we'd simply specify its name or IP address here instaed of localhost
"""

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',      #<- The queue name
                      body='Hello World!')


"""making queue"""
print(" [x] Sent 'Hello World!'")
connection.close()

