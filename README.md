# 🛠️ NICOTIN-Builder-V1

> A GUI-based software project builder that automatically detects project types and currently supports **real Android/Gradle builds with APK output**.

> یک ابزار گرافیکی برای دریافت و ساخت پروژه‌های نرم‌افزاری که نوع پروژه را به‌صورت خودکار تشخیص می‌دهد و در نسخه فعلی از **Build واقعی پروژه‌های Android/Gradle و تولید APK** پشتیبانی می‌کند.

---

## ✨ Features | قابلیت‌ها

* 📦 Receive software projects for Build
* 🔐 Extract projects with basic security controls
* 🔍 Automatically detect project type
* 🤖 Identify Android / Gradle projects
* ⚙️ Support Gradle and Gradle Wrapper
* 🏗️ Execute real Android project Build processes
* 📱 Generate the final APK output
* 📁 Save generated APK to `output/app-debug.apk`
* 🖥️ Display Build process logs directly inside the GUI
* 🔎 Detect other supported project types
* 📥 Install Python dependencies from `requirements.txt`
* ▶️ Run the application with `py -m app.main`

---

## 🎯 Main Purpose | هدف اصلی

NICOTIN-Builder-V1 is designed to simplify the process of receiving and building software projects through a graphical interface.

The application analyzes the incoming project, determines its type, and selects the appropriate workflow.

Currently, Android/Gradle projects have an active Build pipeline capable of producing a real APK file.

---

## 🤖 Automatic Project Detection

The application analyzes the received project and attempts to determine its type automatically.

For Android projects, it can recognize common Gradle-based structures and use either:

* `Gradle`
* `Gradle Wrapper`

for the Build process.

Other project types can also be detected, but their dedicated Build workflow is **not currently enabled** in this version.

---

## 📱 Android Build

Android/Gradle projects are processed through an actual Build workflow.

The general process is:

```text
Project
   │
   ▼
Project Extraction
   │
   ▼
Project Type Detection
   │
   ▼
Android / Gradle Detection
   │
   ▼
Gradle / Gradle Wrapper
   │
   ▼
Android Build
   │
   ▼
APK Generation
   │
   ▼
output/app-debug.apk
```

---

## 📦 APK Output

After a successful Android Build, the generated APK is stored at:

```text
output/app-debug.apk
```

This provides a consistent location for accessing the Build result.

---

## 🖥️ GUI Build Logs

The Build process can produce a large amount of output.

NICOTIN-Builder-V1 displays the Build logs directly inside the graphical interface, making it possible to monitor the process without relying entirely on a separate terminal.

Example workflow:

```text
[INFO] Project received
[INFO] Extracting project...
[INFO] Detecting project type...
[INFO] Android / Gradle project detected
[INFO] Starting Build...
[INFO] Gradle task running...
[INFO] APK generated
[INFO] Output: output/app-debug.apk
```

---

## 🔐 Project Extraction

Received projects are extracted using basic security controls before the Build process begins.

The purpose of this stage is to provide an additional layer of protection while handling project archives.

> ⚠️ Basic extraction controls should not be considered a complete security sandbox. Only Build projects from trusted or controlled sources.

---

## 📥 Python Dependencies

Python dependencies can be installed automatically from:

```text
requirements.txt
```

Install them manually with:

```bash
py -m pip install -r requirements.txt
```

---

## 🚀 Installation & Run

Clone or enter the project directory:

```bash
cd NICOTIN-Builder-V1
```

Install dependencies:

```bash
py -m pip install -r requirements.txt
```

Run the application:

```bash
py -m app.main
```

---

## 📋 Requirements

The project currently expects an environment capable of running:

* 🐍 Python
* 📦 Dependencies listed in `requirements.txt`
* ⚙️ Gradle / Gradle Wrapper for Android projects
* ☕ Java / Android build environment for Android APK generation

The exact Android Build environment depends on the project being built.

---

## 🧩 Supported Project Types

| Project Type             | Detection | Build Support |
| ------------------------ | --------: | ------------: |
| 📱 Android / Gradle      |         ✅ |             ✅ |
| ⚙️ Gradle-based projects |         ✅ |             ✅ |
| 🐍 Python projects       |         ✅ |            🔄 |
| 📦 Other project types   |         ✅ |            🔄 |

> `🔄` indicates that the project type may be recognized, but a dedicated Build pipeline is not currently active in this version.

---

## 📂 Output Structure

After a successful Build, the project can produce an output structure similar to:

