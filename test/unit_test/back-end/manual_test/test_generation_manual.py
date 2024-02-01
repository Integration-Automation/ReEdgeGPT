import asyncio
import os
import shutil
import sys
from pathlib import Path

from re_edge_gpt import ImageGen, ImageGenAsync

# create a temporary output directory for testing purposes
test_output_dir = "test_output"
# download a test image
test_image_url = "https://picsum.photos/200"
auth_cooker = open("bing_cookies.txt", "r+").read()
sync_gen = ImageGen(auth_cookie=auth_cooker)
async_gen = ImageGenAsync(auth_cookie=auth_cooker)


def test_save_images_sync():
    sync_gen.save_images([test_image_url], test_output_dir)
    sync_gen.save_images([test_image_url], test_output_dir, file_name="test_image")
    # check if the image was downloaded and saved correctly
    assert os.path.exists(os.path.join(test_output_dir, "test_image_0.jpeg"))
    assert os.path.exists(os.path.join(test_output_dir, "0.jpeg"))


# Generate image list sync
def test_generate_image_sync():
    print("Generate Big Ben image")
    image_list = sync_gen.get_images("Big Ben")
    print(image_list)
    print("Generate Кра́снаяпло́щадь image")
    image_list = sync_gen.get_images("Кра́снаяпло́щадь")
    print(image_list)


# Generate image list async
async def test_generate_image_async():
    print("Generate La Tour Eiffel image")
    image_list = await async_gen.get_images("La Tour Eiffel")
    print(image_list)


if __name__ == "__main__":
    try:
        # Make dir to save image
        Path("test_output").mkdir(exist_ok=True)
        # Save image
        test_save_images_sync()
        # Generate image sync
        test_generate_image_sync()
        # Generate image async
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test_generate_image_async())
        # Remove dir
        shutil.rmtree(test_output_dir)
    except Exception as error:
        raise error
    finally:
        sys.exit(0)
