import json
import requests
import sys

def get_api(a):
	#with open(sys.argv[1]) as f:
	ready_json = a
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
	def deep_layer(test_dict,n):
		internal_dict = test_dict['replies']
		test_dict['body'] = 'body-' + str(lst_comm[n])	
		if len(internal_dict) != 0:
			for i in internal_dict:
				n += 1
				deep_layer(i,n)
	n = 0
	dict_data = deep_layer(ready_json,n)
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
