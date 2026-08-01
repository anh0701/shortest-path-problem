class Node:

    def __init__(
        self,
        node_id: int,
        name: str,
        latitude: float,
        longitude: float
    ):
        self.id = node_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"{self.name}"