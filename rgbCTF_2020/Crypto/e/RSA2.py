# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:23:19 2020
"""

import math

def getModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


if __name__ == "__main__":
    n = int(0x5fb76f7f36c0d7788650e3e81fe18ad105970eb2dd19576d29e8a8697ebbd97f4fc2582bf1dc53d527953d9615439ca1b546b2fc1cd533db5fce6f72419f268e3182c0324a631a17d6b3e76540f52f2df51ca34983392d274f292139c28990660fa0e23d1b350da7aa7458a3783107a296dcd1720e32afb431954d8896f0587cd1c8f1d20701d6173b7cffe53679ebda80f137c83276d6628697961f5fcd39e18316770917338c6dc59a241dcdc66417fed42524c33093251c1d318b9dbeb6c3d0a69438b875958e8885d242d196e25bc73595e7f237c8124e07a79f7066f2dee393e2130306ba29e7ece1825798ff8b35416b3a0d96bcdc6eca5616ea2874954f8f88232450ddad3e109338bcc5d84e7b592a6b0871bd4130b84f81ed188e9d5495c8545aa8dea2b65e8605f5a49e3a1c221cbcc301665187658784a8f42a23c2ca2572477ba56ff19934019b48f5a1ab8a50626c85bdd476b11e8c1fb0b740c2370de3da5cc06371a7aa2c4e12eee3dc4cda07a8c84ba2bc3ee2017156468af95111d7ee5152ce35e66fa027a944b43c27fbd27faa5b4f9075be3526a7a5be8a533b523cd5c738c724e97597fc2e3666cfcad7c79d972ff8d9572100e860395cdc3761af3f4cc225a6df83a55802723f95cfba5918d83913f2cc9b219210249928c291310d449042772e2d0a50620d666a137f79770de6f10196b30cc756e1)
    e = int(0b1101)
    c = int(0x6003a15ff3f9bc74fcc48dc0f5fc59c31cb84df2424c9311d94cb40570eeaa78e0f8fc2917addd1afc8e5810b2e80a95019c88c4ee74849777eb9d0ee27ab80d3528c6f3f95a37d1581f9b3cd8976904c42f8613ee79cf8c94074ede9f034b61433f1fef835f2a0a45663ec4a0facedc068f6fa2b534c9c7a2f4789c699c2dcd952ed82180a6de00a51904c2df74eb73996845842276d5523c66800034351204b921d4780180ca646421c61033017e4986d9f6a892ed649c4fd40d4cf5b4faf0befb1e2098ee33b8bea461a8626dd8cd2eed05ccd471700e2a1b99ed347660cbd0f202212f6c0d7ad8ef6f878d887af0cd0429c417c9f7dd64890146b91152ea0c30637ce503635018fd2caf436a12378e5892992b8ec563f0988fc0cebd2926662d4604b8393fb2000)


    p = 11991774936877218203611546218822762533806381024952870770
    q = n//p

    phi = (p-1)*(q-1)
    d = getModInverse(e, phi)
    
    # Decrypt ciphertext
    pt = pow(c, d, n)
    # print flag
    h = hex(pt)