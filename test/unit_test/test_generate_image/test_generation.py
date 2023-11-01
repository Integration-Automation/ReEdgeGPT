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
auth_cooker = str(os.getenv("IMAGE_COOKIE"))
sync_gen = ImageGen(auth_cookie=auth_cooker)
async_gen = ImageGenAsync(auth_cookie=auth_cooker)


def test_save_images_sync():
    sync_gen.save_images([test_image_url], test_output_dir)
    sync_gen.save_images([test_image_url], test_output_dir, file_name="test_image")
    # check if the image was downloaded and saved correctly
    assert os.path.exists(os.path.join(test_output_dir, "test_image_0.jpeg"))
    assert os.path.exists(os.path.join(test_output_dir, "0.jpeg"))


def test_generate_image_sync():
    image_list = sync_gen.get_images("Big, Golden, Tree")
    print(image_list)


# Generate image list async
async def test_generate_image_async():
    image_list = await async_gen.get_images("La Tour Eiffel")
    print(image_list)


if __name__ == "__main__":
    try:
        Path("test_output").mkdir(exist_ok=True)
        test_save_images_sync()
        test_generate_image_sync()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test_generate_image_async())
        shutil.rmtree(test_output_dir)
    except Exception as error:
        raise error
    finally:
        sys.exit(0)

