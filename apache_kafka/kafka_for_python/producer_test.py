#!/usr/bin/env python

from random import choice
from config import config
from confluent_kafka import Producer


def delivery_callback(err, msg):
    """
    Optional per-message delivery callback (triggered by poll() or flush())
    when a message has been successfully delivered or permanently
    failed delivery (after retries).
    """
    if err:
        print('ERROR: Message failed delivery: {}'.format(err))
    else:
        print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
            topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))


def main():
    # Create Producer instance
    producer = Producer(config)

    # Produce data by selecting random values from these lists.
    user_ids = ['eabara', 'jsmith', 'sgarcia',
                'jbernard', 'htanaka', 'awalther']
    products = ['book', 'alarm clock', 't-shirts', 'gift card', 'batteries']

    for _ in range(1):
        user_id = choice(user_ids)
        product = choice(products)
        producer.produce('auction', product, user_id, callback=delivery_callback)

    # ensure the delivery of outstanding messages before closing the producer
    producer.flush()


if __name__ == '__main__':
    main()
