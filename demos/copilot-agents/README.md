# Copilot Agents Demo

Use the following 3 files to setup your Copilot Agents demo. 
Paste the ISSUE.md file into a new issue in that repository. 

## What this demo shows
- Assign an issue to Copilot to start an agent task
- Monitor progress in AgentHQ
- Re-steer mid-session with a new requirement
- Review the resulting PR like a teammate’s work

## Demo files
- `ISSUE.md` contains the exact issue text to copy/paste into GitHub
- `STEER.md` contains the mid-session requirement change to paste while the agent is working

## Quick demo steps
1. Create a new GitHub Issue by copying the Title and Body from `ISSUE.md`
2. Assign the issue to Copilot to start the agent task
3. Open AgentHQ to monitor progress
4. Paste `STEER.md` into the agent session to re-steer the work
5. Review the PR diff for clarity, completeness, and constraints.
6. Verify the PR edited the README.md file by adding priority levels plus the steered examples. 

---

## Ticket Triage Policy (Current)

We currently triage support tickets using Severity only.

### Severity levels
- Low means minor annoyance with an easy workaround
- Medium means a meaningful user impact but workarounds exist
- High means blocks key workflows or causes data loss

### Current rules
- Triage happens daily
- High severity should be addressed first
- Use Severity to assign the default Priority on first review

### Priority levels
- **P0** — Active outage, data loss, or security issue needing immediate action
- **P1** — Major workflow is blocked and should be picked up the same day
- **P2** — Important issue with a workaround; schedule in normal planning
- **P3** — Minor issue, polish, or question that can wait

### Default Severity → Priority
| Severity | Default Priority |
| --- | --- |
| High | P1 |
| Medium | P2 |
| Low | P3 |

Escalate to **P0** for active outages, data loss, or security emergencies.

### How to triage in 60 seconds
1. Confirm the reported impact and choose **Low**, **Medium**, or **High** severity.
2. Apply the default Priority from the table above.
3. Escalate to **P0** for emergencies, or adjust one level if customer impact, timing, or workaround quality changes urgency.
4. Add the priority label and route the ticket to the right team or owner.
