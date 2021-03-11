import numpy as np
from PIL import Image

class ImageLoader:
    def __init__(self):
        pass

    def __call__(self, path):
        X = None
        y = None

        img = Image.open(path)
        img = np.asarray(img)
        img = img / 255



        print(img.shape)

        return X, y


if __name__ == "__main__":
    imgLoader = ImageLoader()
    X, y = imgLoader("data/kodim01.png")
    print(X.shape,
          y.shape,
          X.shape[0] == 768*512,
          X.shape[1]==2,
          y.shape[0] == X.shape[0],
          y.shape[1]==3)