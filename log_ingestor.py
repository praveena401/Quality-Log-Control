# log_ingestor/log_ingestor.py

import logging

# Define log format
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# Configure logging
logging.basicConfig(filename='log1.log', level=logging.INFO, format=LOG_FORMAT)

# Example usage
logging.info('This is an info log message')
