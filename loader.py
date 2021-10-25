import csv
import requests
import json
import logging


def url_loader(CSV_URL, use_cache, cache_folder):
    
    logger = logging.getLogger('csv_loader')
    dict_path = f'{cache_folder}\cache_dict.json'
    if use_cache == 'yes':
        try:
            logger.info('checking cache')
            with open(dict_path, 'r') as f:
                cache = json.load(f)
        except Exception as e:
            logger.error(e)
            cache = {}
            
        if CSV_URL in cache:
            logger.info('loading from cache')
            final_list = cache[CSV_URL] 
            return final_list
  
    with requests.Session() as s:
        try:
            logger.info('loading from url')
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            final_list = list(csv.reader(decoded_content.splitlines()))
            logger.info('adding url to cache')
            with open(dict_path, 'w') as d:
                cache[CSV_URL] = final_list 
                json.dump(cache, d)
        except Exception as e:
            logger.error(e)
        
    return final_list
