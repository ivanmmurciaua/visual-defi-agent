## Usage

First of all, use a venv with python 3.11
```bash
uv venv --python 3.11
```

Activate this venv
```bash
source .venv/bin/activate
```

Install deps
```bash
uv pip install browser-use
```

```bash
playwright install
```

Create `.env` file
```bash
cp .env.example .env
```

Fill `OPENAI_API_KEY` with yours.

Run agent
```bash
python agent.py
```

**IMPORTANT**: You MUST enable OpenAI billing with a little amount of $ in order to start with this little visual agent

## Results

This simple task, costs ~.03$ in OpenAI using gpt-4o

### Output example

```
INFO     [browser_use] BrowserUse logging setup complete with level info
INFO     [root] Anonymized telemetry enabled. See https://docs.browser-use.com/development/telemetry for more information.
INFO     [agent] 🚀 Starting task: Go to defillama.com and return DeFi TVL with a humanreadable timestamp
INFO     [agent] 📍 Step 1
INFO     [agent] 🤷 Eval: Unknown as the task has just started.
INFO     [agent] 🧠 Memory: Remember the task: Go to defillama.com and retrieve DeFi TVL with a human-readable timestamp. Current date and time: 2025-02-19 13:41.
INFO     [agent] 🎯 Next goal: Open a new tab and navigate to defillama.com.
INFO     [agent] 🛠️  Action 1/1: {"open_tab":{"url":"https://defillama.com"}}
INFO     [controller] 🔗  Opened new tab with https://defillama.com
INFO     [agent] 📍 Step 2
INFO     [agent] 👍 Eval: Success - Navigated to https://defillama.com and found the TVL information.
INFO     [agent] 🧠 Memory: Retrieved DeFi TVL of $109,079b from https://defillama.com at 2025-02-19 13:41. Task complete.
INFO     [agent] 🎯 Next goal: Finalize the task and provide the information.
INFO     [agent] 🛠️  Action 1/1: {"done":{"text":"The DeFi Total Value Locked (TVL) is $109,079b as of 2025-02-19 13:41."}}
INFO     [agent] 📄 Result: The DeFi Total Value Locked (TVL) is $109,079b as of 2025-02-19 13:41.
INFO     [agent] ✅ Task completed successfully
INFO     [agent] Created GIF at agent_history.gif
```

For more information go to the [project github](https://github.com/browser-use/browser-use)