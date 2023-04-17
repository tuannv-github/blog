Process Management
#############

**Khái niệm**

Một process là một chương trình đang được thực thi (execute) và những tài nguyên được sử dụng bởi chương trình đang thực thi đó.

Các tài nguyên được sử dụng bởi một process bao gồm:

- File đang mở bởi process
- Signal đang chờ process xử lý
- Địa chỉ trong memory mà process đang sử dụng
- Thời gian CPU mà process đang chiếm dụng
- Các threads của process
- ...


**Process vs Thread**

Một process bao gồm ít nhất một hoặc một số thread. Các thread sẽ chạy song song thực tế  (chạy bằng nhiều core CPU) hoặc ảo (chạy bằng một core CPU nhưng lúc chạy thread này, lúc chạy thread khác).


.. note::
    Process và Thread là khái niệm ở trên User Space. Dưới kernel chỉ có một khái niệm duy nhất là Task. Task sẽ là đối tượng để scheduler quản lý. Tùy vào cấu hình, các task có thể chia sẻ hoặc không chia sẻ tài nguyên với nhau. Từ đó tạo ra khái niệm Process và Thread trên user space. Chi tiết :ref:`Process Descriptor and the Task Structure` 

Process Descriptor and the Task Structure
*****************************************

Trong linux kernel, các task là các đối tượng thực thi được quản lý bởi **scheduler**.
Các task có type là :code:`struct task_struct` này được tổ chức bằng cấu trúc dữ liệu **doubly linked list**. 
Mỗi phần tử trong doubly linklist đó được gọi là một **process descriptor** - ý muốn nói phần tử đó dùng để mô tả một process. Đúng ra nên gọi là **task descriptor**, không hiểu sao tài liệu đều để là process descriptor, chắc do quen và không quan trọng lắm.

**PID**

Mỗi **task** có **một PID độc nhất** cho task đó. PID là một biến trong :code:`struct task_struct` có kiểu dữ liệu là :code:`pid_t`.
Ban đầu người ta để giá trị lớn nhất của PID là 32768 (short int), nhưng khi hệ thống lớn nên cần nhiều process hơn nên đã nâng lên thành 4 triệu (int). Giá trị của max của PID có thể được get/set thông qua file **/proc/sys/kernel/pid_max**. Nếu hệ thống muốn có  lớn hơn 4 triệu process thì chỉ có nước là đổi typedef của :code:`pid_t` thành kiểu 64 bit rồi compile lại kernel.

**Máy trạng thái của Task**

.. image:: imgs/task_state_machine.png
    :width: 600
    :name: Process State Machine

* **TASK_RUNNING** Task đang chạy hoặc đang chờ được chạy trong queue.
* **TASK_INTERRUTABLE** Task đang ngủ, chờ một điều kiện nào đó để chạy tiếp ví dụ như ghi xong dữ liệu xuống hard drive hoặc nhận signal.
* **TASK_NONINTERRUTABLE** Giống với trạng thái **TASK_INTERRUTABLE** nhưng ở đây, task không nhận signal.
* **TASK_TRACED** Task đang bị traced bỏi một process khác, ví dự như debuger (gdb).
* **TASK_STOP** Task đã bị dừng và không thể nào quay lại trang thái **TASK_RUNNING**. Task ở trạng thái này để chờ task cha lấy thông tin trả về . Sau khi process cha lấy đủ thông tin rồi thì task mới chính thức bay màu. 

Process Creation
****************

Linux implementation of Threads
*************

Process Termination
*************
