from agents.monitoring_agent import read_logs
from agents.rca_agent import detect_anomaly
from agents.reporter_agent import generate_report

def run_pipeline():
    logs = read_logs()
    analysis = detect_anomaly(logs)
    report = generate_report(analysis)

    print(report)

if __name__ == "__main__":
    run_pipeline()