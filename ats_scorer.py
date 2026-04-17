import re
from collections import Counter

def score_resume(resume_text: str, job_description: str) -> dict:
    def extract_keywords(text):
        words = re.findall(r"[a-zA-Z]{4,}", text.lower())
        return Counter(words)
    resume_kw = extract_keywords(resume_text)
    job_kw = extract_keywords(job_description)
    matches = set(resume_kw) & set(job_kw)
    score = round(len(matches) / max(len(job_kw), 1) * 100, 1)
    missing = set(job_kw) - set(resume_kw)
    return {"score": score, "matched": len(matches), "missing_keywords": list(missing)[:10]}

if __name__ == "__main__":
    import json
    result = score_resume("Python developer Docker Kubernetes AWS", "Python AWS Docker DevOps Terraform")
    print(json.dumps(result, indent=2))
