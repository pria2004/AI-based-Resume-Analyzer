import subprocess
import json
import re

PROMPT_PATH = "prompts/llama_prompt.txt"

def analyze_resume_with_jd(resume_text: str, jd_text: str) -> dict:
    # Load the prompt template
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        base_prompt = f.read()

    # Fill placeholders
    final_prompt = base_prompt.replace("{{JD}}", jd_text).replace("{{RESUME}}", resume_text)

    # Call LLaMA via subprocess
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=final_prompt.encode("utf-8"),
        capture_output=True
    )

    # Check for errors
    if result.returncode != 0:
        return {"error": result.stderr.decode("utf-8")}

    output = result.stdout.decode("utf-8").strip()

    return parse_llama_response(output)


def parse_llama_response(output: str) -> dict:
    try:
        # Safely extract JSON from LLaMA output
        json_start = output.find("{")
        json_end = output.rfind("}")
        if json_start != -1 and json_end != -1:
            json_str = output[json_start:json_end + 1]
            return json.loads(json_str)
        return {"error": "No valid JSON block found in LLaMA output."}
    except Exception as e:
        return {"error": f"Failed to parse response: {str(e)}"}
