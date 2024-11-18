# **Custom App for Encoding and Decoding** 🚀

This application streamlines encoding and decoding tasks with a user-friendly interface, backed by C++ integration for high-performance computation.

---

## **✨ Features**
- **Encoding and Decoding**: Simple and efficient processing.
- **C++ Integration**: Optimized performance for heavy tasks.
- **Customizable Paths**: Easily adjust file paths for flexibility.

---

## **🚀 How to Get Started**

### **Step 1: Clone the Repository**

CREATE conda env with python=3.10
```bash
conda create -n enc_dec python=3.10 -y
```
can create venv
---

Clone the repository to your local machine:
```bash
git clone https://github.com/gir-ish/ENC-DEC.git
```

### **Step 2: Install Dependencies**
Navigate to the project directory and install the required Python packages:
```bash
pip install -r requirements.txt
```

### **Step 3: Run the Application**
Navigate to the `APP` folder and start the app using Streamlit:
```bash
cd APP
streamlit run app.py
```

---

## **🔧 Troubleshooting**

### **Problem: File Not Found Error**
If the app reports missing files or dependencies, follow these steps:

1. Navigate to the `C++` folder in the repository.
2. Compile all `.cpp` files using a C++ compiler (e.g., GCC):
   ```bash
   g++ -o <output_file_name> <source_file_name>.cpp
   ```
3. Ensure the compiled files are named correctly as referenced in the app.

### **Problem: File Path Errors**
If you encounter file path issues:
1. Open `app.py` in the `APP` folder.
2. Update the paths in the script to point to the correct locations of your compiled files.

---

## **📋 Requirements**
- Python 3.7 or later
- Streamlit
- C++ compiler (e.g., GCC)

---

## **📂 Folder Structure**
```
.
├── APP
│   ├── app.py           # Main Streamlit application
│   ├── ...              # Additional files and assets
├── C++
│   ├── file1.cpp        # Source files for C++ integration
│   ├── ...
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## **💡 Tips for Success**
- Ensure your Python environment is up-to-date.
- Double-check the file names and paths in `app.py`.
- Reach out for support if needed—collaboration makes everything better! 🙌  

---

Happy coding! 🎉
