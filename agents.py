# suppress warnings
import warnings

warnings.filterwarnings("ignore")
from together import Together

# Get Client
your_api_key = "9806a2601560024637df1e4acd804862faa67e08637db6598d920b64eebba43e"
client = Together(api_key=your_api_key)


def prompt_llm(prompt, show_cost=False):
    # This function allows us to prompt an LLM via the Together API

    # model
    model = "meta-llama/Meta-Llama-3-8B-Instruct-Lite"

    # Calculate the number of tokens
    tokens = len(prompt.split())

    # Calculate and print estimated cost for each model
    if show_cost:
        print(f"\nNumber of tokens: {tokens}")
        cost = (0.1 / 1_000_000) * tokens
        print(f"Estimated cost for {model}: ${cost:.10f}\n")

    # Make the API call
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


class SummarizerAgent:
    def __init__(self):
        self.client = Together(api_key=your_api_key)

    def process(self, content):
        prompt = """SYSTEM: You are an expert text summarizer. 
        Your task is to condense the provided text into a clear, informative summary of exactly 4 lines.

        INSTRUCTIONS:
        • Identify and include only the most important information
        • Maintain the core meaning of the original text
        • Ensure the summary is exactly 4 lines long
        • Use concise, clear language
        • Show output only - provide just the summary
        
        Text to summarize: {content}
        
        Provide a 4-line summary:"""

        return prompt_llm(prompt.format(content=content))
