from pathlib import Path
import subprocess
import os

class BuildError(RuntimeError):
    pass

def _run(cmd, cwd, log):
    log("$ " + " ".join(map(str, cmd)))
    process = subprocess.Popen(
        cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, encoding="utf-8", errors="replace"
    )
    for line in process.stdout:
        log(line.rstrip())
    code = process.wait()
    if code != 0:
        raise BuildError(f"Build failed with exit code {code}")

def build_android_gradle(root: Path, output_dir: Path, log):
    gradlew = root / ("gradlew.bat" if os.name == "nt" else "gradlew")
    if gradlew.exists():
        cmd = [str(gradlew), "assembleDebug"]
    else:
        cmd = ["gradle", "assembleDebug"]

    _run(cmd, root, log)

    apks = list(root.rglob("*.apk"))
    if not apks:
        raise BuildError("Build finished but no APK was found.")

    output_dir.mkdir(parents=True, exist_ok=True)
    source = max(apks, key=lambda p: p.stat().st_mtime)
    target = output_dir / "app-debug.apk"
    target.write_bytes(source.read_bytes())
    log(f"APK: {target}")
    return target

def build(project, output_dir, log):
    if project.kind == "android-gradle":
        return build_android_gradle(project.root, output_dir, log)
    raise BuildError(
        f"V1 هنوز Build خودکار برای نوع '{project.kind}' ندارد. "
        "تشخیص پروژه انجام شده است."
    )
