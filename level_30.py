# LEVEL 30
# http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
from PIL import Image

nums = []
with open('data/yankeedoodle.csv', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        for n in line.split(','):
            num = n.strip()
            if num:
                nums.append(float(num))
print(len(nums))
# factors found using https://www.mathsisfun.com/numbers/prime-factorization-tool.html

img1 = Image.new('F', (139, 53))
img2 = Image.new('F', (53, 139))
img1.putdata(nums, 256)
img2.putdata(nums, 256)
# img1.show() # garbled
# img2.show() # it's up side down
img3 = img2.transpose(Image.FLIP_LEFT_RIGHT)
img3 = img3.transpose(Image.ROTATE_90)
# img3.show()
# img3 reads:
# n = str(x[i])[5]+str(x[i+1])[5]+str(x[i+2])[6]
message = bytearray()
x = nums
for i in range(0, len(x) - 2, 3):
    # ensure there are enough digits
    x[i] += 0.0000001
    x[i + 1] += 0.0000001
    x[i + 2] += 0.0000001
    n = str(x[i])[5] + str(x[i + 1])[5] + str(x[i + 2])[6]
    message.append(int(n))
print(message)
# ... look at grandpa ...
