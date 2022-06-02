# upscalr
No AI image upscaler that uses watered down bilinear interpolation to create new pixels
![demo](https://user-images.githubusercontent.com/49793238/171527854-bb9fb0ca-2c3a-471f-8da0-ce875e6c5f0a.png)

##

The original inspiration for this project came from the slow, resource heavy nature of AI upscaling. If you want to upscale a say 1080p movie to 4k, you will have to wait days to weeks depending on your hardware. While this algorithm doesn't solve this problem yet, as it is still slow and doesnt support video yet, I will be working to improve the speed. For now, it is just a simplified upscaler that can upscale JPEGs.

Current limitations:
- No GUI
- JPEG only
- 4x upscale only
- messy code

## Installation

- Download the code as a .zip
- Extract archive
- Open a terminal in the folder
- Run the main.py file using:
`>>> python3 main.py`

## Usage

Once program is run, the following prompts will be displayed:

`Path to image:` 
Type in the path of the image you want to upscale.
It may be easiest to simply move the image into the same folder as `main.py` and type the name of the file in the prompt.

`Enter upscale factor:` 
Due to the unfinished nature of this project, you can currently only type `4` for this prompt.
This will quadruple the amount of pixels in your image and double the height and width.

Once you submit these prompts, the program will start running and will eventually display the upscaled image. To save it, you have to save it using the image viewer. `Ctrl+Shift+S` may also work. Note: the image will not be saved unless you manually save it as a file.

Here are the original images used for the demo above:

https://ibb.co/FXz8FHH - Downscaled image to input into program

https://ibb.co/ctCJFw3 - Source image to compare output to

#
