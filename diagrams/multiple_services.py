from diagrams import Cluster, Diagram
from diagrams.aws.compute import Compute
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SQS, SNS, SF
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Kinesis, KinesisDataFirehose


with Diagram("A Service", direction="LR"):

     with Cluster("Service Boundary"):
        orchestrator = Compute("Orchestrator")

        components = [Compute("Component 1"), Compute("Component 2"), Compute("Component 3")]

        orchestrator >> components
