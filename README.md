# Adaptive Multi-LLM Harness

> A model-agnostic AI orchestration system that routes different subtasks to specialized LLMs and combines their outputs into a reliable final response.

## Overview

Large Language Models are good at different things. One model may perform better at reasoning, another at coding, and another at structured data analysis.

This project explores a **multi-LLM harness** that treats LLMs as specialized workers rather than forcing a single model to handle every task.

The harness acts as the orchestration layer between the user and multiple AI models. It can:

- Understand and decompose a user request into subtasks
- Select the most suitable LLM for each subtask
- Provide relevant context through RAG
- Give models access to tools through MCP
- Maintain conversation and task state
- Validate intermediate results
- Combine outputs from multiple models
- Produce a single final response
- Evaluate and benchmark different routing strategies

### Core idea

```text
                         USER
                           |
                           v
                  +------------------+
                  |   LLM HARNESS    |
                  |                  |
                  | Task Planner     |
                  | Model Router     |
                  | Context Manager  |
                  | Memory           |
                  | Validator        |
                  | Synthesizer      |
                  +--------+---------+
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
          +------+      +--------+     +------+
          | Qwen |      | Gemini |     | GPT  |
          | Data |      |Reasoning|    | Code |
          +--+---+      +----+---+     +--+---+
             |               |             |
             +---------------+-------------+
                             |
                             v
                       VALIDATION
                             |
                             v
                       SYNTHESIS
                             |
                             v
                         FINAL
                         ANSWER
```

---

## Why a Harness?

An LLM by itself mainly provides reasoning and generation. Real-world AI applications also need data access, tools, memory, security, validation, and workflow management.

This project separates those responsibilities.

| Component | Responsibility |
|---|---|
| LLM | Reasoning and generation |
| Harness | Orchestration and control |
| Model Router | Selects the best model for a task |
| RAG | Retrieves relevant knowledge |
| MCP | Provides standardized access to tools/data |
| Memory | Maintains useful conversation/task state |
| Validator | Checks intermediate and final results |
| Synthesizer | Combines specialized model outputs |
| Evaluator | Measures quality, latency, and other metrics |

**MCP and RAG are not alternatives to the harness. They can be components managed by the harness.**

---

## Key Features

### 1. Task Decomposition

A complex request can be divided into smaller tasks.

Example:

```text
User:
"Analyze this dataset, identify anomalies, explain the trend,
and generate a visualization."

                 |
                 v
             Task Planner
                 |
       +---------+---------+----------+
       |                   |          |
       v                   v          v
 Data Analysis        Reasoning   Visualization
```

### 2. Intelligent Model Routing

Each task can be assigned to a model based on its strengths.

Example:

```text
Data analysis       -> Qwen
Scientific reasoning -> Gemini
Code generation     -> GPT
General response    -> Gemini
```

The routing policy can later be made dynamic using model performance, task complexity, latency, cost, or historical success rate.

### 3. Multi-Model Collaboration

The outputs of specialized models are converted into structured intermediate results and passed to a validation/synthesis stage.

```text
Qwen output
     +
Gemini output
     +
GPT output
     |
     v
Validator
     |
     v
Synthesizer
     |
     v
Final response
```

### 4. RAG Integration

Retrieval-Augmented Generation can provide grounded information from:

- Documents
- Databases
- Knowledge bases
- Vector stores
- Project-specific data

Potential vector stores include:

- FAISS
- Chroma

### 5. MCP Tool Integration

MCP can expose tools to the AI system, such as:

- Database queries
- Calculations
- File operations
- Data analysis
- Visualization
- External APIs

The harness controls when and how those tools are used.

### 6. Memory

The system can maintain:

- Conversation history
- Task state
- Relevant previous results
- Long-term application context

### 7. Validation

Before producing the final response, the harness can verify:

- Whether required subtasks completed
- Whether tool calls succeeded
- Whether outputs are structurally valid
- Whether retrieved information supports the answer
- Whether a task needs to be retried

### 8. Evaluation and Benchmarking

The project is designed to compare:

```text
Single LLM
    vs
Multiple LLMs
    vs
Multi-LLM Harness
```

Possible metrics include:

- Accuracy
- Groundedness
- Task success rate
- Tool-selection accuracy
- Latency
- Token usage
- Cost
- Failure/retry rate

---

# Architecture

