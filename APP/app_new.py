# import streamlit as st
# import subprocess
# import os
# import io
# import glob
# import time  # To measure time

# # Custom CSS for background and button styling
# st.markdown("""
#     <style>
#     /* Set background color */
#     .stApp {
#         background-color: black;
#     }
    
#     /* Custom header styling */
#     .custom-header {
#         font-size: 30px;
#         color: #4CAF50;
#         text-align: center;
#         font-weight: bold;
#         margin-bottom: 10px;
#     }
    
#     /* Custom subheader styling */
#     .custom-subheader {
#         font-size: 18px;
#         color: #333;
#         text-align: center;
#         margin-bottom: 30px;
#     }
    
#     /* Styling for buttons */
#     .stButton button {
#         width: 100%;
#         height: 60px;
#         border: 2px solid #4CAF50; /* Green border */
#         font-size: 18px;
#         font-weight: bold;
#         color: white;
#         background-color: #4CAF50;
#         transition-duration: 0.4s;
#         border-radius: 10px;
#     }
    
#     .stButton button:hover {
#         background-color: white;
#         color: #4CAF50;
#         border: 2px solid #4CAF50;
#     }

#     </style>
#     """, unsafe_allow_html=True)

# # Header section
# st.markdown("<div class='custom-header'>🔒 File Encryption & Decryption App</div>", unsafe_allow_html=True)
# st.markdown("<div class='custom-subheader'>Encrypt or Decrypt Text and Audio Files Seamlessly</div>", unsafe_allow_html=True)

# # Check if session state variable 'option' exists
# if 'option' not in st.session_state:
#     st.session_state['option'] = None

# # Adding a separator line
# st.markdown("---")

# # Creating a 2x2 grid layout for the options
# col1, col2 = st.columns(2)

# with col1:
#     if st.button("🔐 Encrypt Text"):
#         st.session_state['option'] = 'Encrypt Text'
#     elif st.button("🔊 Encrypt Audio"):
#         st.session_state['option'] = 'Encrypt Audio'

# with col2:
#     if st.button("🔓 Decrypt Text"):
#         st.session_state['option'] = 'Decrypt Text'
#     elif st.button("🔉 Decrypt Audio"):
#         st.session_state['option'] = 'Decrypt Audio'

# # Use the option stored in session state
# option = st.session_state['option']

# # Add a space after the buttons
# st.markdown("###")

# # File uploader for text or audio files based on selected option
# if option == 'Encrypt Audio':
#     uploaded_file = st.file_uploader("Upload a .wav file", type="wav")
# elif option == 'Decrypt Audio':
#     uploaded_file = st.file_uploader("Upload the encrypted .txt file of the audio", type="txt")
# else:
#     uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

# # Add a separator line
# st.markdown("---")

# if uploaded_file is not None and option is not None:
#     input_filename = uploaded_file.name
#     input_data = uploaded_file.read()

#     # Store file in memory (using io.BytesIO)
#     input_file_io = io.BytesIO(input_data)

#     # Save the file locally in memory for subprocess execution (only temporarily)
#     input_filepath = input_filename  # We use the file name in the same directory.

#     # Write the uploaded file to a temporary location (in-memory)
#     with open(input_filepath, 'wb') as f:
#         f.write(input_file_io.getbuffer())

#     # Paths to your C++ binaries
#     cpp_encrypt_executable = '../C++/./enc_txt'  # Path to your compiled encryption C++ binary
#     cpp_decrypt_executable = '../C++/./dec_txt'  # Path to your compiled decryption C++ binary
#     cpp_audio_encrypt_executable = '../C++/./encrypt_audio'  # Path to your compiled audio encryption C++ binary
#     cpp_audio_decrypt_executable = '../C++/./decrypt_audio'  # Path to your compiled audio decryption C++ binary

#     def clean_up_directory():
#         """Delete all non-Python files in the current directory."""
#         for file in glob.glob('*'):
#             if not file.endswith('.py'):
#                 try:
#                     os.remove(file)
#                 except Exception as e:
#                     st.error(f"Error while deleting file {file}: {e}")

