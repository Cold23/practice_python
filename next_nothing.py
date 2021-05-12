import urllib.request
import re

if __name__ == "__main__":
    uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    num = str(16044/2)
    content = urllib.request.urlopen(uri % num).read().decode()
    match = re.search("and the next nothing is (\d+)", content)
    pattern = re.compile("and the next nothing is (\d+)")
    while True:
        content = urllib.request.urlopen(uri % num).read().decode('utf-8')
        print(content)
        match = pattern.search(content)
        if match == None:
            break
        num = match.group(1)