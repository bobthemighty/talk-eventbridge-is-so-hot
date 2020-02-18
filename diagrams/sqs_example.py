from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda, Fargate
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SQS, SNS, SF
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Kinesis, KinesisDataFirehose


with Diagram("SQS Integration", direction="LR", show=False):

   queue = SQS("Queue")
   apig = APIGateway("Producer (http post)")

   with Cluster("Consumers"):
       consumer_a = Lambda("Proc 1")
       consumer_b = Lambda("Proc 2")
       consumer_c = Lambda("Proc 2")

   apig >> queue
   queue << consumer_b
