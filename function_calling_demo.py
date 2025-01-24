from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain_core.utils.function_calling import convert_to_openai_function
from dotenv import load_dotenv
import json
from memory_utils import MemoryStore

# Load environment variables
load_dotenv()

# Initialize memory store
memory = MemoryStore()

def store_memory(topic: str, information: str):
    """Store information about a specific topic in memory.
    
    Args:
        topic: The main subject or category
        information: The information to remember
    """
    return memory.store_memory(topic, information)

def retrieve_memory(topic: str):
    """Retrieve information about a specific topic from memory.
    
    Args:
        topic: The topic to search for
    """
    return memory.retrieve_memory(topic)

# Create the ChatOpenAI instance
llm = ChatOpenAI(model="gpt-4o-mini")

# Convert functions to OpenAI format
memory_functions = [
    convert_to_openai_function(store_memory),
    convert_to_openai_function(retrieve_memory)
]

print("\nAvailable functions:")
for func in memory_functions:
    print(func)

def process_user_input(user_message: str):
    print("\n=== Starting Process ===")
    print(f"1. Received user message: '{user_message}'")
    
    # Create system and user messages
    system_message = SystemMessage(content="""You are a helpful assistant with access to a memory system. 
    ALWAYS use the provided functions to interact with memory:
    - When users share information, use store_memory to save it
    - When users ask questions, ALWAYS use retrieve_memory to check stored information first
    - Never make up information - if you don't find anything in memory, say so
    
    Examples:
    - "Remember that John likes pizza" → Use store_memory
    - "What does John like?" → Use retrieve_memory
    - "What's John's favorite food?" → Use retrieve_memory
    """)
    
    user_msg = HumanMessage(content=user_message)
    messages = [system_message, user_msg]
    print("2. Created messages with system prompt")
    
    print("3. Calling LLM with functions:")
    for idx, func in enumerate(memory_functions):
        print(f"   Function {idx + 1}: {func['name']}")
        print(f"   Description: {func['description']}")
    
    # Get the response with function calling
    print("\n4. Invoking LLM...")
    response = llm.invoke(
        messages,
        functions=memory_functions,
        function_call="auto"
    )
    print(f"5. Received LLM response: {response}")
    
    # Handle function calls if any
    if response.additional_kwargs.get("function_call"):
        print("\n6. Function call detected!")
        function_call = response.additional_kwargs["function_call"]
        function_name = function_call["name"]
        function_args = json.loads(function_call["arguments"])
        
        print(f"   Function name: {function_name}")
        print(f"   Arguments: {function_args}")
        
        print("\n7. Executing function...")
        if function_name == "store_memory":
            result = store_memory(**function_args)
        elif function_name == "retrieve_memory":
            result = retrieve_memory(**function_args)
        
        # Create a follow-up response using the function result
        follow_up_msg = HumanMessage(content=f"Function returned: {result}\nPlease provide a natural response based on this result.")
        final_response = llm.invoke([system_message, user_msg, follow_up_msg])
        print(f"8. Final response: {final_response.content}")
    else:
        print("\n6. No function call detected")
        print(f"7. Direct AI Response: {response.content}")
    
    print("\n=== Process Complete ===")

# Update the main loop prompts
if __name__ == "__main__":
    print("Memory Assistant Ready! (Type 'quit' to exit)")
    print("\nI can help you store and retrieve information. For example:")
    print("- Tell me something to remember: 'Remember that Sarah's birthday is on March 15th'")
    print("- Ask about stored information: 'When is Sarah's birthday?'")
    print("- Ask about someone: 'What do you know about Sarah?'")
    print("- Share facts: 'John works as a software engineer in Google'")
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'quit':
            break
        process_user_input(user_input) 