# phishing-website-detection

Follow below steps to setup phishing detector

1. Clone repo
   ```bash
   git clone https://github.com/rubaramanan/phishing-website-detection.git
   cd phishing-website-detection
   mkdir -p models/sota
   ```
2. build docker image
   ```bash
   docker build . -t phish_detector:1.0
   ```
3. Run the training model
   ```bash
   docker-compose up train_model
   ```
4. Run the testing UI
   ```bash
   docker-compose up -d streamlit
   ```

5. Open the ui using the link: `http://localhost:8501`
   

