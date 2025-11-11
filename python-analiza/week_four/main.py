from string_ops import reverse_string, uppercase_string, remove_vowels, remove_every_third, letter_counts
import asyncio


async def main():
    print(await reverse_string("Hello, World!"))
    print(await uppercase_string("Hello, World!"))
    print(await remove_vowels("This is an example."))
    print(await remove_every_third("This is an example."))
    print(await letter_counts("This is an example."))


if __name__ == "__main__":
    asyncio.run(main())
    