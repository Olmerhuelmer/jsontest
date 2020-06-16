import json
import requests
import sys

def get_api():
	with open(sys.argv[1]) as f:
		ready_json = json.load(f)
	def retr_modif_dict():
		n = 0
		list_comm = []
		while n < 5:
			n += 1
			response = requests.get("https://jsonplaceholder.typicode.com/posts/" + str(n))
			data_json = response.json()
			list_comm.append(data_json['body'])
		return list_comm
			
			 
	lst_comm = retr_modif_dict()

	def deep_layer(test_dict):
		internal_dict = test_dict['replies']
		test_dict['body'] = 'body-' + str(lst_comm[test_dict['id'] - 1])	
		if len(internal_dict) != 0:
			for i in internal_dict:
				deep_layer(i)
	dict_data = deep_layer(ready_json)
	print (ready_json)

if __name__ == '__main__':
	get_api()
