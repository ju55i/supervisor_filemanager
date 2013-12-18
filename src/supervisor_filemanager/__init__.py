import os
import logging

API_VERSION = '0.1'

class FileManagerRPCInterface:
    def __init__(self, supervisord, **config):
        logging.info("Initializing Filemanager")
        self.supervisord = supervisord
        self.config_dir = os.path.normpath(config.get('path'))

    def getAPIVersion(self):
        """
        @return string              version string
        """
        return API_VERSION

    def listFiles(self):
        """
        @return array               list of files in configuration directory
        """
        os.chdir(self.config_dir)
        config_files = os.listdir(".")
        return config_files

    def putFile(self, config_file, content):
        """
        @param  string  config_file configuration filename
        @param  string  content     content of the configuration file
        @return boolean             True if operation was successful
        """
        try:
            os.chdir(self.config_dir)
            f = file(config_file,"w")
            f.write(content)
            return True
        except:
            return False
        finally:
            f.close()


    def getFile(self, config_file):
        """
        @param  string  config_file configuration filename
        @return string              content of the configuration file
        """
        os.chdir(self.config_dir)
        return file(config_file).read()

def make_filemanager_rpcinterface(supervisord, **config):
    return FileManagerRPCInterface(supervisord, **config)
