from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda, Fargate
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SQS, SNS, SF
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Kinesis, KinesisDataFirehose


with Diagram("Lambda Pinball", show=False):

    bucket = S3("bucket")
    ddb = Dynamodb("database")
    apig = APIGateway("HTTP")
    tsp = Lambda("Transpangler")
    steps = [SF("Step 1"), SF("Step 2"), SF("Step 3")]

    apig >> Lambda("POST handler") >> ddb >> Lambda("Stream Listener") >> Kinesis("Event stream") >> KinesisDataFirehose("Firehose") >> bucket >> SNS("Notifier") >> SQS("Job queue") >> tsp >> steps >> bucket >> SNS("Finished") >> Lambda("on finished") >> ddb

    tsp >> ddb
    tsp >> bucket
    steps >> ddb

    apig >> Lambda("GET handler") >> ddb
