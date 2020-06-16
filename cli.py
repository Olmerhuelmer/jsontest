import json
import requests
import sys

def get_api():
	with open(sys.argv[1]) as f:
		ready_json = json.load(f)
	n = 0
	while n < 5:
		n += 1
		response = requests.get("https://jsonplaceholder.typicode.com/posts/" + str(n))
		data_json = response.json()
		def retr_modif_dict(data_json):
			return data_json['body']
		
		def deep_layer(test_dict):
			internal_dict = test_dict['replies']
			test_dict.setdefault('body', 'body-' + retr_modif_dict(data_json))
			if len(internal_dict) != 0:
				for i in internal_dict:
					deep_layer(i)
		dict_data = deep_layer(ready_json)
	print (ready_json)

if __name__ == '__main__':
	get_api()
