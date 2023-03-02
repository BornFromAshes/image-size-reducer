# image-size-reducer
One of the applications of SVD analysis is to reduce the volume of data. In this project, we want to compress uncompressed BMP photos using SVD and reduce their size.
## BMP format
In BMP format, compression is not done on the photo and the pixel information is stored in raw form and as a number between 0 and 255. BMP file in RGB images consists of 3 2D arrays, each of these arrays corresponds to a color channel. To open a BMP file in Python, we used the imread function and to display it, we used the imshow function in the matplotlib library.
## Size reduction
Steps taken:
1. We separated different color channels and stored them in separate matrices. <br>
![image](https://user-images.githubusercontent.com/117355603/222471417-dfb8c646-7fad-4660-bc96-1be795f370ec.png)
2. With the help of library functions, we calculated the SVD decomposition for each of the 3 matrices in the previous step (svd function in numpy). The decomposition result is as follows: <br>
![image](https://user-images.githubusercontent.com/117355603/222471592-433c68a9-c492-49df-b57f-c25f1802de81.png) <br>
The above expression can be written as follows: <br>
![image](https://user-images.githubusercontent.com/117355603/222471810-e866eea6-5803-4d90-ac08-857068f24edb.png) <br>
Since the singular values in the diameter of the 𝚺 matrix are arranged in descending order, the effect of the first sentences of the above sentence is greater than the following sentences. As a result, considering 𝒌 the first term, we can have a good estimate of the initial matrix. which means: <br>
![image](https://user-images.githubusercontent.com/117355603/222472026-60000783-b734-4246-b785-d26658985c2d.png) <br>

<br>
Note that since the matrix of the resulting image is the same size as the original matrix, it seems that compression has not been done here. But be careful, here we don't need to store the final matrix for the photo, but it is enough to store the columns that correspond to the initial 𝒌 term of the SVD expansion and reproduce it when 𝑻 from 𝑼, singular values 𝚺 and rows from 𝑽 display the photo.

### Example
For example, if we store an RGB image with dimensions of 1920 x 1080, we need 1920 x 1080 x 3 = 6,220,800 units in its matrix. But if we store it through SVD expansion up to the sentence 150 = 𝒌, we need to store 150 columns of 𝑼, 150 single values and 150 rows of Vt. That means we need to store 3 * (150 * 1920 + 150 + 150 * 1080) = 1,350,450 entries. As a result, the original image is reduced by about 4,6 times.











