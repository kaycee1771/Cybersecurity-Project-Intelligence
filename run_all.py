import subprocess

def run_script(script_name):
    print(f"🚀 Running {script_name} ...")
    result = subprocess.run(["python", script_name])
    if result.returncode != 0:
        print(f"❌ Failed to run {script_name}")
    else:
        print(f"✅ Finished {script_name}\n")

def main():
    scripts = [
        "run_phase1.py",
        "run_phase2.py",
        "run_phase3.py",
        "run_phase4.py"
    ]

    for script in scripts:
        run_script(script)

    print("🎉 All phases executed. Check logs/project_audit.log and metrics/ for results.")

if __name__ == "__main__":
    main()
