import json
import urllib.request


def get_result(url: str) -> dict:
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_file = response.read().decode(encoding = 'utf-8')
        #Convert the JSON format file to a Python object which is a dictionary.
        python_obj = json.loads(json_file)
        return python_obj
    finally:
        #Assume that we opened the file successfully and close the file after we finish the work.
        if response != None:
            response.close()
