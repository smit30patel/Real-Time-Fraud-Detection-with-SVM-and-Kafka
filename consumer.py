from kafka import KafkaConsumer
import json
import pandas as pd
import joblib

def create_consumer(topic, bootstrap_servers='localhost:9092', group_id='my-group'):
    """
    Create a Kafka consumer instance.
    
    :param topic: Topic name to subscribe to
    :param bootstrap_servers: List of Kafka broker addresses
    :param group_id: Consumer group ID
    :return: KafkaConsumer instance
    """
    print("Creating Kafka consumer...")
    return KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        group_id=group_id,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
def consume_data(consumer, model):
    """
    Consume data from the Kafka topic.  
    :param consumer: KafkaConsumer instance
    """
    print("Starting to consume data...")
    for msg in consumer:
        record = msg.value
        # print(f"Consumed record: {record}")
        tx = pd.DataFrame([msg.value])
        prediction = model.predict(tx)[0]
        # print(f"Predictions: {prediction}")
        if prediction == 1:
            print("⚠️ Fraud Detected:", prediction)
        else:
            print("✅ Legitimate:", prediction)

#Usage 
if __name__ == "__main__":
    topic = 'paysim-tran'
    model = joblib.load('./new_svm_model.pkl')  
    
    consumer = create_consumer(topic)
    
    try:
        consume_data(consumer, model)
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        consumer.close()
        print("Consumer closed.")