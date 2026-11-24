import os
import json
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# 🔥 SAFE JSON PARSER
def safe_json_parse(text):

    text = text.replace("```json", "").replace("```", "").strip()

    # 1️⃣ try direct parse
    try:
        return json.loads(text)
    except:
        pass

    # 2️⃣ extract multiple JSON blocks safely
    matches = re.findall(r"\{.*?\}", text, re.DOTALL)

    for m in matches:
        try:
            return json.loads(m)
        except:
            continue

    raise ValueError("Could not parse JSON")


# 🧠 CHARACTER AGENT
def generate_character(name, age, region, gender, description):

    prompt = f"""
You are a strict JSON generator.

Generate ONLY valid JSON.

No explanation. No markdown.

RULES: 
- Valid JSON only

CHARACTER INFO:
Name: {name}
Age: {age}
Region: {region}
Gender: {gender}
Lifestyle / Role: {description}

You MUST adapt everything based on region and lifestyle.

IMPORTANT:
- Description MUST be visible in ALL scenes
- Scenes MUST include actions related to description
- Objects related to lifestyle MUST appear (example: clay, pottery, gym tools, pets, etc.

Ensure: 
- Same identity across all scenes
- Face must remain consisten
- Outfit must change in each scene
- Pose, camera, lighting must change
- Background MUST match the region realistically
- Lifestyle must reflect in clothing and environment
- Age must reflect in appearance

Examples:
- pet parent → caring, cozy outfits, pets in scene
- gymnastic girl → athletic body, sporty outfit, action poses
- skincare influencer → beauty lighting, aesthetic room, soft visuals
- street fighter → aggressive tone, urban background

background logic:
Background = Region Environment + Lifestyle Activity


FORMAT:
{{
    "appearance": "...based on age + gender + lifestyle + region...",
    "backstory": "...based on lifestyle...",
    "scenes": [
        {{
            "scene": 1,
            "prompt": "scene 1 with lifestyle + region"
        }},
        {{
            "scene": 2,
            "prompt": "scene 2 dramatic scene + same identity + same character + different clothing + different pose + different camera + background  "
        }},
        {{
            "scene": 3,
            "prompt": "scene 3 dramatic scene + different lighting + same identity + same character + different clothing + background"
        }}
    ]
}}
"""    

    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    content = res.choices[0].message.content
    data = safe_json_parse(content)

    # ✅ fallback safety
    data.setdefault("appearance", "a person")
    data.setdefault("backstory", "")
    data.setdefault("scenes", [])

    # 🔥 HARD CONTROL → only 3 scenes
    data["scenes"] = data["scenes"][:3]

    return data 

