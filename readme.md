# uc浏览器缓存视频m3u8转换为mp4文件
#### 缘起
有的时候手机上uc浏览器缓存的视频我想保存下来，但是传到电脑上后都是m3u8和没有后缀的文件。百度了一下，发现网上的方法比较碎片而且居然还有人卖这个软件，作为理工男不能惯着（主要是穷）。因此自己学习总结整理了一下，希望可以帮到人。

#### 注意事项
1. 本文中的代码路径都是按照我本人使用的路径写的，可以按照自己的需求进行修改。
2. 本文不涉及ffmpeg的安装，要是没有请自己百度。要是不会就请放弃吧。
3. 对于m3u8和ts文件来说，有的会有加密，即多一个类似名字叫“k0”的文件，这是缓存视频的秘钥。本文的步骤对于加密或不加密的文件都适用。

#### 思想
简单说一下想法，就是先把原来的m3u8文件中ts文件的路径换成自己本地ts文件的路径，然后用ffmpeg进行合并。不管是加密或者不加密的，只要有秘钥文件，ffmpeg都支持。

#### 环境
1. win10
2. ffmpeg
3. python3

#### 步骤

1. 首先，把所有ts文件和m3u8放在source_m3u8文件夹下；没有这个文件夹就新建一个。
2. 然后，运行a.py，转换m3u8文件中指定的ts文件路径；

以上代码会在gen_m3u8文件夹中生成新的m3u8文件，之后就用这个新的。如果没有gen_m3u8文件夹，要事先手动创建一下。

3. 接着，运行b.py可以生成一个文件，文件中包括所有m3u8文件的转换命令。

4. 最后，打开生成的result_cmd.txt文件，复制其中的每一行，放在cmd中运行就可以了。

对于最后这一步，可能要自己手动一条一条运行，我试了一下用Python自动运行，如果直接来的话应该是不行的。这个问题我没有深究，以后有兴趣了再补吧。

------------

更新更新！

上一步中生成的result_cmd.txt文件直接使用windows命令就可以自动运行所有的了。具体步骤如下：
1. 先把生成的txt文件后缀改成bat
2. 打开cmd窗口，输入：start result_cmd.bat
就这样，可以自动运行所有的了。


