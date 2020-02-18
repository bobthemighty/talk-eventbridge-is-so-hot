from diagrams import Cluster, Diagram
from diagrams.aws.compute import Compute
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SQS, SNS, SF
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Kinesis, KinesisDataFirehose


with Diagram("Fake services", direction="LR"):

   orchestrator = Compute("Orchestrator service")

   components = [Compute("Service 1"), Compute("Service 2"), Compute("Service 3")]

   orchestrator >> components
