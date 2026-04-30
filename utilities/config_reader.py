import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")

def get_config(key):
    return config["DEFAULT"][key]