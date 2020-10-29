import argparse
import cv2
from cropper.cropper import crop_card
from detector.detector import detect_info
from reader import reader
import matplotlib.pyplot as plt
import sys
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default='407.jpg')
args = vars(ap.parse_args())

def plot_img(img):
    plt.show()

img = cv2.imread(args["image"])
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plot_img(img)

warped = crop_card(args["image"])


if warped is None:
    print('Cant find id card in image')
    sys.exit()

try:
    face, number_img, name_img, dob_img, gender_img, nation_img, \
        country_img, address_img, country_img_list, address_img_list = detect_info(
            warped)
except:
    print('Cant find id card in image')
    sys.exit()

number_text = reader.get_id_numbers_text(number_img)
name_text = reader.get_name_text(name_img)
dob_text = reader.get_dob_text(dob_img)
gender_text = reader.get_gender_text(gender_img)
country_text = reader.process_list_img(country_img_list, is_country=True)

print('Số:'+number_text)
print('Họ và tên: ' + name_text)
print('Ngày tháng năm sinh: ' + dob_text)
print('Giới tính: ' + gender_text)
print('Quê quán: ' + country_text)



