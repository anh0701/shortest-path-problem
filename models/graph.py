from models.edge import Edge


class Graph:

    def __init__(self):
        self.nodes = {}
        self.adjacency = {}

    def add_node(self, node):
        self.nodes[node.id] = node
        self.adjacency[node.id] = []

    def add_edge(
        self,
        source_id: int,
        destination_id: int,
        distance: float,
        road_name: str,
        road_type,
        allowed_vehicles,
        speed_limit: int = 50,
        is_one_way: bool = False
    ):

        source = self.nodes[source_id]
        destination = self.nodes[destination_id]

        # source -> destination
        self.adjacency[source_id].append(
            Edge(
                to_node=destination,
                distance=distance,
                road_name=road_name,
                road_type=road_type,
                allowed_vehicles=allowed_vehicles,
                speed_limit=speed_limit,
                is_one_way=is_one_way
            )
        )

        # destination -> source
        if not is_one_way:
            self.adjacency[destination_id].append(
                Edge(
                    to_node=source,
                    distance=distance,
                    road_name=road_name,
                    road_type=road_type,
                    allowed_vehicles=allowed_vehicles,
                    speed_limit=speed_limit,
                    is_one_way=is_one_way
                )
            )

    def neighbors(self, node_id):
        return self.adjacency[node_id]

    def print_graph(self):
        print("=" * 100)

        for node_id, node in self.nodes.items():

            print(f"{node.name}")

            for edge in self.adjacency[node_id]:

                vehicles = ", ".join(
                    vehicle.value for vehicle in edge.allowed_vehicles
                )

                print(
                    f"  -> {edge.to_node.name}"
                    f" | {edge.distance:.1f} km"
                    f" | {edge.road_name}"
                    f" | {edge.road_type.value}"
                    f" | {edge.speed_limit} km/h"
                    f" | {'One-way' if edge.is_one_way else 'Two-way'}"
                    f" | [{vehicles}]"
                )

            print()

        print("=" * 100)