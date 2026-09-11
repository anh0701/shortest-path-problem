# Task

## I. Edge

### 1. Giai đoạn hiện tại

```sh
Edge:

allowed_vehicles = [
    Vehicle.BUS,
    Vehicle.MOTORBIKE
]

```

### 2. Giai đoạn sau

- Giai đoạn 2: Khi bắt đầu tính thời gian và chi phí, lúc đó refactor sang `VehicleRule`

```sh

class VehicleRule:
    vehicle
    average_speed
    cost_per_km


edge.vehicle_rules = [

    VehicleRule(
        BUS,
        speed=35,
        cost=7000
    ),

    VehicleRule(
        MOTORBIKE,
        speed=45,
        cost=3000
    )
]

```

## II. Thuật toán

```sh

  Graph
    ↓
Dijkstra (1 phương tiện)
    ↓
    A*
    ↓
Multimodal (Bus + Motorbike)
    ↓
K-shortest paths (N phương án)

```
