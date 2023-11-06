import asyncio
import shutil
import sys
from pathlib import Path

from re_edge_gpt import ImageGenAsync

# create a temporary output directory for testing purposes
test_output_dir = "test_output"
# download a test image
test_image_url = "https://picsum.photos/200"
auth_cooker = open("bing_cookies.txt", "r+").read()
async_gen = ImageGenAsync(auth_cookie=auth_cooker)


# Generate image list async
async def test_generate_image_async():
    print("Generate Pigeon")
    image_list = await async_gen.get_images("Pigeon")
    print(image_list)


if __name__ == "__main__":
    try:
        for i in range(3):
            # Make dir to save image
            Path("test_output").mkdir(exist_ok=True)
            # Generate image async
            loop = asyncio.get_event_loop()
            loop.run_until_complete(test_generate_image_async())
            # Remove dir
            shutil.rmtree(test_output_dir)
    except Exception as error:
        print(repr(error), file=sys.stderr)
    finally:
        sys.exit(0)
