import configparser

def readConfigData(section,key):
    config = configparser.ConfigParser()
    config.read("./Config/config.cfg")
    return config.get(section,key)


def fetchElementLocators(section,key):
    config = configparser.ConfigParser()
    config.read("./Config/elements.cfg")
    return config.get(section,key)



def readgmailelements(section,key):
    config = configparser.ConfigParser()
    config.read("./Config/gmailelements.cfg")
    return config.get(section,key)

def stepinconfig(section,key):
    config = configparser.ConfigParser()
    config.read("./Config/config.cfg")
    return config.get(section,key)

