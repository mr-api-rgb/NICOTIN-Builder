from pathlib import Path
from dataclasses import dataclass

@dataclass
class ProjectInfo:
    kind: str
    root: Path
    confidence: str
    reason: str

def _has(root, *names):
    return any((root / n).exists() for n in names)

def detect_project(base: Path) -> ProjectInfo:
    roots = [base] + [p for p in base.iterdir() if p.is_dir()] if base.exists() else [base]
    for root in roots:
        if _has(root, "settings.gradle", "settings.gradle.kts", "build.gradle", "build.gradle.kts"):
            return ProjectInfo("android-gradle", root, "high", "Gradle Android project files found.")
        if (root / "pubspec.yaml").exists():
            return ProjectInfo("flutter", root, "high", "pubspec.yaml found.")
        if any(root.glob("*.unity")) or (root / "ProjectSettings").is_dir():
            return ProjectInfo("unity", root, "high", "Unity project markers found.")
        if (root / "buildozer.spec").exists():
            return ProjectInfo("python-kivy", root, "high", "buildozer.spec found.")
        if (root / "package.json").exists() or (root / "index.html").exists():
            return ProjectInfo("web", root, "medium", "Web project markers found.")
    return ProjectInfo("unknown", base, "low", "No supported project marker was found.")
