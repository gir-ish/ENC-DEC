#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// Function to convert WAV file to text
void convertWavToText(const string& inputAudioFile, const string& outputTextFile) {
    // Open the WAV file in binary mode
    ifstream inputFile(inputAudioFile, ios::binary);

    if (!inputFile) {
        cerr << "Could not open the file!" << endl;
        exit(1);
    }

    // Read the WAV header (44 bytes)
    const int headerSize = 44;
    vector<char> headerData(headerSize);
    inputFile.read(headerData.data(), headerSize);

    // Extract important metadata from the header
    int sampleRate = *reinterpret_cast<int*>(&headerData[24]);
    short numChannels = *reinterpret_cast<short*>(&headerData[22]);
    short bitsPerSample = *reinterpret_cast<short*>(&headerData[34]);

    // Move the file pointer to the end to determine file size
    inputFile.seekg(0, ios::end);
    size_t fileSize = inputFile.tellg();
    inputFile.seekg(headerSize, ios::beg);

    // Calculate the size of the raw audio data
    size_t dataSize = fileSize - headerSize;

    // Create a vector to hold the audio data
    vector<char> audioData(dataSize);

    // Read the data into the vector
    inputFile.read(audioData.data(), dataSize);

    // Close the file
    inputFile.close();

    // Open a text file to write both the metadata and audio data
    ofstream outputFile(outputTextFile);

    if (!outputFile) {
        cerr << "Could not create the output text file!" << endl;
        exit(1);
    }

    // Write the metadata first (sample rate, channels, bit depth)
    outputFile << sampleRate << " " << numChannels << " " << bitsPerSample << endl;

    // Write the audio data as integers to the text file
    for (size_t i = 0; i < dataSize; ++i) {
        outputFile << static_cast<int>(static_cast<unsigned char>(audioData[i])) << " ";
    }

    // Close the text file
    outputFile.close();

    cout << "Audio data and metadata written to " << outputTextFile << " successfully!" << endl;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cerr << "Usage: " << argv[0] << " <input_wav_filename> <output_text_filename>" << endl;
        return 1;
    }

    string inputAudioFile = argv[1];
    string outputTextFile = argv[2];

    convertWavToText(inputAudioFile, outputTextFile);

    return 0;
}
