import pika

"""
Hello World! (consumer)
The simplest thing that does something
https://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""

# 1. connect to RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

# 2. Creating a queue using queue_declare
channel.queue_declare(queue='q_name_hello')


# Creating a queue using queue_declare is idempotent
# ‒ we can run the command as many times as we like, and only one will be created.
# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program was run before.
# But we're not yet sure which program to run first.
# In such cases it's a good practice to repeat declaring the queue in both programs.

# 3. Receiving messages from the queue
# Receiving messages from the queue is more complex. It works by subscribing a callback function to a queue.
# Whenever we receive a message, this callback function is called by the Pika library.
# In our case this function will print on the screen the contents of the message.
def callback_func(ch, method, properties, body):
    print(f' [x] Received {body}')


# 4. Next, we need to tell RabbitMQ that this particular callback function should receive messages from our hello queue.
channel.basic_consume(queue='q_name_hello',
                      auto_ack=True,
                      on_message_callback=callback_func)

# 5. we enter a never-ending loop that waits for data and runs callbacks whenever necessary.
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
