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
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    # rgb_colors = [ordered_colors[i] for i in counts.keys()]

    return hex_colors


def index(request):
    if request.method == 'POST':
        uploaded_image = request.FILES.get('image')
        if uploaded_image:
            print(uploaded_image)
            print("file fetched")
            image_upload = Image.objects.create(image=uploaded_image)
            print("file object created")
            number = image_upload.number  # Retrieve the auto-incremented number
            # print(number)
            image_path= image_upload.image.url
            print("file url fetched")
            image_path_for_html= image_path[1:]
            print("Media path :",image_path_for_html)
            path="/_Coding/openCV/Projects/real_world_projects/ShadeSnatch/Shade_Snatch/shade_Snatch_App/static"
            # image_absolute_path = os.path.join(settings.MEDIA_ROOT,image_path)
            image_absolute_path= str("E:"+path+image_path)
            # print(image_absolute_path)
            # img= cv.imread(f"{image_absolute_path}")

            dominent_colours= get_colors(get_image(f"{image_absolute_path}"), 20, True)
            # print(dominent_colours)
            output={
                'hexcodes': dominent_colours,
                'image_path': image_path_for_html
            }
            return render(request,'index.html', {'output': output})
        else:
            return HttpResponse("Image not found")
    else:
        path= "/_Coding/openCV/Projects/real_world_projects/ShadeSnatch/Shade_Snatch/shade_Snatch_App/static/images/banner-bg.jpg"
        image_absolute_path= str("E:"+path)

        # image_path_for_html= image_path[1:]
        image_path_for_html= "./../static/images/banner-bg.jpg"
        # print(image_absolute_path)
        # img= cv.imread(f"{image_absolute_path}")

        dominent_colours= get_colors(get_image(f"{image_absolute_path}"), 20, True)
            # print(dominent_colours)
        output={
            'hexcodes': dominent_colours,
            'image_path': image_path_for_html
        }
        return render(request,'index.html', {'output': output})

def image_processing(request):
    if request.method == 'POST':
        uploaded_image = request.FILES.get('image')
        if uploaded_image:
            image_upload = Image.objects.create(image=uploaded_image)
            number = image_upload.number  # Retrieve the auto-incremented number
            # print(number)
            image_path= image_upload.image.url
            image_path_for_html= image_path[1:]
            print("Media path :",image_path_for_html)
            path="/_Coding/openCV/Projects/real_world_projects/ShadeSnatch/Shade_Snatch/shade_Snatch_App/static"
            # image_absolute_path = os.path.join(settings.MEDIA_ROOT,image_path)
            image_absolute_path= str("E:"+path+image_path)
            # print(image_absolute_path)
            # img= cv.imread(f"{image_absolute_path}")

            dominent_colours= get_colors(get_image(f"{image_absolute_path}"), 20, True)
            # print(dominent_colours)
            output={
                'hexcodes': dominent_colours,
                'image_path': image_path_for_html
            }
            return render(request,'index.html', {'output': output})
    else:
        return render(request, 'index.html')