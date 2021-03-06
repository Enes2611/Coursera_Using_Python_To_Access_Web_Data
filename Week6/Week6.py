# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import urllib
import json

url = raw_input("Enter location: ")
address = urllib.urlopen(url)
data = address.read()

total = 0

while True:
	if len(url)<1: break

	print("Retrieving: ", address)
	print("Retrieved ", len(data)," characters")

	info = json.loads(data)
	info = info["comments"]
	for item in info:
		print("Count: ",item["count"])
		total += int(item["count"])
		print("Sum: ", total)
	print("Final sum: ", total)
	break

# Output:

# Answer: 2908

# Enter location: http://python-data.dr-chuck.net/comments_190811.json
# ('Retrieving: ', <addinfourl at 4509449104 whose fp = <socket._fileobject object at 0x10a9160d0>>)
# ('Retrieved ', 2710, ' characters')
# ('Count: ', 98)
# ('Sum: ', 98)
# ('Count: ', 97)
# ('Sum: ', 195)
# ('Count: ', 96)
# ('Sum: ', 291)
# ('Count: ', 93)
# ('Sum: ', 384)
# ('Count: ', 92)
# ('Sum: ', 476)
# ('Count: ', 90)
# ('Sum: ', 566)
# ('Count: ', 89)
# ('Sum: ', 655)
# ('Count: ', 89)
# ('Sum: ', 744)
# ('Count: ', 89)
# ('Sum: ', 833)
# ('Count: ', 87)
# ('Sum: ', 920)
# ('Count: ', 87)
# ('Sum: ', 1007)
# ('Count: ', 85)
# ('Sum: ', 1092)
# ('Count: ', 84)
# ('Sum: ', 1176)
# ('Count: ', 84)
# ('Sum: ', 1260)
# ('Count: ', 81)
# ('Sum: ', 1341)
# ('Count: ', 81)
# ('Sum: ', 1422)
# ('Count: ', 81)
# ('Sum: ', 1503)
# ('Count: ', 77)
# ('Sum: ', 1580)
# ('Count: ', 77)
# ('Sum: ', 1657)
# ('Count: ', 73)
# ('Sum: ', 1730)
# ('Count: ', 69)
# ('Sum: ', 1799)
# ('Count: ', 67)
# ('Sum: ', 1866)
# ('Count: ', 64)
# ('Sum: ', 1930)
# ('Count: ', 62)
# ('Sum: ', 1992)
# ('Count: ', 61)
# ('Sum: ', 2053)
# ('Count: ', 58)
# ('Sum: ', 2111)
# ('Count: ', 58)
# ('Sum: ', 2169)
# ('Count: ', 57)
# ('Sum: ', 2226)
# ('Count: ', 56)
# ('Sum: ', 2282)
# ('Count: ', 52)
# ('Sum: ', 2334)
# ('Count: ', 51)
# ('Sum: ', 2385)
# ('Count: ', 51)
# ('Sum: ', 2436)
# ('Count: ', 50)
# ('Sum: ', 2486)
# ('Count: ', 44)
# ('Sum: ', 2530)
# ('Count: ', 42)
# ('Sum: ', 2572)
# ('Count: ', 40)
# ('Sum: ', 2612)
# ('Count: ', 37)
# ('Sum: ', 2649)
# ('Count: ', 36)
# ('Sum: ', 2685)
# ('Count: ', 33)
# ('Sum: ', 2718)
# ('Count: ', 32)
# ('Sum: ', 2750)
# ('Count: ', 31)
# ('Sum: ', 2781)
# ('Count: ', 24)
# ('Sum: ', 2805)
# ('Count: ', 23)
# ('Sum: ', 2828)
# ('Count: ', 20)
# ('Sum: ', 2848)
# ('Count: ', 18)
# ('Sum: ', 2866)
# ('Count: ', 13)
# ('Sum: ', 2879)
# ('Count: ', 13)
# ('Sum: ', 2892)
# ('Count: ', 10)
# ('Sum: ', 2902)
# ('Count: ', 4)
# ('Sum: ', 2906)
# ('Count: ', 2)
# ('Sum: ', 2908)
# ('Final sum: ', 2908)
