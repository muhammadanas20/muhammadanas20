from make_phase import C, E, EX, I, Q, asg, drill, mp, phase, th

PHASE = phase(
    num="14",
    title="Capstone",
    tagline="Pick one product. Finish it. Deploy it. Measure it. Talk about it.",
    hours="21-30 days",
    difficulty="Capstone",
    exit_ticket="Public repo, live URL, eval numbers, 2-page design doc, 5-minute demo, resume bullet.",
    objectives=[
        "Choose enterprise RAG, enterprise agent, or AI SaaS.",
        "Write a design doc before infinite coding.",
        "Ship production basics: Docker, auth, evals, traces, threat model.",
        "Freeze scope and polish.",
        "Present like a junior who has shipped.",
    ],
    prerequisites=["Phases 0–13 at least through 8, 11, and 13. Agents/MCP if you pick those tracks."],
    topics=["Enterprise RAG", "Enterprise agent", "AI SaaS", "Production deployment", "Design docs", "Demos"],
    nav="[Home](../../README.md) · Prev: [Phase 13](../13-security/) · [Capstone folders](../../CAPSTONE/)",
    theory=th(
        intro="""A capstone is not 'all remaining tutorials.'

It is **one product** with a user, a constraint, and a number.

Three tracks live in `CAPSTONE/`:

1. **Enterprise RAG** — chat over a corpus with tenancy, citations, evals
2. **Enterprise agent** — tools, MCP, HITL, traces
3. **AI SaaS** — multi-tenant, keys, quotas, a billing-shaped architecture (even if money is fake)

Pick the one you can demo in 5 minutes without sweating.""",
        one_liner="One product, done, deployed, measured, explained.",
        why="""Interviews are project deep dives. A half-finished zoo of repos loses to one sharp story:

> I built X for Y. The constraint was Z. The number is N. Here is what I'd do next.

That story is this phase.""",
        if_missing="you would have 14 mini-projects and nothing to point at.",
        analogy="""A thesis, not a locker of lab reports.

- **Design doc** = proposal
- **Freeze** = stop adding chapters
- **Evals** = results section
- **Deploy** = published paper
- **Demo** = defense
- **Resume bullet** = citation others will read""",
        visual="""```mermaid
flowchart LR
  Choose --> Design
  Design --> Build
  Build --> Eval
  Eval --> Harden
  Harden --> Deploy
  Deploy --> Freeze
  Freeze --> Demo
  Demo --> Resume
```""",
        architecture="""```mermaid
flowchart TB
  subgraph must [Must have]
    Auth
    Docker
    Eval
    Trace
    Threat
    URL
  end
  subgraph track [One track]
    RAG[RAG]
    AG[Agent]
    SaaS[SaaS]
  end
```""",
        beginner="""**Week 1:** design doc, gold set, skeleton compose.

**Week 2–3:** happy path.

**Week 4:** evals, security, deploy.

**Days left:** README, demo script, freeze.

**Definition of done:** [CHECKLIST.md](../../CHECKLIST.md) capstone section.

Do not start a second track.""",
        intermediate="""**Design doc sections:** problem, users, non-goals, architecture, data, eval, cost, security, rollout, risks.

**Non-goals** are how you finish.

**Demo script:** 5 minutes, timed. Upload → question → citation → a failure ('I don't know') → trace screenshot.

**Load a little:** 20 concurrent requests once. Note p95.""",
        advanced="""**What you'd do with a team of 4** — a slide interviewers love.

**Unit economics:** cost per 1k questions.

**Feature flags** for prompt versions.

**Multi-region** as a paragraph, not a build.""",
        production="""Feature freeze 5 days before you call it done. Bugs and docs only. Shipping beats a perfect graph in a private branch.""",
        when="When you can already demo RAG or an agent locally. Not as a substitute for Phase 8.",
        when_not="Don't capstone a model training from scratch. Don't rebuild Kubernetes.",
        code_preview="# There is no magic snippet. There is a calendar and a freeze date.",
        code_notes="See CAPSTONE/*/README.md for track-specific stacks.",
        ex_b="Write the design doc. Peer review (or rubber duck).",
        ex_m="Happy path on compose.",
        ex_h="Eval table + live URL + threat model.",
        project="The capstone itself.",
        interview_preview="Tell me about the project. What would you delete? What's the number? What broke?",
        flash_sample="**Q:** How many capstones?\n**A:** One. Finished.",
        mistakes_preview="Three tracks at 40%. No eval. No URL. README of setup only. Demo that needs your laptop's 37 env vars.",
        debug_preview="Scope creep the week of the demo. Provider outage with no recording.",
        best="Freeze. Number. URL. Honest limitations. Backup demo video.",
        industry="This is how real internships ship: thin slice, measured, behind a URL.",
        perf="p95 on the demo path. Don't live-index a 10GB corpus on stage.",
        security="Threat model in the repo. No customer data. Fake corpus if needed.",
        refs="- SYSTEM_DESIGN_GUIDE.md\n- CHECKLIST.md\n- RESUME_GUIDE.md",
        further="Watch 3 conference talks of people presenting applied LLM work. Steal structure, not slides.",
    ),
    examples=[
        EX(
            title="Scope card",
            why="Tape this to the monitor.",
            code='''"""code/scope.py — not runtime code: a checklist you print"""
MUST = [
    "one user story",
    "compose up",
    "auth",
    "eval number",
    "deployed URL",
    "threat model",
    "5-min demo script",
]
WONT = [
    "mobile app",
    "training a model",
    "kubernetes",
    "five agent personas",
]
print("MUST", len(MUST), "WONT", len(WONT))
''',
            line_by_line="If a new idea is not on MUST, it is WONT until after demo.",
            output="MUST 7 WONT 4",
            dry_run="Read lists. Feel the freeze.",
            memory="n/a",
            time="n/a",
            space="n/a",
            alternatives="A Google doc. A whiteboard photo.",
            optimization="Shorter MUST wins.",
        ),
        EX(
            title="Demo timer outline",
            why="Rehearse with a clock.",
            code='''"""code/demo_script.txt shown here as a string"""
SCRIPT = """
0:00 Problem in one sentence
0:30 Architecture diagram
1:00 Happy path live
2:30 Citation / tool trace
3:30 Failure path (I don't know or denied tool)
4:00 Eval number + cost
4:30 What I'd do next
5:00 Stop
"""
print(SCRIPT)
''',
            line_by_line="Failure path builds more trust than a second happy path.",
            output="The script.",
            dry_run="Say it out loud with a timer.",
            memory="n/a",
            time="300s",
            space="n/a",
            alternatives="A Loom video backup.",
            optimization="Cut until it fits 5:00.",
        ),
    ],
    practice=[
        drill("Design doc", "Two pages max.", "Linked in README."),
        drill("Gold set freeze", "25+ cases. Stop editing labels.", "Hash the file."),
        drill("Record backup demo", "Even if live works.", "MP4 or unlisted YouTube."),
    ],
    exercises={
        "beginner": [
            E("Non-goals", "15 things you will not build.", "In the design doc."),
            E("Resume bullet", "Use RESUME_GUIDE formula.", "One bullet."),
        ],
        "medium": [
            E("Load poke", "20 concurrent simple questions.", "p95 noted."),
            E("Chaos", "Kill the model API (bad key). Show fallback or a clean error.", "Screenshot."),
        ],
        "hard": [
            E("The whole capstone", "See assignment.", "Checklist green."),
        ],
    },
    assignments=[
        asg(
            "flagship",
            "3–4 weeks",
            "Complete one CAPSTONE track. Public repo. Live URL. Design doc. Evals. Threat model. Demo script.",
            ["repo", "URL", "docs/design.md", "eval table", "THREAT_MODEL.md", "demo script"],
            ["stranger can run or use URL", "a number", "limitations section", "resume bullet"],
        )
    ],
    quiz=[
        Q("How many tracks should you finish?", "All three equally", "One", "None, just theory", "Twelve", "B", "Finish one."),
        Q("A capstone without evals is", "Fine", "A demo, not production-shaped", "Better", "A vector DB", "B", "Measure."),
        Q("Non-goals exist to", "Look negative", "Protect the freeze", "Confuse PMs", "Fill pages", "B", "Finish."),
        Q("Demo should include", "Only the happy path", "A failure path", "Training CUDA", "Your .env", "B", "Trust."),
        Q("Feature freeze means", "No more features, polish/bugs/docs", "Delete the repo", "Stop evals", "Raise temperature", "A", "Ship."),
        Q("Live URL matters because", "Fashion", "Hiring managers click", "Docker forbids localhost", "JWT", "B", "Proof."),
        Q("Design doc comes", "After 4 weeks of coding", "Before the bulk of coding", "Never", "In the Dockerfile", "B", "First."),
        Q("Cost per 1k queries", "Optional fluff", "A senior-looking number you should have", "Impossible", "A secret", "B", "Unit economics."),
        Q("Backup demo video", "For losers", "For when Wi-Fi or the vendor dies", "Forbidden", "Replaces the repo", "B", "Insurance."),
        Q("Resume bullet should include", "Passion", "System + constraint + number", "All frameworks you saw", "GPA only", "B", "Proof."),
    ],
    flashcards=[
        C("Three tracks?", "Enterprise RAG, enterprise agent, AI SaaS."),
        C("Exit ticket pieces?", "Repo, URL, eval, design doc, demo, resume bullet."),
        C("Why freeze?", "To actually ship."),
        C("Failure path?", "I don't know / denied tool / fallback."),
        C("Non-goals?", "Listed things you will not do."),
        C("Who is the user?", "You must name them in the doc."),
        C("What is the number?", "Eval, latency, or cost — pick at least one."),
        C("Threat model?", "Phase 13 applied to this product."),
        C("Stranger test?", "Can someone use it without you on voice chat?"),
        C("What next?", "A honest paragraph beats fake roadmap slides."),
    ],
    interview=[
        I("Tell me about your capstone.", "Problem, user, architecture in 3 boxes, constraint, number, one failure, one next step. 90 seconds.", "I used LangChain and OpenAI and Docker and ...", "They will interrupt. Let them."),
        I("What would you delete?", "A component that didn't move the eval. Shows taste.", "Nothing it is perfect.", "Tradeoffs."),
        I("A bug you hit?", "A real one: SSE buffer, tenant leak test, chunking tables. How you saw it.", "It just worked.", "Debug story."),
        I("How much does it cost?", "Order-of-magnitude per 1k queries at chosen models. What you'd do if traffic ×10.", "I don't know I used free credits.", "Unit economics."),
        I("Why not multi-agent?", "If you chose RAG: because a chain met the eval. If you chose agent: because tools were real.", "Everyone uses agents.", "Taste."),
    ],
    whiteboard=[
        "Draw YOUR capstone in 8 boxes from SYSTEM_DESIGN_GUIDE.",
        "Show the eval loop.",
        "Show the threat model data flow.",
    ],
    interview_listen="a finished story with a number and a limitation",
    cheatsheet={
        "remember": "One track. Design first. Freeze. Number. URL. Failure path. Resume bullet.",
        "bash": "See CAPSTONE/*/README.md",
        "python": "# ship, don't start another framework",
        "decisions": "Strongest RAG story → RAG track. Tools/MCP story → agent. Multi-tenant billing shape → SaaS.",
        "numbers": "5-minute demo. 2-page doc. 25+ eval cases. p95 noted once.",
        "do_not": "Three half products. Live-code a new feature on stage. Fake numbers.",
    },
    miniproject=mp(
        name="flagship",
        time="3–4 weeks",
        difficulty="Capstone",
        why="This is the course.",
        story="A hiring manager clones or clicks and gets it.",
        must=["design doc", "compose", "auth", "eval", "deploy", "threat model", "demo script"],
        should=["traces", "rate limits"],
        wont=["everything else"],
        architecture="See ../../CAPSTONE/",
        layout="your-public-repo/",
        rubric=["CHECKLIST capstone green"],
        stretch="A blog post with the ablation table.",
    ),
    resources={
        "official": ["CAPSTONE/enterprise-rag", "CAPSTONE/enterprise-agent", "CAPSTONE/ai-saas"],
        "extra": ["RESUME_GUIDE", "SYSTEM_DESIGN_GUIDE", "INTERVIEW_PREP"],
        "papers": ["Whatever your track needs — don't add a paper for decoration."],
    },
    faq=[
        {"q": "Can I combine RAG + agent?", "a": "A RAG system with one tool is still the RAG track. Don't build three products."},
        {"q": "No money for hosting?", "a": "Free tiers, then a recorded demo + `compose up` as the bar. Say so honestly."},
        {"q": "Group capstone?", "a": "Name who did what. Interviews will split you."},
    ],
    debugging=[
        {
            "title": "Infinite polish",
            "symptom": "Never deployed.",
            "wrong": "The demo needs one more framework.",
            "see": "MUST list.",
            "fix": "Freeze. Ship.",
            "prevent": "Calendar the freeze on day 1.",
        },
        {
            "title": "Demo fail on Wi-Fi",
            "symptom": "Vendor timeout.",
            "wrong": "No backup video, no local fallback.",
            "see": "Chaos exercise.",
            "fix": "Video + local compose.",
            "prevent": "Rehearse offline path.",
        },
    ],
    mistakes=[
        {"title": "Capstone as a rewrite of every phase", "body": "You drown.", "instead": "Reuse your Phase 8/9 repo. Harden it."},
        {"title": "README is pip install only", "body": "No problem statement.", "instead": "Problem, picture, number, limits."},
        {"title": "Fake eval 99%", "body": "They will ask how.", "instead": "A real 78% with a confusion analysis."},
    ],
    prod_tips={
        "cost": "Know it. Put it in the doc.",
        "latency": "Demo on a warm cache honestly, but mention cold.",
        "reliability": "Fallback for the demo gods.",
        "observability": "One trace you can open on stage.",
        "scaling": "A paragraph, not a cluster.",
        "checklist": ["URL", "eval", "threat model", "demo script", "resume bullet", "freeze"],
    },
    challenge={
        "title": "Stranger test",
        "body": "A classmate follows only the README for 20 minutes.",
        "constraints": ["You cannot speak"],
        "success": "They hit the happy path or you fix the README.",
    },
    solutions=[
        {"id": "B1 non-goals", "hint": "If it didn't make the 5-min demo, it's a non-goal.", "approach": "Be savage."},
        {"id": "H1 whole", "hint": "Reuse code. Don't restart from empty.", "approach": "Harden PDF chat or SQL agent into the capstone track."},
    ],
    code_files={
        "scope.py": '''"""Print the only lists that matter."""

MUST = [
    "one user story",
    "compose up",
    "auth",
    "eval number",
    "deployed URL",
    "threat model",
    "5-min demo script",
]
WONT = [
    "mobile app",
    "training a model",
    "kubernetes",
    "five agent personas",
]

if __name__ == "__main__":
    print("MUST", len(MUST), "WONT", len(WONT))
''',
    },
)
