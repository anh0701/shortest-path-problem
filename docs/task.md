# Task

## Giai đoạn hiện tại

```sh

allowed_vehicles = [
    Vehicle.BUS,
    Vehicle.MOTORBIKE
]

```

## Giai đoạn sau

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
