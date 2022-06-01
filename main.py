from PIL import Image, ImageDraw
import operator
import sys
import numpy as np

import upscale


active = True

while active:

    # Get user input for image to upscale + checks if valid path
    try:
        img_path = input('\nPath to image: ')

        # Open image that user selected and assign it to 'img'
        img = Image.open(img_path)

    except:
        print('Invalid path!')
        sys.exit()

    # Get user input for upscale factor
    up_factor = float(input('Enter upscale factor (only 4 works rn): '))

    # Check if input is power of 2 ny checking if log nase 2 of it is whole number
    if up_factor != 4:
        print('Invalid upscale factor!')
        sys.exit()

    # Open image that user selected and assign it to 'img'
    img = Image.open(img_path)

    # Define the dimensions of the image
    width = img.size[0]
    height = img.size[1]

    # Determine size of upscaled image based on upscale factor
    pixel_count = (width*height)
    new_pixel_count = pixel_count * up_factor

    # This check is useless for now but when I add 2x and 8x support it will be useful
    if up_factor == 2:
        up_res_width = int(np.round(width*(np.sqrt(up_factor))))
        up_res_height = int(np.round(height*(np.sqrt(up_factor))))
    else:
        up_res_width = int(np.round(width*(np.log2(up_factor))))
        up_res_height = int(np.round(height*(np.log2(up_factor))))

    # Print original image size and upscaled image size to user
    print('Upscale factor: ' + str(up_factor) + 'x')
    print('\nOld image size: ' + str(width) + 'x' + str(height))
    print('Upscaled image size: ' + str(up_res_width) + 'x' + str(up_res_height))

    # Run the main function
    if up_factor == 2:
        print('Not supported yet sorry!')
        sys.exit()
    elif up_factor == 4:
        upscale.fourx(img, up_factor, up_res_width, up_res_height)
    else:
        print('Not supported yet sorry!')
        sys.exit()
