import os
import json
from image_api import generate_batch, check_status, download_image


def get_url(result):

    gen = result["data"].get("generated", [])

    if not gen:
        return None

    first = gen[0]

    if isinstance(first, dict):
        return first.get("url")

    return first


def main():

    print("🚀 MULTI CHARACTER SYSTEM")

    n = int(input("How many characters? "))

    for i in range(n):

        print(f"\n🔥 Character {i+1}")

        name = input("Name: ")
        age = input("Age: ")
        region = input("Region: ")
        gender = input("Gender: ")
        description = input("Description: ")

        folder = name.replace(" ", "_")

        os.makedirs(f"{folder}/images", exist_ok=True)
        os.makedirs(f"{folder}/artifacts", exist_ok=True)

        tasks, data = generate_batch(name, age, region, gender, description)

        # store generated images info
        data["generated_images"] = []

        for t in tasks:

            print("⏳ Scene", t["scene"])

            result = check_status(t["task_id"])

            if not result:
                continue

            url = get_url(result)

            if not url:
                continue

            path = f"{folder}/images/scene_{t['scene']}.jpg"

            download_image(url, path)

            data["generated_images"].append({
                "scene": t["scene"],
                "image_path": path,
                "prompt": t["prompt"]
            })


        with open(f"{folder}/artifacts/character.json", "w") as f:
            json.dump(data, f, indent=2)

        print(f"✅ {name} DONE!")

    print("🎉 ALL DONE")


if __name__ == "__main__":
    main()