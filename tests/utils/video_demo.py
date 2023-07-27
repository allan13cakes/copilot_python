import os

import cv2

from config import ROOT_DIR


def update_video(file_path, output_file):
    cap = cv2.VideoCapture(file_path)

    # Get the video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"{fps},{width},{height}")

    # Create a VideoWriter object to write the output video
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    # out = cv2.VideoWriter(output_file, fourcc, 30.0, (width//2, height//2))
    out = cv2.VideoWriter(output_file, fourcc, 10.0, (width, height))

    # Loop through the frames of the input video
    # while cap.isOpened():
    #     ret, frame = cap.read()
    #     if ret:
    #         frame = cv2.resize(frame, (width // 2, height // 2))
    #         out.write(frame)
    #         # cv2.imshow('frame', frame)
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break
    #     else:
    #         break
    # Loop through the frames and write every other frame
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if count % 6 == 0:
                out.write(frame)
            count += 1
            # cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release the resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()


# Open the input video file
input_file_folder = f"{ROOT_DIR}/video/python automation"

# Get a list of all files in the folder
file_list = os.listdir(input_file_folder)
for file_input in file_list:
    # Print the list of files
    print(file_input)
    print(type(file_input))
    update_video(input_file_folder + '/' + file_input, file_input)
