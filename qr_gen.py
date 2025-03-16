import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
import os

# Get the user's Downloads folder (Mac & Windows compatible)
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Streamlit App UI
st.title("🎭 BookMyShow QR Code Generator")

# User Input for BookMyShow Play Link
url = st.text_input("🔗 Enter your BookMyShow play link:", "")

if url:
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create QR Code Image
    qr_img = qr.make_image(fill="black", back_color="white")

    # Convert PIL Image to BytesIO (Fix for Streamlit)
    img_io = BytesIO()
    qr_img.save(img_io, format="PNG")
    img_io.seek(0)

    # Display the QR Code using BytesIO object
    st.image(img_io, caption="📸 Your Generated QR Code", use_column_width=False)

    # Save QR Code to Downloads Folder
    qr_filename = os.path.join(downloads_folder, "bookmyshow_qr.png")
    qr_img.save(qr_filename)

    # Show success message
    st.success(f"✅ QR Code saved to: {qr_filename}")

    # Download Button (direct download from browser)
    st.download_button(
        label="📥 Download QR Code",
        data=img_io,
        file_name="bookmyshow_qr.png",
        mime="image/png"
    )
else:
    st.warning("🚀 Enter your BookMyShow play link above to generate a QR code.")
