"""
display_style,      # "dense" is the only supported one right now.
widgets             # Where all the widget's settings are stored.
  size": {"width":1, "height":1},    # span width and span height 
  name": "html",    # the name of the module that we will execute. Will be in extractors.py
  arguments": {}    # The values we will give it initially and everytime we run it. Can be blank.
"""
display_settings = {
    "display_style": "dense",
    "widgets": [
        {
            "name": "html",
            "size": {"width": 2, "height": 2},
            "arguments": {"text_content": "Hey Youtubes!"}
        },
        {
            "name": "html",
            "size": {"width": 2, "height": 2},
            "arguments": {"text_content": "Hey Youtubes!"}
        },
        {
            "name": "html",
            "size": {"width": 2, "height": 2},
            "arguments": {"text_content": "Hey Youtubes!"}
        },
        {
            "name": "html",
            "size": {"width": 2, "height": 2},
            "arguments": {"text_content": "Hey Youtubes!"}
        },
        {
            "name": "html",
            "size": {"width": 2, "height": 2},
            "arguments": {"text_content": "Hey Youtubes!"}
        },
    ]
}
