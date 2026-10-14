"""Optional end-to-end test for real FFmpeg assembly using synthetic local clips.

No external footage, provider API, credentials, or network access is used.
"""
import importlib.util
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
ASSEMBLER_SPEC = importlib.util.spec_from_file_location(
    "media_assembler", ROOT / "src" / "media_assembler.py"
)
assembler = importlib.util.module_from_spec(ASSEMBLER_SPEC)
ASSEMBLER_SPEC.loader.exec_module(assembler)

QUALITY_SPEC = importlib.util.spec_from_file_location(
    "media_quality_check", ROOT / "src" / "media_quality_check.py"
)
quality = importlib.util.module_from_spec(QUALITY_SPEC)
QUALITY_SPEC.loader.exec_module(quality)


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"),
                     "FFmpeg and ffprobe are required for this integration test")
class MediaAssemblyIntegrationTests(unittest.TestCase):
    def test_two_synthetic_clips_assemble_and_pass_technical_quality_gate(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            clips = [root / "clip-a.mp4", root / "clip-b.mp4"]

            # Synthetic color footage is only a pipeline fixture, never a publishable asset.
            for color, clip in zip(("0x244b83", "0x8b4c9e"), clips):
                subprocess.run(
                    [
                        shutil.which("ffmpeg"), "-hide_banner", "-loglevel", "error",
                        "-f", "lavfi", "-i",
                        f"color=c={color}:s=540x960:r=30:d=4",
                        "-t", "4", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p",
                        str(clip),
                    ],
                    check=True, capture_output=True, timeout=60,
                )

            output = root / "assembled.mp4"
            thumbnail = root / "thumbnail.png"
            assembler.assemble_sequence(clips, output, thumbnail, target_duration=8)

            self.assertTrue(output.is_file())
            self.assertGreater(output.stat().st_size, 0)
            self.assertTrue(thumbnail.is_file())
            self.assertEqual(quality.inspect(output, thumbnail), [])
