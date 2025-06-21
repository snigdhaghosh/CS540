# Class-Level Code Generation Using LLMs

This repository contains the code and artifacts for our semester‐long project in CS 540, where we evaluate state-of-the-art large language models (LLMs) on **class-level** code generation tasks using the [ClassEval](https://github.com/FudanSELab/ClassEval) benchmark.

---

## 🚀 Project Overview

Modern LLM benchmarks focus on generating single functions or statements. In contrast, **class-level code generation** requires handling multiple interdependent methods, shared state, and complex logical dependencies—much closer to real-world software engineering. In this project, we:

1. **Integrated** a diverse set of LLMs (closed-source and open-source).
2. Designed a **modular Python pipeline** for:

   * **Inference** (holistic & sampling-based generation, including “test-prediction” prompts)
   * **Domain separation** (7 SE domains)
   * **Automated testing** (unit tests + Pass\@k computation)
3. **Analyzed** model performance across domains, sampling strategies, and architectures.
4. Full final report in pdf format.

---

## 🔑 Key Features

* **Inference Pipeline** (`inference_pipeline.py`):

  * Holistic generation of entire Python classes
  * Nucleus (top-p) and greedy sampling
  * “Test‐prediction” two-step prompting for select models
* **Domain Separation**:

  * Tasks split into 7 domains (e.g., Database Ops, Game Dev)
  * Modular JSON outputs per domain
* **Evaluation Harness** (`evaluate.py`):

  * Runs each generated class against its ClassEval unit tests
  * Produces `detailed_results.json` (per‐test verdicts) and `pass_k.json` (Pass\@1/3/5)
* **Results & Visualization**:

  * Ready-to-use scripts/notebooks for plotting per‐domain and model comparisons

---

## 📦 Repository Structure

```text
.
├── data/
│   ├── ClassEvalData.json        # Original ClassEval tasks & tests
│   └── <domain>_tasks.json       # Sliced subsets per domain
├── inference/
│   ├── inference_pipeline.py     # Main code‐generation driver
│   └── InferenceUtil.py          # Helper functions (prompt construction, sampling)
├── evaluation/
│   ├── evaluate.py               # Runs unittest harness & aggregates pass@k
│   ├── detailed_results.json     # Raw test verdicts (generated at runtime)
│   └── pass_k.json               # Aggregated Pass@k metrics
├── requirements.txt              # Python dependencies
├── notebooks/                    # (Optional) analysis & plotting notebooks
├── README.md                     # ← You are here
└── LICENSE
```

---

## ⚙️ Installation

1. **Clone** this repository:

   ```bash
   git clone https://github.com/TanujDave0/CS540.git
   cd CS540
   ```

2. **Create & activate** a Python 3.9+ virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install** dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure** API keys (for OpenAI, Google, Groq, etc.) as environment variables:

   ```bash
   export OPENAI_API_KEY="…"
   export GOOGLE_API_KEY="…"
   export GROQ_API_KEY="…"
   ```

---

## 🚀 Usage

### 1. Generate Code with LLMs

```bash
python inference/inference_pipeline.py \
  --model MODEL_NAME \
  --data_path data/ClassEvalData.json \
  --strategy holistic \
  --sample 5 \
  --greedy 1 \
  --output_path outputs/MODEL_holistic_outputs.json
```

* `MODEL_NAME`: e.g. `gpt-4`, `chatgpt-o4-mini`, `gemini-2.5-flash`, `deepseek-r1-distilled-llama-70b`, `wizardcoder`, etc.
* `--strategy`: one of `holistic`, `incremental`, `compositional`
* `--sample`: number of nucleus‐samples (top-p)
* `--greedy`: `1` to also generate a greedy output
* `--output_path`: JSON file to store `predict` arrays

### 2. Split Outputs by Domain

```bash
python inference/domain_split.py \
  --input outputs/MODEL_holistic_outputs.json \
  --mapping data/taskid_to_domain.json \
  --out_dir outputs/domains/
```

### 3. Evaluate Generated Classes

```bash
python evaluation/evaluate.py \
  --model MODEL_NAME \
  --domain all              # or one of the seven domains
```

* Produces:

  * `detailed_results.json` (per‐test outcomes)
  * `pass_k.json` (Pass\@1/3/5 aggregates)

### 4. Plot & Analyze

Use the included Jupyter notebooks in `notebooks/` to generate:

* Model vs. domain heatmaps
* Method‐ vs. class‐level performance bar charts
* Dependency recall and error breakdown plots

---

## 📊 Sample Results

* **All Domains Combined**

  * ChatGPT-o4-mini: Method\@5 ≈ 79.3%, Class\@5 ≈ 50.0%
  * Gemini-2.5-flash: Method\@5 ≈ 80.5%, Class\@5 ≈ 53.0%
* **Database Operations**

  * Top closed model: Gemini & ChatGPT-o4-mini (Class\@5 85.7%)
  * Top open model: LLaMA-4-Maverick (Class\@5 85.7%)

*See `pass_k.json` or notebooks for full breakdown.*

---

> **Acknowledgments:**
> We build on the [ClassEval benchmark](https://github.com/FudanSELab/ClassEval).
