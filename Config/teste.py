import configparser

config = configparser.ConfigParser()

config.read('config.ini')

string_val = config.get('backup_local_path', 'local_path')

print(string_val)