#     if option == 'Encrypt Text':
#         # Encrypt the text file
#         try:
#             start_time = time.time()  # Start time measurement
#             subprocess.run([cpp_encrypt_executable, input_filepath], check=True)
#             end_time = time.time()  # End time measurement

#             # Construct the output filename for the encrypted file
#             output_filename = 'encrypted_' + input_filename

#             # Read the encrypted file
#             with open(output_filename, 'rb') as f:
#                 encrypted_file_data = f.read()

#             # Display success message and allow download
#             st.success("✅ Encryption completed successfully!")
#             st.write(f"Time taken for encryption: {end_time - start_time:.2f} seconds")
#             st.download_button('⬇️ Download Encrypted File', encrypted_file_data, file_name=output_filename)

#         except subprocess.CalledProcessError as e:
#             st.error("An error occurred during encryption.")

#         finally:
#             clean_up_directory()

#     elif option == 'Decrypt Text':
#         # Decrypt the text file
#         try:
#             start_time = time.time()  # Start time measurement
#             subprocess.run([cpp_decrypt_executable, input_filepath], check=True)
#             end_time = time.time()  # End time measurement

#             # Construct the output filename for decrypted file
#             output_filename = 'decrypted_' + input_filename

#             # Read the decrypted file
#             with open(output_filename, 'rb') as f:
#                 decrypted_file_data = f.read()

#             # Display success message and allow download
#             st.success("✅ Decryption completed successfully!")
#             st.write(f"Time taken for decryption: {end_time - start_time:.2f} seconds")
#             st.download_button('⬇️ Download Decrypted File', decrypted_file_data, file_name=output_filename)

#         except subprocess.CalledProcessError as e:
#             st.error("An error occurred during decryption.")

#         finally:
#             clean_up_directory()

#     elif option == 'Encrypt Audio':
#         # Encrypt the audio file (WAV)
#         try:
#             start_time = time.time()  # Start time measurement
#             subprocess.run([cpp_audio_encrypt_executable, input_filepath], check=True)
#             end_time = time.time()  # End time measurement

#             # Construct the output filename for the encrypted audio data
#             output_filename = 'encrypted_audio_data.txt'

#             # Check if the file exists before proceeding
#             if os.path.exists(output_filename):
#                 # Read the encrypted audio text file
#                 with open(output_filename, 'rb') as f:
#                     encrypted_audio_data = f.read()

#                 # Display success message and allow download
#                 st.success("✅ Audio encryption completed successfully!")
#                 st.write(f"Time taken for encryption: {end_time - start_time:.2f} seconds")
#                 st.download_button('⬇️ Download Encrypted Audio File', encrypted_audio_data, file_name=output_filename)
#             else:
#                 st.error("File encrypted_audio_data.txt not found after encryption.")

#         except subprocess.CalledProcessError as e:
#             st.error("An error occurred during audio encryption.")

#         finally:
#             clean_up_directory()

#     elif option == 'Decrypt Audio':
#         # Decrypt the audio file and convert it back to WAV
#         try:
#             start_time = time.time()  # Start time measurement
#             subprocess.run([cpp_audio_decrypt_executable, input_filepath], check=True)
#             end_time = time.time()  # End time measurement

#             wav_output_filename = 'reconstructed_audio' + '.wav'

#             # Ensure the WAV file exists before reading
#             if os.path.exists(wav_output_filename):
#                 # Read the decrypted WAV file
#                 with open(wav_output_filename, 'rb') as f:
#                     wav_file_data = f.read()

#                 # Display success message and allow download
#                 st.success("✅ Audio decryption and conversion to WAV completed successfully!")
#                 st.write(f"Time taken for decryption: {end_time - start_time:.2f} seconds")
#                 st.download_button('⬇️ Download Decrypted WAV File', wav_file_data, file_name=wav_output_filename)
#             else:
#                 st.error(f"Decryption failed: {wav_output_filename} not found.")

#         except subprocess.CalledProcessError as e:
#             st.error("An error occurred during audio decryption.")

#         finally:
#             clean_up_directory()



# import streamlit as st
# import subprocess
# import os
# import io
# import glob

