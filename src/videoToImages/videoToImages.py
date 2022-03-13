import os
import cv2
from tqdm import tqdm
from pathlib import Path, PureWindowsPath
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--videoFolder', type=str, default=r"D:\Ali Waqas\Projects\Drone\backup_laptop\anafi_backup\errors",
                    help='full path of path of folder containing videos')
parser.add_argument('--outFolder', type=str, default="", help='output folder to store images')
parser.add_argument('--fps', type=int, default=0, help='frames to output per second.')
parser.add_argument('--img_size', type=int, default=False, help='frames to output per second.')


class VideoToImages:
    def __init__(self, config):
        self.videoFolder = Path(r"{}".format(config.videoFolder))
        if not os.path.exists(self.videoFolder):
            raise RuntimeError('Invalid path: %s' % self.videoFolder)

        self.config = config
        self.files = [file for file in os.listdir(self.videoFolder) if file.endswith(".mp4") or file.endswith(".MP4")]
        self.outFolder = config.outFolder
        self.outfps = config.fps

        if len(config.outFolder) == 0:
            self.outFolder = os.path.join(self.videoFolder, "imagesConverted")
            try:
                # print(f"saving images to : {self.outFolder}")
                os.mkdir(self.outFolder)
            except OSError:
                print("Creation of the directory %s failed, or it already exists." % self.outFolder)
            else:
                print("Successfully created the directory %s " % self.outFolder)
        self.run()

    def run(self):
        print("Starting conversion")
        for idx, file in enumerate(self.files):
            vidcap = cv2.VideoCapture(os.path.join(self.videoFolder, file))
            sourcefps = vidcap.get(cv2.CAP_PROP_FPS)
            if self.outfps > sourcefps:
                self.outfps = 0
            print(f"[{idx+1}/{len(self.files)}]converting file: {file}")
            frameCount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
            skip = 0
            if self.outfps > 0:
                vidcap.set(cv2.CAP_PROP_FPS, self.outfps)
                # Estimating total frames to extract
                frameCount = math.ceil((frameCount / sourcefps) * self.outfps)
                skip = 1000 * math.floor(1000 / (self.outfps * 1000))

            success, image = vidcap.read()
            for i in tqdm(range(frameCount)):
                if not success:
                    break
                if skip > 0:
                    vidcap.set(cv2.CAP_PROP_POS_MSEC, (i * skip))

                if self.config.img_size:
                    image = cv2.resize(image, self.config.img_size)

                cv2.imwrite(os.path.join(self.outFolder, f"{file[:-4]}_{i}.png"), image)
                success, image = vidcap.read()

def main():
    VideoToImages(parser.parse_args())

if __name__ == '__main__':
    main()