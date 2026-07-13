from app.services.granite import ask_granite
from app.services.code_detector import detect_language

def explain_code(
    code: str,
):
    language = detect_language(code)
    
    prompt = f"""
    You are a senior software engineer and programming mentor.

Task:
Analyze the following {language} code and determine whether it is valid.

Code:
{code}

Rules:

1. First check whether the code contains syntax errors, missing brackets, incorrect keywords, invalid structure, or obvious programming mistakes.

2. If the code is INVALID:
   - Start with:

     • Status:
       Invalid Code Detected

   - Briefly explain what is wrong.
   - Provide a corrected version of the code.
   - Then explain the corrected code using the format below.

3. If the code is VALID:
   - Do not mention validation.
   - Directly explain the code using the format below.

4. Explanation Rules:
   - Start directly with the explanation.
   - Do NOT write introductions like "Certainly!".
   - Do NOT write "Code Explanation".
   - Do NOT repeat the original code unless correction is required.
   - Keep explanations concise and beginner-friendly.
   - Explain only what exists in the code.
   - Use markdown bullet points.
   - Explain variables, functions, loops, conditions, classes, and important operations if present.
   - If loops or conditions do not exist, do not mention them.
   - Keep short code explanations short.

5. Use this format:

• Purpose:
  One sentence describing what the code does.

• Breakdown:
  - First important part
  - Second important part
  - Third important part

• Output:
  Describe the expected result.

6. If code correction is required, use this format:

• Status:
  Invalid Code Detected

• Issue:
  Explain the problem briefly.

• Corrected Code:
```language
corrected code here
    """
    explanation =ask_granite(prompt)
    
    return {
        "language": language,
        "explanation": explanation
    }