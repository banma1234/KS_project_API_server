import os
from easyocr.easyocr import *
import easyocr
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# GPU 설정
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'

def perform_ocr(image):
    # Using custom model
    reader = easyocr.Reader(['en'], gpu=True,
                            model_storage_directory='./utils/OCR/',
                            user_network_directory='./utils/OCR/',
                            recog_network='custom')
    print("reader generated")
    result = reader.readtext(image, detail = 0)

    return ' '.join(result)


if __name__ == '__main__':
    ocr_result, file_list = perform_ocr()
