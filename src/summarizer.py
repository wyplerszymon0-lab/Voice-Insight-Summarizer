from openai import OpenAI

class InsightEngine:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def extract_action_items(self, text: str):
        prompt = f"""
        Analyze the following transcript of a business meeting. 
        Extract a list of 'Action Items' with assigned owners if mentioned. 
        Provide a 3-sentence executive summary.
        
        Transcript: {text}
        """
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
