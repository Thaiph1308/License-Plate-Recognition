from recognition import E2E
import cv2
from pathlib import Path
import argparse
import time


def get_arguments():
    arg = argparse.ArgumentParser()
    arg.add_argument('-i', '--image_path', help='link to image', default='./data/example/0243_08319_b.jpg')
    arg.add_argument('-d', '--display_img', help='display img or not', default=1)

    return arg.parse_args()


args = get_arguments()
img_path = Path(args.image_path)
display = args.display_img

# read image
img = cv2.imread(str(img_path))

# start
start = time.time()

# load model
model = E2E()

# recognize license plate
image = model.predict(img)

# end
end = time.time()

print('Model process on %.2f s' % (end - start))

# show image
cv2.imshow('License Plate', image)
if cv2.waitKey(0) & 0xFF == ord('q'):
    exit(0)


cv2.destroyAllWindows()