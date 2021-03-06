import json
import requests
import sys
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
def get_api(a):
	def get_comment(ls_id):
		def retr_modif_dict(addr):
			response = requests.get(addr)
			data_json = response.json()
			body_comm = data_json['body']
			return body_comm
		pool = ThreadPool(5)
		str_url = "https://25.ms/posts/"
		list_url = [str_url + str(i) for i in ls_id]
		results = pool.map(retr_modif_dict, list_url)
		pool.close()
		pool.join()
		return results
	############################
	ready_json = a
	list_id = []
	#############################
	def numb_id(test_dict):	
		internal_dict = test_dict['replies']
		id_key = test_dict['id']
		list_id.append(id_key)	
		if len(internal_dict) != 0:
			for i in internal_dict:
				numb_id(i)
		return list_id
	#############################
	numb_id(ready_json)
	list_comments = get_comment(list_id)
	##############################
	def deep_layer(test_dict):
		internal_dict = test_dict['replies']
		id_key = test_dict['id']
		index_comm = list_id.index(id_key)
		test_dict['body'] = 'body-' + str(list_comments[index_comm])
		if len(internal_dict) != 0:
			for i in internal_dict:
				deep_layer(i)
	#############################
	
	deep_layer(ready_json)
	print (json.dumps(ready_json))

if __name__ == '__main__':
	def red_full_json():
		b = str()
		try:
			while True:
				a = input()
				b += a
		except EOFError:
			c = b
		return eval(c)
	a = red_full_json()
	get_api(a)
