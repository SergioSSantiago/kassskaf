from kafka import KafkaConsumer
import time 
import json

consumer = KafkaConsumer('result111', 
	bootstrap_servers='0.0.0.0:9092',
	auto_offset_reset='earliest')

for msg in consumer:

	parsed_json = json.loads(msg.value)
	
	for key, value in parsed_json.iteritems():
		print key,"=",value
	print "----------------------"
	