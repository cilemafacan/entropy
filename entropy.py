 
import numpy as np
from PIL import Image

 
image1 = Image.open("images/image1.png").convert("L")
image2 = Image.open("images/image2.png").convert("L")
 
def calculate_histogram_and_probabilities(image):
    histogram = np.zeros(256)
    for pixel in image.getdata():
        histogram[pixel] += 1

    pmf = np.zeros(256)
    for i in range(256):
        pmf[i] = histogram[i] / (image.size[0] * image.size[1])

    print("Histogram: ", histogram[0])
    print("PMF: ", pmf[0])
    return histogram, pmf

 
def plot_histogram(histogram):
    import matplotlib.pyplot as plt
    plt.plot(histogram)
    plt.show()

 
image1_histogram, image1_prob = calculate_histogram_and_probabilities(image1)
image2_histogram, image2_prob = calculate_histogram_and_probabilities(image2)

plot_histogram(image1_histogram)
plot_histogram(image2_histogram)

print(len(image1_prob))
print(len(image2_prob))

 
def calculate_entropy(probabilities):
    total = 0
    for i in range(256):
        total += probabilities[i] * np.log2(probabilities[i])

    return -total

 
entropy_1 = calculate_entropy(image1_prob)
entropy_2 = calculate_entropy(image2_prob)

print(f"Entropy of image 1: {entropy_1}")
print(f"Entropy of image 2: {entropy_2}")

 



