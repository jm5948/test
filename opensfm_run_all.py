import sys
import os
import shutil
import multiprocessing as mp
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from opensfm import commands, dataset

subcommands = [module.Command() for module in commands.opensfm_commands]

class sfm_subprocesses(object):
        def __init__(self, selcet_directory):
                self.path = selcet_directory

                if os.path.isdir(self.path):
                        shutil.rmtree(self.path)
                        os.mkdir(self.path)
                        shutil.copy('./config.yaml', self.path)

        def start_webcam(self):
                subcommands[0].run(self.path)

        def run_all(self):
                for command in subcommands:
                        command.run(self.path)

