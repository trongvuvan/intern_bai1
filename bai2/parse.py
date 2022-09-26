import requests

def parse_request(file_name):
	line = ""
	headers = {}
	post_data = ""
	header_collection_done = False
	file_object = open(file_name , "r")
	file_object.seek(0)
	file_object.readline()
	for line in file_object.readlines():
		if header_collection_done is False:
			if line.startswith("\n"):
				header_collection_done = True
			else:
				headers.update({
					line[0:line.find(":")].strip() : line[line.find(":")+1 :].strip()
				})
		else:
			post_data = post_data + line
	file_object.close()
	return (headers , post_data)

headers,post_data = parse_request("request.txt")
print("Headers:\n",headers.items())
print("Content:\n",post_data)
