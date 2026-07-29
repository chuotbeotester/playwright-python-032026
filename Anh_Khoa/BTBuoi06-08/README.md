# BTBuoi09 — Automation Test (Playwright + Pytest)

Bộ test tự động cho hệ thống HRM ([hrm.anhtester.com/erp](https://hrm.anhtester.com/erp/)),
xây dựng theo mô hình **Page Object Model (POM)**.

## Cấu trúc thư mục

```
BTBuoi09/
├── conftest.py              # Fixtures dùng chung (browser, page, logged_in_page)
├── pytest.ini               # Cấu hình pytest (pythonpath)
├── requirements.txt         # Danh sách thư viện
├── page/                    # Các Page Object
│   ├── base_page.py         # BasePage: bọc các thao tác Playwright + xử lý lỗi
│   ├── login_page.py
│   ├── home_page.py
│   ├── core_hr/             # Department, Designation, Policies
│   └── crm/                 # Manage Client, Leads
├── tests/                   # Test case + conftest fixtures riêng cho test
├── utils/                   # path_helper, text_data (sinh dữ liệu unique)
└── resources/
    ├── input_data/          # Dữ liệu đầu vào dạng JSON
    └── upload_files/        # File dùng để upload trong test
```

## Cài đặt

```bash
# 1. (Khuyến nghị) tạo virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

# 2. Cài thư viện
pip install -r requirements.txt

# 3. Cài browser cho Playwright
playwright install chromium
```

## Cấu hình

Thông tin đăng nhập nằm ở `resources/input_data/config.json`:

```json
{
    "URL": "https://hrm.anhtester.com/erp/",
    "USERNAME": "admin_example",
    "PASSWORD": "123456"
}
```

## Chạy test

```bash
# Chạy toàn bộ
pytest

# Chạy 1 file
pytest tests/test_core_hr.py

# Chạy kèm log chi tiết
pytest -v
```

> Test mặc định chạy ở chế độ **headed** (`headless=False`, `slow_mo=300`) để quan sát.
> Đổi trong `conftest.py` (fixture `browser`) nếu muốn chạy headless.
