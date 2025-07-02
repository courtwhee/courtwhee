#!/usr/bin/env python3
"""Interactive network quiz game."""


def main():
    questions = [
        {
            "text": "Which OSI layer is responsible for routing packets across networks?",
            "options": {
                "A": "Data Link",
                "B": "Network",
                "C": "Transport",
                "D": "Session",
            },
            "answer": "B",
            "explanation": "The Network layer (Layer 3) handles logical addressing and routing of packets between networks.",
        },
        {
            "text": "What device is used to connect multiple network segments and route traffic between them?",
            "options": {
                "A": "Switch",
                "B": "Repeater",
                "C": "Router",
                "D": "Hub",
            },
            "answer": "C",
            "explanation": "Routers connect different networks and route traffic based on IP addresses.",
        },
        {
            "text": "Which protocol is commonly used to translate domain names to IP addresses?",
            "options": {
                "A": "FTP",
                "B": "SMTP",
                "C": "DHCP",
                "D": "DNS",
            },
            "answer": "D",
            "explanation": "DNS (Domain Name System) resolves domain names to IP addresses.",
        },
        {
            "text": "What is the default port for HTTPS?",
            "options": {
                "A": "80",
                "B": "21",
                "C": "443",
                "D": "25",
            },
            "answer": "C",
            "explanation": "HTTPS typically uses TCP port 443 for encrypted web traffic.",
        },
        {
            "text": "Which of the following is a private IP address range?",
            "options": {
                "A": "172.16.0.0/12",
                "B": "11.0.0.0/8",
                "C": "139.0.0.0/8",
                "D": "200.200.0.0/16",
            },
            "answer": "A",
            "explanation": "172.16.0.0 to 172.31.255.255 is reserved for private networks.",
        },
        {
            "text": "What protocol does ping use?",
            "options": {
                "A": "TCP",
                "B": "UDP",
                "C": "ICMP",
                "D": "ARP",
            },
            "answer": "C",
            "explanation": "Ping uses ICMP (Internet Control Message Protocol) echo requests and replies.",
        },
        {
            "text": "Which wireless security protocol is considered the most secure for home networks?",
            "options": {
                "A": "WEP",
                "B": "WPA",
                "C": "WPA2",
                "D": "Open",
            },
            "answer": "C",
            "explanation": "WPA2 provides stronger encryption than WEP or WPA and is recommended for home use.",
        },
        {
            "text": "What type of address is used at the Data Link layer for frame delivery?",
            "options": {
                "A": "IP address",
                "B": "MAC address",
                "C": "Port number",
                "D": "Domain name",
            },
            "answer": "B",
            "explanation": "MAC addresses uniquely identify devices on the local network at Layer 2.",
        },
        {
            "text": "Which command can display your computer's current IP configuration on Windows?",
            "options": {
                "A": "ifconfig",
                "B": "netstat",
                "C": "ipconfig",
                "D": "route",
            },
            "answer": "C",
            "explanation": "ipconfig shows IP configuration details on Windows systems.",
        },
        {
            "text": "A small network connecting personal devices within a few meters is called what?",
            "options": {
                "A": "LAN",
                "B": "WAN",
                "C": "PAN",
                "D": "MAN",
            },
            "answer": "C",
            "explanation": "A PAN (Personal Area Network) covers a short range around a person, typically a few meters.",
        },
    ]

    score = 0
    total = len(questions)

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['text']}")
        for option, text in sorted(q["options"].items()):
            print(f"  {option}. {text}")

        user_input = input("Your answer (A/B/C/D): ").strip().upper()
        if user_input == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q['answer']}")
        print(f"Explanation: {q['explanation']}")

    print(f"\nYou scored {score} out of {total}.")


if __name__ == "__main__":
    main()
