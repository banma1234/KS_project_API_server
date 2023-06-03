import os
from easyocr.easyocr import *
import easyocr
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# GPU 설정
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'


def get_files(path):
    file_list = []

    files = [f for f in os.listdir(path) if not f.startswith('.')]  # skip hidden file
    files.sort()
    abspath = os.path.abspath(path)
    for file in files:
        file_path = os.path.join(abspath, file)
        file_list.append(file_path)

    return file_list, len(file_list)

def perform_ocr():
    # Using custom model
    print("start")
    print("==================================")
    reader = easyocr.Reader(['en'], gpu=True,
                            model_storage_directory='./utils/OCR/',
                            user_network_directory='./utils/OCR/',
                            recog_network='custom')
    print("reader generated")
    result = reader.readtext('./utils/OCR/inputImages/example.jpg', detail = 0)
    print("result generated")
    print(result)
    files, count = get_files('./utils/OCR/inputImages/')
    pth = './utils/OCR/inputImages/'
    # Do something with the OCR result or files
    # ...

    return ' '.join(result)


if __name__ == '__main__':
    ocr_result, file_list = perform_ocr()
