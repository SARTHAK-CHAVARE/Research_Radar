# AI Usage DISCLOSURE FORM

## 1. Team Details

**Team Name:** Team ResearchRadar  
**Project / Product Name:** ResearchRadar  
**Organization / Institution (if any):** [Your College Name]  
**Submission Date:** May 2026  

---

## 2. AI Usage Declaration

Did your team use any Artificial Intelligence (AI) in developing this project?  

✅ Yes  

---

## 3. Purpose of AI Usage (Brief Details)

| Purpose | Details |
|---|---|
| Idea generation / brainstorming | Used AI assistants for refining project ideas and architecture discussions |
| Code generation or assistance | Used AI tools for debugging help, boilerplate suggestions, and documentation assistance |
| UI / UX design | AI-assisted formatting ideas for DOCX digest layout |
| Content creation | AI-generated paper summaries and README drafting |
| Data analysis | AI used to analyze and summarize research papers |
| Testing / debugging | AI-assisted debugging and optimization suggestions |
| Other | Prompt engineering and novelty-score evaluation |

---

## 4. Feature Origin Classification

### Feature 1

**Feature Name:** AI Paper Summarization Engine  

**Self-Generated / AI-Generated / Both:** Both  

**Description:**  
- **AI Tools/Platforms Used:** Groq API (`llama-3.3-70b-versatile`), ChatGPT  
- **Prompt Used:**  
  “Summarize this paper using:
  - What
  - How
  - Why it matters
  - Novelty score”
- **Output Summary:**  
  AI generated concise summaries of ArXiv research papers and assigned novelty scores.
- **Modification:**  
  Team designed prompts, integrated APIs, handled formatting, rate limiting, and integrated summaries into the digest pipeline.

---

### Feature 2

**Feature Name:** Top Pick Recommendation System  

**Self-Generated / AI-Generated / Both:** Both  

**Description:**  
- **AI Tools/Platforms Used:** Groq API  
- **Prompt Used:**  
  “From this list of papers, identify the most impactful and novel paper.”
- **Output Summary:**  
  AI selected the highest-impact research paper for the weekly digest.
- **Modification:**  
  Team implemented selection logic, fallback handling, and digest integration.

---

### Feature 3

**Feature Name:** README & Documentation Assistance  

**Self-Generated / AI-Generated / Both:** Both  

**Description:**  
- **AI Tools/Platforms Used:** ChatGPT  
- **Prompt Used:**  
  “Create professional README sections including setup, usage, and architecture.”
- **Output Summary:**  
  AI assisted in generating structured technical documentation.
- **Modification:**  
  Team reviewed, edited, validated, and customized all documentation.

---

### Feature 4

**Feature Name:** DOCX Digest Generation  

**Self-Generated / AI-Generated / Both:** Self-Generated  

**Description:**  
- Built manually using Python and `python-docx`
- Designed digest formatting, section generation, tables, and styling manually
- No AI-generated implementation used directly

---

### Feature 5

**Feature Name:** Multi-Channel Delivery System  

**Self-Generated / AI-Generated / Both:** Self-Generated  

**Description:**  
- Telegram Bot API integration
- Gmail SMTP integration
- Autonomous delivery pipeline
- Implemented fully by the team

---

## 5. Ethical & Compliance Confirmation

✅ AI usage complies with guidelines and policies.  

✅ No proprietary or copyrighted data misused.  

✅ All AI-generated outputs were reviewed and modified by the team before integration.  

---

## 6. Declaration & Sign-Off

**Name of Team Representative:** Sarthak Chavare  

**Role:** Developer / AI Integration Lead  

**Signature:** ____________________  

**Date:** ____________________