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


**Process vs Thread**

Một process bao gồm ít nhất một hoặc một số thread. Các thread sẽ chạy song song thực tế  (chạy bằng nhiều core CPU) hoặc ảo (chạy bằng một core CPU nhưng lúc chạy thread này, lúc chạy thread khác).


.. note::
    Process và Thread là khái niệm ở trên User Space. Dưới kernel chỉ có một khái niệm duy nhất là Task. Task sẽ là đối tượng để scheduler quản lý. Tùy vào cấu hình, các task có thể chia sẻ hoặc không chia sẻ tài nguyên với nhau. Từ đó tạo ra khái niệm Process và Thread trên user space. Chi tiết :ref:`Process Descriptor and the Task Structure` 

Process Descriptor and the Task Structure
*****************************************


Process Creation
****************

Linux implementation of Threads
*************

Process Termination
*************