```text
                              USER
                               |
                               v
                         +-----------+
                         |    API    |
                         +-----+-----+
                               |
                               v
                     +-------------------+
                     |   ORCHESTRATOR    |
                     +---------+---------+
                               |
                               v
                     +-------------------+
                     |   TASK PLANNER    |
                     +---------+---------+
                               |
                               v
                     +-------------------+
                     |   MODEL ROUTER    |
                     +---------+---------+
                               |
              +----------------+----------------+
              |                |                |
              v                v                v
          +-------+        +--------+        +------+
          | Qwen  |        | Gemini |        | GPT  |
          +---+---+        +----+---+        +--+---+
              |                  |               |
              +------------------+---------------+
                                 |
                                 v
                         +---------------+
                         |   VALIDATOR   |
                         +-------+-------+
                                 |
                                 v
                         +---------------+
                         |  SYNTHESIZER  |
                         +-------+-------+
                                 |
                                 v
                              RESPONSE


       Supporting Services
       -------------------

       RAG  <----> FAISS / Chroma / Documents
        |
        +----> PostgreSQL / Other data sources

       MCP  <----> Tools / APIs / Database

       Memory <--> Conversation / Long-term state

       Evaluation <--> Metrics / Benchmarks
```

---

# Project Structure

```text
ai-harness/
|
├── README.md
├── .env
├── .gitignore
├── requirements.txt
├── config.yaml
|
├── app/
│   ├── main.py
│   |
│   ├── api/
│   │   ├── routes.py
│   │   └── schemas.py
│   |
│   ├── harness/
│   │   ├── orchestrator.py
│   │   ├── task_planner.py
│   │   ├── model_router.py
│   │   ├── workflow.py
│   │   ├── context_manager.py
│   │   ├── memory_manager.py
│   │   ├── validator.py
│   │   └── synthesizer.py
│   |
│   ├── models/
│   │   ├── base_model.py
│   │   ├── gemini.py
│   │   ├── qwen.py
│   │   ├── gpt.py
│   │   └── model_registry.py
│   |
│   ├── rag/
│   │   ├── retriever.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   └── document_loader.py
│   |
│   ├── mcp/
│   │   ├── client.py
│   │   ├── tool_registry.py
│   │   └── tools/
│   │       ├── database.py
│   │       ├── calculator.py
│   │       └── visualization.py
│   |
│   ├── memory/
│   │   ├── conversation.py
│   │   └── long_term.py
│   |
│   ├── evaluation/
│   │   ├── evaluator.py
│   │   ├── metrics.py
│   │   └── test_cases.py
│   |
│   └── utils/
│       ├── logger.py
│       ├── errors.py
│       └── helpers.py
|
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
|
├── tests/
│   ├── test_router.py
│   ├── test_rag.py
│   ├── test_tools.py
│   ├── test_harness.py
│   └── test_models.py
|
├── scripts/
│   ├── ingest.py
│   ├── evaluate.py
│   └── benchmark.py
|
└── logs/
```

---

# Component Responsibilities

## `app/harness/`

The core orchestration layer.

### `orchestrator.py`

Coordinates the complete lifecycle of a request:

```text
Request
 -> Planning
 -> Retrieval
 -> Model selection
 -> Tool execution
 -> Validation
 -> Synthesis
 -> Response
```

### `task_planner.py`

Converts a complex user request into executable subtasks.

Example:

```json
{
  "tasks": [
    {
      "id": "task_1",
      "type": "data_analysis"
    },
    {
      "id": "task_2",
      "type": "reasoning"
    },
    {
      "id": "task_3",
      "type": "visualization"
    }
  ]
}
```

### `model_router.py`

Maps tasks to appropriate models.

```text
Task Type            Preferred Model
-------------------------------------
Data Analysis        Qwen
Reasoning            Gemini
Coding               GPT
General              Gemini
```

### `validator.py`

Checks whether outputs are valid and whether failed tasks need to be retried.

### `synthesizer.py`

Combines validated outputs into a coherent final answer.

---

# Model Abstraction

Models should not be tightly coupled to the harness.

The project uses a common interface:

```python
class BaseModel:

    def generate(self, prompt, context=None):
        raise NotImplementedError
```

Then individual adapters implement that interface:

```text
             BaseModel
                 |
       +---------+---------+
       |         |         |
     Gemini     Qwen       GPT
    Adapter    Adapter    Adapter
```

