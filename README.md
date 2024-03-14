<img src="https://github.com/Mikami063/Url_Handler/assets/114184664/739fd3b7-1686-4b59-ad21-7f3dad188808" alt="image" width="200" />
[icon credit to original author]

# Url_Handler

convert special characters in your web url to readable format, without breaking the url

.app excutable MacOS file in release

[icon set build by iconutil]

```
mkdir url_handler.iconset

sips -z 16 16     32x32-pixel-art.png --out url_handler.iconset/icon_16x16.png
sips -z 32 32     32x32-pixel-art.png --out url_handler.iconset/icon_16x16@2x.png
sips -z 32 32     32x32-pixel-art.png --out url_handler.iconset/icon_32x32.png
sips -z 64 64     32x32-pixel-art.png --out url_handler.iconset/icon_32x32@2x.png
sips -z 128 128   32x32-pixel-art.png --out url_handler.iconset/icon_128x128.png
sips -z 256 256   32x32-pixel-art.png --out url_handler.iconset/icon_128x128@2x.png
sips -z 256 256   32x32-pixel-art.png --out url_handler.iconset/icon_256x256.png
sips -z 512 512   32x32-pixel-art.png --out url_handler.iconset/icon_256x256@2x.png
sips -z 512 512   32x32-pixel-art.png --out url_handler.iconset/icon_512x512.png
sips -z 1024 1024 32x32-pixel-art.png --out url_handler.iconset/icon_512x512@2x.png

iconutil -c icns url_handler.iconset
```

[app file build by pyinstall]

```
pyinstaller --windowed --onefile --name Url_Handler --icon=url_handler.icns url_handler.py
```

Example Usage

https://www.anime-sharing.com/threads/help-with-installing-playing-fraternite-hd-remaster-%E3%83%95%E3%83%A9%E3%83%86%E3%83%AB%E3%83%8B%E3%83%86hd%E3%83%AA%E3%83%9E%E3%82%B9%E3%82%BF%E3%83%BC.1266537/

to

https://www.anime-sharing.com/threads/help-with-installing-playing-fraternite-hd-remaster-フラテルニテhdリマスター.1266537/


<img width="574" alt="image" src="https://github.com/Mikami063/Url_Handler/assets/114184664/ad782cf9-7852-4517-9276-9d3b5ad32805">

