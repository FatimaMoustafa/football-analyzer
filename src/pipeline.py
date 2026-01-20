from src.utils.video_utils import read_video
from src.utils.visualization import draw_tracks
from src.utils.file_io import save_json

import cv2
def dummy_tracker(frame_id):
    """
    Simulate tracking output
    """
    tracks = [
        {
            "bbox": (100 + frame_id, 50, 200 + frame_id, 150),
            "id": 1,
            "team": 0
        },
        {
            "bbox": (300, 100 + frame_id, 400, 200 + frame_id),
            "id": 2,
            "team": 1
        }
    ]
    return tracks

def run_pipeline(video_path, output_path):
    frames = read_video(video_path)

    results = []
    output_frames = []

    for frame_id, frame in enumerate(frames):
        tracks = dummy_tracker(frame_id)
        frame = draw_tracks(frame, tracks)
        output_frames.append(frame)

        for t in tracks:
            results.append({
                "frame": frame_id,
                "id": t["id"],
                "team": t["team"],
                "bbox": t["bbox"]
            })

    save_json(results, "outputs/json/tracks.json")

    # Save output video
    height, width, _ = output_frames[0].shape
    out = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        25,
        (width, height)
    )
    for f in output_frames:
        out.write(f)
    out.release()

    return output_path, "outputs/json/tracks.json"


if __name__ == "__main__":
    run_pipeline(
        video_path="data/input/test.mp4",
        output_path="outputs/videos/output.mp4"
    )
