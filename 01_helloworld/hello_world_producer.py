import pika

"""
Hello World! (producer)
The simplest thing that does something
https://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""

# 1. establish a connection with RabbitMQ server.
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

# We're connected now, to a broker on the local machine - hence the localhost.
# If we wanted to connect to a broker on a different machine we'd simply specify its name or IP address here.

# 2. create a hello queue to which the message will be delivered
channel.queue_declare(queue='q_name_hello')
# before sending we need to make sure the recipient queue exists. If we send a message to non-existing location,
# RabbitMQ will just drop the message.

# 3. exchange
# In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
# But let's not get dragged down by the details ‒ you can read more about exchanges in the third part of this tutorial.
# All we need to know now is how to use a default exchange identified by an empty string.
# This exchange is special ‒ it allows us to specify exactly to which queue the message should go.
# The queue name needs to be specified in the routing_key parameter:
channel.basic_publish(exchange='',
                      routing_key='q_name_hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# 4. closing the connection
# Before exiting the program we need to make sure the network buffers were flushed
# and our message was actually delivered to RabbitMQ.
# We can do it by gently closing the connection.
conn.close()
