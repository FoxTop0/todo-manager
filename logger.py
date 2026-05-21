import logging
from datetime import datetime

class TaskLogger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._setup()
        return cls._instance
    
    def _setup(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )
        self.logger = logging.getLogger('TaskLogger')
    
    def log_info(self, message):
        self.logger.info(message)
    
    def log_error(self, message):
        self.logger.error(message)
