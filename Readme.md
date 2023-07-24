# How to run
- Make a Python virtual environment : `python3 -m venv env`
- Install libraries from requirements.txt : `python3 -m pip install -r requirements.txt`
- Make sure you are inside stream-kafka-docker directory and run command `docker-compose up`
- Wait until docker setup the image and container
- Run `python kafka_consumer.py`
- Run `python kafka_producer.py`
- Store output to `producer.log` file

# Solution
This part is for you who face this kind of error message when installing the Python confluent-kafka library
`ERROR: Could not build wheels for confluent-kafka, which is required to install pyproject.toml-based projects`

Steps to reproduce :
- Run `brew install librdkafka` in your terminal
- Export these vars:
    `export C_INCLUDE_PATH=/opt/homebrew/Cellar/librdkafka/2.2.0/include`
    `export LIBRARY_PATH=/opt/homebrew/Cellar/librdkafka/2.2.0/lib `
- Try to run `python3 -m pip install -r requirements.txt` again
