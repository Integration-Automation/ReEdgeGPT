ReEdgeGPT 生成圖片
----

.. code-block:: python

    import asyncio
    import os
    import shutil
    from pathlib import Path

    from re_edge_gpt import ImageGen, ImageGenAsync

    # 如果沒有這個檔案請讀 README.md
    auth_cooker = open("bing_cookies.txt", "r+").read()
    async_gen = ImageGenAsync(auth_cookie=auth_cooker)

    # 非同步產生圖片
    async def test_generate_image_async():
        print("Generate Big Ben image")
        # 取得圖片連結 list
        image_list = await async_gen.get_images("Big Ben")
        # print 圖片連結 list
        print(image_list)


    if __name__ == "__main__":
        # 產生圖片
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test_generate_image_async())

