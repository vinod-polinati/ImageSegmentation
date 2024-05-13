import cv2
import numpy as np
import os

def find_orientation(template_path, test_path):
    # Load images
    template = cv2.imread(template_path, 0)  # Load in grayscale
    test_img = cv2.imread(test_path)
    test_gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(template, None)
    kp2, des2 = orb.detectAndCompute(test_gray, None)

    # Create BFMatcher object and match descriptors
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    # Sort matches by distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros_like(points1)
    for i, match in enumerate(matches):
        points1[i, :] = kp1[match.queryIdx].pt
        points2[i, :] = kp2[match.trainIdx].pt

    # Find homography
    H, _ = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography to transform the template image corners to the test image
    h, w = template.shape
    corners = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
    transformed_corners = cv2.perspectiveTransform(corners, H)

    # Draw boundary
    boundary = np.int32(transformed_corners)
    # Drawing the polygon around the detected object more visibly
    cv2.polylines(test_img, [boundary], True, (0, 255, 255), 3)  # Changed color and thickness

    # Calculate rotation angle
    theta = -np.arctan2(H[0, 1], H[0, 0]) * (180 / np.pi)

    # Annotate test image with rotation
    cv2.putText(test_img, f"Rotation: {theta:.2f} degrees", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)  # Changed text color

    # Create output directory if it doesn't exist
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save annotated image to the output folder
    output_file = os.path.join(output_folder, os.path.basename(test_path))
    cv2.imwrite(output_file, test_img)

    print(f"Annotated image saved: {output_file}")

# Example usage
template_path = 'template images/screenshot_2024-05-02_17-12-17.jpg'
test_path = 'test images/15.jpg'
find_orientation(template_path, test_path)
