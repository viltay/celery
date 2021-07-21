from celery import Celery


app = Celery('main', broker='amqp://guest:guest@localhost:5672//')
# app = Celery('main', broker='amqp://guest:guest@localhost:5673//')


@app.task
def add(first_number, second_number):
    return first_number + second_number


@app.task
def multiply(first_number, second_number=1):
    return first_number * second_number


if __name__ == '__main__':
    multiply.delay(2, second_number=3)
    add.delay(2, 3)
