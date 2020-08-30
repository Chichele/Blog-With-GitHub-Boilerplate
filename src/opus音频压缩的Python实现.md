---
layout: post
title: opus音频压缩的Python实现
categories: 
  - Tech
tags: 
  - 音频处理
date: 2020-08-30 21:14:00
---

> 最近我在开发语音识别应用的时候，接触到opus这种有损音频压缩格式，大概能压缩到原音频的十分之一大小，相当优秀，据说已实际取代了speex的地位。opus的使用上是比较简单的，但网上的资料不多，也花了我一些时间去理解消化，特此记录并分享一下。

# 依赖安装
- Linux下执行`pip3 install opuslib`
- Windows下执行安装`pip3 install opuslib`后，运行时仍会报缺少opus环境，暂未解决。

# 样例代码
```
# 以下代码包含音频压缩与解压
import opuslib
OPUS_FRAME_SIZE = 640 # 单次压缩的片段字节大小，可根据具体业务设置
encoder = opuslib.Encoder(voice_record.RATE, voice_record.CHANNELS, "voip") # opus压缩有3种模式'voip','audio','restricted_lowdelay'
decoder = opuslib.Decoder(voice_record.RATE, voice_record.CHANNELS)

encoder.reset_state() # 重置状态
decoder.reset_state()

# voice_piece是待压缩的音频片段，大小为OPUS_FRAME_SIZE个字节
tmp_enc_piece = encoder.encode(voice_piece, int(OPUS_FRAME_SIZE/2)) # 第二个参数是frame_size，每一frame实际是2字节，所以这里要除以2
tmp_dec_piece = decoder.decode(tmp_enc_piece, int(OPUS_FRAME_SIZE/2), False)

```