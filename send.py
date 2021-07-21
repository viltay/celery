import json

import pika

from uuid import uuid1


def send_add():
    task_id = str(uuid1())
    args = (5, 5)
    kwargs = {}
    message = json.dumps((args, kwargs, {"callbacks": None, "errbacks": None, "chain": None, "chord": None}))

    connection = pika.BlockingConnection(pika.URLParameters(url='amqp://guest:guest@localhost:5673'))
    channel = connection.channel()
    channel.basic_publish(exchange='celery',
                          routing_key='celery',
                          body=message,
                          properties=pika.BasicProperties(
                              headers={
                                  'task': 'main.add',
                                  'id': task_id,

                                  'lang': 'py',
                                  'retries': 0,
                                  'argsrepr': str(args),
                                  'root_id': task_id,
                                  'kwargsrepr': {},
                                  'origin': 'gen8747@inspiron-5720',
                                  'ignore_result': 'false'
                              },
                              content_type='application/json',

                              correlation_id=task_id,
                              reply_to=task_id,
                              content_encoding='utf-8',
                              delivery_mode=2,
                              priority=0
                          ))
    connection.close()


def send_multiply():
    task_id = str(uuid1())
    args = (5,)
    kwargs = {'second_number': 5}
    message = json.dumps((args, kwargs, {"callbacks": None, "errbacks": None, "chain": None, "chord": None}))

    connection = pika.BlockingConnection(pika.URLParameters(url='amqp://guest:guest@localhost:5673'))
    channel = connection.channel()
    channel.basic_publish(exchange='celery',
                          routing_key='celery',
                          body=message,
                          properties=pika.BasicProperties(
                              headers={
                                  'task': 'main.multiply',
                                  'id': task_id,

                                  'lang': 'py',
                                  'retries': 0,
                                  'argsrepr': str(args),
                                  'root_id': task_id,
                                  'kwargsrepr': {},
                                  'origin': 'gen8747@inspiron-5720',
                                  'ignore_result': 'false'
                              },
                              content_type='application/json',

                              correlation_id=task_id,
                              reply_to=task_id,
                              content_encoding='utf-8',
                              delivery_mode=2,
                              priority=0
                          ))
    connection.close()


def send_add_local_rabbit():
    task_id = str(uuid1())
    args = (5, 5)
    kwargs = {}
    message = json.dumps((args, kwargs, {"callbacks": None, "errbacks": None, "chain": None, "chord": None}))

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.basic_publish(exchange='celery',
                          routing_key='celery',
                          body=message,
                          properties=pika.BasicProperties(
                              headers={
                                  'task': 'main.add',
                                  'id': task_id,

                                  'lang': 'py',
                                  'retries': 0,
                                  'argsrepr': str(args),
                                  'root_id': task_id,
                                  'kwargsrepr': {},
                                  'origin': 'gen8747@inspiron-5720',
                                  'ignore_result': 'false'
                              },
                              content_type='application/json',

                              correlation_id=task_id,
                              reply_to=task_id,
                              content_encoding='utf-8',
                              delivery_mode=2,
                              priority=0
                          ))
    connection.close()


def send_multiply_local_rabbit():
    task_id = str(uuid1())
    args = (5,)
    kwargs = {'second_number': 5}
    message = json.dumps((args, kwargs, {"callbacks": None, "errbacks": None, "chain": None, "chord": None}))

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.basic_publish(exchange='celery',
                          routing_key='celery',
                          body=message,
                          properties=pika.BasicProperties(
                              headers={
                                  'task': 'main.multiply',
                                  'id': task_id,

                                  'lang': 'py',
                                  'retries': 0,
                                  'argsrepr': str(args),
                                  'root_id': task_id,
                                  'kwargsrepr': {},
                                  'origin': 'gen8747@inspiron-5720',
                                  'ignore_result': 'false'
                              },
                              content_type='application/json',

                              correlation_id=task_id,
                              reply_to=task_id,
                              content_encoding='utf-8',
                              delivery_mode=2,
                              priority=0
                          ))
    connection.close()


if __name__ == '__main__':
    send_add()
    send_multiply()
    send_add_local_rabbit()
    send_multiply_local_rabbit()
