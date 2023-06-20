import asyncio
import argparse
from tauri import Tauri

async def page_handler():
    print("Running page_handler")

async def main():
    parser = argparse.ArgumentParser(description='Your description here')

    # Define an argument
    parser.add_argument('--name', '-n', type=str, help='Name to greet')

    # Parse the arguments
    args = parser.parse_args()

    # Access the arguments as properties of `args`
    print(f"Hello, {args.name}!")

    # Tauri
    tauri = await (Tauri("/home/simon/projects/tauri-apps/tauri/tooling/python/dylib/target/debug/libapp.so")
             .any_thread()
             .run("/home/simon/projects/tauri-apps/tauri/tooling/python/test-app/tauri.conf.json"))

if __name__ == "__main__":
    asyncio.run(main())
