from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda, Fargate
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SQS, SNS, SF
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Kinesis, KinesisDataFirehose


with Diagram("Kinesis Integration", direction="LR"):

   with Cluster("Sources"):
     producers_l = [APIGateway("Source"), Lambda("Source")]
     producers_r = [Lambda("Source"), Fargate("Source")]
   stream = Kinesis("Stream")

   producers_l >> stream
   producers_r >> stream

   stream >> Lambda("Sink")
