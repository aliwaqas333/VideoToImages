import os

import cv2
from tqdm import tqdm
from pathlib import Path, PureWindowsPath


class VideoToFrames:
    def __init__(self, videoFolder: str = r"D:\Ali Waqas\Projects\Drone\video_to_images\videos"):
        self.videoFolder = PureWindowsPath(r"{}".format(videoFolder))
        self.files = [file for file in os.listdir(self.videoFolder) if file.endswith(".mp4") or file.endswith(".MP4")]
        self.run()


    def run(self):
        print("Starting conversion")
        for file in self.files:
            print(f"converting file: {file}")
            vidcap = cv2.VideoCapture(os.path.join(self.videoFolder, file))
            frameCount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
            success, image = vidcap.read()
            for i in tqdm(range(frameCount)):
                if not success:
                    break
                cv2.imwrite(f"./images/{file}_{i}.png", image)
                success, image = vidcap.read()



if __name__ == '__main__':
    VideoToFrames("D:/Ali Waqas/Projects/Drone/video_to_images/videos")