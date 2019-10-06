from typing import Tuple
import os

import cv2


DATASET_ZIP = 'fingers.zip'
ORIGIN_DIRPATH: str = 'fingers\\'
TARGET_DIRPATH: str = 'fingers_32x32\\'
SIZE: Tuple[int, int] = (32, 32)


if __name__ == '__main__':

    if not os.path.exists(ORIGIN_DIRPATH):
        os.mkdir(ORIGIN_DIRPATH)
        
    if not os.path.exists(TARGET_DIRPATH):
        os.mkdir(TARGET_DIRPATH)
    
    print('Extracting dataset file...', end='')
    with ZipFile(DATASET_ZIP, 'r') as zipObj:
       # Extract all the contents of zip file in current directory
       zipObj.extractall(ORIGIN_DIRPATH)
    print(' Done.')
    
    
    valid_extensions = {'jpg', 'png', 'jpeg'}

    print('Generating a downsampled dataset:')
    for dirpath, dirnames, filenames in os.walk(ORIGIN_DIRPATH):
        destination_dirpath = os.path.join(TARGET_DIRPATH, dirpath[len(ORIGIN_DIRPATH):])
        
        print('  - Processing "{}"...'.format(destination_dirpath), end='')

        if not os.path.exists(destination_dirpath):
            os.mkdir(destination_dirpath)

        for filename in filenames:
            parts = filename.split('.')
            if len(parts) < 2:
                continue

            name = '.'.join(parts[:-1])
            ext = parts[-1]
            if ext.lower() not in valid_extensions:
                continue

            origin_filepath = os.path.join(dirpath, filename)
            target_filepath = os.path.join(destination_dirpath, '.'.join([name, 'png']))

            image = cv2.imread(origin_filepath, cv2.IMREAD_GRAYSCALE)
            if image is None:
                continue

            processed_image = cv2.resize(image, SIZE)
            cv2.imwrite(target_filepath, processed_image)
            
        print(' Done.')
            
    print('Program is complete.')
