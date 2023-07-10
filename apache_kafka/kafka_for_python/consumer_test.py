#!/usr/bin/env python

from config import config
from confluent_kafka import Consumer


def set_consumer_configs():
    config['group.id'] = 'auction-group'
    config['auto.offset.reset'] = 'earliest'
    config['enable.auto.commit'] = False


def main():
    set_consumer_configs()
    # Create Consumer instance
    consumer = Consumer(config)

    # Subscribe to topic
    consumer.subscribe(['auction'])

    # Poll for new messages from Kafka and print them.
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                # Initial message consumption may take up to
                # `session.timeout.ms` for the consumer group to
                # rebalance and start consuming
                continue
            elif msg.error():
                print("ERROR: %s".format(msg.error()))
            else:
                # Extract the (optional) key and value, and print.
                print("Consumed event from topic {topic} with partition number({partition}): key = {key:12} value = {value:12}".format(
                    topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8'), partition=msg.partition()))
                consumer.commit(msg)

    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()


if __name__ == '__main__':
    main()
