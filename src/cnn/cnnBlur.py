import cv2


def face_blur(frame, faces):
    face_count = 0
    for faceRect in faces:
        # retrieve dimensions on detected face
        rect = faceRect.rect
        x = rect.left()
        y = rect.top()
        w = rect.right() - x
        h = rect.bottom() - y

        # create object based on retrieved dimensions
        box = frame[y:y + h, x:x + w]
        box = cv2.GaussianBlur(box, (23, 23), 30)
        # overlay object on frame
        frame[y:y + box.shape[0], x:x + box.shape[1]] = box
        face_count += 1

        if face_count == len(faces):
            print("Face:", face_count)
            print("----------------------")

        else:
            print("Face:", face_count)
            cv2.imshow('Output', frame)
