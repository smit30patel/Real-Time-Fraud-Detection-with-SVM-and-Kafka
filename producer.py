from kafka import KafkaProducer
import json
import pandas as pd
def create_producer(bootstrap_servers='localhost:9092'):
    """
    Create a Kafka producer instance.
    
    :param bootstrap_servers: List of Kafka broker addresses
    :return: KafkaProducer instance
    """
    print("Creating Kafka producer...")
    return KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
def send_data(producer, topic, data):
    """
    Send data to a Kafka topic.
    
    :param producer: KafkaProducer instance
    :param topic: Topic name to send data to
    :param data: Data to be sent (can be a dict or a pandas DataFrame)
    """
    if isinstance(data, pd.DataFrame):
        data = data.to_dict(orient='records')
    print(f"Sending data to topic '{topic}'...")
    for record in data:
        producer.send(topic, value=record)
        producer.flush()  

def close_producer(producer):
    """
    Close the Kafka producer instance.
    
    :param producer: KafkaProducer instance
    """
    print("Closing Kafka producer...")
    producer.close()
    

if __name__ == "__main__":
    producer = create_producer()
    topic = 'paysim-tran'
    data = pd.read_csv('X_test_may28.csv')  
    send_data(producer, topic, data)
    close_producer(producer)
    print("Data sent successfully.")