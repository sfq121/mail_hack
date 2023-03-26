import requests


def getfile(httpurl,filename):
    filepath = '/tmp' + filename
    down_res = requests.get(httpurl)
    with open(filepath, 'wb') as file:
        file.write(down_res.content)
    return filepath, filename

