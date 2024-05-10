from fastapi import FastAPI, UploadFile, File, Response
from PIL import Image
import io
import os
import numpy as np
import torch
from mobile_sam import SamAutomaticMaskGenerator, SamPredictor, sam_model_registry
from tools import fast_process
from main import segment_everything

app = FastAPI()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

sam_checkpoint = "./mobile_sam.pt"
model_type = "vit_t"

mobile_sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
mobile_sam = mobile_sam.to(device=device)
mobile_sam.eval()

mask_generator = SamAutomaticMaskGenerator(mobile_sam)
predictor = SamPredictor(mobile_sam)


@app.post("/segment-image")
async def segment_image(file: UploadFile = File(...)):
    # Read image file
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    
    # Segment the image using the `segment_everything` function
    segmented_image = segment_everything(image)
    
    # Convert the segmented image to bytes
    img_byte_array = io.BytesIO()
    segmented_image.save(img_byte_array, format='PNG')
    
    # Return the segmented image as binary data without attempting to decode it
    return Response(content=img_byte_array.getvalue(), media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
