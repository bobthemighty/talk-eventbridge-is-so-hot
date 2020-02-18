from diagrams import Cluster, Diagram
from diagrams.aws.analytics import ES, Kinesis
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import Eventbridge
from diagrams.aws.storage import S3

with Diagram("Event capture"):
    with Cluster("Production Account"):
        prod_lambdas = [Lambda("Func"), Lambda("Func"), Lambda("Func")]
        prod_bus = Eventbridge("Default")
        prod_lambdas >> prod_bus

    with Cluster("Test Account"):
        test_lambdas = [Lambda("Func"), Lambda("Func"), Lambda("Func")]
        test_bus = Eventbridge("Default")
        test_lambdas >> test_bus

    with Cluster("Logging Account"):
        event_bus = Eventbridge("Shared")
        prod_bus >> event_bus
        test_bus >> event_bus

        stream = Kinesis("Event stream")

        event_bus >> stream
        stream >> S3("Archive")
        stream >> ES("Analytics")
