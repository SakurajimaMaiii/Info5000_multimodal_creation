import json
import os
import requests


novel="""**Name:** The Kingdom of Unwritten Doors

**Outline:**
This opening chapter launches a fifty-chapter fantasy arc set in Calavere, a Magic Kingdom whose spells flow from the Glass Crown and nine ley-lines. On the eve of the Lantern Convergence, Elara Voss, an overlooked apprentice to the royal mapmaker, is sent to deliver a ward-survey to the palace. There she discovers a hidden atlas whose blank pages hold a living map of Calavere—one that shows a black door beneath the throne and erases the king’s name as she watches. When the High Court Mage tries to seize the atlas, he is drawn into a mirror and vanishes; Elara flees with the book, and the map brands her wrist with the words “Unwritten Heir,” awakening a sealed gate beneath the city and setting the main quest in motion.

**Paragraph 1:**
The Magic Kingdom of Calavere did not glitter so much as breathe. On the eve of the Lantern Convergence, every canal in the capital shimmered with contained spellfire, every arched bridge wore garlands of winking glass, and the towers of the palace rose above the rooftops like a crown set down by a careless giant. Nobles walked the processional streets with spellmarks glowing at their temples, their cloaks trailing wisps of colored light, while common folk pressed to the curbs with paper lanterns and quiet, hungry faces. Above them all, the Glass Crown hung in the sky as a fractured halo, feeding the nine ley-lines that kept Calavere’s wards alive, its streets clean, its bread warm, and its poor politely invisible.

**Paragraph 2:**
Elara Voss had spent the whole festival evening carrying a rolled ward-survey through the servants’ corridors of the palace, invisible in the way only an apprentice could be. She was seventeen, ink-stained, and too tall for the low doors of the royal mapmaker’s workshop, where she had learned to copy coastlines, correct noblemen’s estates, and never ask why certain streets vanished from official charts. Her master had sent her to deliver the survey before the Convergence bell, but a wrong turn brought her into a map room she had never seen: a cold, round chamber lined with mirrors, where a black-bound atlas lay open on a pedestal. The pages were blank except for one, and on that page Calavere drew itself in silver ink, street by street, until a black door appeared beneath the palace and the king’s name faded from the royal registry like breath from glass.

**Paragraph 3:**
She was still staring when the High Court Mage entered, his robes hissing with trapped lightning. He saw the atlas, saw Elara, and reached for the book with a command that made the mirrors ring; instead, the pedestal’s reflection seized him by the wrist and pulled him through the silver surface, leaving only a smell of scorched frost and a handprint steaming on the glass. Elara grabbed the atlas and ran, her heart pounding against the festival drums, while guards shouted behind her and the map’s blank pages fluttered like trapped birds. In the stairwell beneath the palace, the atlas burned cold against her arm and wrote upon her skin in silver letters: Unwritten Heir. Far below, something ancient turned in its sleep, and a sealed gate beneath Calavere opened for the first time in three hundred years.

"""
prompt = f"I'll give you some novel excerpts/fragments—help me draw a comic strip to depict the novel.\n {novel}"





url = ""
api_key=""
headers = {
    "Authorization": api_key,
    "Content-Type": "application/json",
}
payload = {
    "model": "gpt-image-2",
    "prompt": prompt,
    "size": "1024x1024",
    "n": 1,
    "quality": "low",
    "response_format": "url",
}
response = requests.request("POST", url, headers=headers, json=payload, timeout=120)
response.raise_for_status()
result = response.json()
if isinstance(result, dict) and (result.get("success") is False or result.get("code") is False or result.get("error")):
    raise RuntimeError(json.dumps(result, ensure_ascii=False))
print(json.dumps(result, ensure_ascii=False, indent=2))

image_url = result["data"][0]["url"]
print(f"fetch images from {image_url}")
response = requests.get(image_url, timeout=30)
response.raise_for_status()

with open("image_output.jpg", "wb") as f:
    f.write(response.content)