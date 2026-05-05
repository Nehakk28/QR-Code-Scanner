import cv2

last_data = ""   # store last scanned result

def read_qr(frame):
    global last_data
    detector = cv2.QRCodeDetector()

    data, bbox, _ = detector.detectAndDecode(frame)

    if bbox is not None and data:
        if data != last_data:
            print("Scanned:", data)

            with open("scanned_result.txt", "a") as file:
               file.write("The scanned code is :- " + data + "\n")

            last_data = data

        for i in range(len(bbox)):
            cv2.line(frame,
                     tuple(map(int, bbox[i][0])),
                     tuple(map(int, bbox[(i + 1) % len(bbox)][0])),
                     (0, 255, 0), 3)

        cv2.putText(frame, data, (20, 50),
                    cv2.FONT_HERSHEY_DUPLEX,
                    0.8, (220, 20, 60), 2)

    return frame


def main():
    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        frame = read_qr(frame)
        cv2.imshow('QR Scanner', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()