from confluent_kafka import Consumer

################

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'python-consumer', 'auto.offset.reset': 'latest'})

print('Available topics to consume: ', c.list_topics().topics)

c.subscribe(['user-tracker'])

################

def main():
    while True:
        msg = c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data = msg.value().decode('utf-8')
        print(data)

        with open('output_user_tracker.txt', 'a') as f:
            f.write(data)


    c.close()

if __name__ == '__main__':
    main()
