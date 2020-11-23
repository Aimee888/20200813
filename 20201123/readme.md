# mouse_kb_listener
参考链接：https://blog.csdn.net/u011367482/article/details/106173994/

## 鼠标监听
mouse_listener1.py  
三种事件：   
- 鼠标移动(on_move)   
- 鼠标滚轮滑动(on_click)
- 鼠标按压释放(on_scroll)  

打印鼠标坐标  
  
mouse_listener2.py  
使用event事件处理三个事件，执行一次  
  
  
  
## 键盘监听
kb_listener.py  
捕捉键盘按压与释放的按键键值，如果释放了ESC按键，则停止监控键盘

kb_listener2.py  
监听一次  

# mouse_kb_listener_ui
mouse_disable.py  
使用user32.dll禁用和打开鼠标键盘    
  
myUI_mouse.py  
使用cv2加载图片，图片大小和原尺寸相同    
  
myUI_mouse1.py  
添加label的双击事件，包含左键双击和右键双击。  
使用devcon.exe禁用USB设备与加载USB设备。  
添加了定时器功能。
