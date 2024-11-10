import streamlit as st
import subprocess
import os

# Streamlit app
st.title("File Encryption and Decryption (Text and Audio)")

# Create a file uploader and radio buttons to select encrypt or decrypt
option = st.radio("Select operation:", ('Encrypt Text', 'Decrypt Text', 'Encrypt Audio'))

# File uploader for both text and audio
if option == 'Encrypt Audio':
    uploaded_file = st.file_uploader("Upload a .wav file", type="wav")
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

if uploaded_file is not None:
    input_filename = uploaded_file.name

    with open(input_filename, 'wb') as f:
        f.write(uploaded_file.read())

    cpp_encrypt_executable = './encrypt_file'  # Path to your compiled encryption C++ binary
    cpp_decrypt_executable = './decrypt_file'  # Path to your compiled decryption C++ binary
    cpp_audio_to_text_executable = './audio_to_text'  # Path to your compiled audio-to-text binary

    if option == 'Encrypt Text':
        # Encrypt the text file
        try:
            subprocess.run([cpp_encrypt_executable, input_filename], check=True)

            # Construct the output filename for encrypted file
            output_filename = 'encrypted_' + input_filename

            # Display success message
            st.success("Encryption completed successfully!")

            # Allow user to download the encrypted file
            with open(output_filename, 'rb') as f:
                st.download_button('Download Encrypted File', f, output_filename)

        except subprocess.CalledProcessError as e:
            st.error("An error occurred during encryption.")

    elif option == 'Decrypt Text':
        # Decrypt the text file
        try:
            subprocess.run([cpp_decrypt_executable, input_filename], check=True)

            # Construct the output filename for decrypted file
            output_filename = 'decrypted_' + input_filename

            # Display success message
            st.success("Decryption completed successfully!")

            # Allow user to download the decrypted file
            with open(output_filename, 'rb') as f:
                st.download_button('Download Decrypted File', f, output_filename)

        except subprocess.CalledProcessError as e:
            st.error("An error occurred during decryption.")

    elif option == 'Encrypt Audio':
        # Convert audio to text and then encrypt
        try:
            # Convert the audio file to a text file
            audio_text_filename = input_filename.split('.')[0] + '_audio_data.txt'
            subprocess.run([cpp_audio_to_text_executable, input_filename, audio_text_filename], check=True)

            # Now encrypt the resulting text file
            subprocess.run([cpp_encrypt_executable, audio_text_filename], check=True)

            # Construct the output filename for encrypted audio text file
            output_filename = 'encrypted_' + audio_text_filename

            # Display success message
            st.success("Audio encryption completed successfully!")

            # Allow user to download the encrypted audio text file
            with open(output_filename, 'rb') as f:
                st.download_button('Download Encrypted Audio File', f, output_filename)

        except subprocess.CalledProcessError as e:
            st.error("An error occurred during the audio processing or encryption.")
