import streamlit as st
import subprocess
import os
import io
import glob

# Streamlit app
st.title("File Encryption and Decryption (Text, Audio, and Image)")

# Create a file uploader and radio buttons to select encrypt or decrypt
option = st.radio("Select operation:", ('Encrypt Text', 'Decrypt Text', 'Encrypt Audio', 'Decrypt Audio', 'Encrypt Image', 'Decrypt Image'))

# File uploader for text, audio, or image files
if option == 'Encrypt Audio':
    uploaded_file = st.file_uploader("Upload a .wav file", type="wav")
elif option == 'Decrypt Audio':
    uploaded_file = st.file_uploader("Upload the encrypted .txt file of the audio", type="txt")
elif option == 'Encrypt Image':
    uploaded_file = st.file_uploader("Upload an image file", type=["png", "jpg", "jpeg", "bmp"])
elif option == 'Decrypt Image':
    uploaded_file = st.file_uploader("Upload the encrypted .txt file of the image", type="txt")
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

if uploaded_file is not None:
    input_filename = uploaded_file.name
    input_data = uploaded_file.read()

    # Store file in memory (using io.BytesIO)
    input_file_io = io.BytesIO(input_data)

    # Save the file locally in memory for subprocess execution (only temporarily)
    input_filepath = input_filename  # We use the file name in the same directory.

    # Write the uploaded file to a temporary location (in-memory)
    with open(input_filepath, 'wb') as f:
        f.write(input_file_io.getbuffer())

    # Paths to your C++ binaries
    cpp_encrypt_executable = '../C++/./enc_txt'  # Path to your compiled encryption C++ binary
    cpp_decrypt_executable = '../C++/./dec_txt'  # Path to your compiled decryption C++ binary
    cpp_audio_encrypt_executable = '../C++/./encrypt_audio'  # Path to your compiled audio encryption C++ binary
    cpp_audio_decrypt_executable = '../C++/./decrypt_audio'  # Path to your compiled audio decryption C++ binary
    cpp_image_encrypt_executable = '../C++/./encrypt_image'  # Path to your compiled image encryption C++ binary
    cpp_image_decrypt_executable = '../C++/./decrypt_image'  # Path to your compiled image decryption C++ binary

    def clean_up_directory():
        """Delete all non-Python files in the current directory."""
        for file in glob.glob('*'):
            if not file.endswith('.py'):
                try:
                    os.remove(file)
                except Exception as e:
                    st.error(f"Error while deleting file {file}: {e}")

    if option == 'Encrypt Image':
        # Encrypt the image file
        try:
            # Debugging: Log file input to ensure correct file name
            st.write(f"Encrypting image: {input_filepath}")
            
            # Run the encryption binary
            subprocess.run([cpp_image_encrypt_executable, input_filepath], check=True)

            # Construct the correct output filename based on the input image filename
            output_filename = 'encrypted_image_data.txt'

            # Check if the file exists before proceeding
            if os.path.exists(output_filename):
                # Read the encrypted image text file
                with open(output_filename, 'rb') as f:
                    encrypted_image_data = f.read()

                # Display success message and allow download
                st.success(f"Image encrypted and saved to {output_filename}")
                st.download_button('Download Encrypted Image File', encrypted_image_data, file_name=output_filename)
            else:
                st.error(f"File {output_filename} not found after encryption.")
                st.write("Please check the encryption process for issues.")

        except subprocess.CalledProcessError as e:
            st.error(f"An error occurred during image encryption: {e}")

        finally:
            clean_up_directory()

    elif option == 'Decrypt Image':
        # Decrypt the image file and convert it back to its original format
        try:
            image_output_filename = 'decrypted_image.png'  # This is the expected output

            # Run the image decryption binary
            subprocess.run([cpp_image_decrypt_executable, input_filepath], check=True)

            # Ensure the image file exists before reading
            if os.path.exists(image_output_filename):
                # Read the decrypted image file
                with open(image_output_filename, 'rb') as f:
                    image_file_data = f.read()

                # Display success message and allow download
                st.success("Image decryption and conversion completed successfully!")
                st.download_button('Download Decrypted Image File', image_file_data, file_name=image_output_filename)
            else:
                st.error(f"Decryption failed: {image_output_filename} not found.")

        except subprocess.CalledProcessError as e:
            st.error(f"An error occurred during image decryption: {e}")

        finally:
            clean_up_directory()