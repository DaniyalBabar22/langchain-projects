from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

load_dotenv()

def main() -> None:
    animal = input("Enter an animal: ").strip()
    if not animal:
        print("No animal provided.")
        return

    valid_animal_template = (
        'Is "{animal}" an animal? Answer only yes or no.'
    )
    valid_animal_prompt_template = PromptTemplate(
        input_variables=["animal"], template=valid_animal_template
    )
    # gemma3:270m is too small for reliable classification
    classifier = ChatOllama(model="llama3.2:1b", temperature=0)
    result = (valid_animal_prompt_template | classifier).invoke(
        input={"animal": animal}
    )
    answer = result.content.strip().lower()

    if not answer.startswith("yes"):
        print("Not an animal.")
        return

    poem_template = """
    Write a short, playful poem about the following animal.
    Animal: {animal}
    """
    poem_prompt_template = PromptTemplate(
        input_variables=["animal"], template=poem_template
    )

    llm = ChatOllama(model="gemma3:270m", temperature=0.7)
    poem = (poem_prompt_template | llm).invoke(input={"animal": animal})
    print(poem.content)

if __name__ == "__main__":
    main()
