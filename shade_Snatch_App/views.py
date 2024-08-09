from django.shortcuts import render, HttpResponse
from .models import Image
import cv2 as cv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
# Create your views here.
def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_image(image_path):
    image = cv.imread(image_path)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return image

def get_colors( image, number_of_colors, show_chart):
    modified_image = cv.resize(image, (600, 400), interpolation = cv.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)

    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)

    counts = Counter(labels)

    center_colors = clf.cluster_centers_
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]

    return hex_colors

def get_total_colors(path):

    img= cv.imread(path)

    height, width, channels= img.shape

    color_dict = {}
    for y in range(height):
        for x in range(width):
            bgr_color = tuple(img[y, x])
            rgb_color = (bgr_color[2], bgr_color[1], bgr_color[0])

            if rgb_color in color_dict:
                color_dict[rgb_color] += 1
            else:
                color_dict[rgb_color] = 1

    total_colours= len(color_dict.keys())
    return total_colours


def index(request):
    if request.method == 'POST':
        uploaded_image = request.FILES.get('image')
        if uploaded_image:
            image_upload = Image.objects.create(image=uploaded_image)
            image_path= image_upload.image.url
            image_path_for_html= image_path[1:]
            path="/_Coding/openCV/Projects/real_world_projects/ShadeSnatch/shade_Snatch_App/static"
            image_absolute_path= str("E:"+path+image_path)

            dominent_colours= get_colors(get_image(f"{image_absolute_path}"), 20, True)
            total_colors= get_total_colors(f"{image_absolute_path}")
            output={
                'hexcodes': dominent_colours,
                'image_path': image_path_for_html,
                'total_colors': total_colors,
            }
            return render(request,'index.html', {'output': output})
        else:
            return HttpResponse("Image not found")
    else:
        path= "/_Coding/openCV/Projects/real_world_projects/ShadeSnatch/shade_Snatch_App/static/images/banner-bg.jpg"
        image_absolute_path= str("E:"+path)

        image_path_for_html= "./../static/images/banner-bg.jpg"

        dominent_colours= get_colors(get_image(f"{image_absolute_path}"), 20, True)
        total_colors= get_total_colors(f"{image_absolute_path}")

        output={
            'hexcodes': dominent_colours,
            'image_path': image_path_for_html,
            'total_colors': total_colors
        }
        return render(request,'index.html', {'output': output})