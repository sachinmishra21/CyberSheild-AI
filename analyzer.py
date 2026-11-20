import ollama

MODEL = "mistral"

PROMPT = """
You are an expert Cyber Security Analyst.

Analyze the given message.

Return:

1. Threat Type
2. Risk Level
3. Explanation
4. Recommendation

Keep the answer simple and professional.
"""

def ai_analysis(text):

    try:

        response = ollama.chat(

            model=MODEL,

            messages=[
                {
                    "role": "system",
                    "content": PROMPT
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return f"AI Error : {e}"