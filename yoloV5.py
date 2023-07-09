from distutils.sysconfig import get_python_inc
import cv2
import matplotlib.pyplot as plt
get_python_inc().run_line_magic('matplotlib', 'inline')

image = cv2.imread("inference/output/zidane.jpg")
height, width = image.shape[:2]
resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)

fig = plt.gcf()
fig.set_size_inches(18, 10)
plt.axis("off")
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.show()



