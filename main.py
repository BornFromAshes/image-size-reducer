import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np

image = im.imread('1.bmp')
r = image[:, :, 0]
g = image[:, :, 1]
b = image[:, :, 2]

Ur, Sr, VTr = np.linalg.svd(r, full_matrices=False)
Ug, Sg, VTg = np.linalg.svd(g, full_matrices=False)
Ub, Sb, VTb = np.linalg.svd(b, full_matrices=False)
Sr = np.diag(Sr)
Sg = np.diag(Sg)
Sb = np.diag(Sb)

k = 250
approx_r = Ur[:, :k] @ Sr[0:k, :k] @ VTr[:k, :]
approx_g = Ug[:, :k] @ Sg[0:k, :k] @ VTg[:k, :]
approx_b = Ub[:, :k] @ Sb[0:k, :k] @ VTb[:k, :]

new_image = np.zeros((1280, 1920, 3))
new_image[:, :, 0] = approx_r
new_image[:, :, 1] = approx_g
new_image[:, :, 2] = approx_b
new_image = new_image.astype(int)

img = plt.imshow(new_image)
plt.axis('off')
plt.show()