This allows the harness to switch models without changing the rest of the application.

---

# Example Workflow

Suppose the user asks:

> "Analyze the dataset, identify anomalies, explain why they may have occurred, and generate a plot."

The harness could execute:

```text
1. Receive request
        |
2. Task Planner
        |
        +--> Data analysis
        +--> Anomaly detection
        +--> Explanation
        +--> Visualization
        |
3. Model Router
        |
        +--> Qwen    -> Data analysis
        +--> Qwen    -> Anomaly detection
        +--> Gemini  -> Explanation
        +--> GPT     -> Visualization/code
        |
4. Collect results
        |
5. Validate outputs
        |
6. Synthesizer
        |
7. Generate final response
```

The routing does not have to be fixed. The system can eventually choose models dynamically.

---

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd ai-harness
```

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure environment variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
HF_TOKEN=your_token_here
```

Never commit `.env` or API keys to Git.

---

# Configuration

Model and system settings can be maintained in `config.yaml`.

Example:

```yaml
models:
  default: gemini

  routing:
    data_analysis: qwen
    reasoning: gemini
    coding: gpt
    general: gemini

rag:
  vector_store: chroma

harness:
  max_retries: 2
  enable_validation: true
  enable_memory: true
```

---

# Development Roadmap

## Phase 1 — Basic Harness

- [ ] Create common model interface
- [ ] Add Gemini adapter
- [ ] Add Qwen adapter
- [ ] Add GPT adapter
- [ ] Implement model registry
- [ ] Implement model router
- [ ] Implement basic orchestrator
- [ ] Implement final synthesizer

## Phase 2 — Intelligent Routing

- [ ] Task classification
- [ ] Dynamic model selection
- [ ] Model fallback
- [ ] Retry mechanism
- [ ] Cost-aware routing
- [ ] Latency-aware routing

## Phase 3 — RAG

- [ ] Document ingestion
- [ ] Embedding generation
- [ ] Vector database
- [ ] Retrieval
- [ ] Context injection
- [ ] Retrieval evaluation

## Phase 4 — MCP and Tools

- [ ] MCP client
- [ ] Tool registry
- [ ] Database tool
- [ ] Calculator tool
- [ ] Visualization tool
- [ ] Tool permission system

## Phase 5 — Memory

- [ ] Conversation memory
- [ ] Task state
- [ ] Long-term memory
- [ ] Context compression

## Phase 6 — Evaluation

- [ ] Benchmark dataset
- [ ] Single-model baseline
- [ ] Multi-model baseline
- [ ] Harness evaluation
- [ ] Accuracy metrics
- [ ] Latency comparison
- [ ] Cost comparison
- [ ] Failure analysis

---

# Research / Project Objective

The central question of this project is:

> **Can intelligently routing specialized tasks to different LLMs produce better overall results than relying on a single general-purpose LLM?**

The system can experimentally compare:

```text
Approach A
Single LLM
      |
      v
   Answer


Approach B
Multiple LLMs without orchestration
      |
      v
   Combined Answer


Approach C
Adaptive Multi-LLM Harness
      |
      +--> Task Planning
      +--> Specialized Models
      +--> RAG
      +--> MCP
      +--> Validation
      +--> Synthesis
      |
      v
   Final Answer
```

This provides a measurable basis for evaluating whether model specialization and orchestration improve quality, reliability, latency, and cost.

---

# Design Principles

### Model Agnostic

The application should not depend on one specific LLM provider.

### Modular

Models, RAG systems, tools, memory, and evaluation should be replaceable independently.

### Observable

The system should record task routing, model execution, failures, latency, and other useful metrics.

### Reliable

The system should validate outputs and avoid presenting unsupported information as fact.

### Extensible

New models and tools should be addable without rewriting the core harness.

---

# Future Extensions

Potential future features include:

- Dynamic model routing using a meta-LLM
- Self-correction and retry loops
- Parallel model execution
- Model voting / ensemble reasoning
- Cost-aware routing
- Latency-aware routing
- Automatic model benchmarking
- Human approval for sensitive tool calls
- Agent-to-agent collaboration
- Distributed execution
- Web-based monitoring dashboard

---

# License

This project is currently intended for educational and research purposes.

Add an appropriate open-source license before public distribution.
