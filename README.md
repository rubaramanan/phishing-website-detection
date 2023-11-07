# phishing-website-detection

Follow below steps to setup phishing detector

1. Clone repo
   ```bash
   git clone https://github.com/rubaramanan/phishing-website-detection.git
   ```
2. Install required libraries
   ```bash
   pip install -r requirements.txt
   ```
3. Run Training pipeline
   ```bash
   python src/train_pipeline.py
   ```
4. Run Testing pipeline
   ```bash
   python src/predict_pipeline.py
   ```