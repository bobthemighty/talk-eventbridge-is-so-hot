from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda, Fargate
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import Eventbridge
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3

with Diagram("Message Broker", show=False):
    with Cluster("Event Processors"):
        with Cluster("System A", direction="TB") as sys_a:
            apig = APIGateway("webhook")
            handler = Lambda("handler")
            ddb_a = Dynamodb("database")
            processor = Lambda("processor")

        broker = Eventbridge("message broker")

        with Cluster("System B", direction="TB") as sys_b:
            event_handler = Lambda("handler")
            bucket = S3("S3")
            file_processor = Lambda("processor")


        apig >> handler >> ddb_a >> processor

        event_handler >> bucket >> file_processor

        processor >> broker >> event_handler 
