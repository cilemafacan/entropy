import io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def calculate_histogram_and_probabilities(image):
    histogram = np.zeros(256)
    for pixel in image.getdata():
        histogram[pixel] += 1

    pmf = np.zeros(256)
    for i in range(256):
        pmf[i] = histogram[i] / (image.size[0] * image.size[1])
    return histogram, pmf

def calculate_entropy(probabilities):
    total = 0
    for i in range(256):
        if probabilities[i] != 0:
            total += probabilities[i] * np.log2(probabilities[i])
    return -total


def apply_entropy(inp1, inp2):
    inp1 = inp1.convert("L")
    inp2 = inp2.convert("L")
    _, pmf1 = calculate_histogram_and_probabilities(inp1)
    _, pmf2 = calculate_histogram_and_probabilities(inp2)
    return calculate_entropy(pmf1), calculate_entropy(pmf2)

def plot_histogram(inp1, inp2):
    inp1 = inp1.convert("L")
    inp2 = inp2.convert("L")
    histogram1, _ = calculate_histogram_and_probabilities(inp1)
    histogram2, _ = calculate_histogram_and_probabilities(inp2)
    
    fig1, ax1 = plt.subplots()
    ax1.plot(histogram1)
    ax1.set_title("Histogram of Image 1")
    ax1.set_xlabel("Pixel Value")
    ax1.set_ylabel("Frequency")

    fig2, ax2 = plt.subplots()
    ax2.plot(histogram2)
    ax2.set_title("Histogram of Image 2")
    ax2.set_xlabel("Pixel Value")

    buf1 = io.BytesIO()
    fig1.savefig(buf1, format="png")
    buf1.seek(0)
    buf2 = io.BytesIO()
    fig2.savefig(buf2, format="png")
    buf2.seek(0)

    hist1 = Image.open(buf1).convert("RGB")
    hist2 = Image.open(buf2).convert("RGB")

    return hist1, hist2