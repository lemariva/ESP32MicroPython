"""
Copyright [2018] [Mauro Riva <lemariva@mail.com> <lemariva.com>]
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.


based on https://rosettacode.org/wiki/MD5/Implementation#Python
adapted for MicroPython
"""

rotate_amounts = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                  5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
                  4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                  6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

#constants = [int(abs(math.sin(i+1)) * 2**32) & 0xFFFFFFFF for i in range(64)] # precision is not enough
constants = [3614090360, 3905402710, 606105819, 3250441966, 4118548399, 1200080426, 2821735955, 4249261313,
             1770035416, 2336552879, 4294925233, 2304563134, 1804603682, 4254626195, 2792965006, 1236535329,
             4129170786, 3225465664, 643717713, 3921069994, 3593408605, 38016083, 3634488961, 3889429448,
             568446438, 3275163606, 4107603335, 1163531501, 2850285829, 4243563512, 1735328473, 2368359562,
             4294588738, 2272392833, 1839030562, 4259657740, 2763975236, 1272893353, 4139469664, 3200236656,
             681279174, 3936430074, 3572445317, 76029189, 3654602809, 3873151461, 530742520, 3299628645,
             4096336452, 1126891415, 2878612391, 4237533241, 1700485571, 2399980690, 4293915773, 2240044497,
             1873313359, 4264355552, 2734768916, 1309151649, 4149444226, 3174756917, 718787259, 3951481745]

init_values = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

functions = 16*[lambda b, c, d: (b & c) | (~b & d)] + \
    16*[lambda b, c, d: (d & b) | (~d & c)] + \
            16*[lambda b, c, d: b ^ c ^ d] + \
            16*[lambda b, c, d: c ^ (b | ~d)]

index_functions = 16*[lambda i: i] + \
    16*[lambda i: (5*i + 1)%16] + \
                  16*[lambda i: (3*i + 5)%16] + \
                  16*[lambda i: (7*i)%16]

def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x<<amount) | (x>>(32-amount))) & 0xFFFFFFFF

def md5(message):
    message = bytearray(message) #copy our input into a mutable buffer
    orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
    message.append(0x80)
    while len(message)%64 != 56:
        message.append(0)
    message += orig_len_in_bits.to_bytes(8, 'little')
    #print (message)

    hash_pieces = init_values[:]

    for chunk_ofst in range(0, len(message), 64):
        a, b, c, d = hash_pieces
        chunk = message[chunk_ofst:chunk_ofst+64]
        #print(a, b, c, d)
        for i in range(64):
            f = functions[i](b, c, d)
            g = index_functions[i](i)
            #print(constants[i])
            to_rotate = a + f + constants[i] + int.from_bytes(chunk[4*g:4*g+4], 'little')
            new_b = (b + left_rotate(to_rotate, rotate_amounts[i])) & 0xFFFFFFFF
            a, b, c, d = d, new_b, b, c
            #print(to_rotate)

        for i, val in enumerate([a, b, c, d]):
            hash_pieces[i] += val
            hash_pieces[i] &= 0xFFFFFFFF
    return sum(x<<(32*i) for i, x in enumerate(hash_pieces))

def digest(message):
    digest = md5(message)
    raw = digest.to_bytes(16, 'little')
    return '{:032x}'.format(int.from_bytes(raw, 'big'))
    #return raw
