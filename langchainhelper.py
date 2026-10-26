
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from secretkey import GROQ_API_KEY


class RestaurantIdea(BaseModel):
    restaurant_name: str
    menu_items: list[str]


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=GROQ_API_KEY,
    temperature=0.3,
    model_kwargs={"response_format": {"type": "json_object"}},
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Generate creative restaurant branding ideas. "
        "Return ONLY valid JSON with exactly this structure: "
        '{{"restaurant_name":"string","menu_items":["item 1","item 2","item 3","item 4","item 5","item 6","item 7","item 8","item 9","item 10"]}}. '
        "The menu_items array must contain exactly ten items."
    ),
    (
        "human",
        "Generate a restaurant name and ten menu items "
        "for {cuisine} cuisine."
    ),
])


chain = prompt | llm


def generate_name_and_items(cuisine: str) -> dict:
    response = chain.invoke({"cuisine": cuisine})
    return RestaurantIdea.model_validate_json(response.content).model_dump()
