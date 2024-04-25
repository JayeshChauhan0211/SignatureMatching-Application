import cv2
from skimage.metrics import structural_similarity as ssim

def match():
    sign1 = cv2.imread(".\\runtimeAssets\sign1.png")
    sign2 = cv2.imread(".\\runtimeAssets\sign2.png")
    sign1 = cv2.cvtColor(sign1, cv2.COLOR_BGR2GRAY)
    sign2 = cv2.cvtColor(sign2, cv2.COLOR_BGR2GRAY)
    sign1 = cv2.resize(sign1, (300, 300))
    sign2 = cv2.resize(sign2, (300, 300))
    similarity_index = "{:.2f}".format(ssim(sign1, sign2) * 100)
    return float(similarity_index)