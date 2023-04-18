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

**Process Context**

Một Process chạy trên Linux sẽ có 2 mode **User Mode** và **Kernel Mode** . Thông thường process sẽ chạy ở **User Mode**. Tuy nhiên, khi process gọi **System Call** hoặc **Trigger Exception** thì process sẽ chuyển qua chạy ở **Kernel Mode**. Khi kernel chạy handler cho system call hay exception nhận được từ process thì ta cũng có thể nói rằng Kernel đang chạy "on behalf of the process" hay đang trong **process context**.

**Process Family Tree**

Các process trong Linux được tổ chức theo quan hệ cha con. **init** process có PID = 1 và là process duy nhất không có process cha. Tất cả các process khác đều là con cháu của **init** process. Mỗi process đó sẽ có 1 process cha và 0 hoặc một số process con. Trong process descriptor sẽ có một pointer trỏ tới process cha và một list các con trỏ trỏ tới process con của nó.

Kernel process sẽ là process con của **kthreadd** (PID=2). Để  list các process của kernel ta dùng câu lệnh sau:

.. code:: bash

    ps --ppid 2 -o uname,ppid,pid,cmd

Process Creation
****************

Đa phần các hệ điều hành sẽ implement một có chế **spawn** để tạo ra một process mới.
Tuy nhiên, đối với Unix system trong đó có Linux, để tạo ra một process mới cần thực hiện hai bước:

* **fork()**: Tạo ra một process con là copy của process hiện tại.
* **exec()**: Load chương trình lên RAM và thực hiện chương trình đó.

**Copy-on-Write**

Khi thực hiện lệnh **fork()**, tất cả các tài nguyên của process cha sẽ được duplicated cho process con. Nếu implement một cách ngây thơ (naive) thì copy kiểu này sẽ rất không hiệu quả vì phải copy quá nhiều thứ mà có khi không cần dùng đến sau này. Trong trường hợp chạy luôn chương trình mới thì coi như mất công copy qua gần không dùng được gì cả. Do đó, **fork()** của Linux implement một cơ chế gọi là **Copy-on-Write**, tức là chỉ thực hiện copy ra chỗ khác khi cần write, còn nếu không đụng tới hoặc chỉ read thui thì không cần copy chi cho tốn công.

Đơn vị nhỏ nhất của **Copy-on-Write** là page. Tức là nếu cần write vào một byte trong page thì cũng phải copy cả page.


**Forking**

**vfork()**

Linux implementation of Threads
*******************************

Process Termination
*******************
