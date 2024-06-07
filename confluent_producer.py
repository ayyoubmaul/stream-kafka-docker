from confluent_kafka import Producer
import json
from faker import Faker
import random

fake=Faker()

def read_config():
  # reads the client configuration from client.properties
  # and returns it as a key-value map
  config = {}
  with open("client.properties") as fh:
    for line in fh:
      line = line.strip()
      if len(line) != 0 and line[0] != "#":
        parameter, value = line.strip().split('=', 1)
        config[parameter] = value.strip()
  return config

def main():
    config = read_config()
    topic = "transactions"

    # creates a new producer instance
    producer = Producer(config)

    while True:
        data = {
           'user_id': fake.random_int(min=20000, max=100000),
           'user_name': fake.name(),
           'user_address': fake.street_address() + ' | ' + fake.city() + ' | ' + fake.country_code(),
           'platform': random.choice(['Mobile', 'Laptop', 'Tablet', 'Handphone', 'Car']),
           'signup_at': str(fake.date_time_this_month())
           }

        m = json.dumps(data)
        producer.poll(1)
        producer.produce(topic, key='data', value=m.encode('utf-8'))
        producer.flush()

if __name__ == '__main__':
  main()
