# stream-topics-mq

1. Requirements on Ubuntu LTS 14.04 (Provisoned using Vagrant)
	rabbitmq-server
	pika

2. Run the RabbitMQ consumer that creates topic binding queues
	python consume_log_from_topic.py <topic1> <topic2>
		Eg: python consume_log_from_topic.py "bangalore" "mysore"

	Verify this using:
		vagrant@vagrant-ubuntu-trusty-64:~$ sudo rabbitmqctl list_bindings
		Listing bindings ...
			exchange	amq.gen-VbyMGePtbZB20-47e7PaYg	queue	amq.gen-VbyMGePtbZB20-47e7PaYg	[]
			log_to_topic	exchange	amq.gen-VbyMGePtbZB20-47e7PaYg	queue	bangalore	[]
			log_to_topic	exchange	amq.gen-VbyMGePtbZB20-47e7PaYg	queue	mysore	[]

3. Run the RabbitMQ producer that will produce when there is a new line appended to the log.txt
	python publish_log_to_topic.py

4. Append test data to the log in this format:
	echo "<topic1> <content of log line>" >> log.txt
	Eg: echo "bangalore updated data" >> log.txt
		here: bangalore, the first word is the topic
			  rest are read as long content and published to the bangalore topic queue 