# # Custom CSS for background and button styling
# st.markdown("""
#     <style>
#     /* Set background color */
#     .stApp {
#         #background-color: #f0f2f6;
#         background-color: black;
#     }
    
#     /* Custom header styling */
#     .custom-header {
#         font-size: 30px;
#         color: #4CAF50;
#         text-align: center;
#         font-weight: bold;
#         margin-bottom: 10px;
#     }
    
#     /* Custom subheader styling */
#     .custom-subheader {
#         font-size: 18px;
#         color: #333;
#         text-align: center;
#         margin-bottom: 30px;
#     }
    
#     /* Styling for buttons */
#     .stButton button {
#         width: 100%;
#         height: 60px;
#         border: 2px solid #4CAF50; /* Green border */
#         font-size: 18px;
#         font-weight: bold;
#         color: white;
#         background-color: #4CAF50;
#         transition-duration: 0.4s;
#         border-radius: 10px;
#     }
    
#     .stButton button:hover {
#         background-color: white;
#         color: #4CAF50;
#         border: 2px solid #4CAF50;
#     }
    
#     /* Add padding for the grid layout */
#     .css-1l02zno {
#         padding: 10px;
#     }

#     </style>
#     """, unsafe_allow_html=True)

# # Header section
# st.markdown("<div class='custom-header'>🔒 File Encryption & Decryption App</div>", unsafe_allow_html=True)
# st.markdown("<div class='custom-subheader'>Encrypt or Decrypt Text and Audio Files Seamlessly</div>", unsafe_allow_html=True)

# # Check if session state variable 'option' exists
# if 'option' not in st.session_state:
#     st.session_state['option'] = None

# # Adding a separator line
# st.markdown("---")

# # Creating a 2x2 grid layout for the options
# col1, col2 = st.columns(2)

# with col1:
#     if st.button("🔐 Encrypt Text"):
#         st.session_state['option'] = 'Encrypt Text'
#     elif st.button("🔊 Encrypt Audio"):
#         st.session_state['option'] = 'Encrypt Audio'

# with col2:
#     if st.button("🔓 Decrypt Text"):
#         st.session_state['option'] = 'Decrypt Text'
#     elif st.button("🔉 Decrypt Audio"):
#         st.session_state['option'] = 'Decrypt Audio'

# # Use the option stored in session state
# option = st.session_state['option']

# # Add a space after the buttons
# st.markdown("###")

# # File uploader for text or audio files based on selected option
# if option == 'Encrypt Audio':
#     uploaded_file = st.file_uploader("Upload a .wav file", type="wav")
# elif option == 'Decrypt Audio':
#     uploaded_file = st.file_uploader("Upload the encrypted .txt file of the audio", type="txt")
# else:
#     uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

# # Add a separator line
# st.markdown("---")

# if uploaded_file is not None and option is not None:
#     input_filename = uploaded_file.name
#     input_data = uploaded_file.read()

#     # Store file in memory (using io.BytesIO)
#     input_file_io = io.BytesIO(input_data)

#     # Save the file locally in memory for subprocess execution (only temporarily)
#     input_filepath = input_filename  # We use the file name in the same directory.

#     # Write the uploaded file to a temporary location (in-memory)
#     with open(input_filepath, 'wb') as f:
#         f.write(input_file_io.getbuffer())

#     # Paths to your C++ binaries
#     cpp_encrypt_executable = '../C++/./enc_txt'  # Path to your compiled encryption C++ binary
#     cpp_decrypt_executable = '../C++/./dec_txt'  # Path to your compiled decryption C++ binary
#     cpp_audio_encrypt_executable = '../C++/./encrypt_audio'  # Path to your compiled audio encryption C++ binary
#     cpp_audio_decrypt_executable = '../C++/./decrypt_audio'  # Path to your compiled audio decryption C++ binary

#     def clean_up_directory():
#         """Delete all non-Python files in the current directory."""
#         for file in glob.glob('*'):
#             if not file.endswith('.py'):
#                 try:
#                     os.remove(file)
#                 except Exception as e:
#                     st.error(f"Error while deleting file {file}: {e}")

