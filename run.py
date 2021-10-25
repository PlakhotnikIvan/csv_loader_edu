from datetime import datetime
import pandas as pd
import logging

from loader import url_loader

logger = logging.getLogger('csv_loader')


def csv_saver(path, content):
    try:
        file_name = f'output-csv-{datetime.now().strftime("%Y%m%d-%H%M%S")}.csv'
        file_path = f'{path}\{file_name}'
        logger.info(f'creating csv file: {file_path}')
        content.to_csv(file_path)
        logger.info('File created')
    except Exception as e: 
        logger.error(e)
        
def json_saver(path, content):
    try:
        file_name = f'output-json-{datetime.now().strftime("%Y%m%d-%H%M%S")}.json'
        file_path = f'{path}\{file_name}'
        logger.info(f'creating json file: {file_path}')
        content.to_json(file_path)
        logger.info('File created')
    except Exception as e:
        logger.error(e)



def run(CSV_URL, file_path, output_format, use_cache, cache_folder):
    
    data = url_loader(CSV_URL, use_cache, cache_folder)
    data_sample = pd.DataFrame(data, columns = data[0]).iloc[1:11, :5]
    if output_format == 'json':
        json_saver(file_path, data_sample)
    else:
        csv_saver(file_path, data_sample)

