import os
import time
import requests
from dotenv import load_dotenv
from agent import generate_character

load_dotenv()

API_KEY = os.getenv("FREEPIK_API_KEY")

BASE_URL = "https://api.freepik.com/v1/ai/text-to-image"


# 🖼️ CREATE TASK
def generate_image(prompt):

    url = f"{BASE_URL}/nano-banana-pro-flash"

    payload = {
        "prompt": prompt,
        "aspect_ratio": "9:16",
        "resolution": "2K",
        "num_images": 1
    }

    headers = {
        "x-freepik-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    return requests.post(url, json=payload, headers=headers).json()


# ⏳ CHECK STATUS
def check_status(task_id):

    url = f"{BASE_URL}/nano-banana-pro-flash/{task_id}"

    headers = {"x-freepik-api-key": API_KEY}

    for _ in range(25):

        res = requests.get(url, headers=headers).json()

        if "data" not in res:
            return None

        status = res["data"].get("status")

        print("⏳", status)

        if status == "COMPLETED":
            return res

        if status == "FAILED":
            return None

        time.sleep(5)

    return None


# 📥 DOWNLOAD
def download_image(url, path):

    img = requests.get(url)

    if img.status_code == 200:
        with open(path, "wb") as f:
            f.write(img.content)


# 🔥 BATCH GENERATION
def generate_batch(name, age, region, gender, description):

    data = generate_character(name, age, region, gender, description)

    tasks = []

    for item in data["scenes"]:

        prompt = f"""
{data['appearance']},

- same face, same identity,
- full face visible, consistent facial features, looking at camera,
- Same facial structure, same eyes, same nose, same lips
- Same skin tone, same hairstyle
- do not change identity

{item['prompt']},

cinematic lighting, ultra realistic, 4k
"""

        res = generate_image(prompt)

        if "data" in res and "task_id" in res["data"]:

            tasks.append({
                "scene": item["scene"],
                "task_id": res["data"]["task_id"],
                "prompt": prompt
            })

    return tasks, data