#     if option == 'Encrypt Text':
#         # Encrypt the text file
#         try:
#             subprocess.run([cpp_encrypt_executable, input_filepath], check=True)

#             # Construct the output filename for the encrypted file
#             output_filename = 'encrypted_' + input_filename

#             # Read the encrypted file
#             with open(output_filename, 'rb') as f:
#                 encrypted_file_data = f.read()

#             # Display success message and allow download
#             st.success("✅ Encryption completed successfully!")
#             st.download_button('⬇️ Download Encrypted File', encrypted_file_data, file_name=output_filename)

#         except subprocess.CalledProcessError as e:
#             st.error("An error occurred during encryption.")

#         finally:
#             # Clean up all files except .py after task completion
#             clean_up_directory()

#     elif option == 'Decrypt Text':
#         # Decrypt the text file
#         try:
#             subprocess.run([cpp_decrypt_executable, input_filepath], check=True)

#             # Construct the output filename for decrypted file
#             output_filename = 'decrypted_' + input_filename

#             # Read the decrypted file
#             with open(output_filename, 'rb') as f:
#                 decrypted_file_data = f.read()

#             # Display success message and allow download
#             st.success("✅ Decryption completed successfully!")
#             st.download_button('⬇️ Download Decrypted File', decrypted_file_data, file_name=output_filename)

#         except subprocess.CalledProcessError as e:
#             st.error("An error occurred during decryption.")

#         finally:
#             # Clean up all files except .py after task completion
#             clean_up_directory()

#     elif option == 'Encrypt Audio':
#         # Encrypt the audio file (WAV)
#         try:
#             subprocess.run([cpp_audio_encrypt_executable, input_filepath], check=True)

#             # Construct the output filename for the encrypted audio data
#             output_filename = 'encrypted_audio_data.txt'

#             # Check if the file exists before proceeding
#             if os.path.exists(output_filename):
#                 # Read the encrypted audio text file
#                 with open(output_filename, 'rb') as f:
#                     encrypted_audio_data = f.read()

#                 # Display success message and allow download
#                 st.success("✅ Audio encryption completed successfully!")
#                 st.download_button('⬇️ Download Encrypted Audio File', encrypted_audio_data, file_name=output_filename)
#             else:
#                 st.error("File encrypted_audio_data.txt not found after encryption.")

#         except subprocess.CalledProcessError as e:
#             st.error("An error occurred during audio encryption.")

#         finally:
#             clean_up_directory()

#     elif option == 'Decrypt Audio':
#         # Decrypt the audio file and convert it back to WAV
#         try:
#             wav_output_filename = 'reconstructed_audio' + '.wav'

#             # Run the audio decryption binary
#             subprocess.run([cpp_audio_decrypt_executable, input_filepath], check=True)

#             # Ensure the WAV file exists before reading
#             if os.path.exists(wav_output_filename):
#                 # Read the decrypted WAV file
#                 with open(wav_output_filename, 'rb') as f:
#                     wav_file_data = f.read()

#                 # Display success message and allow download
#                 st.success("✅ Audio decryption and conversion to WAV completed successfully!")
#                 st.download_button('⬇️ Download Decrypted WAV File', wav_file_data, file_name=wav_output_filename)
#             else:
#                 st.error(f"Decryption failed: {wav_output_filename} not found.")

#         except subprocess.CalledProcessError as e:
#             st.error("An error occurred during audio decryption.")

#         finally:
#             clean_up_directory()




#latest


import streamlit as st
import subprocess
import os
import io
import glob
import time  # To measure time

# Custom CSS for background and button styling
st.markdown("""
    <style>
    /* Set background color */
    .stApp {
        background-color: black;
    }
    
    /* Custom header styling */
    .custom-header {
        font-size: 30px;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    /* Custom subheader styling */
    .custom-subheader {
        font-size: 18px;
        color: #333;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* Styling for buttons */
    .stButton button {
        width: 100%;
        height: 60px;
        border: 2px solid #4CAF50; /* Green border */
        font-size: 18px;
        font-weight: bold;
        color: white;
        background-color: #4CAF50;
        transition-duration: 0.4s;
        border-radius: 10px;
    }
    
    .stButton button:hover {
        background-color: white;
        color: #4CAF50;
        border: 2px solid #4CAF50;
    }

    </style>
    """, unsafe_allow_html=True)

