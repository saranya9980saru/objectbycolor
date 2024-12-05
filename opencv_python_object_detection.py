import cv2
import numpy as np
import os

def nothing(x):
    pass

# Create window
cv2.namedWindow("Tracking")

# Create trackbars for adjusting HSV values
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    # Ensure that the path is correct. You can print the current working directory to verify.
    image_path = r"C:\Users\saranya\OneDrive\Documents\projects\object by color\smarties.png"  # Update this path if needed
    if not os.path.exists(image_path):
        print(f"Error: Image file {image_path} not found!")
        break
    
    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found or unable to read.")
        break

    # Convert image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Get trackbar positions for lower and upper HSV values
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    # Define the lower and upper bounds of the HSV range
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # Apply the mask
    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(image, image, mask=mask)

    # Show the original image, mask, and result
    cv2.imshow("frame", image)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    # Wait for the 'Esc' key to exit
    key = cv2.waitKey(1)
    if key == 27:  # 27 is the ASCII value for the 'Esc' key
        break

# Close all windows after the loop ends
cv2.destroyAllWindows()
