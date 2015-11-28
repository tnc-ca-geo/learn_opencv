import os
import cv2

IMAGE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img/')

def main():
    img_location = '%srabbit.jpg' % IMAGE_FOLDER
    img = cv2.imread(img_location, 0)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
