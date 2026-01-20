# AI Football Analyzer

**AI Football Analyzer** is a football analysis project using Python and Computer Vision.  
Goal: Track players and the ball, analyze tactics, and display results in an interactive interface.

---

## Project Structure
football-analyzer/
├─ src/
│ ├─ pipeline.py # End-to-End pipeline
│ └─ utils/
│ ├─ video_utils.py # Video reading and frame extraction
│ ├─ visualization.py # Drawing bounding boxes and IDs
│ └─ file_io.py # Saving and loading JSON
├─ streamlit_app.py # Streamlit interface
├─ data/
│ └─ input/
│ └─ test.mp4 # Sample input video
├─ outputs/
│ ├─ videos/
│ └─ json/
└─ README.md

## Running the Project
  1- Run the Pipeline independently (Dummy Tracker):
      python -m src.pipeline

  2- Run Streamlit interface:
      streamlit run streamlit_app.py


## Upload a video

    Click Analyze

    View the output video and JSON results

## Notes

   Currently, the pipeline uses a Dummy Tracker.

   YOLO and ByteTrack integration will be added later for real detection and tracking.

   The pipeline is ready to handle real video analysis once the AI modules are integrated.

## Today's Output

  Dummy output video

  Dummy JSON file

  Working Streamlit interface