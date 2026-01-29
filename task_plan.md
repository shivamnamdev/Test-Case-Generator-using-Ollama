# Task Plan
##- **North Star**: Local LLM testcase generator using Ollama (Llama 3.2) with a stored custom template (UI Chat based).
- **Tech Stack**: Python (Backend), HTML/CSS/JS (Frontend), Ollama (Model: `llama3.2`).
- **Template strategy**: Internal template variable/file.
- **Delivery**: Web UI Chat Interface.s

### Phases
- [ ] **Phase 1: Initialization & Planning**
    - [x] Initialize Project Memory (`task_plan.md`, `findings.md`, `progress.md`, `gemini.md`)
    - [x] Integrate with Ollama (`llama3.2`)
- [x] Define internal Template structure
- [x] Defined Data Schema in `gemini.md`
- [x] Approve Blueprint

- [x] Integrate with Ollama (`llama3.2`)
- [x] Define internal Template structure
- [x] Defined Data Schema in `gemini.md`
- [x] Approve Blueprint

- [x] **Phase 2: Core Implementation (Active)**
    - [x] **Architecture (Done)**
        - [x] Define SOPs in `architecture/`
    - [x] **Backend (SOP_backend.md)**:
        - [x] Install `fastapi`, `uvicorn`
        - [x] Create `backend/main.py` (API Routes)
        - [x] Create `backend/generator.py` (Ollama Logic)
    - [x] **Frontend (SOP_frontend.md)**:
        - [x] Create `frontend/index.html`
        - [x] Create `frontend/style.css` (Glassmorphism)
        - [x] Create `frontend/script.js`





- [ ] **Phase 3: Testing & Refinement**
    - [ ] Test with sample prompts
    - [ ] Refine generation logic

### Active Goals
- Gather requirements and prompt from user.
- Define architecture.
