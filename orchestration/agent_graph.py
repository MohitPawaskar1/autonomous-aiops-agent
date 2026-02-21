from agents.monitoring_agent import read_logs
from agents.rca_agent import detect_anomaly
from agents.reporter_agent import generate_report

from rag.memory_manager import store_incident, search_similar_incidents


def run_pipeline():
    print("\n🚀 Running Autonomous AIOps Pipeline...\n")

    # Step 1 — Read logs
    logs = read_logs()

    # Step 2 — Detect anomaly
    analysis = detect_anomaly(logs)

    # Step 3 — Search similar past incidents
    similar = search_similar_incidents(str(logs))
    print("\n🔎 Similar Past Incidents:\n", similar)

    # Step 4 — Generate report
    report = generate_report(analysis)

    print("\n===== INCIDENT REPORT =====\n")
    print(report)
    print("\n===========================\n")

    # Step 5 — Store incident in memory
    store_incident(report)


if __name__ == "__main__":
    run_pipeline()