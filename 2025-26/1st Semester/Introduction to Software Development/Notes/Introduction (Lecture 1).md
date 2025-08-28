**Course goal:** Learn to build and evolve a substantial software system using OO analysis/design/programming/testing; develop professional competence with classes, objects, methods, inheritance, polymorphism; and “learn how to learn.”

## Tools you’ll use

- **WARP**: existing Java codebase you’ll extend (originally Swift).
    
- **Eclipse IDE**: coding, building, running, debugging; rich plugin ecosystem (e.g., CheckStyle).
    
- **Git**: distributed version control (CLI emphasized).
    
- **GitLab**: remote repo, issues, CI; supports full SDLC.
    

---

## What is WARP (high level)

- A teaching/research codebase to program **wireless sensor networks (WSNs)**.
    
- You’ll read/modify/extend non-trivial existing code (like real industry work).
    
- **Core idea:** specify network behavior as **program fragments** that run in **time slots** on each node to meet **reliability** and **deadline** constraints.
    

### Wireless Sensor Networks (WSN) context

- Used in automated warehouses, process control, reconfigurable manufacturing; devices are getting more capable; wireless tech improving.
    
- Networks carry **flows** of periodic messages over multi-hop paths; flows have **static priorities** and must meet **deadlines** and **reliability** targets.
    

---

## Scheduling approaches you’ll see

### Table (TDMA) schedules

- Assign transmissions to discrete **time slots** (and channels).
    
- Can be constructed to **tolerate single-packet loss** by duplicating opportunities.
    

### WirelessHART (state-of-the-art reference)

- Central network manager builds routes + TDMA schedules via a **scheduling matrix**; topology/workload changes require **global rescheduling**.
    

### WARP’s perspective

- Treat schedules as **programs**: expressive enough to improve performance; simple enough to analyze/synthesize.
    

---

## WARP mini-DSL (intermediary language)

**Intent:** describe per-node behavior per slot with small, analyzable building blocks.

```
// Grammar (informal)
fragment      := cmd | if-stmt
if-stmt       := if bool-expr then fragment else fragment
cmd           := push(flow) | pull(flow) | wait | sleep
bool-expr     := has(flow) | !has(flow)
flow          := flow identifier
```

- **State:** each node tracks whether it **has(flow)**’s packet.
    
- **Instructions:** `pull`, `push`, `wait`, `sleep`; decisions via `has(...)`.
    
- Programs can be constructed to handle **no loss**, **one loss**, or **probabilistic losses**.
    

---

## Example program snippets (conceptual)

- **No-loss** 3-node round-trip (A↔C via B) assigns pushes/waits across slots.
    
- **Handles 1 loss:** duplicate opportunities for each flow across slots.
    

---

## Flow model & workload

- **Flow attributes:**
    
    - **Priority:** lower number = higher priority
        
    - **Period:** time between releases
        
    - **Deadline:** release → sink arrival bound
        
    - **Phase:** first release offset from time 0
        
- **Workload description:** list flows with attributes and paths (e.g., `F1(0,10,10,0): A→B→C`). More real-time theory comes later.
    

---

## Why use WARP for the course?

- Practice **reading/refactoring** someone else’s code.
    
- Add **docs (Javadoc)**, **contracts/asserts**, **unit/integration tests**, and **new features**.
    
- Learn from real-world tradeoffs (some code is intentionally imperfect).
    

---

## IDE, Eclipse, and why it matters

- **IDE = Integrated Development Environment** for editing, building, debugging (open-source & proprietary options exist).
    
- **Eclipse:** open platform, broad language support, widely used; steeper learning curve than IntelliJ, but valuable for your toolbox.
    

---

## Git & GitLab essentials

- **Git:** distributed VCS; commit, diff, checkout versions; CLI preferred for fluency.
    
- **GitLab:** hosted repos, issues, CI; unlimited private repos; full SDLC coverage.
    

---

## Quick study checklist

-  Install Eclipse and explore basic workflows (build/run/debug).
    
-  Set up Git locally; clone/pull/push; branch & merge basics.
    
-  Create a GitLab project; try an Issue + CI pipeline.
    
-  Read the WARP codebase top-down; sketch the main components and data flow.
    
-  Re-implement a tiny WARP DSL fragment and reason about loss handling.
    

---




