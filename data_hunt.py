from simple_image_download import simple_image_download as sm

request = sm.simple_image_download
images = ['cats','dogs']
for img in images:
    request().download(img,limit=7)
