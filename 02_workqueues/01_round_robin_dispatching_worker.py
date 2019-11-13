import time
import pika

"""
Work queues
Distributing tasks among workers (the competing consumers pattern)
https://www.rabbitmq.com/tutorials/tutorial-two-python.html
"""

"""
Round-robin dispatching
"""

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.queue_declare(queue='q_for_example_2')


def callback_func_for_exam_2(ch, method, properties, body):
    print(f' [x] Received {body}')
    time.sleep(body.count(b'.'))
    print(' [x] Done.')


channel.basic_consume(queue='q_for_example_2',
                      auto_ack=True,
                      on_message_callback=callback_func_for_exam_2)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
