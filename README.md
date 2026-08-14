# 🚀 IFinance - Nền tảng Quản lý Tài chính Cá nhân Thông minh cùng AI

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-19-61DAFB.svg?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![Docker](https://img.shields.io/badge/Docker-Supported-2496ED.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com)

**IFinance** là một ứng dụng quản lý tài chính cá nhân toàn diện, kết hợp sức mạnh của Trí tuệ Nhân tạo (Google Gemini) để tự động hóa việc nhập liệu, phân tích thói quen chi tiêu và tư vấn tài chính. Dự án được xây dựng theo kiến trúc hiện đại, phân tách rõ ràng giữa Backend (FastAPI 3-Tier) và Frontend (ReactJS), kết hợp cùng hệ thống Unit Test mạnh mẽ.

---

## 🌟 Tính năng nổi bật (Features)

*   **💳 Quản lý Thu / Chi linh hoạt:** Hỗ trợ chuyển tiền nội bộ, quản lý đa ví, cấu trúc danh mục (category) đa tầng.
*   **🤖 Trợ lý AI Thông minh (Gemini Flash):**
    *   **Smart Input:** Thêm nhanh giao dịch qua câu lệnh tự nhiên (VD: *"Sáng nay đổ xăng 50k bằng tiền mặt"*).
    *   **Smart Bulk Import:** Trích xuất mảng dữ liệu khổng lồ bằng AI. Dán một đoạn Ghi chú (Note) chứa nhiều giao dịch, AI sẽ tự động bóc tách thành các dòng độc lập cực thông minh.
    *   **OCR Hóa đơn:** Quét, đọc và trích xuất dữ liệu tự động từ ảnh chụp biên lai/hóa đơn.
    *   **Chatbot RAG:** Trợ lý ảo hiểu ngữ cảnh tài chính của bạn, có khả năng tư vấn và tự động ghi nhận giao dịch thông qua *Function Calling*.
*   **📥 Nhập liệu Hàng loạt Cơ chế Thông minh (Smart Bulk Import):**
    *   Hỗ trợ nhập trực tiếp File `.csv` / `.xlsx` (Excel).
    *   Tự động bắt từ khóa (Fuzzy Matching) để tự ghép Cột, Map Danh mục và Map Ví Tiền một cách chính xác.
    *   **Auto-Generation:** Nếu File chứa Danh mục lạ hoặc Ví tiền mới, hệ thống sẽ tự động cấu trúc lại Data và tự khởi tạo mới đính kèm vào Database mà không bắt bạn phải đi tạo bằng tay.
    *   **Auto Debt Tracking:** Tự động trích xuất Tên Chủ Nợ (Ví dụ *"Vay anh Sơn"*), ngay lập tức lập Hợp đồng Nợ (Debts) tương ứng và tự động gạch nợ ngay trong lúc import vòng lặp.
*   **🎓 Hướng dẫn tương tác cho người dùng mới (Interactive Tutorial):**
    *   Tour hướng dẫn tự động xuất hiện ngay sau khi tạo tài khoản mới, giới thiệu lần lượt các tính năng chính qua các bước chú thích trực quan.
    *   Hỗ trợ cả Desktop và Mobile với giao diện responsive, tự động chuyển đổi khi thay đổi kích thước cửa sổ.
    *   Đồng bộ trạng thái "đã xem" lên Server (`PATCH /users/me/preferences`) với cơ chế retry 3× exponential backoff và tối ưu hóa bằng localStorage.
*   **📅 Ngân sách & Định kỳ (Budgets & Subscriptions):** Cảnh báo an toàn chi tiêu, hỗ trợ cộng dồn (rollover) sang tháng sau. Hệ thống auto-worker chạy ngầm (`APScheduler`) tự động xử lý các khoản chi tiêu định kỳ tới hạn.
*   **📈 Đầu tư & Quản lý Nợ (Investments & Debts):** Tự động định giá và cập nhật Tỷ giá thời gian thực đối với Tiền điện tử (CoinGecko) & Cổ phiếu/Chứng khoán (vnstock Proxy Backend API). Quản lý chi tiết số lượng, tỷ suất sinh lời (ROI), phí/thuế, lịch sử trả nợ và biểu đồ phân bổ danh mục.

---

## 🛠 Tech Stack (Công nghệ sử dụng)

*   **Frontend:** ReactJS, Vite, Tailwind CSS, Recharts, Lucide Icons, Axios (Global Interceptors), React Hot Toast, react-joyride v3 (Lazy-loaded Interactive Tour).
*   **Backend:** Python, FastAPI, SQLAlchemy, Alembic, Pydantic, APScheduler, Pytest.
*   **Database:** PostgreSQL (Dữ liệu quan hệ lõi) & MongoDB (Lịch sử Chat AI).
*   **AI Integration:** Google Generative AI (Gemini Studio API).

---

## 📁 Cấu trúc Dự án (Project Structure)

Dự án áp dụng mô hình kiến trúc **3-Tier (Router - Service - CRUD)** phía Backend giúp dễ dàng mở rộng và test cô lập.

```text
aminhtoan-Finance/
├── backend/                      # Source code Backend (FastAPI)
│   ├── alembic/                  # Quản lý Migration Database (Lịch sử Schema Database)
│   ├── app/
│   │   ├── api/v1/routers/       # [Lớp 1: Routers] Tiếp nhận HTTP Request và Validate Input đầu vào.
│   │   ├── services/             # [Lớp 2: Services] Xử lý Business Logic cốt lõi (Kiểm tra số dư, Gọi AI...).
│   │   ├── crud/                 # [Lớp 3: CRUD Database] Xử lý truy vấn CSDL, tương tác trực tiếp với SQLAlchemy.
│   │   ├── models/               # SQLAlchemy Models (Schema Definition trong DB)
│   │   ├── schemas/              # Pydantic Models (Validate Data I/O)
│   │   ├── db/                   # Object Session kết nối PostgreSQL & MongoDB
│   │   ├── core/                 # Cấu hình bảo mật, xử lý JWT Token & Authenticate
│   │   └── main.py               # File entry point chạy server FastAPI
│   ├── tests/                    # 🧪 [THƯ MỤC TEST] Chứa các cấu hình Pytest, Mocking và Unit Test Cases.
│   ├── alembic.ini               # Cấu hình Alembic
│   ├── Dockerfile                # Cấu hình build Docker cho backend
│   └── requirements.txt          # Các thư viện Python cần thiết
│
└── frontend/                     # Source code Frontend (ReactJS)
    ├── public/                   # Static assets (icons, favicon...)
    ├── src/
    │   ├── api/                  # Axios Client & Auto Token Refresh Interceptor
    │   ├── components/           # Reusable UI (Sidebar, CurrencyInput, Popup modal...)
    │   ├── contexts/             # React Context (UserContext, TutorialContext)
    │   ├── pages/                # Màn hình chức năng (Auth, Dashboard, Transactions, AI Chat...)
    │   ├── tutorial/             # Định nghĩa bước hướng dẫn Desktop & Mobile (tutorialSteps.js)
    │   ├── utils/                # Helpers: format tiền tệ/thời gian, tutorialAnalytics
    │   ├── App.jsx               # Navigation & Routing system
    │   └── main.jsx              # File entry point của React
    ├── package.json              # Các thư viện NPM cần thiết
    ├── tailwind.config.js        # Cấu hình Tailwind CSS
    └── vite.config.js            # Cấu hình Vite builder
```

---

## 🐳 Hướng dẫn chạy bằng Docker (Khuyên dùng)

Sử dụng Docker là cách nhanh nhất để khởi chạy toàn bộ hệ thống (Frontend, Backend, Database) mà không cần cài đặt môi trường phức tạp.

### Yêu cầu:
*   Đã cài đặt **Docker** và **Docker Compose**.

### Bước 1: Cấu hình Môi trường
Tạo file `.env` ở **thư mục gốc** của dự án (ngang hàng với `docker-compose.yml`):
```env
GEMINI_API_KEY=your_google_gemini_api_key_here
SECRET_KEY=your_super_secret_key_here
```

### Bước 2: Khởi động hệ thống
Mở terminal tại thư mục gốc và chạy:
```bash
docker-compose up -d --build
```
*Hệ thống sẽ tự động tải các image cần thiết, cấu hình Database và chạy tự động lệnh tạo bảng (Migration).*

### Bước 3: Nạp dữ liệu mẫu (Seed Data)
Để nạp dữ liệu trải nghiệm mẫu (User, Danh mục, Ví, Giao dịch...), chạy lệnh sau:
```bash
docker exec -it ifinance_backend python seed.py
```

### Bước 4: Trải nghiệm ứng dụng
*   **Frontend Web App:** Truy cập `http://localhost:5173`
    *   *Tài khoản test:* `test@ifinance.com`
    *   *Mật khẩu:* `Test@123`
*   **Backend API Docs (Swagger UI):** Truy cập `http://localhost:8000/docs`

> **Các lệnh Docker hữu ích:**
> *   Xem log backend: `docker logs -f ifinance_backend`
> *   Dừng hệ thống: `docker-compose stop`
> *   Xóa dữ liệu cũ & Database (Làm lại từ đầu): `docker-compose down -v`

---

## 💻 Hướng dẫn chạy thủ công (Local Development)

### Yêu cầu hệ thống
*   Python 3.10+
*   Node.js 20+
*   PostgreSQL & MongoDB (Local hoặc Cloud)
*   API Key từ Google AI Studio (Gemini)

### 1. Backend (FastAPI)
```bash
cd backend

# Khởi tạo và kích hoạt môi trường ảo
python -m venv .venv
# Trên Windows:
.\.venv\Scripts\activate
# Trên macOS/Linux:
source .venv/bin/activate

# Cài đặt thư viện
pip install -r requirements.txt
```

Cấu hình file `.env` bên trong thư mục `backend/`:
```env
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/ifinance
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/
SECRET_KEY=your_super_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
GEMINI_API_KEY=your_google_gemini_api_key_here
VNSTOCKS_API_KEY=your_vnstocks_api_key_here
```

Nạp dữ liệu mẫu (Seed Data) & Khởi chạy Server:
```bash
# Cập nhật cấu trúc database
alembic upgrade head

# Nạp dữ liệu mẫu (Tài khoản test@ifinance.com / mật khẩu Test@123)
python seed.py

# Khởi chạy backend API
uvicorn app.main:app --reload --port 8000
```

### 2. Frontend (ReactJS)
Mở cửa sổ Terminal thứ 2, chạy giao diện:
```bash
cd frontend
npm install
npm run dev
```
Giao diện sẽ chạy ở `http://localhost:5173`

---

## 🧪 Hướng dẫn chạy Unit Test (Xác thực Logic)

IFinance được trang bị bộ khung kiểm thử (Unit Tests) vô cùng toàn diện tập trung vào tầng **Services** thông qua thư viện `pytest`. Quá trình Test diễn ra trên một cơ sở dữ liệu `sqlite:///:memory:` hoàn toàn biệt lập, không tác động đến dữ liệu thực. Đồng thời, API gọi Gemini AI được Mock 100% để tốc độ test luôn siêu tốc độ (< 5 giây) và không tốn chi phí gọi Google API.

### Chạy hệ thống Test:
Đảm bảo bạn đang ở trong thư mục `backend` và có kích hoạt môi trường ảo.
```bash
cd backend
pytest -v
```

Kiểm tra độ bao phủ mã nguồn (Code Coverage):
```bash
pytest --cov=app.services --cov-report=term-missing
```

### Các modules kiểm tra bao gồm:
*   `test_transactions_wallets.py`: Test luồng tài chính cốt lõi (Giao dịch, chuyển tiền, auto tính toán số dư Ví).
*   `test_debt_investment.py`: Test luồng vay/nợ, thuật toán trả nợ từng phần.
*   `test_ai_service.py`: Test AI (Chatbot RAG Function Calls, OCR Nhận thức Hóa đơn, Budget Planning).
*   `test_auth_service.py`: Test chuẩn xác cơ chế đăng nhập, Blacklist Token và Bảo mật.
