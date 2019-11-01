#!/usr/bin/env python
import pika
import sys

class Producer():
    def __init__(self, routing_key, message):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

        channel.basic_publish(
            exchange='topic_logs', routing_key=routing_key, body=message)
        print(" [x] Sent %r:%r" % (routing_key, message))
        connection.close()