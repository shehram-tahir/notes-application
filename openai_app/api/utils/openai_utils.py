from langchain.llms import OpenAI


def get_note_summarization(description: str):
    """
        This utility is to summarize text using openai LLM
        Parameters:
            description (str):
    """
    llm = OpenAI(temperature=0.7,
                 model_name="gpt-3.5-turbo",
                 token=40)
    template = f"""
    Please summarize the following note:
    {description}
    """
    return llm.invoke(template)
