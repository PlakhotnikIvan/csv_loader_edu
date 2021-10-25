import yaml

from run import run
import sys
import logging
from logging import StreamHandler


logger = logging.getLogger('csv_loader')
logger.setLevel(logging.INFO)
handler = StreamHandler(stream = sys.stdout)
logger.addHandler(handler)


with open('csv_loader.yaml') as f:
    parameters = yaml.safe_load(f)


CSV_URL = parameters['CSV_URL']
save_folder = parameters['save_folder']   
output_format = parameters['output_format'] 
use_cache = parameters['use_cache']
cache_folder = parameters['cache_folder']


run(CSV_URL, save_folder, output_format, use_cache, cache_folder)