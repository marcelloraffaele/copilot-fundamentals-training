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

## Ticket Triage Policy

### Severity levels
| Severity | Description |
|----------|-------------|
| Low | Minor annoyance with an easy workaround |
| Medium | Meaningful user impact but workarounds exist |
| High | Blocks key workflows or causes data loss |

### Priority levels
| Priority | Meaning | Response target |
|----------|---------|-----------------|
| P0 | Critical — system down, data loss, security breach | Immediate (< 1 hr) |
| P1 | Major — core feature broken, no workaround | Same day (< 4 hr) |
| P2 | Moderate — impaired feature, workaround exists | Next business day |
| P3 | Minor — cosmetic or low-impact issue | Best effort / backlog |

### Severity → Priority mapping
| Severity | Default Priority |
|----------|-----------------|
| High | P0 or P1 |
| Medium | P2 |
| Low | P3 |

### How to triage in 60 seconds ✅
1. **Read** the ticket title and description.
2. **Assign severity** (High / Medium / Low) based on user impact.
3. **Set priority** using the mapping above; adjust if context warrants.
4. **Label** the ticket with the priority (P0–P3).
5. **Assign** an owner or team queue and set the response-target due date.
6. **Done** — move on to the next ticket.
