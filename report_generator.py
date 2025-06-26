def generate_report(delivery_status, tls_status, headers):
    with open("report.txt", "w") as f:
        f.write("=== EMAIL DELIVERY REPORT ===\n")
        f.write(f"Delivery Status: {delivery_status}\n")
        f.write(f"TLS Check: {tls_status}\n")
        f.write("Headers:\n")
        for k, v in headers.items():
            f.write(f"{k}: {v}\n")
    print("📄 Report saved to report.txt.")
