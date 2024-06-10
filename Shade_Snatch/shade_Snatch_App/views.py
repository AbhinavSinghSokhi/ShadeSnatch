from django.shortcuts import render
from .models import Image
import cv2 as cv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
# Create your views here.
def index(request):
    return render(request,"index.html")

def image_processing(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            image_upload = Image.objects.create(image=image)
            number = image_upload.number  # Retrieve the auto-incremented number
            print(number)
            image_path= image_upload.image.url
            print(image_path)
            path="/_Coding/openCV/Projects/real_world_projects/ShadeSnatch/Shade_Snatch/shade_Snatch_App/static"
            # image_absolute_path = os.path.join(settings.MEDIA_ROOT,image_path)
            image_absolute_path= str("E:"+path+image_path)
            print(image_absolute_path)
            img= cv.imread(f"{image_absolute_path}")
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
                rgb_colors = [ordered_colors[i] for i in counts.keys()]

        # if (show_chart):
        #     plt.figure(figsize = (8, 6))
        #     plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)

                return rgb_colors
        get_colors(get_image('/P_20190718_080222.jpg'), 20, True)
    return render(request, 'index.html', {'imagedata': number})
