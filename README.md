### Template Matching and Orientation Detection using OpenCV

This repository contains a Python script for template matching and orientation detection in images using OpenCV. The script utilizes keypoint detection, feature matching, homography estimation, and rotation angle calculation to identify and annotate the orientation of a template image within a larger test image.

#### Prerequisites
- Python 3.x
- OpenCV (`pip install opencv-python`)

#### Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/vinod-polinati/ImageSegmentation.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ImageSegmentation
   ```

3. Run the `salam.py` script with the paths to your template and test images as arguments:
   ```bash
   python salam.py --template <path_to_template_image> --test <path_to_test_image>
   ```
   Replace `<path_to_template_image>` and `<path_to_test_image>` with the file paths of your images.

#### Description
The `salam.py` script performs the following steps:

1. **Image Loading:** Load the template image and the test image.
2. **Feature Detection and Description:**
   - Use the ORB (Oriented FAST and Rotated BRIEF) detector to find keypoints and compute descriptors for both images.
3. **Feature Matching:**
   - Match the descriptors of the template image with those of the test image using a Brute-Force matcher.
4. **Homography Estimation:**
   - Calculate the homography matrix using RANSAC (Random Sample Consensus) to find a perspective transformation between the keypoints.
5. **Transform Template Corners:**
   - Use the homography matrix to transform the corners of the template image onto the test image.
6. **Rotation Angle Calculation:**
   - Determine the rotation angle based on the homography matrix.
7. **Annotate Test Image:**
   - Draw a polygon around the detected object (template) on the test image and annotate the rotation angle.
8. **Display Result:**
   - Show the annotated test image with the detected object and rotation angle.

#### Example
```python
salam('template_images/screenshot_template.jpg', 'test_images/screenshot_test.jpg')
```

#### Note
- Ensure that the specified paths to the template and test images are correct.
- The script will display the annotated test image in a window. Press 'Q' to close the window and end the script.

#### References
- [OpenCV Documentation](https://opencv.org/)
- [ORB (Oriented FAST and Rotated BRIEF) Detector](https://docs.opencv.org/master/d1/d89/tutorial_py_orb.html)
- [Homography Estimation](https://docs.opencv.org/master/d9/dab/tutorial_homography.html)

Feel free to modify and integrate this script into your projects for template matching and orientation detection tasks.
