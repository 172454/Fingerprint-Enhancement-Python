# -*- coding: utf-8 -*-

# Run: python main_enhancement.py "..\images\StockProcessed.png"

import numpy as np
import matplotlib.pylab as plt;
import scipy.ndimage
import sys
import imageio
import matplotlib

import PIL ##

from image_enhance import image_enhance

from PIL import Image ##

if(len(sys.argv)<2):
    print('loading sample image');
    img_name = '1.jpg'
#    img = scipy.ndimage.imread('../images/' + img_name);
    img = imageio.imread('../images/' + img_name); ##
elif(len(sys.argv) >= 2):
    img_name = sys.argv[1];
#    img = scipy.ndimage.imread(sys.argv[1]);
    img = imageio.imread(sys.argv[1]); ##

if(len(sys.argv) >= 3):
    output_name = sys.argv[2];
else:
    output_name = '../enhanced/' + 'enhanced.png';


# Just a debug check if anything is even happening:
# # matplotlib.image.imsave('../enhanced/' + 'copy-of-input.png', img) ##
# matplotlib.image.imsave('g:/Work/Fingerprints/Fingerprint-Enhancement-Python-master/images/' + 'copy-of-input.png', img) ##

if(len(img.shape)>2):
    img = np.dot(img[...,:3], [0.299, 0.587, 0.114]);

rows,cols = np.shape(img);
aspect_ratio = np.double(rows)/np.double(cols);

new_rows = 350;             #randomly selected number
new_cols = new_rows/aspect_ratio;

#img = scipy.misc.imresize(img,(np.int(new_rows),np.int(new_cols)));
#img = np.array(Image.fromarray(img).resize((int(new_cols), int(new_rows)), Image.LANCZOS)) ##

enhanced_img = image_enhance(img);

if(1):
#    print('saving the image')
#    matplotlib.image.imsave('../enhanced/' + 'enhanced.jpg', enhanced_img)
#    matplotlib.image.imsave('../enhanced/' + 'enhanced.png', enhanced_img) ##
    matplotlib.image.imsave(output_name, enhanced_img) ##
else:
    plt.imshow(enhanced_img,cmap = 'Greys_r');

