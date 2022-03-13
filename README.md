# Videos To images command line
This repository can be used to convert `mp4` files to images, more extensions will be added soon.
# Installation
`pip install videoToImages`

# Usage
### Convert video folder to images
```py
videoToimages --videoFolder [pathToVideoFolder]
```
example: `videoToimages --videoFolder "c:/videos"`

Running the above command will generate images from the video and store in the directory `imagesConverted` in the videos folder. 
Alternatively, you can also pass output folder name: `--outFolder`

### Convert video folder to images at specific rate (fps)
```py
videoToimages --videoFolder [pathToVideoFolder] --fps 10
```
example: `example: videoToimages --videoFolder "c:/videos" --fps 10`

This command will capture 10 frames from each second of video data. You can use any `integer value < original fps`. 

#  Useful Arguments
- `--videoFolder` - (string) Full path of path of folder containing videos. example: `~/videos`
- `--outFolder` - (string) Full path of path of folder to store output images (.png). example: `~/videos/images`
- `--fps` - (int) sampling rate per second from the videos. example: `15`
- `--img_size` - (tuple) or (int) resize output images to specific size. example: `(512, 512)`

# License
Apache-2.0 License