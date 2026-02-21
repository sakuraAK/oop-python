from singleton import Singleton
from datetime import datetime
from os.path import join

class SingletonLogger(metaclass=Singleton):
    _log_file = None

    def __init__(self, path):
        if self._log_file is None:
            path_parts = __file__.split("\\")[:-1]
            path_parts.append(path)
            self._log_file = open(path, "w")
    
    def log(self, record):
        self._log_file.write(f'[{datetime.now()}]-[{record}]\n')


    def close_log(self):
        if self._log_file:
            self._log_file.close()
            self._log_file = None