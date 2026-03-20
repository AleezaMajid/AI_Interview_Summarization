from engine.summarizer import summarize_transcript
from engine.insight_extractor import extract_concepts

with open("prompts/summarization_prompt.txt") as f:
    prompt = f.read()

with open("sample_data/transcript.txt") as f:
    transcript = f.read()

summary = summarize_transcript(prompt, transcript)

concepts = extract_concepts(transcript)

print("\n===== SUMMARY =====\n")
print(summary)

print("\n===== TECH CONCEPTS =====\n")
print(concepts)