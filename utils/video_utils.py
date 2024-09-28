import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames, output_video_path, fps=25):
    height, width, layers = output_video_frames[0].shape
    size = (width, height)
    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'XVID'), fps, size)

    for frame in output_video_frames:
        out.write(frame)
    out.release()

    


