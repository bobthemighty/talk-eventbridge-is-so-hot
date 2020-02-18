from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda, Fargate
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import Eventbridge
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3

with Diagram("Message Broker Refactored"):
    with Cluster("Event Processors"):
        with Cluster("System C", direction="TB"):
            apig = APIGateway("webhook")
            handler = Lambda("handler")

        with Cluster("System D", direction="TB"):

            processor = Lambda("handler")
            ddb = Dynamodb("database")
            stream_listener = Lambda("processor")

        broker = Eventbridge("message broker")

        with Cluster("System B", direction="TB"):
            event_handler = Lambda("handler")
            bucket = S3("S3")
            file_processor = Lambda("processor")


        apig >> handler >> broker >> processor

        processor >> ddb >> stream_listener >> broker

        broker >> event_handler >> bucket >> file_processor
