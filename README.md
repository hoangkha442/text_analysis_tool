# Text Analysis Tool (English)

## Giới thiệu

Text Analysis Tool là ứng dụng web giúp phân tích văn bản tiếng Anh, sử dụng spaCy để xử lý ngôn ngữ tự nhiên và Streamlit để xây dựng giao diện. Ứng dụng cho phép nhập văn bản tiếng Anh và nhận kết quả phân tích chi tiết về token, lemma, POS, dependency, stopword, và nhận diện thực thể (NER).

---

## Thành viên nhóm

| MSSV    | Họ và Tên        |
| ------- | ---------------- |
| 2591306 | Châu Hoàng Kha   |
| 2591314 | Trần Thị Bảo My  |
| 2591320 | Nguyễn Thành Quí |

---

## Tính năng

- Tách từ (Tokenization) và hiển thị thông tin chi tiết cho từng token.
- Phân loại từ loại (POS tagging).
- Nhận diện thực thể (Named Entity Recognition - NER) với trực quan hóa.
- Xuất dữ liệu token dưới dạng file CSV.

---

## Yêu cầu hệ thống

- Python >= 3.10
- Các thư viện: `streamlit`, `spacy`, `pandas`

Cài đặt nhanh các thư viện bằng lệnh:

```sh
pip install -r requirements.txt
```

---

## Hướng dẫn sử dụng

1. Khởi động ứng dụng:
   ```sh
   streamlit run main.py
   ```
2. Nhập hoặc dán đoạn văn bản tiếng Anh vào ô nhập liệu.
3. Nhấn nút **Analyze** để xem kết quả phân tích:
   - Bảng token chi tiết.
   - Bảng POS tags.
   - Trực quan hóa các thực thể (NER).
4. Nhấn nút **Download tokens CSV** để tải bảng token về máy.

---

## Cấu trúc thư mục

```
text_analysis_tool/
├── main.py           # Mã nguồn chính của ứng dụng
├── requirements.txt  # Danh sách thư viện cần thiết
└── README.md         # Tài liệu hướng dẫn sử dụng
```

---

## Giải thích mã nguồn chính (`main.py`)

- Tự động kiểm tra và tải model spaCy `en_core_web_sm` nếu chưa có.
- Phân tích văn bản đầu vào, trích xuất thông tin token, POS, lemma, dependency, stopword, và thực thể.
- Hiển thị bảng token, bảng POS, trực quan hóa thực thể, và nút tải file CSV bằng Streamlit.
- CSS tùy chỉnh giúp làm nổi bật các thực thể và làm mờ các token không phải thực thể.

---

**© 2025 - Nhóm 1**
