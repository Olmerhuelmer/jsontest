import json
import requests
import sys

def get_api():
	n = 0
	while True:
		n += 1
		response = requests.get("https://jsonplaceholder.typicode.com/posts/" + str(n))
		data_json = response.json()
		def retr_modif_dict(data_json):
			#data_json.setdefault("body", 'body-' + str(data_json['id']))
			data_json['body'] = 'body-' + str(data_json['id'])
		retr_modif_dict(data_json)
		print (data_json)
if __name__ == '__main__':
	get_api()
