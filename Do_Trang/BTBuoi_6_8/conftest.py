from playwright.sync_api import sync_playwright
import pytest
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORTS_DIR = ROOT / "reports"

def pytest_configure(config):
    """Cấu hình pytest trước khi bắt đầu thực thi test.
    Tự động tạo thư mục report (nếu chưa tồn tại) và sinh tên file
    HTML report theo thời gian chạy để tránh ghi đè report cũ.

    Args:
        config (pytest.Config): Đối tượng cấu hình của pytest, dùng để
            thiết lập các tùy chọn trong quá trình khởi tạo test.

    Returns:
        None
    """
    report_dir = REPORTS_DIR
    report_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Lấy tên file test từ lệnh pytest
    if config.args:
        test_name = Path(config.args[0]).stem
    else:
        test_name = "all"

    config.option.htmlpath = str(report_dir / f"report_{test_name}_{timestamp}.html")
    config.option.self_contained_html = True

@pytest.fixture(scope = "session")
def browser_instance():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    yield browser
    browser.close()
    p.stop()

@pytest.fixture(scope = "session")
def page(browser_instance):
    context = browser_instance.new_context( viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    yield page
    page.close()
    context.close()