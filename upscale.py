from PIL import Image, ImageDraw
import operator
import sys
import numpy as np

# Define the function for the 4x upscaling method


def fourx(img, up_factor, up_res_width, up_res_height):

    # Create new image to write to
    upscaled = Image.new('RGB', (up_res_width, up_res_height), 'black')

    # Load the pixel maps
    pm = upscaled.load()
    old_pm = img.load()

    # 1. Go though every pixel in the original image
    for i in range(img.size[0]):
        for j in range(img.size[1]):

            # 2. Find its new location in the upscaled image

            if up_factor == 2:
                w = int(np.sqrt(up_factor)*(i))
                z = int(np.sqrt(up_factor)*(j))
            else:
                w = int(np.log2(up_factor)*(i))
                z = int(np.log2(up_factor)*(j))

            # 3. Paste it there
            pm[w, z] = (old_pm[i, j])

    # Loop through every empty pixel in the new image that has an even x val and even y val -> ones that have colored adjacent pixels to the L and R
    for o in range(upscaled.size[0]):
        if o % 2 == 1:
            for p in range(upscaled.size[1]):

                # Assigns adjacent pixels to variables "left" and "right"
                # Then it takes the avg of adjacent pixels and colors the one in between
                if p % 2 == 0:

                    # Check if pixel is on left edge on image
                    if o == 0:
                        left = (pm[o, p])
                    else:
                        left = (pm[o-1, p])

                    try:
                        right = (pm[o+1, p])

                        add = tuple(map(operator.add, left, right))

                        # Copied from stackoverflow no idea why it works but it does
                        res = tuple(ele1 // ele2 for ele1,
                                    ele2 in zip(add, (2, 2, 2)))

                        # Assign pixel to new pixel map
                        pm[o, p] = res
                    except:

                        # Assign pixel to new pixel map but if pixel is on right edge
                        pm[o, p] = left

    # Do same process but for all empty pixels that are left
    # These remaining blank pixels will be in rows that have an odd x value
    for n in range(upscaled.size[1]):
        if n % 2 == 1:
            for m in range(upscaled.size[0]):

                # Do more checks to see if adjacent pixels are on the edge
                # Assigns adjacent pixels to more variables
                # This average takes in 6 pixels -> upper left, upper right, upper, bottom left, bottom right, bottom
                # Probably need to refactor
                if n == (upscaled.size[1]-1):
                    down = (pm[m, n-1])
                    try:
                        dl = (pm[m-1, n-1])
                    except:
                        dl = (pm[m, n-1])

                    try:
                        dr = (pm[m+1, n+1])
                    except:
                        dr = (pm[m, n-1])
                else:
                    down = (pm[m, n+1])

                    try:
                        dl = (pm[m-1, n+1])
                    except:
                        dl = down

                    try:
                        dr = (pm[m+1, n+1])
                    except:
                        dr = down

                up = (pm[m, n-1])

                try:
                    ul = (pm[m-1, n-1])
                except:
                    ul = up

                try:
                    ur = (pm[m+1, n-1])
                except:
                    ur = up

                # Takes the variables and calculates average
                # I came up with the method so probably slow but we'll see
                red = int((down[0] + up[0] + dl[0] + dr[0] + ul[0] + ur[0])/6)
                green = int(
                    (down[1] + up[1] + dl[1] + dr[1] + ul[1] + ur[1])/6)
                blue = int((down[2] + up[2] + dl[2] + dr[2] + ul[2] + ur[2])/6)

                # Assign pixel to new pixel map
                pm[m, n] = (red, green, blue)

    # Display the image
    upscaled.show()
