from ultralytics import solutions

inf = solutions.Inference(
    model="./wts/yolov11.pt"
)

inf.inference()

### Make sure to run the file using command `streamlit run <file-name.py>`