```text
NICOTIN-Builder-V1/
│
├── app/
│   └── main.py
│
├── output/
│   └── app-debug.apk
│
├── requirements.txt
└── README.md
```

---

## 🔄 Build Workflow

```text
Receive Project
       ↓
Secure Extraction
       ↓
Automatic Detection
       ↓
Project Classification
       ↓
Android / Gradle Build
       ↓
Build Logs → GUI
       ↓
APK Generation
       ↓
output/app-debug.apk
```

---

## 🚧 Current Status

### ✅ Currently Available

* Project receiving
* Basic-secured extraction
* Automatic project detection
* Android / Gradle detection
* Gradle support
* Gradle Wrapper support
* Real Android Build
* APK generation
* GUI Build logs
* `requirements.txt` dependency installation

### 🔜 Future Expansion

The architecture can be extended to support dedicated Build workflows for additional project types beyond Android/Gradle.

---

## ⚠️ Security Notice

NICOTIN-Builder-V1 executes Build-related commands from received software projects.

Only process projects from sources you trust or in environments specifically intended for testing and Build operations.

Do not treat the application as a fully isolated or malware-proof execution sandbox.

---

## 👨‍💻 Developer

**mr-api**

---

# 🇮🇷 نسخه فارسی

# 🛠️ NICOTIN-Builder-V1

**NICOTIN-Builder-V1** یک ابزار گرافیکی برای دریافت و Build پروژه‌های نرم‌افزاری است که نوع پروژه را به‌صورت خودکار تشخیص می‌دهد.

در نسخه فعلی، تمرکز اصلی پروژه روی **Build واقعی پروژه‌های Android/Gradle و تولید فایل APK** است.

---

## ✨ قابلیت‌ها

* 📦 دریافت پروژه برای Build
* 🔐 استخراج پروژه با کنترل‌های امنیتی پایه
* 🔍 تشخیص خودکار نوع پروژه
* 🤖 شناسایی پروژه‌های Android / Gradle
* ⚙️ پشتیبانی از Gradle و Gradle Wrapper
* 🏗️ اجرای فرآیند واقعی Build پروژه Android
* 📱 تولید فایل APK
* 📁 ذخیره APK در مسیر `output/app-debug.apk`
* 🖥️ نمایش لاگ‌های Build داخل رابط گرافیکی
* 🔎 شناسایی سایر انواع پروژه‌ها
* 📥 نصب Dependencyها از طریق `requirements.txt`
* ▶️ اجرای برنامه با `py -m app.main`

---

## 🎯 هدف پروژه

هدف NICOTIN-Builder-V1 ساده‌تر کردن فرآیند دریافت و Build پروژه‌ها از طریق یک رابط گرافیکی است.

برنامه پروژه دریافت‌شده را بررسی کرده، نوع آن را تشخیص می‌دهد و Workflow مناسب را انتخاب می‌کند.

در نسخه فعلی، پروژه‌های Android/Gradle دارای فرآیند Build فعال هستند و می‌توانند یک APK واقعی تولید کنند.

---

## 🤖 تشخیص خودکار نوع پروژه

پروژه پس از دریافت، بررسی می‌شود تا نوع آن به‌صورت خودکار مشخص شود.

برای پروژه‌های Android، ساختارهای مبتنی بر Gradle شناسایی شده و Build می‌تواند با یکی از موارد زیر انجام شود:

* `Gradle`
* `Gradle Wrapper`

سایر انواع پروژه نیز ممکن است شناسایی شوند، اما در نسخه فعلی فرآیند Build اختصاصی آن‌ها فعال نیست.

---

## 📱 فرآیند Build اندروید

فرآیند کلی Build به شکل زیر است:

```text
دریافت پروژه
     ↓
استخراج پروژه
     ↓
تشخیص نوع پروژه
     ↓
شناسایی Android / Gradle
     ↓
اجرای Gradle / Gradle Wrapper
     ↓
Build پروژه Android
     ↓
تولید APK
     ↓
output/app-debug.apk
```

---

## 📦 فایل خروجی APK

پس از موفقیت‌آمیز بودن Build، فایل APK در مسیر زیر قرار می‌گیرد:

```text
output/app-debug.apk
```

---

## 🖥️ نمایش لاگ‌ها در GUI

تمام مراحل Build می‌توانند خروجی و لاگ‌های مختلفی ایجاد کنند.

