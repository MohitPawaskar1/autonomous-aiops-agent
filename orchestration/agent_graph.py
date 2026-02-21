from agents.monitoring_agent import read_logs
from agents.rca_agent import detect_anomaly
from agents.reporter_agent import generate_report
from rag.memory_manager import store_incident, search_similar_incidents


def run_pipeline():
    print("\nRunning Autonomous AIOps Pipeline...\n")

    logs = read_logs()

    similar = search_similar_incidents(str(logs))
    print("Similar Past Incidents:\n", similar)

    analysis = detect_anomaly(logs)
    report = generate_report(analysis)

    print(report)

    store_incident(report)
    print("\nIncident stored in memory")


if __name__ == "__main__":
    run_pipeline()