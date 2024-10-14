import requests as rq

GetParams = {'param1': 'value1', 'param2': 'value2'}
response = rq.get('https://httpbin.org', GetParams)

print(response)
print(response.url)

PostParams = {'param1': 'value1', 'param2': 'value2'}
response = rq.post('https://httpbin.org/post', PostParams)

print(response.json()['form'])

response = rq.options('https://httpbin.org')

print(response.headers)

from PIL import Image, ImageFilter
image = Image.open('i.jpg')
image.show()

cropped = image.crop((0, 80, 200, 400))
cropped.save('cropped_i.jpg')

blurred_jelly = image.filter(ImageFilter.BLUR)
blurred_jelly.save('blurry_i.jpg')
