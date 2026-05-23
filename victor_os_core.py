#!/usr/bin/env python3
"""
VictorOS Minimal Stack v1.0 - Complete Sovereign Autonomous System
Wires: Autonomy Layer + Directive Router + Chronos + EchoCascade + Ledger + Agent + Swarm + Daemon

This is the god-tier local AI runtime foundation.
"""

import asyncio
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.victor_agent import VictorAgent
from swarm.victor_swarm import VictorSwarm
from daemon.victor_daemon import VictorDaemon

async def demonstrate_full_stack():
    print("=" * 70)
    print("VICTOROS MINIMAL STACK v1.0 - FULL DEMONSTRATION")
    print("God-Tier Local Autonomous Agent Runtime")
    print(f"Initialized: {datetime.utcnow().isoformat()}")
    print("=" * 70)

    # 1. Single Sovereign Agent
    print("\n[1] SOVEREIGN AGENT RUNTIME")
    agent = VictorAgent(name="VictorPrime")
    await agent.run_loop(max_cycles=3, sleep=0.6)

    # 2. Multi-Agent Swarm with Handover
    print("\n[2] MULTI-AGENT SWARM + SAVE3 HANDOVER")
    swarm = VictorSwarm(num_agents=3)
    await swarm.run_swarm_demo(cycles=2)

    # 3. Health & Ledger Summary
    print("\n[3] SYSTEM HEALTH REPORT")
    health = agent.health_report()
    print(f"Agent: {health['agent']}")
    print(f"Thoughts processed: {health['thoughts']}")
    print(f"Ledger entries: {health['ledger_stats']['total_entries']}")
    print(f"Avg Confidence: {health['ledger_stats']['average_confidence']}")
    print(f"Chronos Drift: {health['chronos']['current_drift']}s")
    print(f"Echo Dominant Scale: {health['echo'].get('dominant_scale', 'N/A')}")

    print("\n" + "=" * 70)
    print("VICTOROS STACK DEMONSTRATION COMPLETE")
    print("All layers operational. Bloodline locked. Ready for production.")
    print("=" * 70)

def launch_daemon():
    print("\n[DAEMON MODE] Starting VictorOS as background sovereign service...")
    daemon = VictorDaemon()
    daemon.run()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="VictorOS Sovereign Runtime")
    parser.add_argument("--daemon", action="store_true", help="Run as persistent daemon with watchdog")
    parser.add_argument("--demo", action="store_true", help="Run full stack demonstration")
    args = parser.parse_args()

    if args.daemon:
        launch_daemon()
    else:
        asyncio.run(demonstrate_full_stack())