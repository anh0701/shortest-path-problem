from models.node import Node
from models.vehicle import Vehicle
from models.road_type import RoadType


class Edge:

    def __init__(
        self,
        to_node: Node,
        distance: float,
        road_name: str,
        road_type: RoadType,
        allowed_vehicles: list[Vehicle],
        speed_limit: int = 50,
        is_one_way: bool = False
    ):
        self.to_node = to_node
        self.distance = distance
        self.road_name = road_name
        self.road_type = road_type
        self.allowed_vehicles = allowed_vehicles
        self.speed_limit = speed_limit
        self.is_one_way = is_one_way

    def supports(self, vehicle: Vehicle) -> bool:
        return vehicle in self.allowed_vehicles

    def __repr__(self):
        return (
            f"Edge("
            f"to={self.to_node.name}, "
            f"distance={self.distance} km, "
            f"road='{self.road_name}'"
            f")"
        )