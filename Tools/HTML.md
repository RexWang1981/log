# HTML 

## 折叠列表

<details>
    <summary>abc</summary>
        <li> xxx
        <li> xxx
        <li> xxx
</details>

## 进度条

<label for="file">File progress:</label>
<progress id="file" max="100" value="70">70%</progress>

## 段落

<p fontcolor="red">
  Geckos are a group of usually small, usually nocturnal lizards. They are found on every continent except Antarctica.
</p>

## 图片

<img
  class="fit-picture"
  src="/"
  alt="Grapefruit slice atop a pile of other slices" width="300">

## 视频

<video controls width="250">
  <source src="/media/cc0-videos/flower.mp4" type="video/mp4" />
  <a href="/media/cc0-videos/flower.mp4">MP4</a>
</video>

## 音频

<figure>
  <figcaption>Listen to the T-Rex:</figcaption>
  <audio controls src="/media/cc0-audio/t-rex-roar.mp3"></audio>
  <a href="/media/cc0-audio/t-rex-roar.mp3"> Download audio </a>
</figure>


## 列表

<label for="ice-cream-choice">Choose a flavor:</label>
<input list="ice-cream-flavors" id="ice-cream-choice" name="ice-cream-choice" />
<datalist id="ice-cream-flavors">
<option value="Chocolate"></option>
<option value="Coconut"></option>
<option value="Mint"></option>
<option value="Strawberry"></option>
<option value="Vanilla"></option>
</datalist>

## 折叠内容

<details>
  <summary>Details</summary>
  Something small enough to escape casual notice.
</details>

## 链接

<a href="https://www.wikipedia.org/">A link to Wikipedia!</a>

## 删除线

<s>hello</s>

or <del>hello

## 调整字体大小

<big>abc</big>
abc
<small>abc</small>
<small><small>abc</small></small>

## 下标

2<sub>3


## 下划线

<u>下划线</u>

## 按钮

<button name="button"> Good morning</button>

## 下拉列表

<label for="pet-select">Choose a pet:</label>

<select id="pet-select">
  <option value="">--Please choose an option--</option>
  <option value="dog">Dog</option>
  <option value="cat">Cat</option>
  <option value="hamster">Hamster</option>
  <option value="parrot">Parrot</option>
  <option value="spider">Spider</option>
  <option value="goldfish">Goldfish</option>
</select>

## 文本框

<label for="story">Tell us your story:</label>

<textarea id="story" name="story" rows="5" cols="33">
It was a dark and stormy night...
</textarea>

## 设置背景音

<figure>
  <figcaption>Listen to the T-Rex:</figcaption>
  <audio controls src="/media/cc0-audio/t-rex-roar.mp3"></audio>
  <a href="/media/cc0-audio/t-rex-roar.mp3"> Download audio </a>
</figure>

## 设置剧中

<center> 这段文字将居中</center>

## 换行

<br/>

## 插入分割线

<hr/>

## 输入信息

<input type="text"> <!-- This is for text input -->
<input type="file"> <!-- This is for uploading files -->
<input type="checkbox"> <!-- This is for checkboxes -->

## 注释

<!-- This is a comment -->

## 鼠标移过，显示说明信息

<abbr id="anId" class="jargon" style="color:purple;" title="Hypertext Markup Language">HTML</abbr>

&lt