# Header section
st.markdown("<div class='custom-header'>🔒 File Encryption & Decryption App</div>", unsafe_allow_html=True)
st.markdown("<div class='custom-subheader'>Encrypt or Decrypt Text, Audio, and Image Files Seamlessly</div>", unsafe_allow_html=True)

# Check if session state variable 'option' exists
if 'option' not in st.session_state:
    st.session_state['option'] = None

# Adding a separator line
st.markdown("---")

# Creating a 2x2 grid layout for the options
col1, col2 = st.columns(2)

with col1:
    if st.button("🔐 Encrypt Text"):
        st.session_state['option'] = 'Encrypt Text'
    elif st.button("🔊 Encrypt Audio"):
        st.session_state['option'] = 'Encrypt Audio'
    elif st.button("🖼️ Encrypt Image"):
        st.session_state['option'] = 'Encrypt Image'

with col2:
    if st.button("🔓 Decrypt Text"):
        st.session_state['option'] = 'Decrypt Text'
    elif st.button("🔉 Decrypt Audio"):
        st.session_state['option'] = 'Decrypt Audio'
    elif st.button("🖼️ Decrypt Image"):
        st.session_state['option'] = 'Decrypt Image'

# Use the option stored in session state
option = st.session_state['option']

# Add a space after the buttons
st.markdown("###")

# File uploader for text, audio, or image files based on selected option
if option == 'Encrypt Audio':
    uploaded_file = st.file_uploader("Upload a .wav file", type="wav")
elif option == 'Decrypt Audio':
    uploaded_file = st.file_uploader("Upload the encrypted .txt file of the audio", type="txt")
elif option == 'Encrypt Image':
    uploaded_file = st.file_uploader("Upload an image file (.png or .jpg)", type=["png", "jpg"])
elif option == 'Decrypt Image':
    uploaded_file = st.file_uploader("Upload the encrypted .txt file of the image", type="txt")
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

# Add a separator line
st.markdown("---")

