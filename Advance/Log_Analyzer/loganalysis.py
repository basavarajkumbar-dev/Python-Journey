import re
from collections import Counter, defaultdict
from datetime import datetime

class LogAnalyser:
    def __init__(self):
        self.total_requests = 0
        self.ipaddresses = Counter()
        self.status_codes = Counter()
        self.resources = Counter()
        self.suspicious_ips = defaultdict(int)
        self.file_name = "access.log"
    
    def parse_log_line(self, line):
        pattern = r'(\d+.\d+.\d+.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'
        match = re.match(pattern, line)
        if match:
            return {
                "ip": match.group(1),
                "timestamp": match.group(2),
                "request": match.group(3),
                "status_code": int(match.group(4)),
                "size": int(match.group(5))
            }
    
    def process_enrty(self, parsed_entry):
        self.total_requests += 1
        ip = parsed_entry["ip"]
        status = parsed_entry["status_code"]

        self.ipaddresses[ip] += 1
        self.status_codes[status] +=1

        resource_parts = parsed_entry["request"].split()
        if len(resource_parts) >= 2:
            resource = resource_parts[1]
            self.resources[resource] += 1
        
        if status == 403:
            self.suspicious_ips[ip] += 1

    def generate_report(self):
        report = []
        report.append("="*50)
        report.append("LOG FILE ANALYSIS REPORT")
        report.append("="*50)
        report.append(f"Total Requests: {self.total_requests}")

        report.append("\n--- STATUS CODE SUMMARY ---")
        for code, count in self.status_codes.items():
            percentage = (count/self.total_requests)*100
            report.append(f"{code}: {count} requests ({percentage:.2f}%)")

        report.append("\n--- TOP 5 IP ADDRESSES ---")
        for ip, count in self.ipaddresses.most_common(5):
            percentage = (count/self.total_requests)*100
            report.append(f"{ip}: {count} requests ({percentage:.2f}%)")
        
        report.append("\n--- SECURITY FINDINGS ---")
        for ip, count in self.suspicious_ips.items():
            if count >= 3:
                report.append(f"⚠️ {ip}: {count} 403 Forbidden errors")
        
        return "\n".join(report)


def main():
    analyser = LogAnalyser()

    try:
        with open("access.log", "r") as file:
            log_data = file.readlines()
            for line in log_data:
                parsed_entry = analyser.parse_log_line(line.strip())
                analyser.process_enrty(parsed_entry)
    except FileNotFoundError:
        print("Error: Log file not found!!")
    else: 
        report = analyser.generate_report()
        print(report)

        if report:
            with open("analysis_report.txt", "w", encoding="utf-8") as file:
                file.write(report)


if __name__ == "__main__":
    main()