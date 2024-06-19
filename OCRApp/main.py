import streamlit as st
from PIL import Image, ImageDraw
import pytesseract
from pytesseract import TesseractNotFoundError

def main():
    st.title("OCR App")
    st.write("Upload an image for text extraction:")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            
            if st.button('Extract Text'):
                text, bounding_boxes = extract_text(image)
                st.write("Extracted Text:")
                st.write(text)
                
                # Draw bounding boxes on the image
                drawn_image = draw_boxes(image, bounding_boxes)
                st.image(drawn_image, caption='Image with Bounding Boxes', use_column_width=True)
        except TesseractNotFoundError:
            st.error("Tesseract OCR is not installed or cannot be found.")
            st.write("Please refer to the installation instructions in the app's documentation.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

def extract_text(image):
    # Use pytesseract to extract text and bounding boxes from the image
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    
    text = ""
    bounding_boxes = []
    for i in range(len(data['text'])):
        # Skip empty text and non-confident detections
        if data['text'][i].strip() != "" and int(data['conf'][i]) > 0:
            text += data['text'][i] + " "
            left = data['left'][i]
            top = data['top'][i]
            width = data['width'][i]
            height = data['height'][i]
            bounding_boxes.append((left, top, left+width, top+height))
    
    return text, bounding_boxes

def draw_boxes(image, bounding_boxes):
    drawn_image = image.copy()
    draw = ImageDraw.Draw(drawn_image)
    for box in bounding_boxes:
        draw.rectangle(box, outline="red", width=2)
    return drawn_image

if __name__ == '__main__':
    main()
