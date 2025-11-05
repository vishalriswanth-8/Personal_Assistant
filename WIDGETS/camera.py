import cv2

def capture_image(image_path="captured_image.jpg"):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(image_path, frame)
        cap.release()
        return image_path
    else:
        cap.release()
        print("Failed to capture image.")
        return None