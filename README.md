# Real-Time Fraud Detection with SVM and Kafka

A real-time fraud detection system using Support Vector Machine (SVM) and Apache Kafka for streaming transaction processing.

## Overview

This project implements a real-time fraud detection system with the following components:
- A pre-trained SVM model for fraud detection
- Kafka producer-consumer architecture for real-time transaction processing
- Streamlit dashboard for visualization and testing

## Components

### 1. Machine Learning Model
- SVM (Support Vector Machine) model trained on transaction data
- Model file: `new_svm_model.pkl`
- Training data: Split into train/test sets (`X_train_may28.csv`, `y_train_may28.csv`, etc.)

### 2. Kafka Streaming
- `producer.py`: Sends transaction data to Kafka topic
- `consumer.py`: Processes transactions in real-time using the trained model
- `create_kafka_topic.sh`: Script to set up required Kafka topics

### 3. Web Dashboard
- Built with Streamlit
- Features:
  - Upload custom test datasets
  - Run real-time predictions
  - Visualize fraud prediction distribution
  - Download prediction results as CSV

## Setup and Installation

1. Ensure you have Python installed and Apache Kafka running locally
2. Install required dependencies:
   ```bash
   pip install streamlit pandas kafka-python joblib scikit-learn
   ```
3. Start Kafka and create required topics:
   ```bash
   ./create_kafka_topic.sh
   ```

## Usage

1. Start the Streamlit dashboard:
   ```bash
   streamlit run app.py
   ```

2. For real-time processing:
   - Start the consumer:
     ```bash
     python consumer.py
     ```
   - Run the producer to send transactions:
     ```bash
     python producer.py
     ```

## Features

- Real-time transaction fraud detection
- Interactive web dashboard
- Support for batch predictions
- Visualization of fraud distribution
- Easy export of prediction results
- Kafka-based streaming architecture

## Project Structure
```
├── app.py                 # Streamlit dashboard
├── consumer.py           # Kafka consumer
├── producer.py           # Kafka producer
├── create_kafka_topic.sh # Kafka setup script
├── new_svm_model.pkl    # Trained SVM model
├── *_may28.csv          # Training and test datasets
└── *.ipynb              # Jupyter notebooks for EDA and model development
```

## Model Training

The model was trained using the PaySim dataset. The training process and exploratory data analysis can be found in:
- `eda-paysim-df.ipynb`
- `fraud_det.ipynb`

## Made By
Smit Patel

[GitHub Repository](https://github.com/smit30patel/Real-Time-Fraud-Detection-with-SVM-and-Kafka)