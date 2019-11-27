import pika

print('enter a msg to emit: ', end='')
msg = input()

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=msg)

print(f' [x] Sent [{msg}]')
