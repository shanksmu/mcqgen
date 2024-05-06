Use Generative AI models to create a MCQ generator on any specific topic


1. Setup a new server - can use AWS, GCP, Linode
2. Update/Upgrade the instance
    - sudo apt update
    - sudo apt-get update
    - sudo apt upgrade -y
3. Install Necessary libraries
    - sudo apt install git curl unzip tar make sudo vim wget -y
    - apt install python3-pip
    - pip3 install -r requirements.txt
4. Clone repository
    - git clone https://github.com/shanksmu/mcqgen.git

    Setup user.name and user.email
    - git config --global user.email "abc@domain.tld"
    - git config --global user.name "username"
6. Create a .env folder to store Open AI keys.
    - touch .env
    Open the .env file using an editor and paste Open AI key - use the below code.
    - OPENAI_API_KEY = "Paste your key here"
7. Run the app
    - streamlit run streamlitapp.py
8. Use the External URL to access the application.

