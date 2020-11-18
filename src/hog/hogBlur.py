import cv2
from imutils import face_utils


def face_blur(frame, faces):
    face_count = 1

    for (i, faces) in enumerate(faces):
        if:
            
        # create object based on retrieved dimensions
        (x, y, w, h) = face_utils.rect_to_bb(faces)
        box = frame[y:y + h, x:x + w]

        # TODO fix this debug issue
        try:
            box = cv2.GaussianBlur(box, (99, 99), 25)

        except:
            break

        # overlay object on frame
        frame[y:y + box.shape[0], x:x + box.shape[1]] = box

        # output face coordinates
        print("Face:", face_count, faces)
        face_count += 1
        cv2.imshow('Video', frame)
