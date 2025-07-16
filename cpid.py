import argparse
from core.phase1_ingest import run as phase1
from core.phase2_metrics import run as phase2
from core.phase3_anomaly import run as phase3
from core.phase4_forecast import run as phase4
from core.phase5_audit import run as phase5
from core.isms_mapper import run as phase6

import os

os.makedirs("metrics", exist_ok=True)
os.makedirs("logs", exist_ok=True)

def run_all():
    print("Running Full CPID Pipeline\n")
    phase1()
    phase2()
    phase3()
    phase4()
    phase5()
    phase6()
    print("\nAll phases completed.\n")

def run_phase(phase):
    phases = {
        "phase1": phase1,
        "phase2": phase2,
        "phase3": phase3,
        "phase4": phase4,
        "phase5": phase5,
        "phase6": phase6
    }

    if phase in phases:
        print(f"Running {phase}\n")
        phases[phase]()
    else:
        print(f"Unknown phase: {phase}")
        print("Valid options: phase1, phase2, phase3, phase4, phase5, phase6")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Cybersecurity Project Intelligence Dashboard (CPID)"
    )

    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Run full pipeline or a specific phase")
    run_parser.add_argument(
        "target", choices=["all", "phase1", "phase2", "phase3", "phase4", "phase5", "phase6"],
        help="Which phase to run"
    )

    subparsers.add_parser("audit", help="Run audit logger and ISMS control mapping only")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()

    elif args.command == "run":
        if args.target == "all":
            run_all()
        else:
            run_phase(args.target)

    elif args.command == "audit":
        print("Running audit + ISMS mapping...\n")
        phase5()
        phase6()
