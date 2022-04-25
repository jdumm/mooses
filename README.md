# Mooses

Count how many moosies have gone over the river Älven in Den Stora Älgvandringen!

Status:
* Reads a single frame (screenshot) from a file using OpenCV.
* Looks for the Älg counter in the bottom left corner and reads the digits using pytesseract.
* Draws the extracted number over the screenshot for quality control

Next up:
* Somehow read from the video feed (easiest would be screen capture with Open CV)
