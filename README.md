# Serenata
This project combines facial emotion analysis with song recommendation based on mood and listening history. The system uses the DeepFace library to analyze emotions from an image and the Gemini API to generate song recommendations. It also integrates with the Spotify API to fetch the user's listening history.

## READ ME FILE FOR Hackathon

### Requirements
•	Python 3.9 or higher
•	deepface library
•	google-generativeai library
•	requests library
•	tensorflow library (for any TensorFlow-specific operations, though it is not directly used here)
•	base64 (standard library, no installation required)
•	datetime (standard library, no installation required)
•	httplib2 (if used, install using pip install httplib2)

### Installation
1.	Clone the Repository (if applicable):
bash
Copy code
git clone https://github.com/yourusername/serenata.git
cd serenata
2.	Create and Activate a Virtual Environment:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3.	Install Required Packages:
bash
Copy code
pip install deepface google-generativeai requests tensorflow
4.	Set Up API Keys:
- Spotify API: Replace client_id and client_secret with your own Spotify API credentials.
- Gemini API: Replace API_KEY with your own Google Gemini API key.

### Usage
1.	Prepare the Image: Place the image you want to analyze in the same directory as the script and name it abc.png or update the img_path parameter in the code.
2.	Run the Script:
bash
Copy code
python cutie.py
3.	Output:
- The script analyzes the mood from the image using DeepFace and prints the dominant emotion.
- It then uses this emotion and a predefined listening history to request a song recommendation from the Gemini API.
- The recommended song and its Spotify link are printed.

### Code Explanation
#### Spotify API Setup:
- Authenticates with Spotify using client_id and client_secret to retrieve an access token.
- DeepFace Analysis:
- Analyzes the facial emotion from an image (abc.png).
#### Gemini API Setup:
- Configures the Gemini API with the provided API key.
- Constructs a prompt using the analyzed emotion and listening history to request a song recommendation.

### Troubleshooting
•	Ensure that you have the correct credentials and API keys.
•	Make sure all required libraries are installed.
•	Verify that the image path and file name are correct.
•	Check for any specific error messages in the output and consult the documentation for the respective libraries.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
 
Feel free to adjust the content according to the specific details of your project and any additional instructions you might need to include.



