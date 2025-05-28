echo "Creating topic 'paysim-transactions'..."
$KAFKA_BIN/kafka-topics --create --topic paysim-transactions \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1

echo "Kafka and Zookeeper started. Topic 'paysim-transactions' created."
