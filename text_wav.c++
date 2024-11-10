#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>  // Include cmath for round() and cbrt()
#include <vector>
#include <string>

using namespace std;

// Function to decrypt a 5-digit code (same as in the text decryption)
char decryptCode(const string& code) {
    int num = stoi(code);

    if (num >= 90000 && num <= 99999) {
        // Handle blank space
        return ' ';
    } else {
        // Extract parts from the code
        int encryptedValue = stoi(code.substr(0, 3));
        int hundreds = stoi(code.substr(3, 1));
        int ones = stoi(code.substr(4, 1));

        // Calculate the tens digit
        int sumOfSquares = (hundreds * hundreds) + (ones * ones);
        int difference = encryptedValue - sumOfSquares;

        // Find the cube root of the difference to get the tens digit
        int tens = std::round(std::cbrt(difference));  // Use std:: for round and cbrt

        // Reconstruct the ASCII value
        int asciiValue = (hundreds * 100) + (tens * 10) + ones;

        // Return the corresponding character
        return static_cast<char>(asciiValue);
    }
}

// Function to decrypt the full encrypted audio text message
string decryptMessage(const string& encryptedMessage) {
    stringstream decryptedMessage;
    size_t pos = 0;
    size_t nextPos;

    while (pos < encryptedMessage.length()) {
        nextPos = pos + 5;
        if (nextPos > encryptedMessage.length()) {
            // Handle unexpected end of string
            break;
        }

        string code = encryptedMessage.substr(pos, 5);
        decryptedMessage << decryptCode(code);
        pos = nextPos;
    }

    return decryptedMessage.str();
}

// Main function to decrypt an audio text file
int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <encrypted_audio_text_filename>" << endl;
        return 1;
    }

    string inputFilename = argv[1];
    string outputFilename = "decrypted_" + inputFilename;

    ifstream inputFile(inputFilename);

    // Check if the file opened successfully
    if (!inputFile.is_open()) {
        cerr << "Error opening file: " << inputFilename << endl;
        return 1;
    }

    // Read the encrypted message from the file
    stringstream buffer;
    buffer << inputFile.rdbuf();
    string encryptedMessage = buffer.str();

    // Close the input file
    inputFile.close();

    // Decrypt the message
    string decryptedMessage = decryptMessage(encryptedMessage);

    ofstream outputFile(outputFilename);

    // Check if the output file opened successfully
    if (!outputFile.is_open()) {
        cerr << "Error opening file: " << outputFilename << endl;
        return 1;
    }

    // Write the decrypted message to the output file
    outputFile << decryptedMessage;

    // Close the output file
    outputFile.close();

    cout << "Decrypted message saved to: " << outputFilename << endl;

    return 0;
}
