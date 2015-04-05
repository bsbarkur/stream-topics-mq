import pika
import sys
import filetail

# This tail log read module is taken from https://github.com/cloudtrends/CloudStack-LogViewer/blob/master/filetail.py
# This improves Activestate recipe code written by John Moore 
tail = filetail.Tail("log.txt")

# AMQP connection via Pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='log_to_topic', type='topic')

# for each new appended line in log, publish to queue
# first word of the log line contains the topic keyword
# rest words are the logger lines that are published to relevant topic queues
for line in tail:
        msg = line.split(" ")
        routing_key = msg[0]
        message = msg[1:]

        channel.basic_publish(exchange='log_to_topic',
                      routing_key=routing_key,
                      body=' '.join(message))
        print " [x] Sent %r:%r" % (routing_key, message)

connection.close()
