from diagrams import Cluster, Diagram
from diagrams.aws.compute import Compute, Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SQS, SNS, Eventbridge
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Kinesis, KinesisDataFirehose


with Diagram("Procurement services", show=False):

     broker = Eventbridge()

     with Cluster("Lot Selection"):
        inbox = S3("Listings")
        listing_queue = SQS()
        textract = Lambda("Extract lots")
        listings_db = Dynamodb("Listings db")
        selector = Lambda("Select lots")

        inbox >> listing_queue >> textract >> listings_db >> selector

     with Cluster("Buying app"):
          pricer = Lambda("Bid calculator")
          purchases = Dynamodb("Buying db")
          apig = APIGateway("Manager app")
          ls = Lambda("View proposals")
          put = Lambda("Set price")
          invoices = S3("Invoice bucket")
          invoice_listener = Lambda("Invoice listener")
          listener = Lambda("Lot listener")

          listener >>  pricer >> purchases
          apig >> ls >> purchases
          apig >> put >> purchases

          invoices >> invoice_listener >> purchases

          selector >> broker

     broker >> listener
