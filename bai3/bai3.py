import re, json
import requests

Request = """GET /gen_204?s=webhp&t=cap&atyp=csi&ei=RGwxY9WBLcWEr7wPyYy0oA8&rt=wsrt.2357,cbt.106&bl=x9VE HTTP/2
Host: www.google.com
Cookie: 1P_JAR=2022-09-26-09; AEC=AakniGPB8tq-E05P2NYD9O9bdlMLB2AfWt0A4I4RxzyJYcZ02sa0rSx1D9Y; NID=511=h5UnvT3IzcYd4wdiknZoBqB3p9EmEPefZ7Nkz9wfPrS1yMAWdbfDmvjK6iyL1jmc5_RMHn9rhK1TQDrU1gqIjKW6i9Q-nRTs9c4m0qZwMBsKCvBeabp94DKHIaJdyy5u1ZdSVKmaDBVNPlBlPc4vvKk0qBOu7dsrSJcnzr55qmM
Content-Length: 0
Sec-Ch-Ua: "Chromium";v="105", "Not)A;Brand";v="8"
Content-Type: text/plain;charset=UTF-8
Sec-Ch-Ua-Model: 
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Sec-Ch-Ua-Arch: "x86"
Sec-Ch-Ua-Full-Version-List: "Chromium";v="105.0.5195.102", "Not)A;Brand";v="8.0.0.0"
Sec-Ch-Ua-Platform-Version: "10.0.0"
Sec-Ch-Ua-Bitness: "64"
Sec-Ch-Ua-Wow64: ?0
Sec-Ch-Ua-Full-Version: "105.0.5195.102"
Sec-Ch-Ua-Platform: "Windows"
Accept: /
Origin: https://www.google.com
X-Client-Data: CIqDywE=
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: empty
Referer: https://www.google.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
"""
result = {
    'method': None,
    'url': None,
    'args': [],
    'headers': {},
    'origin': None,
    'files': None,
    'form': None,
    'json': None,
    'data': None,
}

header = re.match(r'(?P<method>\w+) (?P<path>.*?)\?(?P<params>.*?) (?P<http_version>HTTP\/[\d\.]+)',
                  Request).groupdict()

result['method'] = header['method']
result['url'] = header['path']
result['args'] = [pair.split('=') for pair in header['params'].split('&')]

for line in Request.splitlines()[1:]:
    key, value = re.match(r'(?P<key>.*?): (?P<value>.*)', line).groups()

    if key == "Origin":
        result["origin"] = value
    else:
        result["headers"][key] = value

print("Url :",result['origin']+result['url'])
print("-------------------------Respone------------------------")
r = requests.get(result['origin']+result['url'], auth=('user', 'pass'))
print("Status code :",r.status_code)
print("Encoding :",r.encoding)
print("Header :",r.headers)