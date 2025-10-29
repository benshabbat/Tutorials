import random

emojis = [
    "😀", "🎉", "🚀", "🌟", "🍎", "🐍", "⚡", "🔥",
    "💡", "🎈", "🍕", "🌈", "🎵", "🏆", "📚", "🧩",
    "🛡️", "🎮", "🚴", "🌍", "🍔", "🎤", "📷", "💻",
    "🧸", "🎲", "🚗", "🌸", "🍩", "🎬", "🏀", "📱"
]



def generate_symbols(size: int, *, emoji: bool = False) -> list[str]:
    if emoji:
        return random.sample(emojis[:size], size)
    else:
        return random.sample([chr(ord('A') + i) for i in range(size)], size)
    

print(generate_symbols(4))
print(generate_symbols(4, emoji=True))
