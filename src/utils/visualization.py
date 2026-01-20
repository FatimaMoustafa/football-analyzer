import cv2
import numpy as np

def draw_bbox(frame, bbox, color=(0, 255, 0), label=None, thickness=2):
    """
    Draw a single bounding box on the frame.
    bbox: (x1, y1, x2, y2)
    color: BGR tuple
    label: string (optional)
    """
    x1, y1, x2, y2 = bbox
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)
    
    if label:
        cv2.putText(
            frame, label, (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2
        )
    return frame

def draw_tracks(frame, tracks):
    """
    Draw multiple tracks.
    tracks: list of dicts, each with keys:
        - bbox: (x1, y1, x2, y2)
        - id: int or str
        - team: 0 or 1
    """
    colors = [(0, 0, 255), (0, 255, 0)]  

    for track in tracks:
        bbox = track["bbox"]
        tid = track.get("id", "")
        team = track.get("team", 0)
        color = colors[team % len(colors)]
        label = f"ID:{tid}"
        draw_bbox(frame, bbox, color=color, label=label)
    
    return frame
