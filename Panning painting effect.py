import cv2
import numpy as np

image = cv2.imread("example.png")
rows, cols, _ = image.shape

for i in range(100):
    # 创建仿射变换矩阵
    M = np.float32([[1, 0, i], [0, 1, i]])
    shifted_image = cv2.warpAffine(image, M, (cols, rows))
    cv2.imshow("Translated", shifted_image)
    cv2.waitKey(100)

cv2.destroyAllWindows()
