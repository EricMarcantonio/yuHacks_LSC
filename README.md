# Writing Ransomware in Python - Lassonde Security Club :lock:

### For educational purposes only :school:

### Author: Eric Marcantonio :rocket:

## Getting Started :new:

If you don't already have a virtual environment setup, please download and create one. I personally like to use [anaconda.](https://www.anaconda.com/products/individual)

```sh
$ git clone https://github.com/EricMarcantonio/yuHacks_LSC.git
$ cd yuHacks_LSC
$ conda create --name any_name_you_like
$ conda activate any_name_you_like
```

This terminal is now prepared to run your program. Why did we need to do this? Python loves environments, and sometimes I could have something installed on my global environment that you don't have, making it difficult for me to share it among others. If you want to learn more, here is a linked [article.](https://realpython.com/python-virtual-environments-a-primer/#:~:text=At%20its%20core%2C%20the%20main,dependencies%20every%20other%20project%20has.)



## Setup :wrench:

There are 2 different branch's; one for you to practice on, and one with the "answers". If you get stuck, I would #tryharder, until you see other code I wrote. I have provided files that take care of most of the encryption process, (i.e read_write, AES, RSA) all you have to do is implement them. Writing effective ransomware is a multi-hour process, and usually involves in-depth knowledge of a language.



## Can I use this in the real world? :world_map:

Yes and No. It depends on what you are using it for. Effectively this is unweaponized malware, as we are just encrypting files. We won't show how to weaponize it, but with a few changes, it can be a dangerous tool. See MERKWare for an example :smile:
