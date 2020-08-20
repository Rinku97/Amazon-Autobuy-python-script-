"""
Note: This is strictly advised, Do not modify/change/delete this file.If does, it will stop working.

@author: Rinku
This is the python script that is used to autobuy the product from the amazon during the flash sale or in daily
routine.

"""
from configparser import ConfigParser

file = "config.ini"
config = ConfigParser()
config.read(file)

username = config['Data']['USERNAME']
password = config['Data']['PASSWORD']
url = config['Data']['URL']

