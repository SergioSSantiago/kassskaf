from kafka import KafkaConsumer, KafkaProducer
import json 
from bson import json_util



consumer = KafkaConsumer('test10', 
	bootstrap_servers='0.0.0.0:9092' ,
	auto_offset_reset='earliest'
)
producer2 = KafkaProducer(bootstrap_servers='0.0.0.0:9092')

somme=0
count=0
for msg in consumer:
	
	
	parsed_json = json.loads(msg.value)
	print(parsed_json[u'documentTotal'].get(u'grossTotal'))
	grossTotal=parsed_json[u'documentTotal'].get(u'grossTotal')
	somme+=grossTotal
	
	count+=1
	print somme
	result = {'Somme total':somme,'Num total tickets':count}

	producer2.send('result111', json.dumps(result, indent=4, default=json_util.default).encode('utf-8'))


	producer2.flush()