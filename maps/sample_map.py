from models.graph import Graph
from models.node import Node
from models.vehicle import Vehicle
from models.road_type import RoadType


def create_sample_map():

    graph = Graph()

    # =========================
    # Nodes
    # =========================

    graph.add_node(
        Node(
            1,
            "AEON Mall Hai Phong",
            20.8442,
            106.6884
        )
    )

    graph.add_node(
        Node(
            2,
            "Nga Tu Quan Toan",
            20.9000,
            106.6200
        )
    )

    graph.add_node(
        Node(
            3,
            "Trang Due Industrial Park",
            20.9625,
            106.6160
        )
    )

    graph.add_node(
        Node(
            4,
            "An Duong Bus Station",
            20.9390,
            106.6150
        )
    )

    # =========================
    # Edges
    # =========================

    graph.add_edge(
        source_id=1,
        destination_id=2,
        distance=8.5,
        road_name="National Highway 5",
        road_type=RoadType.PRIMARY,
        speed_limit=60,
        allowed_vehicles=[
            Vehicle.MOTORBIKE,
            Vehicle.CAR,
            Vehicle.BUS
        ]
    )

    graph.add_edge(
        source_id=2,
        destination_id=3,
        distance=5.2,
        road_name="Road 208",
        road_type=RoadType.SECONDARY,
        speed_limit=50,
        allowed_vehicles=[
            Vehicle.MOTORBIKE,
            Vehicle.CAR
        ]
    )

    graph.add_edge(
        source_id=2,
        destination_id=4,
        distance=2.1,
        road_name="An Duong Street",
        road_type=RoadType.RESIDENTIAL,
        speed_limit=40,
        allowed_vehicles=[
            Vehicle.MOTORBIKE,
            Vehicle.BUS,
            Vehicle.WALK
        ]
    )

    graph.add_edge(
        source_id=4,
        destination_id=3,
        distance=3.8,
        road_name="Industrial Road",
        road_type=RoadType.SECONDARY,
        speed_limit=40,
        allowed_vehicles=[
            Vehicle.BUS,
            Vehicle.MOTORBIKE
        ]
    )

    return graph