import random
from collections import defaultdict

print("🔵 Starting Markov Text Generation Project")
print("🔵 Task-03 | ProDigy Infotech")
print("-" * 50)

# Step 1: Training text
print("📘 Loading training text...")
text = """
dark neon lights glow
neon lights shine bright
dark lights shine
"""

# Step 2: Splitting text into words
words = text.split()
print("📘 Words extracted from text:")
print(words)
print("-" * 50)

# Step 3: Creating Markov Chain
print("⚙️ Building Markov Chain model...")
markov_chain = defaultdict(list)

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    markov_chain[current_word].append(next_word)

print("⚙️ Markov Chain created successfully!")
print("📊 Word transition map:")
for key, value in markov_chain.items():
    print(f"  {key} → {value}")

print("-" * 50)

# Step 4: Text generation function
def generate_text(start_word, length=8):
    print(f"✨ Starting text generation from word: '{start_word}'")
    current_word = start_word
    result = [current_word]

    for step in range(length - 1):
        next_words = markov_chain.get(current_word)

        if not next_words:
            print("⚠️ No next word found. Stopping generation.")
            break

        chosen_word = random.choice(next_words)
        print(f"➡️ Step {step + 1}: '{current_word}' → '{chosen_word}'")

        result.append(chosen_word)
        current_word = chosen_word

    return " ".join(result)

# Step 5: Generate and display text
print("🚀 Generating text using Markov Chain...\n")
generated_text = generate_text("dark", 8)

print("\n✅ Text Generation Completed!")
print("📝 Generated Text:")
print(generated_text)
print("-" * 50)

