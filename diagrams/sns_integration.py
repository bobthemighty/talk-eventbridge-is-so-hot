from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda, Fargate
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SQS, SNS, SF
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Kinesis, KinesisDataFirehose


with Diagram("SNS Integration", direction="LR", show=False):

   apig = APIGateway("Producer (http post)")
   topic = SNS("Topic")

   with Cluster("Consumers"):
    consumers_l = [Lambda("Consumer"), Lambda("Consumer"), Lambda("Consumer")]

   apig >> topic
   consumers_l >> topic
