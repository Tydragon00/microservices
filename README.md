# Assignment for ITS ICT Microservices



## List of microservices 
>1. [Books microservice](./microservice/books):
>expose CRUD opereration, use flask framework and mongodb database
>1. [Customer microservice](./microservice/customer):
>expose CRUD opereration, use flask framework and mysql database
>1. [Borrowing microservice](./microservice/borrowing):
>expose CRUD opereration, use flask framework and mysql database

## Test:

[Test books microservice script](./microservice/books/my_test.py): python script for testing boook microservice, test post, put, get all, get one and delete.
This script return true or false.

## Notification

[Notification Script](./test/notification.py): python script for run a Subscribe RabbutMQ, this is used for notification when a new borrowing is added.

## Diagram:


![](my_diagram.png)


## Logging:
[Logging](./microservice/Logging_and_tracing): Logging is managed by Elasticsearch and Kibana.



## For run microservices locally:
There are two bash script:
>1. [Start with logging](./microservice/start.sh): Start all microservices with logging.
>1. [Start without logging](./microservice/start_noLog.sh): Start all microservices without logging.










## Assignment:

Develop 4 microservices as depicted in this diagram:

![](diagram.png)

Microservices can be developed in any any techology , but they must comply with following constraints:

- Use HTTP/REST for synchronous communication
- Use at least two different database technology (RDBMS and NoSQL).
- Use a message broker (Kafka, Active MQ, Rabbit MQ) for asynchronous communications (ie: calling the Notification service)

Evaluation criteria:

- Microservices         (0 to 5 points)
- Design patterns       (0 to 5 points)
- Testing               (0 to 5 points)
- Logging and tracing   (0 to 5 points)
- CI/CD                 (0 to 5 points)
- Docker and Kubernetes (0 to 5 points)
 
