======================
Introduction to SphinX
======================

Sphinx
======
* Sử dụng SphinX để viết document cho code, design document, user guide, specications, application notes,... thay thế cho MS Word.
* SphinX là mã nguồn mở, tài liệu nhiều, có nhiều extension, theme
* Sử dụng một ngôn ngữ thuộc loại Markup Language đơn giản (ví dụ như Markdown, reStructuredText) để viết tài liệu, sau đó dùng SphinX để build các tài liệu đó, xuất ra file sử dụng cuối cùng.
* Viết tài liệu dự án như viết code (ngôn ngữ đủ đơn giản để học nhanh):
  
  * Có thể dùng git diff để thấy được sự thay đổi của document.
  * Có thể dùng git để biết ai là người đã thay đổi document, thay đổi vào thời điểm nào, tại sao thay đổi (dựa vào commit message).
  * Có thể đưa project viết document vào làm submodule của project chính, giúp việc đồng bộ giữa tài liệu và code dễ dàng hơn, khi build code thì đồng thời build tài liệu cho version đó của code luôn.

* Sử dụng ngôn ngữ Markup:
	
  * Có cú pháp riêng dành cho việc giải thích hàm, biến.
  * Có syntax highlight cho code trong doc.
  * Hỗ trợ LaTeX để viết công thức toán học trong file document.

* Xuất file nhiều định dạng HTML, Windows HTML Help, LaTeX, PDF, ePub, Texinfo, Man Page, plain text.
* Xuất document dạng HTML có thể mở bằng trình duyệt:

  * Có tính năng tìm kiếm theo text, giúp việc tìm kiếm tài liệu dễ dàng hơn, gần được giống như google.
  * Có thể link từ document này sang document khác, click là có thể mở document mới ngay, nhanh chóng hơn MS Word rất nhiều.
  * Có khả năng sử dụng label và reference để nhảy đến phần khác của tài liệu một cách nhanh chóng.

* Có khả năng include document generate từ docstrings, docstrings là tool generate document từ comment trong code.
* Dễ dàng tổ chức document theo cấu trúc nhiều lớp (nhiều directory), trong lớp cha có thể liệt kê và tạo link đến lớp con dễ dàng, giúp người đọc nhanh chóng nắm bắt được cấu trúc của dự án.

Read the Doc
===================
* Read the Docs Theme là môt theme của Sphinx
* Theme mã nguồn mở, miễn phí
* Theme đơn giản, đủ đẹp nhưng vẫn dễ dàng sử dụng
