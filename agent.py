from google import genai
from dotenv import load_dotenv
import os
import json


# ---------------------------------
# Load Environment Variables
# ---------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# ---------------------------------
# Connect to Gemini
# ---------------------------------

client = genai.Client(
    api_key=api_key
)


# ---------------------------------
# AI Civic Agent
# ---------------------------------

def ask_agent(complaint):

    prompt = f"""
You are an AI Civic Action Agent.

Analyze the following citizen civic complaint.

Return ONLY a valid JSON object.
Do not use markdown.
Do not add explanations outside the JSON.

The JSON must contain exactly these fields:

{{
    "issue_type": "Main type of civic issue",
    "severity": "Low, Medium, High, or Critical",
    "department": "Responsible government department",
    "reason": "Explain why this department is responsible",
    "action": "Recommended action to solve the problem"
}}

Citizen Complaint:

{complaint}
"""


    # ---------------------------------
    # Send Request to Gemini
    # ---------------------------------

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )


    # ---------------------------------
    # Get AI Response
    # ---------------------------------

    response_text = response.text.strip()


    # ---------------------------------
    # Remove Markdown if AI Adds It
    # ---------------------------------

    if response_text.startswith("```"):

        response_text = response_text.replace(
            "```json",
            ""
        )

        response_text = response_text.replace(
            "```",
            ""
        )

        response_text = response_text.strip()


    # ---------------------------------
    # Convert JSON Text to Python Dictionary
    # ---------------------------------

    try:

        result = json.loads(
            response_text
        )

        return result


    except json.JSONDecodeError:

        # Fallback if AI does not return valid JSON

        return {
            "issue_type": "Other",
            "severity": "Medium",
            "department": "Municipal Administration",
            "reason": "The complaint requires review by the appropriate civic administration department.",
            "action": "Please submit the complaint to the relevant local government department for further investigation."
        }


# ---------------------------------
# Test AI Agent
# ---------------------------------

if __name__ == "__main__":

    complaint = input(
        "Describe your civic problem: "
    )


    result = ask_agent(
        complaint
    )


    print(
        "\n--- AI CIVIC ACTION ANALYSIS ---\n"
    )


    print(
        json.dumps(
            result,
            indent=4
        )
    )