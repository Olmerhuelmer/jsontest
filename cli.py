import json
import requests
import sys

def get_api(a):
	#with open(sys.argv[1]) as f:
	ready_json = a
	def retr_modif_dict(n):
		response = requests.get("https://jsonplaceholder.typicode.com/posts/" + str(n))
		data_json = response.json()
		body_comm = data_json['body']
		return body_comm
			
	def deep_layer(test_dict):
		internal_dict = test_dict['replies']
		id_key = test_dict['id']
		test_dict['body'] = 'body-' + retr_modif_dict(id_key)	
		if len(internal_dict) != 0:
			for i in internal_dict:
				deep_layer(i)
	dict_data = deep_layer(ready_json)
	print (ready_json)

if __name__ == '__main__':
	def red_full_json():
		b = str()
		try:
			while True:
				a = input()
				b += a
				#print (b,' g')
		except EOFError:
			c = b
		return eval(c)
	a = red_full_json()
	get_api(a)
