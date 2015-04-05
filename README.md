# stream-topics-mq

## Install 

```
[Tested on Ubuntu LTS 14.04 (Provisoned using Vagrant)]
	1. rabbitmq-server
	2. pika
```

## Start consumer 

```
Run the RabbitMQ consumer that creates topic binding queues

# python consume_log_from_topic.py <topic1> <topic2>
	Eg: python consume_log_from_topic.py "bangalore" "mysore"

Verify this using:
 vagrant@vagrant-ubuntu-trusty-64:~$ sudo rabbitmqctl list_bindings
	Listing bindings ...
		exchange	amq.gen-VbyMGePtbZB20-47e7PaYg	queue	amq.gen-VbyMGePtbZB20-47e7PaYg	[]
		log_to_topic	exchange	amq.gen-VbyMGePtbZB20-47e7PaYg	queue	bangalore	[]
		log_to_topic	exchange	amq.gen-VbyMGePtbZB20-47e7PaYg	queue	mysore	[]

```

## Start producer

```
Run the RabbitMQ producer that will produce when there is a new line appended to the log.txt

# python publish_log_to_topic.py

```

## Log format

```
Append test data to the log in this format:

# echo "<topic1> <content of log line>" >> log.txt
	Eg: echo "bangalore updated data" >> log.txt
		here: bangalore, the first word is the topic
			  rest are read as long content and published to the bangalore topic queue 
```
