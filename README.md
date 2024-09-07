# Diagnox

## Overview

This project focuses on improving lung cancer detection through a multidisciplinary approach, integrating various cutting-edge technologies. The following components are included in the project:

1. **Chatbot for Lung Cancer Guidance**  
   We developed a chatbot powered by Long Short-Term Memory (LSTM) networks, allowing users to ask lung cancer-related questions and receive real-time responses. This provides vital information and guidance to patients and healthcare providers. 💬🤖
   ![image](https://github.com/user-attachments/assets/06e09a32-d789-4196-aad7-8cadd474ebcc)


3. **Research Summarization with Transformer Models**  
   Utilizing transformer-based models, we provide concise and informative summaries of lung cancer research articles, helping users stay updated with the latest scientific advancements. 📰🔍

4. **Nodule Detection System**  
   Our Convolutional Neural Networks (CNNs)-based system automatically detects suspicious nodules in medical images. This critical step improves early diagnosis, leading to better patient outcomes. 📊🔬
![image](https://github.com/user-attachments/assets/01cb3cf4-f10b-40fd-ae63-caccd6a1ef82)

5. **Lung Cancer Type Recognition**  
   Leveraging machine learning algorithms, we identify different types of lung cancer based on histopathological tissue sample analysis. This enables personalized treatment strategies tailored to cancer subtypes. 🧠🩺

6. **3D Medical Image Visualization**  
   We implemented 3D visualization techniques to provide comprehensive views of lung structures and anomalies. This tool assists clinicians in assessing and interpreting complex anatomical features, improving diagnostic accuracy. 🖥️🫁

7. **Statistical Analysis of Patient Data**  
   By analyzing patient data collected through forms, we gain insights into risk factors, disease progression, and treatment outcomes. This helps clinicians make more informed decisions, improving patient care. 📈👨‍⚕️👩‍⚕️

## How to Run the Project

To run this Django project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply the migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application:
   ```
   http://127.0.0.1:8000/
   ```
