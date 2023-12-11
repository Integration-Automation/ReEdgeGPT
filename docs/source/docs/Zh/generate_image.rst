ReEdgeGPT 生成圖片
----

.. code-block:: python

    import os
    import shutil
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
        image_list = sync_gen.get_images("tree")
        print(image_list)

    if __name__ == "__main__":
        # Make dir to save image
        Path("test_output").mkdir(exist_ok=True)
        # Save image
        test_save_images_sync()
        # Generate image sync
        test_generate_image_sync()
        # Remove dir
        shutil.rmtree(test_output_dir)

