<!--  -->
# SPP (shortest path problem)

## 1. Problem

- Tìm đường ngắn nhất với nhiều phương tiện không yêu cầu người dùng rành đường 

## 2. Vì sao Google Maps không giải quyết được bài toán này / Tại sao Google không tự chọn điểm đổi phương tiện cho tôi?

- Mỗi phương tiện là 1 graph khác nhau

    - Xe máy: graph đường bộ
    - Bus: graph tuyến + thời gian
    - Đi bộ: graph không ràng buộc

- Điểm đổi phương tiện là decision point

    - gửi xe ở đâu?
    - gửi có an toàn không?
    - có chỗ gửi không?
    - mất bao lâu?

- Xe máy là bài toán use-case địa phương

    - Việt Nam xe máy ở mọi nơi
    - Nước khác có thể không có hoặc rất ít

## 3. Giải pháp

- Bài toán không tính đến việc tự lái xe máy, xe máy sẽ là phương tiện đặt ở app khác, do đó những vấn đề về việc gửi xe sẽ không tồn tại.

