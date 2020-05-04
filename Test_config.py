from configparser import ConfigParser

objconfig=ConfigParser()
objconfig.read("./venv/Config.cfg")
username = objconfig.get("Section1","username")
print(username)

url = objconfig.get("Section2","url")
print(url)