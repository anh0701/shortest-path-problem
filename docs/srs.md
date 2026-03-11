# shortest path problem

- Tìm đường ngắn nhất với nhiều phương tiện không yêu cầu người dùng rành đường
- Bài toán không tính đến việc tự lái xe máy, xe máy sẽ là phương tiện đặt ở app khác, do đó những vấn đề về việc gửi xe sẽ không tồn tại. Nên tính thời gian sẽ cộng thêm 3-5p đợi xe.

- Thuật toán sử dụng: A*

## Database

> A. Bảng Nodes (Điểm nút): lưu trữ tọa độ của tất cả các điểm: trạm bus, ngã tư, hoặc điểm đặt xe.

- id: primary key
- name: Tên điểm (VD: Trạm 102 Trần Hưng Đạo)
- lat, lon: tọa độ địa lý
- node_type: loại điểm (walking_stop, bus_stop, app_pickup_point)

> B. Bảng Edges (Cạnh nối/Đoạn đường)

- id: primary key
- from_node_id, to_node_id: kết nối giữa 2 điểm
- distance: độ dài (mét)
- travel_mode: loại phương tiện (walking, bus, motorbike_app)
- base_weight: chi phí cơ bản (thời gian di chuyển dự kiến)
- complexity_score: chỉ số "khó đi" (dành cho người không rành đường, điểm càng cao thì càng khó đi, ngõ ngách)

> C. Bảng Bus_Schedules (lịch trình bus)

- Vì xe buýt chạy theo giờ, trọng số của cạnh "bus" sẽ thay đổi theo thời gian thực.
- edge_id: foreign key tới bảng edges
- arrival_time: giờ xe đến trạm
- route_number: số hiệu xe (VD: Tuyến 01, 02)

> D. Bảng App_Services (cấu hình app xe máy)

- Lưu thông số để tính toán việc đặt xe qua app
- service_name: grab, be, xanhsm
- avg_waiting_time: thời gian chờ trung bình (VD: 5 phút)
- price_per_km: đơn giá (để gợi ý nếu người dùng quan tâm chi phí)
