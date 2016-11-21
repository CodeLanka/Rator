from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')


def clean_env(path):
    f = open(path, 'r')
    for line in f:
        key = line.split("=")[0].strip(' ')
        try:
            del os.environ[key]
        except:
            pass


print("Clean environment variables : Start")
clean_env(dotenv_path)
print("Clean environment variables : Complete")

print("Set up new environment variables : Start")
load_dotenv(dotenv_path)
print("Set up new environment variables : Complete")







#installation
#https://github.com/theskumar/python-dotenv

