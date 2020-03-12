
import cvtimages
import webcam
import shutil
import multiprocessing as mp
import os

path = '/Users/chaejaemin/Downloads/opensfm/OpenSfM/data/lund/'
img_path = '/Users/chaejaemin/Downloads/opensfm/OpenSfM/data/lund/images'
blur_path = '/Users/chaejaemin/Downloads/opensfm/OpenSfM/data/lund/blurimages'

if os.path.isdir(img_path) and os.path.isdir(blur_path):
    shutil.rmtree(img_path)
    shutil.rmtree(blur_path)


command = []
command.append(webcam.Command())
command.append(cvtimages)

# for subcommand in command:
p = mp.Process(target = command[0].run, args = (path, ))
q = mp.Process(target = command[1].cvt, args = (img_path, ))
p.start()
q.start()

p.join()
q.join()

# class apple():
#     def add(self, a):
#         print(a*a)
#
# djdj = apple()
# list = [1,2,3]
#
# def add(a):
#     print(a*a)
#
# for index, i in enumerate(list):
#     p = mp.Process(target=djdj.add, args=(i, ))
#     p.start()
#     p.join()