NICOTIN-Builder-V1 این لاگ‌ها را مستقیماً داخل رابط گرافیکی نمایش می‌دهد تا کاربر بتواند فرآیند Build را مشاهده و بررسی کند.

نمونه:

```text
[INFO] Project received
[INFO] Extracting project...
[INFO] Detecting project type...
[INFO] Android / Gradle project detected
[INFO] Starting Build...
[INFO] Gradle task running...
[INFO] APK generated
[INFO] Output: output/app-debug.apk
```

---

## 🔐 استخراج پروژه

پروژه‌های دریافت‌شده قبل از Build با استفاده از کنترل‌های امنیتی پایه استخراج می‌شوند.

هدف این مرحله، اضافه کردن یک لایه محافظتی هنگام پردازش فایل‌های پروژه است.

> ⚠️ این کنترل‌ها یک Sandbox امنیتی کامل محسوب نمی‌شوند. فقط پروژه‌های مورد اعتماد یا پروژه‌هایی که برای تست در نظر گرفته شده‌اند را Build کنید.

---

## 📥 نصب Dependencyها

Dependencyهای پایتون از طریق فایل زیر قابل نصب هستند:

```text
requirements.txt
```

برای نصب:

```bash
py -m pip install -r requirements.txt
```

---

## 🚀 نصب و اجرا

ابتدا وارد پوشه پروژه شوید:

```bash
cd NICOTIN-Builder-V1
```

سپس Dependencyها را نصب کنید:

```bash
py -m pip install -r requirements.txt
```

در نهایت برنامه را اجرا کنید:

```bash
py -m app.main
```

---

## 📋 پیش‌نیازها

برای اجرای پروژه به محیطی با موارد زیر نیاز است:

* 🐍 Python
* 📦 Dependencyهای موجود در `requirements.txt`
* ⚙️ Gradle یا Gradle Wrapper برای پروژه‌های Android
* ☕ Java و محیط Build اندروید برای تولید APK

پیش‌نیازهای دقیق Build اندروید می‌تواند به پروژه‌ای که قرار است Build شود وابسته باشد.

---

## 🧩 انواع پروژه‌ها

| نوع پروژه           | شناسایی | Build |
| ------------------- | ------: | ----: |
| 📱 Android / Gradle |       ✅ |     ✅ |
| ⚙️ پروژه‌های Gradle |       ✅ |     ✅ |
| 🐍 پروژه‌های Python |       ✅ |    🔄 |
| 📦 سایر پروژه‌ها    |       ✅ |    🔄 |

> `🔄` یعنی نوع پروژه قابل شناسایی است، اما Workflow اختصاصی Build آن در نسخه فعلی فعال نیست.

---

## 📂 ساختار خروجی

نمونه‌ای از ساختار پروژه:

```text
NICOTIN-Builder-V1/
│
├── app/
│   └── main.py
│
├── output/
│   └── app-debug.apk
│
├── requirements.txt
└── README.md
```

---

## 🔄 چرخه Build

```text
دریافت پروژه
      ↓
استخراج کنترل‌شده
      ↓
تشخیص خودکار
      ↓
تعیین نوع پروژه
      ↓
Build پروژه Android / Gradle
      ↓
نمایش لاگ در GUI
      ↓
تولید APK
      ↓
output/app-debug.apk
```

---

## 🚧 وضعیت فعلی پروژه

### ✅ قابلیت‌های فعال

* دریافت پروژه
* استخراج با کنترل‌های امنیتی پایه
* تشخیص خودکار نوع پروژه
* شناسایی Android / Gradle
* پشتیبانی از Gradle
* پشتیبانی از Gradle Wrapper
* Build واقعی Android
* تولید APK
* نمایش لاگ‌های Build در GUI
* نصب Dependencyهای `requirements.txt`

### 🔜 توسعه‌های آینده

ساختار پروژه می‌تواند در نسخه‌های بعدی برای پشتیبانی از Workflowهای اختصاصی Build برای انواع بیشتری از پروژه‌ها گسترش پیدا کند.

---

## ⚠️ نکات امنیتی

NICOTIN-Builder-V1 دستورات مرتبط با Build را از پروژه‌های دریافت‌شده اجرا می‌کند.

بنابراین فقط پروژه‌هایی را پردازش کنید که به آن‌ها اعتماد دارید یا برای تست و Build در یک محیط کنترل‌شده قرار دارند.

این پروژه یک Sandbox کامل برای اجرای کدهای ناشناس محسوب نمی‌شود.

---

## 👨‍💻 توسعه‌دهنده

**mr-api**
