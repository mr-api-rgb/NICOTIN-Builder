import shutil
import threading
from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog, messagebox

from .config import WORKSPACE, OUTPUT
from .extractor import extract_zip
from .detector import detect_project
from .builder import build, BuildError

class BuilderApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("NICOTIN Builder V1")
        self.geometry("900x650")
        self.minsize(760, 560)

        self.zip_path = None
        self.project = None

        ctk.CTkLabel(self, text="NICOTIN BUILDER", font=ctk.CTkFont(size=28, weight="bold")).pack(pady=(25, 5))
        ctk.CTkLabel(self, text="ZIP → Detect → Build APK").pack(pady=(0, 20))

        top = ctk.CTkFrame(self)
        top.pack(fill="x", padx=30, pady=10)

        self.path_label = ctk.CTkLabel(top, text="هیچ فایلی انتخاب نشده", anchor="w")
        self.path_label.pack(side="left", fill="x", expand=True, padx=15, pady=15)

        ctk.CTkButton(top, text="انتخاب ZIP", command=self.select_zip, width=130).pack(side="right", padx=10)

        self.detect_label = ctk.CTkLabel(self, text="نوع پروژه: ---", anchor="w")
        self.detect_label.pack(fill="x", padx=35, pady=(10, 5))

        self.build_button = ctk.CTkButton(
            self, text="BUILD APK", height=45, command=self.start_build, state="disabled"
        )
        self.build_button.pack(fill="x", padx=30, pady=15)

        self.log_box = ctk.CTkTextbox(self, font=("Consolas", 12))
        self.log_box.pack(fill="both", expand=True, padx=30, pady=(0, 25))

    def log(self, text):
        self.after(0, self._append_log, text)

    def _append_log(self, text):
        self.log_box.insert("end", text + "\n")
        self.log_box.see("end")

    def select_zip(self):
        path = filedialog.askopenfilename(
            title="انتخاب فایل پروژه",
            filetypes=[("ZIP files", "*.zip")]
        )
        if not path:
            return

        self.zip_path = Path(path)
        self.path_label.configure(text=str(self.zip_path))
        self.build_button.configure(state="disabled")
        self.detect_label.configure(text="نوع پروژه: در حال بررسی...")
        self.log_box.delete("1.0", "end")

        try:
            if WORKSPACE.exists():
                shutil.rmtree(WORKSPACE)
            WORKSPACE.mkdir(parents=True)

            self.log("Extracting project...")
            extract_zip(self.zip_path, WORKSPACE)
            self.project = detect_project(WORKSPACE)

            self.detect_label.configure(
                text=f"نوع پروژه: {self.project.kind} | اطمینان: {self.project.confidence}"
            )
            self.log(f"Root: {self.project.root}")
            self.log(f"Reason: {self.project.reason}")

            if self.project.kind == "android-gradle":
                self.build_button.configure(state="normal")
                self.log("Android/Gradle project is ready to build.")
            else:
                self.log("این نوع پروژه در V1 فقط شناسایی شده و Build خودکار ندارد.")

        except Exception as exc:
            self.detect_label.configure(text="نوع پروژه: خطا")
            self.log(f"ERROR: {exc}")
            messagebox.showerror("خطا", str(exc))

    def start_build(self):
        if not self.project:
            return

        self.build_button.configure(state="disabled")
        self.log_box.delete("1.0", "end")
        self.log("Starting build...")

        threading.Thread(target=self._build_worker, daemon=True).start()

    def _build_worker(self):
        try:
            if OUTPUT.exists():
                for p in OUTPUT.iterdir():
                    if p.is_file():
                        p.unlink()
                    elif p.is_dir():
                        shutil.rmtree(p)

            apk = build(self.project, OUTPUT, self.log)
            self.after(0, lambda: messagebox.showinfo("موفق", f"APK ساخته شد:\n{apk}"))
        except (BuildError, Exception) as exc:
            self.log(f"ERROR: {exc}")
            self.after(0, lambda: messagebox.showerror("Build Failed", str(exc)))
        finally:
            self.after(0, lambda: self.build_button.configure(state="normal"))

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = BuilderApp()
    app.mainloop()
