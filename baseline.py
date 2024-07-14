import cv2
import cv2.aruco as aruco

def main():
    # Change the index to the correct one for your USB camera
    cap = cv2.VideoCapture(0)  # Replace 1 with the correct index

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Load the dictionary that was used to generate the markers.
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)
    parameters = aruco.DetectorParameters()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the markers in the image
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

        # Draw the markers on the image
        frame = aruco.drawDetectedMarkers(frame, corners, ids)

        cv2.imshow('AR Tag Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
