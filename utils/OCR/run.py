from easyocr.easyocr import *
import easyocr
import cv2
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


if __name__ == '__main__':

    # # Using default model
    # reader = Reader(['en'], gpu=True)

    # Using custom model
    reader = easyocr.Reader(['en'], gpu=True,
                    model_storage_directory='./easyocr/utils/',
                    user_network_directory='./easyocr/utils/',
                    recog_network='custom')
    result = reader.readtext('./easyocr/inputImages/django.png')
    print (result)
    files, count = get_files('./easyocr/inputImages')
    pth = './easyocr/inputImages'
    #for idx, file in enumerate(files):
     #   filename = os.path.basename(file)
    #    print(filename)
        #img = cv2.imread(pth+filename)
     #   result = reader.readtext(pth+filename)

        # ./easyocr/utils.py 733 lines
        # result[0]: bbox
        # result[1]: string
        # result[2]: confidence
        #for (bbox, string, confidence) in result:
            #print("filename: '%s', confidence: %.4f, string: '%s'" % (filename, confidence, string))
            # print('bbox: ', bbox)