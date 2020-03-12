import cv2
import os
import time

def cvt(self):
    count = 0
    time.sleep(10)
    path = "/Users/chaejaemin/Downloads/opensfm/OpenSfM/data/lund/"
    mk_file_name = "blurimages/"

    while True:
        is_dir = os.path.isdir(path + "images")
        os.chdir(path + "images")
        if is_dir == True:
            os.mkdir(path + "blurimages")
            while True:
                image_name = "{}.jpg".format(count)
                if os.path.isfile(image_name)==True:
                    images_tmp = cv2.imread(image_name)
                    gray_images = cv2.blur(images_tmp, (5, 5))
                    gray_image_name = "{}{}{}.jpg".format(path, mk_file_name, count)
                    cv2.imwrite(gray_image_name, gray_images)
                    count += 1
                else:
                    time.sleep(2)
                    continue
                if count == 100:
                    break
            break
        else:
            print("경로가 설정되지 않았습니다.")
            break
