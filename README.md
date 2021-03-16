# Angle-finder-using-OpenCV

Simple angle finder between Points using OpenCv <br>
Purpose: learning openCv

 <img src="https://github.com/HarshitDolu/Face-Recognition-Attendance-System/blob/main/Screenshot%20(386).png" width="900">

This project is find the exact angle between points selected on any test image<br>
concept is simple:
1. using mouse events to extract the coordinates in image.<br>
2. put the points in list.<br>
3. create a function that calculates slope of line using 2 points.<br>
4. use tan @ = abs(m1-m2)/(1+m1*m2), and find angle(radians) convert into degree.<br>
5. use cv2.line and cv2.putText for displaying it on image.<br>