if uploaded_file is not None and option is not None:
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
    cpp_encrypt_executable = '../C++/./enc_txt'  # Path to your compiled encryption C++ binary for text
    cpp_decrypt_executable = '../C++/./dec_txt'  # Path to your compiled decryption C++ binary for text
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

    if option == 'Encrypt Text':
        # Encrypt the text file
        try:
            start_time = time.time()  # Start time measurement
            subprocess.run([cpp_encrypt_executable, input_filepath], check=True)
            end_time = time.time()  # End time measurement

            # Construct the output filename for the encrypted file
            output_filename = 'encrypted_' + input_filename

            # Read the encrypted file
            with open(output_filename, 'rb') as f:
                encrypted_file_data = f.read()

            # Display success message and allow download
            st.success("✅ Encryption completed successfully!")
            st.write(f"Time taken for encryption: {end_time - start_time:.4f} seconds")
            st.download_button('⬇️ Download Encrypted File', encrypted_file_data, file_name=output_filename)

        except subprocess.CalledProcessError as e:
            st.error("An error occurred during encryption.")

        finally:
            clean_up_directory()

    elif option == 'Decrypt Text':
        # Decrypt the text file
        try:
            start_time = time.time()  # Start time measurement
            subprocess.run([cpp_decrypt_executable, input_filepath], check=True)
            end_time = time.time()  # End time measurement

            # Construct the output filename for decrypted file
            output_filename = 'decrypted_' + input_filename

            # Read the decrypted file
            with open(output_filename, 'rb') as f:
                decrypted_file_data = f.read()

            # Display success message and allow download
            st.success("✅ Decryption completed successfully!")
            st.write(f"Time taken for decryption: {end_time - start_time:.4f} seconds")
            st.download_button('⬇️ Download Decrypted File', decrypted_file_data, file_name=output_filename)

        except subprocess.CalledProcessError as e:
            st.error("An error occurred during decryption.")

        finally:
            clean_up_directory()

    elif option == 'Encrypt Audio':
        # Encrypt the audio file (WAV)
        try:
            start_time = time.time()  # Start time measurement
            subprocess.run([cpp_audio_encrypt_executable, input_filepath], check=True)
            end_time = time.time()  # End time measurement

            # Construct the output filename for the encrypted audio data
            output_filename = 'encrypted_audio_data.txt'

            # Check if the file exists before proceeding
            if os.path.exists(output_filename):
                # Read the encrypted audio text file
                with open(output_filename, 'rb') as f:
                    encrypted_audio_data = f.read()

                # Display success message and allow download
                st.success("✅ Audio encryption completed successfully!")
                st.write(f"Time taken for encryption: {end_time - start_time:.4f} seconds")
                st.download_button('⬇️ Download Encrypted Audio File', encrypted_audio_data, file_name=output_filename)
            else:
                st.error("File encrypted_audio_data.txt not found after encryption.")

        except subprocess.CalledProcessError as e:
            st.error("An error occurred during audio encryption.")

        finally:
            clean_up_directory()

    elif option == 'Decrypt Audio':
        # Decrypt the audio file and convert it back to WAV
        try:
            start_time = time.time()  # Start time measurement
            subprocess.run([cpp_audio_decrypt_executable, input_filepath], check=True)
            end_time = time.time()  # End time measurement

            wav_output_filename = 'reconstructed_audio' + '.wav'

            # Ensure the WAV file exists before reading
            if os.path.exists(wav_output_filename):
                # Read the decrypted WAV file
                with open(wav_output_filename, 'rb') as f:
                    wav_file_data = f.read()

                # Display success message and allow download
                st.success("✅ Audio decryption and conversion to WAV completed successfully!")
                st.write(f"Time taken for decryption: {end_time - start_time:.4f} seconds")
                st.download_button('⬇️ Download Decrypted WAV File', wav_file_data, file_name=wav_output_filename)
            else:
                st.error(f"Decryption failed: {wav_output_filename} not found.")

        except subprocess.CalledProcessError as e:
            st.error("An error occurred during audio decryption.")

        finally:
            clean_up_directory()

    elif option == 'Encrypt Image':
        # Encrypt the image file (PNG or JPG)
        try:
            start_time = time.time()  # Start time measurement
            subprocess.run([cpp_image_encrypt_executable, input_filepath], check=True)
            end_time = time.time()  # End time measurement

            # Construct the output filename for the encrypted image data
            output_filename = 'encrypted_image_data.txt'

            # Check if the file exists before proceeding
            if os.path.exists(output_filename):
                # Read the encrypted image text file
                with open(output_filename, 'rb') as f:
                    encrypted_image_data = f.read()

                # Display success message and allow download
                st.success("✅ Image encryption completed successfully!")
                st.write(f"Time taken for encryption: {end_time - start_time:.4f} seconds")
                st.download_button('⬇️ Download Encrypted Image File', encrypted_image_data, file_name=output_filename)
            else:
                st.error("File encrypted_image_data.txt not found after encryption.")

        except subprocess.CalledProcessError as e:
            st.error("An error occurred during image encryption.")

        finally:
            clean_up_directory()

    elif option == 'Decrypt Image':
        # Decrypt the image file and convert it back to PNG or JPG
        try:
            start_time = time.time()  # Start time measurement
            subprocess.run([cpp_image_decrypt_executable, input_filepath], check=True)
            end_time = time.time()  # End time measurement

            img_output_filename = 'decrypted_image' + '.png'

            # Ensure the image file exists before reading
            if os.path.exists(img_output_filename):
                # Read the decrypted image file
                with open(img_output_filename, 'rb') as f:
                    img_file_data = f.read()

                # Display success message and allow download
                st.success("✅ Image decryption and conversion to PNG completed successfully!")
                st.write(f"Time taken for decryption: {end_time - start_time:.4f} seconds")
                st.download_button('⬇️ Download Decrypted Image File', img_file_data, file_name=img_output_filename)
            else:
                st.error(f"Decryption failed: {img_output_filename} not found.")

        except subprocess.CalledProcessError as e:
            st.error("An error occurred during image decryption.")

        finally:
            clean_up_directory()
