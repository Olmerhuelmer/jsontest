import json
import requests
import sys

def get_api():
	response = sys.argv[1]
	#print (response)
	ready_json = {"id": 1, "replies": [{"id": 2, "replies": []}, {"id": 3,"replies": [{"id": 4,"replies": []}, {"id": 5,"replies": []}]}]}
	#response = requests.get("https://jsonplaceholder.typicode.com/posts/ID ")
	data_json = ready_json
	def deep_layer(test_dict):
		internal_dict = test_dict['replies']
		test_dict.setdefault('body', 'body-' + str(test_dict['id']))
		if len(internal_dict) != 0:
			for i in internal_dict:
				deep_layer(i)
	dict_data = deep_layer(data_json)
	print (data_json)


if __name__ == '__main__':
	get_api()

