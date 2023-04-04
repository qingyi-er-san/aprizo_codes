function I() {
    if (isStorageSpdLocalAll && !i) {
        var n = localStorage.getItem(m);
        if (null != n) {
            var o = n.replace(/id:/g, "");
            t = o.split(","),
            y = "" == n ? 0 : t.length,
            t.forEach(function(e, t) {
                D(e.replace("id:", ""))
            }),
            e(c).html(window.countComparePage || y)
        }
    }
}
function D(t, n) {
    var i = e(r + '[data-id="' + t + '"]:not(.' + h + ")");
    i.addClass(h).removeClass(f).find(".t4s-text-pr").text(v),
    i.find(".t4s-svg-pr-icon").html(x),
    n && n.trigger("updateTooltip")
}
function A(t, i = !1) {
    C && T4SThemeSP.getToFetchSection(null, "text", t.replace("view=compare", "section_id=compare-popup")).then(t = >{
        "NVT_94" != t && (i && n && n.remove(), T4SThemeSP.$appendComponent.after(t), n = e(".t4s_section__compare-popup"), i && setTimeout(function() {
            n.addClass(g)
        },
        20), T4SThemeSP.Tooltip())
    })
}
return {
    init: function() {
        isStorageSpdLocalAll && !i && (history.replaceState && _ && window.history.replaceState({},
        document.title, p + "/?view=compare"), k(), _ && (window.isEmtyCompare && window.isComparePerformed ? localStorage.removeItem(m) : (window.countComparePage != t.length && window.isComparePerformed && (e(dt_count_wishlist).html(window.countComparePage), localStorage.setItem(t4s_wis, window.listIDPrs)), !window.isEmtyCompare || window.isComparePerformed || "" == t.toString() || IsDesignMode || (window.location.href = w))), a.on("click", r + "." + h,
        function(e) {
            e.preventDefault(),
            e.stopPropagation(),
            C ? n.addClass(g) : window.location.href = w
        }), a.on("click", s,
        function(e) {
            e.preventDefault(),
            window.location.href = w
        }), a.on("click", d,
        function(i) {
            i.preventDefault(),
            n.removeClass(g);
            let o = t.length;
            for (let n = 0; n < o; n++) {
                let i = t[n].replace("id:", "");
                e(r + '[data-id="' + i + '"]').removeClass(h).find(".t4s-text-pr").text(T),
                e(r + '[data-id="' + i + '"]').find(".t4s-svg-pr-icon").html(b)
            }
            t = [],
            localStorage.setItem(m, t.toString()),
            y = 0,
            e(c).html(y),
            k()
        }),
浏览器概述
1.代码嵌入网页的方法
    1.1 <script> 元素之间嵌入代码
    1.2 <script> 标签加载外部脚本
    1.3 事件属性
        当网页元素的事件属性(比如onlick和onmouseover),可以写入JS代码，当指定事件发生时，就会调用这些代码。
        <button id="myBtn" onclick="console.log(this.id)">点击</button>
    1.4 URL 协议  
2.script元素      
2.1工作原理
    浏览器加载JS脚本，主要通过<script>元素完成。正常的网页加载流程是这样的：
    1.浏览器一步下载HTML网页，一边开始解析。也就是说，不等到下载完，就开始解析。
    2.遇到<script>元素，停止解析，把网页渲染的控制权交给JS引擎。
    3. 如果<script>元素引用了外部脚本。就会先下载脚本再执行。
    4.JS引擎执行完，控制权还个渲染引擎，恢复往下解析HTML网页。
    为什么会把控制权交给JS引擎?因为JS代码是可以修改DOM，所以必须把控制权交给它。
    那么就会有一个问题了，如果外部JS代码加载时间很长，那么浏览器就会一直等待脚本下载完成，造成网页长时间
    失去响应，浏览器就会呈现‘假死’状态。这就是‘阻塞效应’。
    为了避免这种情况，较好的做法是将<script>标签放在页面底部。这样哪怕是外部脚本无法下载，但是网站的主体已经有了
2.2 Defer属性
        为了解决脚本文件下载阻塞网页渲染的问题，一个方法是对<script>元素加入defer属性。它的作用是延迟脚本的执行，等到DOM加载生成后，再执行脚本。
        <script src='a.js' defer></script>
        此时的运行顺序就是 
        1.浏览器解析HTML网页
        2.发现defer属性的<script>元素。
        3.浏览器继续往下解析网页，并同时下载<script>元素的外部脚本。
        4.浏览器完成解析HTML网页，此时再执行已经下载完成的脚本。
    而且js脚本的执行顺序是就是出现在HTML中的顺序。
    对于内置的JS代码的<script>标签，以及动态生成script标签，defer属性不起作用。
2.3 async 属性
        解决 ‘阻塞效应’的另一方法是对<script>元素加入async属性
        <script src="a.js" async> </script>
        使用另一个进程下载脚本，下载是不会阻塞渲染。
        1.浏览器开始解析HTML网页
        2.发生有async属性的script
        3.浏览器继续往下解析HTML网页，同时并行下载<script>标签中的外部脚本
        4.脚本下载完成，浏览器暂停解析HTML网页，开始执行下载的脚本
        5.脚本执行完毕，浏览器恢复解析HTML网页。
        这个属性就可以保证脚本





Event对象
在Js中，事件发生之后，会产生一个事件对象，作为参数传给监听函数。浏览器元素提供一个event对象，所有的事件都是这个对象的实例
Event对象本身就是一个构造函数
event = new Event(type,options);
2. 实例属性:
2.1Event.bubbles,Event.eventPhase
        bubbles-> Boolean:检查该事件是否会冒泡，只读属性，除非显示声明，否则Event构造函数生成的事件，默认是不冒泡的
        eventPhase-> int: 表示事件目前所处的阶段，只读属性。只有四个返回值
        0：事件没有发生，
        1：事件目前处于捕获阶段，
        2：事件到底目标阶段，Event.target属性指向的那个节点
        3：事件处于冒泡阶段，
2.2 Event.cancelable, cancelBubble,defaultPrevented
        cancelabe->Boolean:返回一个boolean值,b表示事件是否可以取消，只读。
        当Event.cancelable属性为true时，调用Event.preventDefault()就可以取消这个事件，阻止浏览器对该事件的默认行为。
        如果事件不能取消，调用Event.preventDefault()会没有任何效果。所以使用这个方法之前，最好用Event.cancelable属性判断一下是否可以取消
        event.defaultPrevented-> Boolean: 表示事件是否调用过Event.preventDefault()
2.3 Event.currentTarget,target:
        任意事件都有两个与事件相关的节点，一个是事件的原始触发节点(Event.target),另一个是事件当前正在通过的节点(Event.currentTarget).
2.4 Event.type
        该属性返回一个字符串，表示事件类型。事件类型是在生成事件的时候指定的。
2.5 Event.timeStamp:
        返回一个毫秒时间戳，表示事件发生的时间，它是相对于网页加载成功开始计算的

3.实例方法
3.1 Event.preventDefault()
        取消浏览器对当前时间的默认行为，比如说点击链接之后，浏览器默认是跳转到另外一个页面
        使用这个方法之后，就不会跳转了。但是有个前提是时间对象的cancelable属性为true，如果为false，调用该方法没有任何效果。
        有一点需要注意的是，该方法不会组长事件的传播，如果要阻止传播，需要使用stopPropagation() 或者 stopImmediatePropagation()
3.2 Event.stopPropagation()
        阻止事件在DOM中继续传播，防止再触发定义带别的节点上的监听函数。但是不包括当前节点上其他的事件监听函数
3.3 Event.stopImmediatePropagation()
        阻止同一个事件的其他监听函数被调用，不管监听函数定义在当前节点还是其他节点，也就是说，该方法阻止事件的传播，比stopPropagation()更彻底。
        比如说 同一个节点的同一个事件还有其他监听函数，这些函数是根据添加的顺序依次调用的。只要有一个监听函数调用了该方法，其他的监听函数就不会再执行了。

3.4 Event.comprosedPath()-> list:
        成员是事件的最底层节点喝依次冒泡经过的所有上层节点。


鼠标事件
1.点击事件
        1.1 click: 点击鼠标触发
        1.2 dbclick:双击时触发
        1.3 mousedown:按下鼠标时触发
        1.4 mouseup: 释放按下的鼠标键时触发。
        触发顺序为 1.3 1.4 1.1 1.2
2.移动事件:
        1.1 mousemove: 当鼠标在一个节点内部移动时触发
        1.2 mouseenter: 当鼠标进入一个节点时触发，进入子节点不会触发这个事件
        1.3 mouseover: 鼠标进入一个节点时触发，进入子节点会再触发依次
        1.4 mouseout:  鼠标立刻一个节点时触发，立刻父节点也会触发这个事件。
        1.5 mouseleave: 鼠标离开一个节点时触发，立刻父节点不会触发 。
3. MouseEvent接口：
该接口涉及到鼠标相关的事件，点击，双击，松开鼠标，按下鼠标，滚轮，拖拉都是MouseEvent的实例 事件对象。
MouseEvent接口继承了Event接口，所以用于Event的所有属性和方法，并且还提供鼠标独有的属性和方法。
原生构造函数 MouseEvent()，用于新建一个MouseEvent实例。
var event = new MouseEvent(type,options);
4. MouseEvent接口的实例属性
4.1 MouseEvent.altKey,MouseEvent.ctrlKey,MouseEvent.metaKey,MouseEvent.shiftKey:
        四个属性都返回一个boolean值，表示当事件发生时，是否按下对应的键。只读属性。
        metaKey是 window键
4.2 MouseEvent.button, MouseEvent.buttons
        button
        返回一个数值，表示事件发生时按下了鼠标的哪个按键，该属性只读。
        0：按下主键，（通常是左键），或者该事件没有初始化这个属性。
        1：按下辅助键（通常是中键或者滚轮键）
        2：按下次键（通常是右键）
        buttons
        返回一个三个比特位的值，表示同时按下了那些键。它用来处理同时按下多喝鼠标键的情况。该属性只读。
        001：按下左键。
        010：按下右键
        100：中键或者滚轮键
        对应的位置有值那就是按下了相应的值，比如111，那就是三键一起按了。
4.3 MouseEvent.clientX, MouseEvent.clientY
        返回鼠标相对于浏览器窗口左上角的水平坐标
5. MouseEvent 接口的实例方法：
        方法返回一个Boolean值，表示有没有按下特定的功能键。它的参数是一个表示功能键的字符串。
6. WheelEvent接口接口：
        继承了MouseEvent实例，代表鼠标滚轮事件的实例对象。
        var wheelEvent = new WheelEvent(type,options);
        type：string，表示事件类型，对应滚轮事件来说，这个值就只能是wheel。
        该方法没有实例方法，只要实例属性。且都是只读。

键盘事件
1. 键盘事件的种类
由用户敲键盘触发，主要由keydown,keypress,keyup三个事件。继承了KeyboardEvent接口。
keydown:按下键盘时触发
keypress: 按下有值的键时触发，ctrl，alt等不会触发。
keyup: 松开键盘时触发该事件。
如果用户一直按键不松口，就会连续触发键盘事件，触发的顺序如下：
        1.keydown
        2.keypress
        3.keydown
        4.keypress
        .
        .
        -1.keyup
2.KeyboardEvent接口的描述
KeyboardEvent接口用来描述用户与键盘的互动。这个接口继承了Event接口，并且定义了自己的实例属性和实例方法。
KeyboardEvent构造函数。
var key = KeyboardEvent(type,options)
3.KeyboardEvent的实例属性
3.1 KeyboardEvent.altKey, KeyboardEvent.ctrlKey,KeyboardEvent.metaKey, KeyboardEvent.shiftKey
返回一个boolean值,表示是否按下对应的键。
3.2 KeyboardEvent.code
返回一个字符串，表示当前按下的键的字符串形式，只读。
3.3 KeyboardEvent.key 
返回一个字符串，表示按下的键名。
3.4 KeyboardEvent.location
返回一个整数，表示按下的键处在键盘的哪一个区域。
3.5 KeyboardEvent.repeat
返回一个boolean，代表该键是否被按着不放。
4.KeyboardEvent的实例方法
4.1 getModifierState()
进度事件
1. 进度事件的种类
资源加载的进度，主要由Ajax，img，audio，video等外部资源的加载触发，继承了ProgressEvent接口。
2. ProgressEvent 接口
构造函数 ProgressEvent(type,options)

表单事件（未理解未完）
1.表单事件的种类
1.1 input事件
触发事件（未完待续）





事件模型
1. 监听函数。
浏览器的事件模型：通过监听函数对事件做出反应。 也就是事件发生后，浏览器监听到了这个事件，就会执行对应的监听函数。
这就是事件驱动编程模式(event-driven)的主要编程方式。
1.1 HTML的on- 属性：
直接在HTML元素的属性中，定义某些事件的监听代码
#<div onclick='console.log('触发事件')'>
只在冒泡阶段触发。
1.2 元素节点的事件属性：
div.onclick = function(event){
    console.log('')
}
1.3 EventTarget.addEventListener()(推荐使用)
所有DOM节点实例都要addEventListener方法，用来为该节点定义事件的监听函数。

2. this的指向：
监听函数的内部的this指向触发事件的那个元素节点。
3. 事件的传播
一个事件发生后，会在子元素和父元素直接传播。分为三个阶段
    第一阶段： 捕获阶段，从window对象传到目标阶段。(capture phase)
    第二阶段： 在目标节点上触发，称为‘目标阶段’(target phase)
    第三阶段： 从目标节点传导回window对象(从底层传回到上层)，称为‘冒泡阶段’(bubbing phase)
这种三阶段的传播模型，使得同一个事件会在多个节点上触发。
4. 事件的代理
因为事件回在冒泡阶段向上传递，使用子节点的监听函数可以定义在父节点上，由父节点的监听函数同意处理多个子元素的事件
这个就是事件的代理(delegation).$appendComponent


事件
事件的本质是程序各个组成部分之间的一种通信方式。
EventTarget接口
DOM节点监听事件。
DOM节点的监听和触发都定义在EventTarget接口。 所有的节点对象和一些浏览器内置对象（XMLHttpRequest,AudioNode,AudioContext）
都部署了这个接口。
该接口主要提供了三个实例方法。
addEventListener(): 绑定 事件的监听函数。
removeEventListener():移除 事件的监听函数。
dispatchEvent(): 触发事件。
2. EventTarget.addEventListener()

t.addEventListener(type,listener[,useCapture]);
type:事件名称，大小写敏感。
listener:监听函数。事件发生时，调用该监听函数。
useCapture:Boolean,监听函数是否在捕获阶段触发。

3.EventTarget.removeEventListener()
移除addEventListener()方法添加的事件监听函数。
参数和addEventListener()是一样的，该方法移除的监听函数，add方法添加的那个监听函数，
而且必须在同一个元素节点。参数都要一样才可以。

4. EventTarget.dispatchEvent()



Mutation Observer API(待续)
CSS操作(待续)
Text节点和DocumentFragment节点(待续)
属性的操作(待续)     
Element节点(待续)
Document节点(待续)
ParentNode,childNodes接口(待续)

NodeList接口，HTMLCollection接口。
        能够容纳多个节点的数据结构
        NodeList包含各种类型的节点，HTMLCollection只能包含HTML元素节点。
        类似数组，有length属性和forEach方法，但是没有pop，push方法。
        如果想用数组方法，可以将其转为真正的数组
        var nodeArr = Array.prototype.slice.call(children);
        1.NodeList
        注意NodeList是动态集合，只有Node.childNodes返回的是一个动态集合，其他的NodeList都是静态集合。
        动态集合是指DOM新增或者删除一个相关节点都会立刻反映在NodeList实例。

        2.HTMLCollection接口。
        节点对象的集合，只包含元素节点。没有forEach方法，只能for循环。
Node 接口
1.属性
1.1 Node.prototype.nodeType
        document.nodeType // 9
        文档节点的类型值为9.
        Node对象中定义了几个常量，对应这些类型值：

        文档节点（document）：9，对应常量Node.DOCUMENT_NODE
        元素节点（element）：1，对应常量Node.ELEMENT_NODE
        属性节点（attr）：2，对应常量Node.ATTRIBUTE_NODE
        文本节点（text）：3，对应常量Node.TEXT_NODE
        文档片断节点（DocumentFragment）：11，对应常量Node.DOCUMENT_FRAGMENT_NODE
        文档类型节点（DocumentType）：10，对应常量Node.DOCUMENT_TYPE_NODE
        注释节点（Comment）：8，对应常量Node.COMMENT_NODE

        确定节点类型，使用nodeType属性是常用方法

        var node = document.documentElement.firstChild;
        if( node.nodeType === Node.ELEMENT_NODE){
            console.log('element node')
        }
1.2 Node.prototype.nodeName
        该属性返回节点的名称
1.3 Node.prototype.nodeValue
        该属性返回一个字符串，表示当前节点本身的文本值，该属性值可读写。
        只有文本节点，注释节点，和属性节点有文本值，只有这三类节点nodeValue可以返回结果，其他类型的节点一律返回null。
        也只有这三种节点可以设置nodeValue属性值。
1.4 Node.prototype.textContent
        返回当前节点和它所有后代节点的文本内容。自动忽略节点内部的HTML标签，返回所有文本内容。
1.5 Node.prototype.nextSibling 
        返回当前节点后面的第一个同级节点，如果没有同级节点则返回null。
1.6 Node.prototype.previousSibling 
        返回当前节点前面的第一个同级节点。
1.7 Node.prototype.parentNode
        返回父节点。
1.8 Node.prototype.firstChild, Node.prototype.lastChild
        返回当前节点的第一个子节点 或者最后一个子节点。
        注意 该属性返回的除了元素节点，还可能是文本节点或者注释节点。
1.9 Node.prototype.childNodes
        返回一个NodeList集合，成员包括当前节点的所有子节点。
1.10 Node.prototype.isConnected
        返回一个boolean值，表示当前节点是否在文档之中。
2.方法。
2.1 Node.prototype.appendChild(agr:Node) -> Node:
        将参数作为最后一个子节点插入当前节点。返回该子节点
2.2 Node.prototype.hasChildNodes()-> Boolean:
        表示当前节点是否有子节点。
2.3 Node.prototype.cloneNode(arg:Boolean)-> Node:
        返回克隆的节点，arg表示是否克隆子节点。
        该方法有一些缺点：
        1.会丢失该节点的回调函数
        2.返回的节点不在文档中，需要使用Node.appendChild这样的方法添加到文档中
        3.因为是克隆，所有DOM可能会有两个id和name都一样的网页元素。需要修改其中一个id和name
2.5 Node.prototype.removeChild(arg:Node)-> Node:
        删除一个子节点，返回值也是该子节点。
2.6 Node.prototype.replaceChild(newChild:Node,oldChild:Node)
        取代一个子节点.
2.7 Node.prototype.contains(arg:Node):-> Node:
        检查参数节点是否为当前节点
        参数节点为当前节点的子节点
        参数节点为当前节点的后代节点
2.8 Node.prototype.isEqualNode(arg:Node), Node.prototype.isSameNode(arg:Node) -> Boolean:
        isEqualNode检查两个节点是否相等，类型，属性，子节点相同
        isSameNode 表示两个节点是否为同一个节点。

DOM概述
1.DOM
    Document Object Model, 将网页转为一个JS对象，也就是HTML中元素，属性等都转为一个个节点，构成一颗树。

2.节点 Node
    节点的类型有七种。
    Document：整个文档树的顶层节点
    DocumentType：doctype标签（比如<!DOCTYPE html>）
    Element：网页的各种HTML标签（比如<body>、<a>等）
    Attr：网页元素的属性（比如class="right"）
    Text：标签之间或标签包含的文本
    Comment：注释
    DocumentFragment：文档的片段

    浏览器提供一个原生的节点对象Node，上面这七种节点都继承了Node，
    因此具有一些共同的属性和方法
3.节点树： 

    document节点，代表整个文档。





Promise对象(待续)










定时器
JS提供定时执行代码的功能，叫做定时器(timer)，主要是由 setTimeout() 和 setInterval()这两个函数来完成。
1. setTimeout()
    该函数指定某个函数或者某段代码在多少毫秒之后执行，它返回一个整数，表示定时器编号，以后可以用来取消这个定时器
    var timerId = setTimeout(func|code,delay,arg1,arg2,arg3);
    参数一为要执行的代码或者函数，
    参数二为要延迟的时间，
    其余的为将要传入函数的参数
    console.log(1);
    setTimeout('console.log(2)',1000);
    console.log(3);
    //1 3 2 

    有一个需要注意的是如果回调函数是对象的方法，那么setTimeout使得方法内部的this关键字指向全局环境。这个时候要避免错误就要把对象固定下来。
    解决办法之一：将回调函数放入一个匿名函数中。
    setTimeout(function(){ obj.y},1000);
    二就是使用bind方法
    setTimeout(obj.y.bind(obj),1000);
 2.setInterval()
    与setTimeout一致，但是setInterval()在与指定某个任务每隔一段时间就执行一次，无限次的定时间执行。

    setInterval的一个常见用途是实现轮询:
    var hash = window.location.hash;
    var hashWatcher = setInterval(function(){
        if (window.location.hash != hash ){
            updatePage();
        }
    },1000);
    setInterval 指定的是开始执行之间的间隔，其中并没有考虑到每次任务执行本身所消耗的时间，因此两次执行
    之间的间隔会小于指定的时间，比如说,setInterval 指定每100ms执行一次，每次执行需要5ms，那么第一次执行结束后的95ms后，第二次执行就会立马开始。又
    比如说一个任务需要105ms的执行时间，那么下一个任务就会在这个任务结束之后立马开始。

3.clearTimeout(),clearInterval()
这两个函数就是用来取消定时器的。
setTimeout 和 setInterval 函数，都会返回一个整数值，将这个整数传入clear函数就可以取消对应的定时器。


4. 实例: debounce 函数
防抖动，防止短时间内用户不停重复某一个操作，导致向服务器发送过多的ajax请求，原理在于设置一个时间间隔，
如果在这个时间间隔内，用户不触发新的ajax请求，则将请求发送出去，如果触发则刷新时间间隔，直到状态稳定。
$('textarea').on('keydown',debounce(ajaxAction,2500));
function debounce(fn,delay){
    var timer = null; //申明计时器
    return function(){
        var context = this;
        var args = arguments;
        clearTimeout(timer);
        timer = setTimeout(function(){
            fn.apply(context,args);
        },delay);
    }
}
5. 运行机制
    其实没有办法保证setTimeout 和 setInterval 指定的任务一定会按照预定时间执行。
    因为set方法就是将指定的代码移出本轮事件循环，等到下一轮事件循环的时候，再检查是否到了指定时间。
    那么问题就来了，如果这个set事件之后有一个巨耗时间的任务，那就会导致哪怕时间间隔已经到了，但是set指定事件依然要等到
    前面的任务完成才能进入主线程。
6.setTimeout(f,0)
    6.1含义
        即使delay被设置为0了，也不会立刻执行这个任务，因为这个任务会被移出本来事件循环，delay为0只能保证这个任务在下一轮事件循环一开始被执行。
    6.2应用（待续）
        1.调整事件的发生顺序。
        2.




1.异步操作的概述：
JS由于历史原因所以一直采用单线程。但是单线程的坏处就在如果一个任务耗时太长就会阻塞整个程序，
其实JS的运行速度不慢，慢是因为IO操作，所以JS内部就采取了事件循环机制(Event Loop)：即当一个任务在等待IO操作返回结果时，CPU就会挂起处于等待中的事件，先运行
下面的任务，等到IO操作出结果了再回头把挂起的任务继续执行。
2.同步任务和异步任务
同步任务时指再主线程上排队，没有被挂起的任务。
异步线程是被引擎放入任务队列的任务，只有在引擎任务这个任务可以被执行，该任务才会进入主线程
3.任务队列和事件循环
JS运行时，除了一个正在运行的主线程，还会有一个任务队列(task queue)，里面就是需要当前程序处理的异步任务。
执行顺序：主线程先执行完所有的同步任务，等到同步任务都执行完了，就去看任务队列中的异步任务。如果条件满足，该任务
就调入主线程执行该任务，直到清空任务队列。
异步任务的写法通常是 回调函数，一旦异步任务进入主线程就会执行相应的回调函数。
4. 异步操作的模式
4.1 回调函数：
也就是将一个函数作为参数传给另外一个函数。当一个函数结束会立马驱动另外一个函数。有点简单好理解。缺点代码不好阅读与维护，
各个部分之间高度耦合。
4.2事件监听：
以事件驱动模式。异步任务的执行不取决与代码的顺序，而是取决于某个事件是否发生。
f1.on('done',f2);
这句话就是当f1发生 done事件事件，就执行f2
优点，比较容易理解，可以绑定多个事件，去耦合化，但是整个程序就变成了事件驱动型，运行流程会变得不清晰。

4.3 发布/订阅
事件被理解成'信号'，如果存在一个信号中心，某个任务完成时就向任务中心发布(pulish)一个信号，其他任务可以向信号中心'订阅'这个信号，从而知道什么时候自己可以开始执行
这个就是（publish-subscrib pattern） 或者 observer pattern.
例子
jQuery.subscrib('done',f2);//f2向jQuery订阅了done这个信号
function f1(){
    setTimeout(function(){
        jQuery.publish('done');
    },1000);
}
f2执行完成之后记得取消订阅 
jQuery.unsubscrib('done',f2);
5.异步操作的流程控制:(待续)




严格模式：(待续)
strict mode
1.启用方法
在脚本文件的第一行，整个脚本都将以严格模式运行，如果这行语句不在第一行就无效了，
可以用在整个脚本，一看只用于单个函数。
3.显示报错

Object 对象的相关方法
1. Object.getPrototypeOf()
    得到参数对象的原型。
2.Object.setPrototypeOf(object1,obj2)
    将obj2设置为objec1原型对象，那么object1就能共享obj2的属性
3.Object.create()
参数为一个对象，然后以这个对象为原型，返回一个实例对象。该实例完全继承原型对象的属性。
// 原型对象
var A = {
    print: function () {
      console.log('hello');
    }
  };
  
  // 实例对象
  var B = Object.create(A);
  
  Object.getPrototypeOf(B) === A // true
  B.print() // hello
  B.print === A.print // true

4. Object.prototype.hasOwnProperty() -> Boolean:
用于判断某个属性定义在对象自身，还是定义在原型链上。
5. 对象的copy(待续)


对象的继承：
1. 原型对象的概述
    1.1 构造函数的缺点
        每生成一个对象实例，就会生成一个对象其中包含所有的属性和方法，这就意味着，函数对象也会生成多次。
        造成内存浪费，但是对象方法是对象实例完全同意的行为，完全应该共享的。
        所以就可以使用JS的原型对象(prototype)
    1.2 prototype属性的作用
        JS的继承思路是，原型对象上的所有属性和方法都能被实例对象共享，那么属性和方法定义在原型对象上，所有的实例对象
        不就共享这些属性和方法吗，这就是继承了
        prototype这个属性对于一般的函数没啥用，最主要的是在构造函数中。
        对于构造函数来说是，当生成实例对象时，该属性会自动成为实例对象的原型对象，那么也就是说实例对象继承了该原型对象
        所有的属性和方法
        function Animal(name){
            this.name = name;
        }
        Animal.prototype.color = 'white';
        var cat1 = new Animal('x');
        var cat2 = new Animal('y');
        //cat1 与cat2都有color属性，且值为white。
    1.3 原型链
        JS规定，所有的对象都要自己的原型对象，原型对象也有自己的原型对象，一层一层的就会形成原型链(prototype chain)
        往上一直溯源的话时Object.prototype，这也是为什么所有对象都有valueOfhtoString方法，那这个对象的原型对象是什么呢？ 是null，所以null是原型链的终点。
        Js引擎先寻找对象实例本身的属性，如果找不到，就到它的原型去找，这样一层一层的找，最后没有找到就会返回undefined。
        如果对象自身和它的原型，都定义了一个同名属性，那么优先读取对象自身的属性，这个叫做 '覆盖' (overriding)

    1.4 constructor属性
        prototype 对象有一个 constructor 属性，默认指向prototype对象所在的构造函数。
        function P(){}
        P.prototype.constructor === P //true
        constructor的作用是，可以得知某个实例对象，到底是哪个构造函数产生的
2. instanceof 运算符
    返回一个boolean，表示对象是否为某个构造函数的实例：
    var v =  new Vehicle();
    v instanceof Vehicle ;// true
    instanceof 是检查整个原型链，因此同一个实例对象，可能会对多个构造函数都返回true。
3. 构造函数的继承
    分为两步：
        3.1 调用父辈构造函数
            在子类的构造函数中，调用父类的构造函数
        3.2 让子类的原型指向父类的原型
        function Shape(){
            this.x = 0;
            this.y = 0;
        }
        
        Shape.prototype.move = function (x,y){
            this.x += x;
            this.y += y;
        }

        让Rectangle构造函数继承Shape:
        第一步 子类继承父辈的实例
        function Rectangle(){
            Shape.call(this);//调用父类构造函数
        }
        第二步：子类继承父类的原型
        Rectangle.prototype = Object.create(Shape.prototype);
        Rectangle.prototype.constructor = Rectangle;
4. 多重继承
    JS是不允许多重继承，变通一下：
    function M1() {
        this.hello = 'hello';
      }
      
      function M2() {
        this.world = 'world';
      }
      
      function S() {
        M1.call(this);
        M2.call(this);
      }
    // 继承 M1
    S.prototype = Object.create(M1.prototype);
    // 继承链上加入 M2
    Object.assign(S.prototype, M2.prototype);

    // 指定构造函数
    S.prototype.constructor = S;

var s = new S();
s.hello // 'hello'
s.world // 'world'






this 关键字：
1.一句话简介：this就是属性或者方法‘当前’所在的对象，无论什么场合，this都会返回一个对象。
2. JS内存的数据结构：
        为什么会有this关键字，其实就是由于内存的数据结构。
        在JS中，对象，数组，函数等复杂类型的值是 对象在内存中的地址，当我们创建一个对象时，Js会为其
        分配一段内存空间，并将该对象的属性和方法储存在该内存空间中，而变量则仅保存该对象的内存地址。
        由于这个机制在，就存在深复制和浅复制的区别了。（Java，Python都一样）
        再提一句，基础类型的值就是直接保存在变量所在的内存空间中。
        这种机制是为什么对象这些复杂类都比较大而且结构复杂，直接储存在变量所在的内存空间中不现实，保存
        地址就高效。
        说的更深一点，对象中每个属性都对应着一个 属性描述对象 （没错，表面看着是个值，在内存中是一个对象）
        var obj = { foo:5};
        在内存中是 
        {
            foo:{
                [[value]]:5
                [[writable]]:true
                [[Enumerable]]:true
                [[configurable]]:true
            }
        }
        再来个复杂的情况：属性值是function的时候，函数也是复杂类型的数据结构，所以也是变量保存的是函数在内存中的地址
        var obj = { foo:function(){ } 
        };
        在内存中是
        {
            foo:{
                [[value]]:函数地址
            }
            
        }
总结一下，JS语言中，一切都是对象，运行环境也是对象，所以函数都是在某个对象之中运行，this就是函数运行时所在的对象（环境）

3.使用场合
        this主要的使用场合。
        1. 全局环境：
            在全局环境中使用this，那么就是指向顶层对象window。
        2. 构造函数：
            构造函数中，this指向的是实例对象。
        3. 对象的方法：
            如果对象的方法中包含this，那么这个this的指向就是方法运行时所在的对象，该方法赋值给另外一个对象，就会改变
            this的指向。这里就包含了函数在内存中的储存方法了
            var obj = {
                foo:function(){
                    console.log(this);
                }
            }
            obj.foo();
            此时返回的值是 obj。这个好理解foo函数运行环境是obj，下面的情况就不一样了。
            (obj1.foo = obj.foo)()
            这段话的含义在将 obj.foo 值赋予给 obj1.foo，得到的结果是 (obj1.foo)() 然后再访问obj的foo属性，将其作为普通函数来属性，此时函数的
            上下文运行对象就是全局环境，this就指向window对象。这个原因是 obj.foo 储存的是foo函数的地址，那么obj1.foo的值就是foo函数的地址，所以obj1.foo的调用
            就成了普通函数的调用。
4.使用注意点
        避免多层this
            由于this的指向不确定，所以不用在函数中包含多层this
            var o = {
                f1: function () {
                    console.log(this);
                    var f2 = function () {
                    console.log(this);
                    }();
                }
                }
                
                o.f1()
                //obj
                //window
            解决方法是使用变量固定this的值，然后在内层函数中调用这个变量
            var o = {
                f1: function() {
                    console.log(this);
                    var that = this;
                    var f2 = function() {
                    console.log(that);
                    }();
                }
                }
                
                o.f1()
                // Object
                // Object
5.绑定this的方法
    由于this的动态切换，导致编程变得困难和模糊，所以有时候需要把this固定下来，Js提供了call，apply，bind方法 来切换/固定this方法

    5.1 Function.prototype.call(arg:Object,arg1,arg2....)
        函数实例的call方法，可以指定函数内部的this的指向，在指定的作用域中，调用该函数。
        var obj = {};
        var f = function(){
            return this;
        }

        f() // window
        f.call(obj) // obj

        call的参数应该是一个对象，如果参数为空，null，undefined，则默认传入全局对象。

        call(object,arg1,arg2,arg3....)可以接受多个参数,第一个参数为要指向的对象，后面的arg是function的参数
    5.2 Function.prototype.apply(Object,[arg1,arg2...])
        和call方法类似，区别在函数的参数可以使用一个数组来传参

        一个有趣的应用：
            1.找出数组最大的元素，
                JS不提供出数组最大元素的函数。结合使用apply()方法和Math.max()方法。就可以返回最大值
                var a = [10,2,4,15,9]
                Math.max.apply(null,a)
                // 15
    5.3 Function.prototype.bind()
        bind()方法用于将函数体内的this绑定到某个对象，然后返回一个函数。
        var d = new Date();
        d.getTime()
        var print = d.getTime()
        print() 
        这样会报错的，因为getTime()赋值给print以后，内部的this已经不指向Date对象了，此时就需要bind()方法来将Data内部的this指向相应的对象
        var print = d.getTime.bind(d)
        print() // 这样就是ok的，因为bind将this指向d对象。
        注意点。
        每一次都返回一个新函数



实例对象和NEW命令：
    1.构造函数
    
        与Java不同，Java的对象体系是基于class的，而JS的对象体系是基于构造函数和原型链的。
        JS使用构造函数来对位对象的模板，描述了实例对象的基本结果。
            var Vehicle = function (p) {
                this.price = p;
            };
        这就是一个JS构造函数。构造函数名字第一个字母大写与普通函数进行区别
        this关键字代表了所要生成的对象实例

    2.new 命令
        执行构造函数，返回一个实例对象。
        var v = new Vehicle(500);
        一定要加new关键字，不加会有奇奇怪怪的结果，如果不加new，构造函数就会变成普通函数，
        var v1 = Vehicle(500)
        那么 this就会指向全局对象window，那么就会生成构造函数中相应属性的全局变量（如生成一个price全局变量）
        此时 v1是一个空对象，
        所以在构造函数内部使用严格模式，在第一行加上'use strict'
            function Vehicle(500){
                'use strict';
                this.price = 500;
            }
            在调用Vehicle()时，如果不加new就会报错，或者另一种方式：在构造函数中添加判断条件
            “如果构造函数以普通函数的方式被调用，那么就会是由new 重新调用这个构造函数。”
            function Vehicle(p){
                if( !(this instanceof Vehicle)){
                    return new Vehicle(p);
                }
                this.price = p;
            }
    3.使用new命令，构造函数会执行下面的步骤：
    var v = new Vehicle(500)
            1. 创建一个空对象，作为将要返回的对象实例: 也就是  v
            2. 将这个空对象的原型，指向构造函数的prototype属性:
                v 指向 Vehicle.prototype,这样v就可以用从vehicle构造函数的原型中继承属性和方法。
            3. 将空对象赋值给函数内部关键字this。也就是 将新创建的对象 v 作为this关键字的值传递给构造函数Vehicle，这样
            构造函数就可以访问并操作v对象了，
            4. 开始执行构造函数内部代码，也就是对这个对象的属性进行赋值。


JSON对象(未完，待续)
 JSON格式:
        JSON对 值的类型和格式有严格的规定。
        1.复合类型的值只能是数组或者对象，不能是函数，正则表达式，日期对象等
        2.原始类型只有四种： string，number，boolean，null
        3.字符串必须使用双引号表示，不能使用单引号
        4.键名必须放在双引号里面
 JSON静态方法
    JSON.stringify()
    将一个值转为JSONz字符串。该字符串符号JSON格式，并且可以被JSON.parse()
String对象
 实例属性
    String.prototype.length
        'abc'.length;
 实例方法
    1.String.prototype.charAt()
        charAt方法返回指定位置的字符，参数是从0开始编号的
        完全可以使用下角标来进行替代
            'abc'.charAt(1);
            'abc'[1];
    2.String.prototype.concat(arg1,arg2,arg3...)
        concat 方法用于连接两个字符串，返回一个新的字符串，并且不会改变原来的字符串
        如果参数不是string类型的，则会先转为string，再连接
            var s = 'abc';
            var t = 'def';
            new_s = s.concat(t);//abcdef
    3. String.prototype.slice(arg1,arg2)
        slice 方法用于提取出子字符串，不会修改原字符串。
        arg1: 子字符串开始的地方
        arg2：子字符串结束的地方(不含该位置)
            var s = "JavaScript";
            s.slice(0,4) // Java
    4. String.prototype.indexOf(arg1,arg2)
        arg1 是需要匹配的字符串 (必须)
        arg2 表示从该位置开始向后匹配 (可选)
        返回一个字符串在另一个字符串中第一次出现的位置，返回匹配开始的位置，如果不匹配，返回-1.
            var s = 'JavaScript';
            var t = 'ava';
            s.indexOf(t);// 1 
    5. String.prototype.lastIndexOf(arg1,arg2)
        类似于indexOf()
    6. String.prototype.trim()
        去掉字符串两端的空格，包括制表符\t,\v,\n,\r        
        返回一个新的字符串
    7. String.prototype.toLowerCase(); String.prototype.toUpperCase()
        转为大写或者小写
    8. String.prototype.search(arg1); String.prototype.replace(arg1,arg2)
        在一个字符串中匹配arg1，如匹配成功返回第一个位置，
        将arg1替换为arg2；
    9. String.prototype.split(arg1)
        arg1 代表分隔符号
        返回一个数组

        