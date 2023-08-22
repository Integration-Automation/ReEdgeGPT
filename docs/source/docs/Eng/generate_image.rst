ReEdgeGPT Generate Image
----

.. code-block:: python

    import asyncio
    import os
    import shutil
    from pathlib import Path

    from re_edge_gpt import ImageGen, ImageGenAsync

    # Read auth_cookie if you don't have this file please read README.md
    auth_cooker = open("bing_cookies.txt", "r+").read()
    async_gen = ImageGenAsync(auth_cookie=auth_cooker)

    # Generate image list async
    async def test_generate_image_async():
        print("Generate Big Ben image")
        # Get image links
        image_list = await async_gen.get_images("Big Ben")
        # Print image link list
        print(image_list)


    if __name__ == "__main__":
        # Generate image async
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test_generate_image_async())

