"""
Verification Script for Shashwat Bikram Singh's (25BTRCN173) 80:20 Experimental Suite.
Runs all 15 model scripts in SDGC_60_40_0.2 and validates that each exits cleanly with code 0.
"""

import sys
import subprocess
from pathlib import Path

target_dir = Path(__file__).resolve().parent / "SDGC_60_40_0.2"
scripts = sorted(list(target_dir.glob("SDGC 60,40 *.py")))

print(f"\n======================================================================")
print(f"VERIFYING 80:20 SUITE (15 SCRIPTS) - CONTRIBUTOR: SHASHWAT BIKRAM SINGH")
print(f"======================================================================\n")

passed = 0
failed = 0

for s in scripts:
    print(f"Running: {s.name} ... ", end="", flush=True)
    res = subprocess.run([sys.executable, str(s)], capture_output=True, text=True)
    if res.returncode == 0:
        print("PASS [Exit 0]")
        passed += 1
    else:
        print(f"FAIL [Exit {res.returncode}]")
        print("--- STDERR ---")
        print(res.stderr[:500])
        print("--------------")
        failed += 1

print(f"\n======================================================================")
print(f"RESULTS: {passed} PASSED, {failed} FAILED (Total: {len(scripts)})")
print(f"======================================================================\n")

if failed > 0:
    sys.exit(1)

