import cv2

face_cascade = cv2.CascadeClassifier('9-haarcascade_frontalface_default.xml')

image_name = 'TICs.png'
flag = input(
    'Read the image from File or Camera? (Choose one of the two.)  ').lower().strip()
if flag == 'file':
    image_original = cv2.imread(image_name)
elif flag == 'camera':
    image_cam = cv2.VideoCapture(0)
    _, image_original = image_cam.read()
image_detected = image_original.copy()

# taking out the extension of the file .jpg, .png, among others
ext = image_name.find('.')
ext_in = image_name[ext:]


'''face_detected_name = image_name[:ext] + '_detected.jpg' '''
ext_out = '.jpg'
face_detected_name = 'Face_Detected_' + image_name[:ext] + ext_out
message = 'Found You!'

gray = cv2.cvtColor(image_detected, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(image_detected, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(image_detected, message, org=(x, y), fontFace=0,
                fontScale=1.3, color=(0, 0, 255), thickness=2)


# Part that shows the images and save the result
'''
The part starts with the original image shown

A variable k is created to translate the key pressed into its value. This
value is used to make the actions in the while loop, and to get out of it.

the actions are:
o - open the Original image
d - open the Detected image
s - Save the detected image into a file
c - Clear all the image windows
a - Capture again the image from the Camera
q - quit program
'''
k = 1
while k != 27:  # wait for ESC key to exit
    if k == 1:
        if flag == 'file':
            cv2.imshow(image_name[:ext], image_original)
        else:
            _, image_original = image_cam.read()
            image_detected = image_original.copy()
            cv2.imshow(image_name[:ext], image_original)

    k = cv2.waitKey(0) & 0xFF  # & 0xFF selects only the first 8 bits
    # print(k)
    if k == ord('o'):  # Pressing o - wait for the 'o' key to shows the original image
        cv2.destroyAllWindows()
        cv2.imshow(image_name[:ext], image_original)
    elif k == ord('d'):  # Presing d - wait for the 'd' key to shows the detected image
        cv2.imshow(face_detected_name, image_detected)
    elif k == ord('s'):  # Pressing s - wait for 's' key to save and exit
        cv2.imwrite(face_detected_name, image_detected)
    elif k == ord('c'):
        cv2.destroyAllWindows()
    elif flag == 'camera' and k == ord('a'):
        cv2.destroyAllWindows()
        _, image_original = image_cam.read()
        image_detected = image_original.copy()
        gray = cv2.cvtColor(image_detected, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(image_detected, (x, y),
                          (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(image_detected, message, org=(x, y),
                        fontFace=0, fontScale=1.3,
                        color=(0, 0, 255), thickness=2)
        # cv2.imshow(image_name[:ext], image_original)
        cv2.imshow(face_detected_name, image_detected)
    elif k == ord('q'):
        break

image_cam.release()

# input('\n\n\n')
# Other way of doing the stuff
'''show = input('\nDo you want to show the picture? (yes / no)\n').strip().lower()
if show == 'yes':
    time = int(
        input('\nHow may seconds the image will be displayed? \n')) * 1000

    cv2.imshow(image_name[:ext], image_original)
    cv2.waitKey(time)  # in miliseconds
    cv2.imshow(face_detected_name, image_detected)
    cv2.waitKey(time)  # in miliseconds

    cv2.destroyAllWindows()'''


'''save_image = input(
    '\nDo you want to save the new image? (yes / no)\n').strip().lower()
if save_image == 'yes':
    cv2.imwrite(face_detected_name, image_detected)
else:
    pass'''
