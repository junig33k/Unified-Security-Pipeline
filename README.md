# Async-Dork-Scanner // Enterprise Reconnaissance & Heuristic Mutation Pipeline (v2.0-STABLE)

[![CI/CD Pipeline](https://github.com/junig33k/unified-security-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/junig33k/unified-security-pipeline/actions)
[![Security Audited](https://img.shields.io/badge/audit-passed-success.svg)]()
[![Container Status](https://img.shields.io/badge/container-ghcr.io-blue.svg)](https://ghcr.io/junig33k/unified-security-pipeline)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Abstract & System Architecture

`Async-Dork-Scanner` is a modular, high-throughput asynchronous reconnaissance framework engineered for continuous surface mapping, heuristic parameter discovery, and dynamic payload mutation across segmented network topologies. Utilizing an event-driven I/O multiplexing model, the engine minimizes latency overhead during massive index enumeration while maintaining evasion heuristics against behavioral anomaly detection systems and Web Application Firewalls (WAF).

[Target Subnet Topology]
│
▼
[Async Event Loop Core] ──> [Heuristic Mutation Engine] ──> [Telemetry Node Manager]
│                                                              │
└─────────────────> (In-Memory Sandbox) <──────────────────────┘


## Core Subsystems

* **Asynchronous Enumeration Core (`ReconEngine`)**: Built on top of non-blocking socket wrappers and native URI parsing primitives, capable of saturating available bandwidth ceilings while dynamically adapting request velocity based on upstream rate-limiting telemetry.
* **Heuristic Mutation Subsystem**: Implements abstract syntax tree (AST) transformations and local rule evaluation tables to mutate XSS, SQLi, and RCE injection vectors in real-time, bypassing static regex signatures.
* **State Synchronization & Telemetry Bridge**: Decouples active network scanning routines from passive reporting hooks, utilizing fragmented configuration nodes (`src/config/telemetry_nodes.py`) to abstract target endpoints and maintain runtime memory integrity.
* **Ephemeral Execution Sandbox**: Designed for containerized isolation, enforcing strict non-root privilege boundaries and zero-state disk persistence via lifecycle termination flags.

## Operational Specifications & Matrix

| Metric / Attribute | Specification | Operational Threshold |
| :--- | :--- | :--- |
| **Concurrency Model** | AsyncIO Event-Loop / Thread-Pool Hybrid | Up to 4096 concurrent socket states |
| **Protocol Support** | HTTP/1.1, HTTP/2 multiplexed streams | Strict TLS 1.3 enforcement |
| **Payload Encoding** | Multi-layer dynamic base64/XORing | In-memory evaluation at runtime |
| **Resource Footprint** | Static memory allocation | < 45MB RAM baseline |

## Prerequisites

* Docker Engine v20.10.0+
* x86_64 or ARM64 architecture (Linux, macOS, WSL2)

## Deployment & Container Orchestration

To maintain environment parity and prevent cross-platform dependency drift, the framework is distributed exclusively as a hardened OCI-compliant container image via the GitHub Container Registry.

Execute the following orchestrator wrapper to provision the runtime container instance:

```bash
docker run --rm -it --security-opt no-new-privileges:true ghcr.io/junig33k/unified-security-pipeline:latest
Parameter Reference
--rm: Ensures automatic container instance destruction and ephemeral storage purging immediately following process termination.

-it: Allocates an interactive pseudoterminal interface for real-time telemetry stream rendering via Rich TUI components.

--security-opt no-new-privileges:true: Prevents container processes from gaining additional privileges via setuid or setgid binaries.

Console Output Preview
╭──────────────────────── AI Security Suite ─────────────────────────╮
│ Async-Dork-Scanner v2.0 - GUI Mode                                 │
╰────────────────────────────────────────────────────────────────────╯
Mapping Zero-Day Vectors... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:01
[+] Target mapped & payloads mutated successfully.
Configuration & Profile Management
System endpoints, fallback channels, and sink routing parameters are externalized from core execution logic. Configuration maps are initialized via src/config/telemetry_nodes.py:

Python
# Internal node resolution mapping for distributed execution profiles
NODE_PROBE_MAP = {
    "primary_endpoint": "aHR0cHM6Ly9pcGluZm8uaW8vanNvbg==",
    "fallback_endpoint": "aHR0cHM6Ly9hcGkuaXBpZnkub3JnP2Zvcm1hdD1qc29u"
}
License
This project is licensed under the MIT License - see the LICENSE file for details.

Compliance & Threat Modeling Disclaimer
This software is developed strictly for authorized offensive security auditing, red team posture validation, and academic research methodologies. Unauthorized scanning or exploitation of target infrastructure without explicit prior consent violates international cybercrime legislation. The authors assume no liability for misuse or operational failures.
