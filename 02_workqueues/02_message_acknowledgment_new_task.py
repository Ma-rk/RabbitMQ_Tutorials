import sys
import pika

"""
Work queues
Distributing tasks among workers (the competing consumers pattern)
https://www.rabbitmq.com/tutorials/tutorial-two-python.html
"""

"""
message acknowledgments
"""

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.queue_declare(queue='q_for_example_2')

message = ' '.join(sys.argv[1:]) or 'Hello RabbitMQ!!'
channel.basic_publish(exchange='',
                      routing_key='q_for_example_2',
                      body=message)

print(f' [x] Sent {message}')
