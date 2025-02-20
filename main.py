from crewai.flow.flow import Flow, start, listen  # type: ignore
from litellm import completion
from dotenv import load_dotenv, find_dotenv

_: bool = load_dotenv(find_dotenv())

class projectcrew(Flow):

    @start()
    def generate_topic(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {"role": "user",
                "content": "Generate a topic for a blog post about the benefits of learning Agentic AI.only share the text of the topic" 
                }
              ]
        )
        self.state["topic"] = response["choices"][0]["message"]["content"]
        print(f"Step 1: Generated topic: {self.state['topic']}")

def kickoff():
    flow = projectcrew()
    flow.kickoff()
    # print("flow Response: ", flow.response)

