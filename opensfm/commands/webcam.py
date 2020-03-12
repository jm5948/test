import cv2
import logging
import os
import shutil

class Command:
    def run(self, args):
        path_name = ('%s/images/' %args)
        counter = 0
        images_num = 0

        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        os.mkdir(path_name)

        while True:
            ret, frame = capture.read()
            cv2.imshow("image", frame)

            if counter == 30:
                cv2.imwrite('%s%d.jpg' % (path_name, images_num), frame)
                images_num += 1
                counter = 0
            else:
                counter += 1

            if cv2.waitKey(1) == ord('q'): break
        capture.release()
        cv2.destroyAllWindows()

