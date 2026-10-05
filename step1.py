from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# loading env variables
load_dotenv()

def message_to_text(message):
    # Every reply object keeps its answer in .content
    content = message.content

    # Case 1: content is already a plain string, so just hand it back
    if isinstance(content, str):
        return content

    # Case 2: content is a list of blocks, e.g. [{"type": "text", "text": "..."}]
    elif isinstance(content, list):
        # An empty list to collect each piece of text into
        parts = []

        # Visit the blocks one at a time
        for block in content:
            # Only dictionaries have a "text" key we can read
            if isinstance(block, dict):
                # .get returns the value, or None if the key is missing
                text = block.get("text")

                # Skip blocks with no text (for example an image block)
                if text:
                    parts.append(text)

        # The loop is finished: glue all pieces into one string
        return " ".join(parts)

    # Case 3: anything unexpected, convert it to a string so we never crash
    else:
        return str(content)



# getting the model
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")


# invoking the model with a query
response = llm.invoke("My wheat leaves are turning yellow. what should i do?")

print(message_to_text(response))