import easyocr

# Create the reader
reader = easyocr.Reader(['en'])  # English only; add ['en', 'ne'] for Nepali

# Run OCR
results = reader.readtext('/home/mrkc/Project_Koki/OCR/test_data/1.png')

# Print results
for (bbox, text, prob) in results:
    print(f"Text: {text} (Confidence: {prob:.2f})")
